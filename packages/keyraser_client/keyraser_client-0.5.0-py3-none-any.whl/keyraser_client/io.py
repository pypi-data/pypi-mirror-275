"""IO specific classes"""

import io
import pathlib
import subprocess
import typing


class _Input:
    """
    Base class that represents an input from which data can be read.
    """

    def is_done(self) -> bool:
        """
        Called to determine if there is no further data to read.

        Returns: `True` if the end of data has been reached, otherwise `False`.
        """
        return True

    def process(self, process: subprocess.Popen):
        """
        Called to copy input data from the input to a subprocess.
        """

    def cli_params(self) -> typing.List[str]:
        """
        CLI params to use the input with the keyraser client.
        """
        return []

    def popen_kwargs(self) -> typing.Dict:
        """
        Kwargs that need to be setup when creating the subprocess.
        """
        return {}


class _FileInput(_Input):
    """
    Class that represents a file from which data can be read.
    """

    def __init__(self, src_path: pathlib.Path):
        self.src_path = src_path

    def cli_params(self) -> typing.List[str]:
        return ["-input", str(self.src_path)]

    def popen_kwargs(self) -> typing.Dict:
        return {}


class _StreamInput(_Input):
    """
    Class that represents a stream from which data can be read.
    """

    def __init__(self, reader: io.BufferedIOBase):
        self.reader = reader
        self.buffer = bytearray(1000000)
        self.read = -1

    def is_done(self) -> bool:
        return 0 == self.read

    def process(self, process):
        self.read = self.reader.readinto(self.buffer)
        if self.read > 0:
            process.stdin.write(self.buffer[: self.read])
        else:
            process.stdin.close()

    def cli_params(self) -> typing.List[str]:
        return []

    def popen_kwargs(self) -> typing.Dict:
        return {'stdin': subprocess.PIPE}


class _Output:
    """
    Base class that represents an output to which data can be written.
    """

    def is_done(self) -> bool:
        """
        Called to determine if there is no further data to write.

        Returns: `True` if the end of data has been reached, otherwise `False`.
        """
        return True

    def process(self, process: subprocess.Popen):
        """
        Called to copy output data from the subprocess to the output.
        """

    def cli_params(self) -> typing.List[str]:
        """
        CLI params to use the output with the keyraser client.
        """
        return []

    def popen_kwargs(self) -> typing.Dict:
        """
        Kwargs that need to be setup when creating the subprocess.
        """
        return {}


class _FileOutput(_Output):
    """
    Class that represents a file to which data can be written.
    """

    def __init__(self, dest_path: pathlib.Path):
        self.dest_path = dest_path

    def cli_params(self) -> typing.List[str]:
        return ["-output", str(self.dest_path)]

    def popen_kwargs(self) -> typing.Dict:
        return {}


class _StreamOutput(_Output):
    """
    Class that represents a stream to which data can be written.
    """

    def __init__(self, writer: io.BufferedIOBase):
        self.writer = writer
        self.buffer = bytearray(1000000)
        self.read = -1

    def is_done(self) -> bool:
        return 0 == self.read

    def process(self, process):
        self.read = process.stdout.readinto(self.buffer)
        if self.read is not None:
            if self.read > 0:
                self.writer.write(self.buffer[: self.read])
            else:
                process.stdout.close()

    def cli_params(self) -> typing.List[str]:
        return []

    def popen_kwargs(self) -> typing.Dict:
        return {'stdout': subprocess.PIPE}


def create_input(
    src: typing.Union[str, pathlib.Path, io.BufferedIOBase, bytes]
) -> _Input:
    """
    Create a new `_Input` instance that interfaces with the input of the keyraser
    binaries.

    Args:
        src: Source where the input comes from.

    Returns:
        The `_Input` implementation from which a input can be read.
    """
    if isinstance(src, pathlib.Path):
        return _FileInput(src)
    if isinstance(src, str):
        return _FileInput(pathlib.Path(src))
    if isinstance(src, bytes):
        return _StreamInput(io.BytesIO(src))
    if isinstance(src, io.IOBase):
        return _StreamInput(src)
    raise ValueError(f"Unsupported input src {src}")


def create_output(
    dest: typing.Union[str, pathlib.Path, io.BufferedIOBase, bytes]
) -> _Output:
    """
    Create a new `_Output` instance that interfaces with the output of the keyraser
    binaries.

    Args:
        dest: Destination where the output result should end up in.

    Returns:
        The `_Output` implementation from which a result can be read.
    """
    if isinstance(dest, pathlib.Path):
        return _FileOutput(dest)
    if isinstance(dest, str):
        return _FileOutput(pathlib.Path(dest))
    if isinstance(dest, io.IOBase):
        return _StreamOutput(dest)
    raise ValueError(f"Unsupported output dest {dest}")
