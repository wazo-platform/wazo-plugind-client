# wazo-plugind-client

A python client library to access wazo-plugind

## Usage

### Creating a client

```python
from wazo_plugind_client import Client
client = Client('localhost', verify_certificate=False, token=<xivo-auth-token>)
```

### Installing a plugin from a git URL

```python
client.plugins.install(<url>, 'git')
```

### Getting the service configuration

```python
client.config()
```

## Debian package

Follow the following steps to build a debian package for wazo-plugind-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-plugind-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
