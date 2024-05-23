import time
from typing import Union

from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils import dir_delta

import os


class TrackedFile(SendableMixin):
    __slots__ = ["_remote_path", "_local_path", "_file", "_last_seen", "_size"]

    def __init__(self, local_path: str, remote_path: str, file: str):
        self._remote_path = remote_path
        self._local_path = local_path
        self._file = file

        self._last_seen = {"remote": -1, "local": -1}
        self._size = -1

    def __repr__(self) -> str:
        return self.local

    def __fspath__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        """Returns the filename"""
        return self._file

    @property
    def importstr(self) -> str:
        """
        Returns the filename without extension

        Suitable for python imports
        """
        return os.path.splitext(self._file)[0]

    @property
    def remote(self) -> str:
        """Returns the full remote path"""
        return os.path.join(self._remote_path, self.name)

    @property
    def local(self) -> str:
        """Returns the full local path"""
        return os.path.join(self._local_path, self.name)

    @property
    def remote_dir(self) -> str:
        """Returns the remote dir"""
        return self._remote_path

    @property
    def local_dir(self) -> str:
        """Returns the full local dir"""
        return self._local_path

    def relative_remote_path(self, other: str) -> str:
        """
        Return a path relative to `cwd`

        Args:
            other:
                working dir to compare against

        Returns:
            relative path
        """
        # if our remote path is an abspath, we already have what we need
        if os.path.isabs(self.remote_dir):
            return self.remote

        # we're already in the remote, just return the filename
        if self.remote_dir == other:
            return self.name

        # find the deepest shared path, treat it as a "root"
        stem = os.path.commonpath([self.remote_dir, other])
        # find how far down this stem is from `other`
        dirdelta = dir_delta(stem, other)
        # generate a ../ string that steps "down" to the common path
        down = "../" * dirdelta

        tmp_remote = self.remote_dir.replace(stem, "").strip("/")
        # rebuild up from our virtual root
        return os.path.join(down, tmp_remote, self.name)

    @property
    def content(self) -> Union[str, None]:
        """
        Attempts to read the file contents

        Returns None if the file cannot be read
        """
        if not os.path.isfile(self.local):
            return None
        with open(self.local, "r") as o:
            self.confirm_local()
            return o.read()

    def _write(
        self, content: Union[str, list], append: bool, add_newline: bool
    ) -> None:
        """
        Write to the file

        Args:
            content:
                Content to add
            append:
                Appends to file if True, overwrites otherwise
            add_newline:
                Finish the write with an extra newline if True
        """
        if not os.path.isdir(self.local_dir):
            os.makedirs(self.local_dir)
        # try to join lists, falling back on a basic str coercion
        if not isinstance(content, str):
            try:
                content = "\n".join(content)
            except TypeError:
                content = str(content)

        if append:
            mode = "a+"
        else:
            mode = "w+"

        with open(self.local, mode) as o:
            o.write(content)

            if add_newline and not content.endswith("\n"):
                o.write("\n")

        self.confirm_local()

    def write(self, content: Union[str, list], add_newline: bool = True) -> None:
        """
        Write `content` to the local copy of the file

        Args:
            content:
                content to write
            add_newline:
                enforces a newline character at the end of the write if True
                (default True)
        """
        self._write(content, append=False, add_newline=add_newline)

    def append(self, content: Union[str, list], add_newline: bool = True) -> None:
        """
        Append `content` to the local copy of the file

        Args:
            content:
                content to append
            add_newline:
                enforces a newline character at the end of the write if True
                (default True)
        """
        self._write(content, append=True, add_newline=add_newline)

    def confirm_local(self, t: Union[int, None] = None) -> None:
        """
        Confirm sighting of the file locally

        Args:
            t: Optionally set the time to `t` instead of time.time()
        """
        if t is None:
            t = int(time.time())
        self._last_seen["local"] = t

    def confirm_remote(self, t: Union[int, None] = None) -> None:
        """
        Confirm sighting of the file on the remote

        Args:
            t: Optionally set the time to `t` instead of time.time()
        """
        if t is None:
            t = int(time.time())
        self._last_seen["remote"] = t

    @property
    def exists_local(self) -> bool:
        """Returns True if the file exists locally"""
        return os.path.exists(self.local)

    def last_seen(self, where: str) -> int:
        """
        Returns the last_seen_<where>

        Where <where> is remote or local

        Args:
            where:
                remote or local
        """
        return self._last_seen[where]

    @property
    def last_seen_local(self) -> int:
        """Returns the time this file was last confirmed seen on the local machine"""
        return self.last_seen("local")

    @property
    def last_seen_remote(self) -> int:
        """Returns the time this file was last confirmed seen on the remote machine"""
        return self.last_seen("remote")

    @property
    def size(self) -> int:
        """
        Returns the filesize (needs to be set externally)

        -1 if not set
        """
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        """Sets the filesize"""
        self._size = size
