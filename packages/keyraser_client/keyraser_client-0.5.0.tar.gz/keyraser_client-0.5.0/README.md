# keyraser python client

 [![pipeline status](https://gitlab.com/kantai/keyraser/python-client/badges/mainline/pipeline.svg)](https://gitlab.com/kantai/multimeter/-/commits/mainline)
 [![coverage report](https://gitlab.com/kantai/keyraser/python-client/badges/mainline/coverage.svg)](https://gitlab.com/kantai/multimeter/-/commits/mainline)

Keyraser is a system that helps you to use key-shredding for managing data privacy in
distributed system. This python library includes a client that allows to encrypt or
decrypt data with keys that are managed by keyraser.

## What it does

The library contains a single class `Client` that exposes methods for encrypting or
decrypting data that is either provided in form of files, python io streams or `bytes`.
The data is encrypted with encryption keys that are specific for the owning entity of
the data. Encrypted data contains an identifier of the key that it was encrypted with
so it can be automatically fetched from the keyraser keystore.

## How it works

Internally the library uses the
[Keyraser client binaries](https://docs.kant.ai/keyraser/go-client) for en-/decrypting
the data. The python process communicates with the cli client in a subprocess using
stdout/stdin.

Using the library is quite easy:

```python
import keyraser_client

...

client = keyraser_client.Client(
    keystore_address='localhost:1996',
    credential_path='/path/to/credential.kred',
)

src = '/path/to/ndjson/file'
dest = '/path/to/encrypted/file'

client.encrypt(
    keyraser_client.NdjsonFormat(id_property = 'user_id'), src, dest,
)
```

After importing the module we can create a new `Client` to which we need to provide
configuration parameter like the address of the keystore, from where the keys should be
fetched and the credential that should be used for authenticating the client.
With the client we can then `encrypt` or `decrypt` by proving the arguments on where to
read the data from and where to write it into.

For more information take a look at the latest
[user guide](https://docs.kant.ai/keyraser/python-client/latest/user_guide/).

## Develop

The Keyraser python client uses [tox](https://tox.wiki/en/latest/index.html) to build and test the library.
Tox runs all tests on different python versions, can generate the documentation and run
linters and style checks to improve the code quality.
In order to install all the necessary python modules, please run:

```bash
pip install tox
```

Afterwards the tests can be run by just calling

```bash
tox
```

from the project directory. For this to work, you need to have multiple python
interpreters installed. If you don't want to run the tests on all supported platforms
just edit the tox.ini file and set
```
envlist = py38,py39,py310,py311,py312
```
to contain only the python version you want to use. Another option is to run tox with
the additional command line argument
['--skip_missing_interpreters'](https://tox.wiki/en/latest/config.html#conf-skip_missing_interpreters)
which skips python versions that aren't installed.

Alternatively, one can use [pyenv](https://github.com/pyenv/pyenv) which will use the
available python version and skip the others. For this to work, export the 
`VIRTUALENV_DISCOVERY` environment variable with a value of `pyenv`.

```bash
export VIRTUALENV_DISCOVERY=pyenv
```

## Documentation

The latest version of the documentation can always be found under https://docs.kant.ai/keyraser/python-client/latest.
The documentation is written in [Markdown](https://daringfireball.net/projects/markdown/)
and is located in the `docs` directory of the project.
It can be built into static HTML by using [MkDocs](https://www.mkdocs.org/).
In order to manually generate the documentation we can use tox to build the HTML pages from our markdown.

```bash
tox -e docs
```

## Release

### Releasing a new package version

Releasing new versions of multimeter is done using [flit](https://flit.readthedocs.io/en/latest/).

```bash
pip install flit
```

In order to be able to publish a new release, you need an account with PyPI or their
respective test environment.

Add those accounts into your `~.pypirc`:
```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username: <my-user>

[pypitest]
repository: https://test.pypi.org/legacy/
username: <my-test-user>
```


### Publishing a new release to test

```bash
flit publish --repository pypitest
```

### Releasing a new version of the documentation

The package uses [mike](https://github.com/jimporter/mike)
to manage multiple versions of the documentation. The already generated documentation is kept
in the `docs-deployment` branch and will be automatically deployed, if the branch is pushed to
the repository.

In order to build a new version of the documentation, we need to use the corresponding tox environment:

```bash
VERSION_TAG='<my-version>' tox -e docs-release
```

The `VERSION_TAG` environment variable should be set to the new version in format '<major>.<minor>'.
This will build the documentation and add it as new commits to the `docs-deployment` branch.

By pushing the updated branch to the gitlab repository, the documentation will be automatically
deployed to [the official documentation website](https://docs.kant.ai/keyraser/python-client).
