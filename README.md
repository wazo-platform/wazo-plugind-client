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

### Installing a plugin from a git URL in a branch or a tag

```python
client.plugins.install(<url>, 'git', options={'ref': '<branch or tag>'})
```

### Listint plugins available for installation

```python
# List all plugins
client.market.list()

# List for official plugins
client.market.list('official')

# Order plugins by name ascending with pagination
client.market.list(order='name', direction='asc', limit=5, offset=10)
```

### Listing installed plugins

```python
client.plugins.list()
```


### Getting the metadata of an installed plugin

```python
client.plugins.get(<namespace>, <name>)
```

### Uninstalling a plugin

```python
client.plugins.uninstall(<namespace>, <name>)
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
