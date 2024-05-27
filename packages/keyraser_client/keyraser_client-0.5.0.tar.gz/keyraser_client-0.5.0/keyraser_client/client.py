"""Keyraser wrapper client"""

import fcntl
import io
import os
import pathlib
import shutil
import subprocess
from typing import Dict, List, Optional, Union

from .format import Format, IdFormat
from .io import create_input, create_output


binary_paths = {}

_required_binaries = ['kr-encrypt', 'kr-decrypt', 'kr-keys']


def set_binary_path(path: str, binary: Optional[str] = None):
    """
    Define the path to use for a binary or all binaries.

    Args:
        path: The path to the directory or the individual file containing the binary.
        binary: The name of the binary, or `None` if the path points to a directory.
    """
    if binary is None:
        for binary in _required_binaries:
            binary_path = os.path.join(path, binary)
            _check_path(binary, binary_path)
    else:
        _check_path(binary, path)


def _check_path(binary, binary_path):
    if not os.path.exists(binary_path):
        raise RuntimeError(f"binary {binary} not found in path {binary_path}")
    binary_paths[binary] = binary_path


if 'KR_BINARIES' in os.environ:
    set_binary_path(os.environ['KR_BINARIES'])
else:
    for binary in _required_binaries:
        path = shutil.which(binary)
        if path is not None:
            binary_path = os.path.join(path, binary)
            _check_path(binary, binary_path)


class Client:
    """
    Class that provides the functionality of encrypting and decrypting data.

    The `Client` can be configured with two different values:

    `keystore_address` contains the hostname and port of the keystore from where the
        client will fetch the encryption keys. Defaults to `None` in which case the
        default address used in the binary is used.
    `credential_path` contains the path to a file which is used for authenticating the
        client. Defaults to `None`. In this case no explicit credential file is used,
        which requires the credential to be provided using the `KR_CREDENTIAL`
        environment variable.

    Examples:
        ```python
            import keyraser_client

            client = keyraser_client.Client(
                keystore_address='localhost:1996',
                credential_path='/my/path/to/the/client.kred',
            )
        ```

    """

    def __init__(
        self,
        *,
        keystore_address: Optional[str] = None,
        credential_path: Optional[str] = None,
    ):
        """
        Creates a new `Client`.

        Args:
            keystore_address: The string with the address of the keystore, defaults to
                `None`.
            credential_path: The file path to the credential to authenticate the
                client, defaults to `None`.
        """
        self.keystore_address = keystore_address
        self.credential_path = credential_path

    def encrypt(
        self,
        format: Format,
        src: Union[str, pathlib.Path, io.BufferedIOBase, bytes],
        dest: Union[str, pathlib.Path, io.BufferedIOBase],
    ):
        """
        Encrypts a stream of data.

        Args:
            format: The format of the data that will be encrypted.
            src: Either a path to a file or a stream from which the data is read to be
                encrypted.
            dest: Either a path to a file or a stream to which the encrypted data will
                be written.
        """
        args = [binary_paths['kr-encrypt']]

        args.extend(format.as_cli_params())

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        src_input = create_input(src)
        args.extend(src_input.cli_params())

        dest_output = create_output(dest)
        args.extend(dest_output.cli_params())

        open_kwargs: Dict = {}
        open_kwargs.update(**src_input.popen_kwargs())
        open_kwargs.update(**dest_output.popen_kwargs())
        with subprocess.Popen(args, **open_kwargs) as process:
            while not src_input.is_done() or not dest_output.is_done():
                src_input.process(process)
                dest_output.process(process)

            process.wait()

    def decrypt(
        self,
        src: Union[str, pathlib.Path, io.BufferedReader, bytes],
        dest: Union[str, pathlib.Path, io.BufferedWriter],
    ):
        """
        Decrypts an encrypted stream of data.

        Args:
            src: Either a path to a file or a stream from which the encrypted data
                will be read.
            dest: Either a path to a file or a stream to which the decrypted data will
                be written.
        """
        args = [binary_paths['kr-decrypt']]

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        src_input = create_input(src)
        args.extend(src_input.cli_params())

        dest_output = create_output(dest)
        args.extend(dest_output.cli_params())

        open_kwargs: Dict = {}
        open_kwargs.update(**src_input.popen_kwargs())
        open_kwargs.update(**dest_output.popen_kwargs())

        with subprocess.Popen(args, **open_kwargs) as process:
            if hasattr(process.stdout, 'fileno'):
                fd = process.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

            while not src_input.is_done() or not dest_output.is_done():
                src_input.process(process)
                dest_output.process(process)

            process.wait()

    def encrypt_block(
        self, entity_id: str, src: bytes, *, id_format: IdFormat = IdFormat.STRING_UTF8
    ) -> bytes:
        """
        Encrypts a single block of data.

        Args:
            entity_id: A string containing the entity id for which the data block will
                be encrypted.
            src: A single buffer containing the bytes to encrypt.
            id_format: The format of the entity_id. Defaults to using the utf8
                encoded string as entity id.

        Returns:
            bytes: A buffer containing the encrypted data block.
        """
        args = [binary_paths['kr-encrypt'], 'block']

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        src_input = create_input(src)
        args.extend(src_input.cli_params())

        buffer = io.BytesIO()
        dest_output = create_output(buffer)
        args.extend(dest_output.cli_params())

        open_kwargs: Dict = {}
        open_kwargs.update(**src_input.popen_kwargs())
        open_kwargs.update(**dest_output.popen_kwargs())

        args.extend(id_format.as_cli_params())
        args.extend(['-id', entity_id])

        with subprocess.Popen(args, **open_kwargs) as process:
            if hasattr(process.stdout, 'fileno'):
                fd = process.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

            while not src_input.is_done() or not dest_output.is_done():
                src_input.process(process)
                dest_output.process(process)

            process.wait()
            if process.returncode != 0:
                raise subprocess.CalledProcessError(
                    process.returncode, process.args, stderr=process.stderr
                )

        return buffer.getvalue()

    def decrypt_block(self, src: bytes) -> bytes:
        """
        Decrypts a single block of data.

        Args:
            src: A single buffer containing the encrypted bytes to decrypt.

        Returns:
            bytes: A buffer containing the decrypted data.
        """
        args = [binary_paths['kr-decrypt'], 'block']

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        src_input = create_input(src)
        args.extend(src_input.cli_params())

        buffer = io.BytesIO()
        dest_output = create_output(buffer)
        args.extend(dest_output.cli_params())

        open_kwargs: Dict = {}
        open_kwargs.update(**src_input.popen_kwargs())
        open_kwargs.update(**dest_output.popen_kwargs())

        with subprocess.Popen(args, **open_kwargs) as process:
            if hasattr(process.stdout, 'fileno'):
                fd = process.stdout.fileno()
                fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

            while not src_input.is_done() or not dest_output.is_done():
                src_input.process(process)
                dest_output.process(process)

            process.wait()
            if process.returncode != 0:
                raise subprocess.CalledProcessError(
                    process.returncode, process.args, stderr=process.stderr
                )

        return buffer.getvalue()

    def create_keys(
        self, entity_ids: List[str], *, id_format: IdFormat = IdFormat.STRING_UTF8
    ):
        """
        Create keys for a list of entities.

        Args:
            entity_ids: A list of strings containing the entity ids for which the keys
                will be created.
            id_format: The format of the entity ids. Defaults to using the utf8
                encoded string as entity id.
        """
        args = [binary_paths['kr-keys'], 'create']

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        args.extend(id_format.as_cli_params())

        for entity_id in entity_ids:
            args.extend(['-id', entity_id])

        subprocess.run(args, check=True)

    def delete_keys(
        self, entity_ids: List[str], *, id_format: IdFormat = IdFormat.STRING_UTF8
    ):
        """
        Delete keys for a list of entities.

        Args:
            entity_ids: A list of strings containing the entity ids for which the keys
                will be deleted.
            id_format: The format of the entity ids. Defaults to using the utf8
                encoded string as entity id.
        """
        args = [binary_paths['kr-keys'], 'delete']

        if self.keystore_address is not None:
            args.extend(["-address", self.keystore_address])

        if self.credential_path is not None:
            args.extend(["-credential", self.credential_path])

        args.extend(id_format.as_cli_params())

        for entity_id in entity_ids:
            args.extend(['-id', entity_id])

        subprocess.run(args, check=True)
