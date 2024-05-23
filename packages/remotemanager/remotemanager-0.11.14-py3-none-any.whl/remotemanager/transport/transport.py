"""
Baseclass for any file transfer
"""

import logging
import os.path
from typing import Union

from remotemanager.logging.decorate_verbose import make_verbose
from remotemanager.logging.verbosity import Verbosity
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.storage.trackedfile import TrackedFile
from remotemanager.utils import ensure_list, ensure_dir
from remotemanager.utils.flags import Flags

logger = logging.getLogger(__name__)


@make_verbose
class Transport(SendableMixin):
    """
    Baseclass for file transfer

    Args:
        url (URL):
            url to extract remote address from
        dir_mode:
            compatibility mode for systems that do not accept multiple explicit
            files per transfer, copies files to a directory then pulls it
    """

    _do_not_package = ["_url"]

    def __init__(
        self,
        url=None,
        dir_mode: bool = False,
        flags: str = None,
        verbose: Union[None, int, bool, "Verbosity"] = None,
        *args,
        **kwargs,
    ):
        self.verbose = verbose
        self._remote_address = None

        if url is None:
            # deferred import required to prevent circular import issue with URL
            from remotemanager.connection.url import URL

            url = URL()

        self._url = url
        self.set_remote(url)

        if flags is not None:
            self._flags = Flags(str(flags))
        else:
            self._flags = Flags()

        self._transfers = {}
        self._cmds = []
        self._request_stream = False

        self._dir_mode = dir_mode

    @property
    def dir_mode(self) -> bool:
        return self._dir_mode

    @dir_mode.setter
    def dir_mode(self, mode: bool):
        self._dir_mode = mode

    def queue_for_push(
        self, files: [list, str, TrackedFile], local: str = None, remote: str = None
    ):
        """
        Queue file(s) for sending (pushing)

        Args:
            files (list[str], str, TrackedFile):
                list of files (or file) to add to push queue
            local (str):
                local/origin folder for the file(s)
            remote (str):
                remote/destination folder for the file(s)
        Returns:
            None
        """
        if isinstance(files, TrackedFile):
            logger.info("adding TrackedFile %s to PUSH queue)", files.name)
            self.add_transfer(files.name, files.local_dir, files.remote_dir, "push")
            return
        logger.info(
            "adding to PUSH queue)",
        )
        self.add_transfer(files, local, remote, "push")

    def queue_for_pull(
        self, files: [list, str, TrackedFile], local: str = None, remote: str = None
    ):
        """
        Queue file(s) for retrieving (pulling)

        Args:
            files (list[str], str, TrackedFile):
                list of files (or file) to add to pull queue
            local (str):
                local/destination folder for the file(s)
            remote (str):
                remote/origin folder for the file(s)
        Returns:
            None
        """
        if isinstance(files, TrackedFile):
            logger.info("adding TrackedFile %s to PULL queue)", files.name)
            self.add_transfer(files.name, files.remote_dir, files.local_dir, "pull")
            return
        logger.info(
            "adding to PULL queue)",
        )
        self.add_transfer(files, remote, local, "pull")

    def add_transfer(self, files: [list, str], origin: str, target: str, mode: str):
        """
        Create a transfer to be executed. The ordering of the origin/target
        files should be considered as this transport instance being a
        "tunnel" between wherever it is executed (origin), and the destination
        (target)

        Args:
            files (list[str], str):
                list of files (or file) to add to pull queue
            origin (str):
                origin folder for the file(s)
            target (str):
                target folder for the file(s)
            mode (str: "push" or "pull"):
                transfer mode. Chooses where the remote address is placed
        Returns:
            None
        """
        modes = ("push", "pull")
        if mode.lower() not in modes:
            raise ValueError(f"mode must be one of {modes}")

        if origin is None:
            origin = "."
        if target is None:
            target = "."

        # ensure dir-type
        origin = os.path.join(origin, "")
        target = os.path.join(target, "")

        if mode == "push":
            pair = f"{origin}>{self._add_address(target)}"
        else:
            pair = f"{self._add_address(origin)}>{target}"

        files = [os.path.split(f)[1] for f in ensure_list(files)]

        logger.info(
            "adding transfer: %s -> %s",
            Transport.split_pair(pair)[0],
            Transport.split_pair(pair)[1],
        )
        logger.info("for files %s", files)

        if pair in self._transfers:
            self._transfers[pair] = self._transfers[pair].union(set(files))
        else:
            self._transfers[pair] = set(files)

    def _add_address(self, dir: str) -> str:
        """
        Adds the remote address to the dir `dir` if it exists

        Args:
            dir (str):
                remote dir to have address appended

        Returns:
            (str) dir
        """
        if self.address is None:
            return dir
        return f"{self.address}:{dir}"

    @staticmethod
    def _format_for_cmd(folder: str, inp: list) -> str:
        """
        Formats a list into a bash expandable command with brace expansion

        Args:
            folder (str):
                the dir to copy to/from
            inp (list):
                list of items to compress

        Returns (str):
            formatted cmd
        """

        if isinstance(inp, str):
            raise ValueError(
                "files is stringtype, " "was a transfer forced into the queue?"
            )

        if len(inp) > 1:
            return os.path.join(folder, "{" + ",".join(inp) + "}")
        return os.path.join(folder, inp[0])

    @property
    def transfers(self) -> dict:
        """
        Return the current transfer dict

        Returns (dict):
            {paths: files} transfer dict
        """
        return {k: sorted(list(v)) for k, v in self._transfers.items()}

    def print_transfers(self):
        """
        Print a formatted version of the current queued transfers

        Returns:
            None
        """
        i = 0
        for pair, files in self.transfers.items():
            i += 1
            print(
                f"transfer {i}:"
                f"\norigin: {Transport.split_pair(pair)[0]}"
                f"\ntarget: {Transport.split_pair(pair)[1]}"
            )
            j = 0
            for file in files:
                j += 1
                print(f"\t({j}/{len(files)}) {file}")

    @property
    def address(self):
        """
        return the remote address

        Returns (str):
            the remote address
        """
        return self._remote_address

    @address.setter
    def address(self, remote_address):
        """
        set the remote address

        Returns:
            None
        """
        self._remote_address = remote_address

    @property
    def url(self) -> "URL":  # noqa: F821
        if self._url is not None:
            return self._url
        import remotemanager.connection.url as url

        return url.URL()

    @url.setter
    def url(self, url):
        self._url = url

    def set_remote(self, url=None):
        """
        set the remote address with a URL object

        Returns:
            None
        """
        logger.info("setting rsync url to %s", url)
        if url is None:
            logger.info(
                "url is None, setting None)",
            )
            self._remote_address = None
        elif url.is_local:
            logger.info(
                "url is local, setting None)",
            )
            self._remote_address = None
        else:
            logger.info(
                "url okay, setting)",
            )
            self._remote_address = url.userhost
            self.url = url

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, new):
        self._flags = Flags(str(new))

    def cmd(self, primary, secondary):
        """
        Returns a formatted command for issuing transfers. It is left to
        the developer to implement this method when adding more transport
        classes.

        The implementation should take two strings as arguments, `primary` and
        `secondary`:

        `primary`: This is the source folder, containing the files for transfer

        `secondary`: This is the destination folder for the files

        At its most basic:

        ```
        def cmd(self, primary, secondary):
            cmd = "command {primary} {secondary}"
            base = cmd.format(primary=primary,
                                    secondary=secondary)
            return base
        ```

        You can, of course, extend upon this. View the included transport
        methods for ideas on how to do this.

        Returns (str):
            formatted command for issuing a transfer
        """
        raise NotImplementedError

    def transfer(
        self,
        dry_run: bool = False,
        prepend: bool = True,
        raise_errors: bool = True,
        dir_mode: bool = None,
        verbose: Union[None, int, bool, Verbosity] = None,
    ):
        """
        Perform the actual transfer

        Args:
            dry_run (bool):
                do not perform command, just return the command(s) to be
                executed
            prepend (bool):
                enable forced cmd prepending
            raise_errors (bool):
                will not raise any stderr if False
            dir_mode:
                compatibility mode for systems that do not accept multiple explicit
                files per transfer, copies files to a directory then pulls it

        Returns (str, None):
            the dry run string, or None
        """
        if verbose is not None:
            verbose = Verbosity(verbose)
        else:
            verbose = self.verbose

        logger.info("executing a transfer")

        if dir_mode is None:
            dir_mode = self._dir_mode

        commands = []
        tmp_dirs = {}  # temporary directory storage if we're running dir_mode
        for pair, files in self.transfers.items():
            primary, secondary = Transport.split_pair(pair)

            if dir_mode and len(files) > 1:
                # directory based compatibility mode.
                # First, create a temp dir to copy files to using cp -r
                # Then set the primary to this dir, and files to "*"
                local = ":" not in primary

                if not local:
                    tmp_remote, tmp_primary = primary.split(":")
                else:
                    tmp_remote = None
                    tmp_primary = primary

                tmp_dirname = f"tmp_copy_{tmp_primary}"
                self.url.cmd(
                    f"mkdir -p {tmp_dirname} && cp -r "
                    f"{self._format_for_cmd(tmp_primary, files)} {tmp_dirname}",
                    prepend=prepend,
                    raise_errors=raise_errors,
                    local=local,
                )

                if tmp_remote is not None:
                    primary = f"{tmp_remote}:{tmp_dirname}"
                else:
                    primary = tmp_dirname

                files = ["*"]

                tmp_dirs[tmp_dirname] = local

            primary = self._format_for_cmd(primary, files)

            base_cmd = self.cmd(primary=primary, secondary=secondary)

            commands.append(base_cmd)

        if dry_run:
            self._cmds = [
                self.url.cmd(cmd, dry_run=True, local=True, prepend=prepend)
                for cmd in commands
            ]
            return self._cmds

        nfiles = sum(len(filelist) for filelist in self.transfers.values())
        filestr = "File" if nfiles == 1 else "Files"

        msg = ["Transferring", str(nfiles), filestr]

        ntransfers = len(self.transfers)
        if ntransfers > 1:
            msg += ["in", str(ntransfers), "Transfers"]

        end = "\n" if self._request_stream else "... "

        verbose.print(" ".join(msg), end=end, level=1)
        try:
            self._cmds = [
                self.url.cmd(
                    cmd,
                    local=True,
                    prepend=prepend,
                    verbose=verbose,
                    raise_errors=raise_errors,
                    stream=self._request_stream,
                )
                for cmd in commands
            ]
        except Exception as ex:
            verbose.print("Error", level=1)
            raise ex
        else:
            verbose.print("Done", level=1)
        # wipe the transfer queue
        self.wipe_transfers()

        # clean up if we have created temporary dirs
        for dir, local in tmp_dirs.items():
            self.url.cmd(
                f"rm -rf {dir}", prepend=prepend, raise_errors=raise_errors, local=local
            )

    def wipe_transfers(self):
        logger.info("wiping transfers")
        self._transfers = {}

    @property
    def cmds(self):
        return self._cmds

    @staticmethod
    def split_pair(pair: str) -> list:
        """
        Convert a "dir>dir" string into list format

        Args:
            pair (tuple):
                (dir, dir) tuple to be split

        Returns (list):
            [dir, dir]

        """
        return [ensure_dir(os.path.split(p)[0]) for p in pair.split(">")]

    @staticmethod
    def get_remote_dir(path):
        if ":" not in path:
            return path
        return path.split(":")[1]
