"""
Python client library for the Keyraser key shredding system

This library contains a client implementation wrapping around the keyraser command line
binaries that allow to encrypt/decrypt data using the Keyraser key shredding system.

In order to use the library, it requires to know the location of the binaries.
As a default the library looks for them within the PATH by using `shutil.which()`.
If this doesn't work, one has to define the location of the keyraser binaries
that are called by the wrapper class. This can happen using in two ways:

Define the `KR_BINARIES` environment variable

If this environment variable is specified, the library expects all binaries to be
located in the directory, that its value points to. If a binary is missing, a
`RuntimeError` is raised.

Define the binary paths by using `set_binary_path(path, binary=None)`

This function takes in either the path of a directory containing all binaries or a
path to a file together with the name of a binary that this path is used for. If the
path is not valid or a binary can't be found at the location, a `RuntimeError` is
raised.
"""

from .client import Client, IdFormat, set_binary_path
from .format import NdjsonFormat


__version__ = '0.5.0'
