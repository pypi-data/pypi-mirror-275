# User guide

This user guide can be used as a starting point for getting a deeper understanding of
the inner workings of the keyraser_client library. It is meant for users who want to learn
about individual details.

## Install the library

The library can be installed in two different ways:

### Use stable release from PyPI

All stable versions of keyraser_client are available on
[PyPI](https://pypi.org/project/keyraser_client/)
and can be downloaded and installed from there. The easiest option to get it installed
into your python environment is by using `pip`:

```bash
pip install keyraser_client
```

### Use from source

The [python-client's Git repository](https://gitlab.com/kantai/keyraser/python-client/-/tree/mainline) is
available for everyone and can easily be cloned into a new repository on your local
machine:

```bash
$ cd /your/local/directory
$ git clone https://gitlab.com/keyraser/python-client.git
$ cd python-client
```

If you want to make changes to library, please follow the guidance in the
[README.md](https://gitlab.com/kantai/keyraser/python-client/-/blob/mainline/README.md) on how
to setup the necessary tools for testing your changes.

If you just want to use the library, it is sufficient to add the path to your local
python-client repository to your `$PYTHONPATH` variable, e.g.:

```bash
$ export PYTHONPATH="$PYTHONPATH:/your/local/directory/python-client"
```

## How the python client works

First we start with some high-level description of the individual parts of the library.

### Client

[`Client`](api.md#keyraser_client.Client) is the central class which is
used by the user to interact with keyraser. The `Client` takes the configuration, that
defines to which keystore the client should connect and which credential should be
used for authenticating the client. This configuration is usually given directly as
constructor arguments, when instantiating the object:

```python
import keyraser_client

...

client = keyraser_client.Client(
    keystore_address='localhost:1996',
    credential_path='/path/to/my/credential.kred',
)
```
