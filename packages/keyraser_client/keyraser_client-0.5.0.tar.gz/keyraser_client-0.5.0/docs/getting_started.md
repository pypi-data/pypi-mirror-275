# Getting started

## Install the library

Install the latest version from [PyPI](https://pypi.org/project/keyraser_client/)
using pip:

```bash
pip install keyraser_client
```

## Install the client binaries

Please follow the general keyraser documentation for information on how to setup
a keystore, create the credentials and install the client binaries.

## Create a `keyraser_client.Client` in your python script

```python
import keyraser_client

client = keyraser_client.Client(
    keystore_address='localhost:1996',
    credential_path='/path/to/credential.kred',
)

```

## Encrypt a newline delimited json file

```python
...

src = '/path/to/ndjson/file'
dest = '/path/to/encrypted/file'

client.encrypt(
    keyraser_client.NdjsonFormat(id_property = 'user_id'), src, dest,
)
```



## Decrypt a file

```python
...

src = '/path/to/encrypted/file'
dest = '/path/to/decrypted/file'

client.decrypt(src, dest)
```

## Where to go from here?

Read the [user guide](../user_guide/) for some more in-depth explanation about
the individual functionalities provided by keyraser.
