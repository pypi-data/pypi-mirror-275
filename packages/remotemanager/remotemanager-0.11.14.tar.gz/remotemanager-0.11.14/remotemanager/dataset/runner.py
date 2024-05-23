import copy
import json
import logging
import os
import time
from datetime import datetime
from typing import Union

from remotemanager.dataset.runnerstates import RunnerState
from remotemanager.logging.decorate_verbose import make_verbose
from remotemanager.logging.utils import format_iterable
from remotemanager.logging.verbosity import Verbosity
from remotemanager.storage.database import Database
from remotemanager.storage.sendablemixin import INTERNAL_STORAGE_KEYS
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.storage.trackedfile import TrackedFile
from remotemanager.utils import object_from_uuid, _time_format, ensure_list
from remotemanager.utils.uuid import generate_uuid

logger = logging.getLogger(__name__)


SERIALISED_STORAGE_KEY = INTERNAL_STORAGE_KEYS["SERIALISED_STORAGE_KEY"]

localwinerror = """Local runs on windows machines are not supported.
Please use a URL which connects to a non-windows machine or consider using
Docker to continue."""


def format_time(t: datetime.time) -> str:
    """
    Format the datetime object into a dict key

    Args:
        t (datetime.time):
            time object to be formatted to string

    Returns:
        (str):
            formatted time
    """
    return t.strftime(_time_format)


@make_verbose
class Runner(SendableMixin):
    """
    The Runner class stores any info pertaining to this specific run. E.g.
    Arguments, result, run status, files, etc.

    .. warning::
        Interacting with this object directly could cause unstable behaviour.
        It is best to allow Dataset to handle the runners. If you require a
        single run, you should create a Dataset and append just that one run.
    """

    _defaults = {
        "skip": True,
        "force": False,
        "asynchronous": True,
        "local_dir": "temp_runner_local",
        "remote_dir": "temp_runner_remote",
    }

    _args_replaced_key = "~serialised_args~"

    _do_not_package = ["_serialiser", "_parent", "_database"]

    def __init__(
        self,
        arguments: dict,
        dbfile: str,
        parent,
        self_id: str,
        extra_files_send: list = None,
        extra_files_recv: list = None,
        verbose: Union[None, int, bool, "Verbosity"] = None,
        extra: str = None,
        **run_args,
    ):
        self.verbose = verbose

        self._run_args_internal = run_args
        self._run_args_temp = {}  # temporary args for storing runtime overrides
        self.extra = extra

        self._extra_filenames_base = {
            "send": extra_files_send if extra_files_send is not None else [],
            "recv": extra_files_recv if extra_files_recv is not None else [],
        }
        self._extra_filenames_temp = copy.deepcopy(self._extra_filenames_base)
        # temp arrays for storing TrackedFile instances for extra files
        self._extra_files_send = []
        self._extra_files_recv = []

        if arguments is None:
            arguments = {}

        if not isinstance(arguments, dict):
            raise ValueError(f"runner arguments ({type(arguments)}) must be dict-type")

        # parent and id setting
        self._parent = parent
        self._parent_uuid = parent.uuid  # used for parent memory recovery

        self._dbfile = dbfile
        self._database = Database(file=self._dbfile)

        self._id = self_id

        # check that we can properly serialise the args
        # this needs to be within the runner, so we can properly generate uuids
        self._args_replaced = False
        try:
            # check that the args can be sent via json
            self._args = json.loads(json.dumps(arguments))
            self._generate_uuid()
            logger.info("args pass a json dump, proceeding directly")
        except TypeError:
            # if they can't, fall back on the serialiser
            file = f"{self.parent.argfile}-{self.id}{self.serialiser.extension}"
            logger.info("args require treatment, using file %s", file)
            lpath = os.path.join(self.parent.local_dir, file)

            if not os.path.isdir(self.parent.local_dir):
                os.makedirs(self.parent.local_dir)

            content = self.parent.serialiser.dumps(arguments)
            with open(lpath, self.serialiser.write_mode) as o:
                o.write(content)

            # adding the file in here forces the run_args to swap out
            # run_args for a repo.load
            arguments = {file: Runner._args_replaced_key}
            self._args = arguments
            self._args_replaced = True

            uuid_extra = {"uuid_base": generate_uuid(str(content))}
            self._generate_uuid(uuid_extra)

            self._extra_filenames_base["send"].append(lpath)

        logger.info("new runner (id %s) created", self.uuid)

        self._dependency_info = {}

        self._history = {}
        self.set_state("created", force=True)
        self.last_submitted = 0
        self._run_state = None

        self._identifier = f"{self.parent.name}-{self.parent.short_uuid}-{self.id}"

        # store a reference for all trackedfiles for updating
        self._trackedfiles = {}

    def __hash__(self) -> hash:
        return hash(self.uuid)

    def __repr__(self) -> str:
        return self.identifier

    def _generate_uuid(self, extra=None):
        slug = {}
        slug.update(self.run_args)

        if extra is not None:
            slug.update(extra)
        else:
            slug.update(self._args)

        self._runner_uuid = generate_uuid(format_iterable(slug))
        self._uuid = generate_uuid(self._runner_uuid + str(self.parent.uuid))

    @property
    def database(self) -> Database:
        """
        Access to the stored database object.
        Creates a connection if none exist.

        Returns:
            Database
        """
        if not hasattr(self, "_database") or self._database is None:
            self._database = Database(file=self._dbfile)
        return self._database

    @property
    def parent(self):
        """Returns the parent Dataset object"""
        if self.is_missing("_parent"):
            self._parent = object_from_uuid(self._parent_uuid, "Dataset")
        return self._parent

    @property
    def serialiser(self):
        """Returns the parent Serialiser object"""
        return self.parent.serialiser

    @staticmethod
    def _set_defaults(kwargs: dict = None) -> dict:
        """
        Sets default arguments as expected. If used as a staticmethod, returns
        the defaults
        """

        if kwargs is None:
            kwargs = {}

        for k, v in Runner._defaults.items():
            if k not in kwargs:
                kwargs[k] = v

        return kwargs

    @property
    def uuid(self) -> str:
        """
        The uuid of this runner
        """
        return self._uuid

    @property
    def short_uuid(self) -> str:
        """
        A short uuid for filenames
        """
        return self.uuid[:8]

    @property
    def id(self) -> str:
        """Returns this Runner's current ID"""
        return self._id

    @property
    def name(self) -> str:
        """Returns this Runner's name"""
        return self._id

    @property
    def identifier(self) -> str:
        """Returns the identifier, a string used for file uniqueness"""
        return self._identifier

    def _format_filename(self, ftype: str, ext: str) -> str:
        """
        Formats internal file names consistently.

        Args:
            ftype (str):
                file type. Jobscript, result file, etc.
            ext (str):
                file extension

        Returns:
            str: formatted filename
        """
        return f"{self.identifier}-{ftype}{ext}"

    def _trackedfile_factory(self, remote, ftype, extension):
        ext = self._format_filename(ftype, extension)
        return TrackedFile(self.local_dir, remote, ext)

    @property
    def runfile(self) -> TrackedFile:
        """
        Filename of the python runfile
        """
        file = self._trackedfiles.get("runfile", None)

        if file is None:
            file = self._trackedfile_factory(self.remote_dir, "run", ".py")
            self._trackedfiles["runfile"] = file

        return file

    @property
    def jobscript(self) -> TrackedFile:
        """
        Filename of the run script
        """
        file = self._trackedfiles.get("jobscript", None)

        if file is None:
            file = self._trackedfile_factory(self.remote_dir, "jobscript", ".sh")
            self._trackedfiles["jobscript"] = file

        return file

    @property
    def resultfile(self) -> TrackedFile:
        """
        Result file name
        """
        file = self._trackedfiles.get("resultfile", None)

        if file is None:
            if self.parent.function is None:
                result_ext = ".txt"
            else:
                result_ext = self.parent.serialiser.extension
            file = self._trackedfile_factory(self.run_path, "result", result_ext)
            self._trackedfiles["resultfile"] = file

        return file

    @property
    def errorfile(self) -> TrackedFile:
        """
        File tracker for error dumpfile
        """
        file = self._trackedfiles.get("errorfile", None)

        if file is None:
            file = self._trackedfile_factory(self.run_path, "error", ".out")
            self._trackedfiles["errorfile"] = file

        return file

    @property
    def local_dir(self) -> str:
        """
        Local staging directory
        """
        return self.run_args.get("local_dir")

    @local_dir.setter
    def local_dir(self, path: str) -> None:
        """
        Sets the local_dir
        """
        self._run_args_internal["local_dir"] = path

    @property
    def remote_dir(self) -> str:
        """
        Target directory on the remote for transports
        """
        return self._replacehome(self.run_args["remote_dir"])

    @remote_dir.setter
    def remote_dir(self, path: str) -> None:
        """
        Sets the remote_dir
        """
        logger.debug("setting remote dir to %s", path)
        self._run_args_internal["remote_dir"] = path

    @property
    def run_path(self) -> [str, None]:
        """
        Intended running directory. If not set, uses remote_dir

        .. note::
            If both remote_dir and run_dir are set, the files will be
            transferred to remote_dir, and then executed within run_dir
        """
        if "run_dir" in self.run_args and self.run_args["run_dir"] is not None:
            return os.path.join(self.remote_dir, self.run_args["run_dir"])
        return self.remote_dir

    @property
    def run_dir(self) -> [str, None]:
        """
        Intended running directory. If not set, uses remote_dir

        .. note::
            If both remote_dir and run_dir are set, the files will be
            transferred to remote_dir, and then executed within run_dir
        """
        if "run_dir" in self.run_args and self.run_args["run_dir"] is not None:
            return self._replacehome(self.run_args["run_dir"])
        return self.remote_dir

    @run_dir.setter
    def run_dir(self, dir: str) -> None:
        """
        Sets the run_dir
        """
        self._run_args_internal["run_dir"] = dir

    def _replacehome(self, path):
        if "$HOME" in path:
            return path.replace("$HOME", self.parent.url.home)
        elif path.startswith("~"):
            return path.replace("~", self.parent.url.home)
        return path

    @property
    def run_args(self) -> dict:
        """
        Returns the base run args.

        Returns:
            _run_args
        """
        base = copy.deepcopy(self.parent._global_run_args)
        base.update(self._run_args_internal)
        base.update(self._run_args_temp)

        return base

    def set_run_arg(self, key: str, val) -> None:
        """
        Set a single run arg `key` to `val`

        Args:
            key:
                name to set
            val:
                value to set to

        Returns:
            None
        """
        self._run_args_internal[key] = val

    def set_run_args(self, keys: list, vals: list) -> None:
        """
        Set a list of `keys` to `vals

        .. note::
            List lengths must be the same

        Args:
            keys:
                list of keys to set
            vals:
                list of vals to set to
        """
        keys = ensure_list(keys)
        vals = ensure_list(vals)

        if len(keys) != len(vals):
            raise ValueError(
                f"number of keys ({len(keys)}) != number of vals ({len(vals)}"
            )

        for key, val in zip(keys, vals):
            self._run_args_internal[key] = val

    def update_run_args(self, d: dict) -> None:
        """
        Update current global run args with a dictionary `d`

        Args:
            d:
                dict of new args
        """
        self._run_args_internal.update(d)

    @property
    def args(self) -> dict:
        """
        Arguments for the function
        """
        if self._args is None:
            return {}
        return self._args

    @property
    def extra_files(self) -> dict:
        """
        Returns the extra files set for this runner
        """
        return self._extra_filenames_temp

    @property
    def extra_files_send(self) -> list:
        """Returns the list of extra files to be sent"""
        return self._extra_files_send

    @property
    def extra_files_recv(self) -> list:
        """Returns the list of extra files to be retrieved"""
        return self._extra_files_recv

    @property
    def history(self) -> dict:
        """
        State history of this runner
        """
        return self._history

    @property
    def status_list(self) -> list:
        """
        Returns a list of status updates
        """
        return list(self._history.values())

    def insert_history(self, t: datetime, newstate: str) -> None:
        """
        Insert a state into this runner's history

        Args:
            t (datetime.time):
                time this state change occurred
            newstate (str):
                status to update
        """
        if not isinstance(t, datetime):
            raise ValueError(f"time of type {type(t)} should be a datetime instance")

        base_timekey = format_time(t)
        idx = 0
        timekey = f"{base_timekey}/{idx}"
        while timekey in self._history:
            idx += 1

            timekey = f"{base_timekey}/{idx}"

        logger.info(
            "(%s) updating runner %s history -> %s", timekey, self.short_uuid, newstate
        )
        self._history[timekey] = newstate

    @property
    def state(self) -> RunnerState:
        """
        Returns the most recent runner state
        """
        return self._state

    @state.setter
    def state(self, newstate):
        self.set_state(newstate)

    def set_state(self, newstate: str, force: bool = False) -> None:
        """
        Update the state and store within the runner history

        .. versionadded:: 0.9.3
            now checks the current state before setting, won't duplicate states unless
            force=True

        Args:
            newstate:
                state to set to
            force:
                skip currentstate checking if True
        """
        if not force and self.state == newstate:
            return

        t = int(time.time())
        state_time = datetime.fromtimestamp(t)

        self.insert_history(state_time, newstate)
        self._state = RunnerState(newstate)

        if newstate == "submit pending":
            logger.info("updating last_run (%s) to t=%s", self, t)
            self.last_submitted = t

    def stage(
        self,
        extra_files_send: list = None,
        extra_files_recv: list = None,
        python: str = "python",
        repo: str = None,
        extra: str = None,
        summary_only: bool = False,
        parent_check: str = "",
        child_submit: list = None,
        force_ignores_success: bool = False,
        verbose: Union[None, int, bool, Verbosity] = None,
        **run_args,
    ) -> bool:
        """
        Prepare this runner for a run by creating files in the local dir

        Args:
            extra_files_send:
                list of extra files to send
            extra_files_recv:
                list of extra files to receive
            python:
                python command to use
            repo (str):
                override the repo target
            extra (str):
                extra lines to append to jobscript. This goes _last_.
            summary_only (bool):
                INTERNAL, used during a lazy append to skip printing.
                (Calls assess_run with quiet enabled)
            parent_check (str):
                INTERNAL, extra string to check that the parent result exists
            child_submit (list):
                INTERNAL, list of extra lines to submit childen
            force_ignores_success (bool):
                If True, `force` takes priority over `is_success` check
            verbose:
                local verbosity
            run_args:
                temporary run args for this run

        Returns:
            bool: True if runner is ready
        """
        if summary_only:
            verbose = Verbosity(0)
        elif verbose is not None:
            verbose = Verbosity(verbose)
        else:
            verbose = self.verbose
        self._run_args_temp = run_args
        # create the run_args for this run
        # start empty, so we don't overwrite, then update with stored and temp args
        # now we have our run_args, check if we're even running
        if not self.assess_run(
            self.run_args, force_ignores_success=force_ignores_success, verbose=verbose
        ):
            return False
        # handle extra files the same as the args
        self._extra_filenames_temp = copy.deepcopy(self._extra_filenames_base)
        if extra_files_send is not None:
            self._extra_filenames_temp["send"] += ensure_list(extra_files_send)
        if extra_files_recv is not None:
            self._extra_filenames_temp["recv"] += ensure_list(extra_files_recv)

        # clear out and recreate any TrackedFiles that might be from previous runs
        self._trackedfiles = {}
        self._extra_files_send = []
        for file in self._extra_filenames_temp["send"]:
            local, name = os.path.split(file)

            self._extra_files_send.append(TrackedFile(local, self.remote_dir, name))

        self._extra_files_recv = []
        for file in self._extra_filenames_temp["recv"]:
            remote, name = os.path.split(file)
            remote = str(os.path.join(self.run_path, remote))
            self._extra_files_recv.append(TrackedFile(self.local_dir, remote, name))

        if self.parent.function is not None:
            self.stage_python(
                repo=repo,
                python=python,
                parent_check=parent_check,
                child_submit=child_submit,
                extra=extra,
            )
        else:
            self.stage_bash(extra=extra)

        # set state to staged and return
        self._result = None
        self._error = None
        self.state = "staged"
        return True

    def stage_python(
        self, repo: str, python: str, parent_check: str, child_submit: list, extra: str
    ):
        # check if we have replaced args with a file, and use that if so
        if self._args_replaced:
            argstore = list(self.args.keys())[0]
            # args are stored in path at argstore we need the
            # relative path from run_dir, set up a temporary TrackedFile for this
            tmp = TrackedFile("", self.remote_dir, argstore)
            path = tmp.relative_remote_path(self.run_path)

            logger.debug("using argstore path %s", path)
            argline = f'kwargs = repo.{self.parent.serialiser.loadfunc_name}("{path}")'
        else:
            argline = f"kwargs = {self.args}"

        # python file writing
        # if repo is not overidden by a dependency, generate the import path here
        if repo is None:
            repo = self.parent.repofile.name

        errorpath = self.errorfile.relative_remote_path(self.run_path)
        dir_env_name = f"DIR_{self.short_uuid}"
        # script proper
        runscript = [
            f"import importlib.util, os, sys",
            f"path = os.path.expandvars('${dir_env_name}/{repo}')",
            f"runtime = os.path.getmtime(path)",
            f"spec = importlib.util.spec_from_file_location('repo', path)",
            f"repo = importlib.util.module_from_spec(spec)",
            f"spec.loader.exec_module(repo)\n",
            "vmaj, vmin, vpat, *extra = sys.version_info",
            "if vmaj < 3:",
            '\traise RuntimeError(f"Python version {vmaj}.{vmin}.{vpat} < 3.x.x")',
            argline,
            f"result = repo.{self.parent.function.name}(**kwargs)",
            f"# if the error file mtime (created at run) has changed, don't output",
            f"if os.path.getmtime(path) == runtime:",
            f"\trepo.{self.parent.serialiser.dumpfunc_name}"  # note the lack of comma
            f"(result, '{self.resultfile.name}')",
        ]
        # if this runner is a child, we need to import the previous results
        if self.parent.is_child:
            # if the script changes, the insert point may need to be updated
            runscript.insert(6, self._dependency_info["parent_import"])

        self.runfile.write("\n".join(runscript), add_newline=self._parent.add_newline)

        # jobscript writing
        # note the "[ -s {errorpath} ] ||" block prevents a job run
        # if the error file exists
        if self.run_path != self.remote_dir:
            logger.debug("run dir is separate to remote dir, appending extras")
            submit = (
                f"export {dir_env_name}={self.short_uuid}_master\n"
                f"pydir=$PWD\n"
                f"{parent_check}cd {self.run_dir} && "
                f"{python} ${{pydir}}/{self.runfile.name} 2>> {errorpath}"
            )
        else:
            submit = (
                f"export {dir_env_name}={self.short_uuid}_master\n"
                f"{parent_check}{python} {self.runfile.name} 2>> {errorpath}"
            )
            logger.debug("directly using script %s", submit)

        # generate the script proper
        # append or inject the submission lines
        submit_stub = "#SUBMISSION_SUBSTITUTION#"
        append_submit = True

        run_args = copy.deepcopy(self.run_args)
        run_args["runner_extra"] = self.extra
        run_args["tmp_extra"] = extra

        script = self.parent._script_sub(**run_args)
        script_clean = []
        for line in script.split("\n"):
            if submit_stub in line:
                script_clean.append(submit)
                append_submit = False
            else:
                script_clean.append(line)
        # if we didn't replace the stub, append it to the script end
        if append_submit:
            script_clean.append(submit)
            logger.info("appended submit block")

        # if this runner has children, append the lines to submit them
        if child_submit is not None:
            for line in child_submit:
                script_clean.append(line)

        script = "\n".join(script_clean)
        self.jobscript.write(script, add_newline=self._parent.add_newline)

    def stage_bash(self, extra: str):
        if self._args_replaced:
            raise RuntimeError(
                "Arguments have been replaced by a file "
                "(potentially for serialisation purposes). "
                "This is only compatible with a python function."
            )

        run_args = copy.deepcopy(self.run_args)
        run_args["runner_extra"] = self.extra
        run_args["tmp_extra"] = extra

        run_args.update(self.args)

        script = self.parent._script_sub(**run_args)
        self.jobscript.write(script, add_newline=self._parent.add_newline)

    def assess_run(
        self,
        run_args: dict,
        force_ignores_success: bool = False,
        verbose: Union[None, int, bool, Verbosity] = None,
    ) -> bool:
        """
        Check whether this runner should be running.

        If `force` is True we always run

        If `skip` is True, we have to check if a run is ongoing, or a result exists

        Args:
            quiet:
                Do not print status if True
            run_args:
                Temporary args specific to this run instance
            force_ignores_success (bool):
                If True, `force` takes priority over `is_success` check
            verbose:
                local verbosity
        Returns:
            bool: True if runner has the green light
        """
        if verbose is not None:
            verbose = Verbosity(verbose)
        else:
            verbose = self.verbose
        logger.info("assessing run for runner %s", self)
        verbose.print(f"assessing run for runner {self}", end="... ", level=1)
        logger.info("run args: %s", format_iterable(run_args))

        if self.is_success and not force_ignores_success:
            msg = "ignoring run for successful runner"
            logger.warning(msg)
            verbose.print(msg, level=1)
            self._run_state = "skip"
            return False

        if run_args["force"]:
            msg = "force running"
            logger.warning(msg)
            verbose.print(msg, level=1)
            self._run_state = "force"
            return True

        if run_args["skip"]:
            if self.is_finished:
                msg = "skipping already completed run"
                logger.warning(msg)
                verbose.print(msg, level=1)
                self._run_state = "skip"
                return False

            if self.state >= "submit pending":
                msg = "skipping already submitted run"
                logger.warning(msg)
                verbose.print(msg, level=1)
                self._run_state = "skip"
                return False

        logger.info("running")
        verbose.print("running", level=1)
        self._run_state = "run"
        return True

    @property
    def is_finished(self) -> [bool, None]:
        """
        Returns True if this runner has finished

        (None if the runner has not yet been submitted)
        """
        logger.info("checking is_finished for %s. Current state: %s", self, self.state)
        if self.state <= "staged":
            # run has not yet been submitted
            return None

        if self.state >= "completed":
            # run is finished
            return True

        logger.info("Not marked completed, returning False")
        return False

    @property
    def is_success(self) -> bool:
        """Returns True if this runner is considered to have succeeded"""
        return self.state.success

    @property
    def is_failed(self) -> Union[bool, None]:
        """
        Returns True if this runner is considered to have failed

        (None if incomplete)
        """
        if self.state < "completed":
            return False
        return not self.state.success

    def read_local_files(self) -> None:
        """
        Reads all local files attached to this Runner.

        Fills out the resulting attributes (result, error, state, etc.)

        Returns:
            None
        """
        satisfied = False
        success = False
        if self.state == "reset":
            logger.info("runner is in a reset state, ignoring file read")
            return

        if os.path.isfile(self.resultfile.local):
            if os.path.getmtime(self.resultfile.local) > self.last_submitted:
                logger.info("reading recent results file")
                # need to change the serialiser if we have a txt output
                if self.parent.function is None:
                    with open(self.resultfile.local) as o:
                        data = o.read().strip()
                    if data == "":
                        data = None
                    self.result = data
                else:
                    self.result = self.parent.serialiser.load(self.resultfile.local)
                satisfied = True
                success = True
            else:
                logger.info("local results file is outdated")
                satisfied = False

        if os.path.isfile(self.errorfile.local):
            if os.path.getmtime(self.errorfile.local) > self.last_submitted:
                logger.info("reading recent error file")
                self.error = self.errorfile.content.strip().split("\n")[-1]
                satisfied = True
            else:
                logger.info("local error file is outdated")
                satisfied = False

        if satisfied and not self.state == "satisfied":
            self.state = "satisfied"
            self.state.success = success

    def verify_local_files(self) -> bool:
        """
        Check the existence of local files on disk

        Returns:
            (bool): True if everything is okay
        """
        if not self.state == "satisfied":
            return True

        return self.resultfile.exists_local and all(
            [f.exists_local for f in self.extra_files_recv]
        )

    @property
    def result(self):
        """Returns the result attribute, if available"""
        self.read_local_files()
        if self.is_failed:
            return RunnerFailedError(self.error)
        if hasattr(self, "_result"):
            try:
                if SERIALISED_STORAGE_KEY in self._result:
                    self._result = self.parent.serialiser.loads(self._result[1])
            except TypeError:
                pass
            except ValueError:
                pass
            return self._result
        return None

    @result.setter
    def result(self, result) -> None:
        """
        Creates and sets the result property, setting the state to "completed"

        Args:
            result:
                run result
        """
        self._result = result

    @property
    def error(self):
        """
        Error (If one exists)
        """
        self.read_local_files()
        if hasattr(self, "_error"):
            return self._error
        return None

    @error.setter
    def error(self, error) -> None:
        """
        Creates and sets the error property

        Args:
            error:
                run error string
        """
        self._error = error

    @property
    def full_error(self) -> [str, None]:
        """
        Reads the error file, returning the full error

        Returns:
            str
        """
        if self.error is not None:
            return self.errorfile.content
        return None

    def clear_result(self, wipe: bool = True) -> None:
        """
        Clear the results properties and set the state to "reset", which blocks some
        functions until the runner is rerun

        Args:
            wipe:
                Additionally deletes the local files if True. Default True
        Returns:
            None
        """
        logger.info("clear_result called for runner %s", self)
        try:
            del self._result
            logger.info("deleted result attribute")
        except AttributeError:
            logger.info("no result attribute found")

        try:
            del self._error
            logger.info("deleted error attribute")
        except AttributeError:
            logger.info("no error attribute found")

        self._trackedfiles = {}
        self._extra_files_send = []
        self._extra_files_recv = []

        if wipe:
            if os.path.isfile(self.resultfile.local):
                os.remove(self.resultfile.local)
                logger.info("deleted result file")

            if os.path.isfile(self.errorfile.local):
                os.remove(self.errorfile.local)
                logger.info("deleted error file")

        self.state = "reset"

    def run(self, *args, **kwargs) -> None:
        """
        Run a single runner. See Dataset.run() for args.

        This function is inefficient and should not be used in a general workflow
        """
        logger.info("solo running runner %s", self)
        self.parent.run(uuids=[self.uuid], *args, **kwargs)


class RunnerFailedError:
    """
    Temporary "exception" to be passed in lieu of a missing result due to a failure.

    Args:
        message:
            error message
    """

    def __init__(self, message: str):
        self.message = message

    def __repr__(self):
        return f"RunnerFailedError('{self.message}')"
