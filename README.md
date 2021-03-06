yum-repo-client [![Build Status](https://travis-ci.org/ImmobilienScout24/yum-repo-client.svg?branch=master)](https://travis-ci.org/ImmobilienScout24/yum-repo-client)
===============

## Aim
_yum-repo-client_ is a command line interface for interacting with the [yum-repo-server](https://github.com/ImmobilienScout24/yum-repo-server).
The aim is to provide a command line wrapper for every functionality the yum-repo-server provides so you don't have to fiddle with REST requests.
This is especially good for automations that can run command line tools because you can modify the [yum-repo-server](https://github.com/ImmobilienScout24/yum-repo-server) as you wish without breaking your automation (provided you include the modifications in the yum-repo-client).

## Usage
After installation the toplevel command ```repoclient``` will be available.
### Available commands
 * create
 * deleterpm
 * deletestatic
 * deletevirtual
 * generatemetadata
 * linktostatic
 * linktovirtual
 * propagate
 * propagaterepo
 * querystatic
 * queryvirtual
 * queryrpm
 * redirectto
 * taglist
 * tag
 * untag
 * uploadto

Please consult ```repoclient -h``` for more information.

## Getting started
### Building the yum-repo-client
Start by installing all required dependencies (runtime + build):

```python
pip install -r requirements.txt
```

Then it is recommended to run the tests:
<code>
python setup.py test
</code>

These should always be successful.
#### Build RPM
Optionally after that you can run:
<code>
python setup.py bdist_rpm
</code>
to get an rpm of the yum-repo-client.
#### Build DEB
To build a DEB package first install python-stdeb and then run:
<code>
python setup.py --command-packages=stdeb.command bdist_deb
</code>
The resulting deb package will be in the `deb_dist` subfolder. Please keep in mind that in most cases it is not a good idea to build RPMs on Debian as the RPM dependencies can go horribly wrong. Creating Source RPMs should be less problematic.

### Installing the yum-repo-client
If you have built a rpm file in the step above, then you can install it as usual.

Without the rpm file you can install the yum-repo-client with:

<code>
python setup.py install
</code>

Make sure you installed the build and runtime dependencies as described above. 

#### Mac installation
Installation works on Mac as described above, too. Only the rpmsearch command will not work, as it requires rpmbuild installed.

If you do not have pip installed, execute

<code>
sudo easy_install pip
</code> 

After that you may need to get a fresh shell. 


### Static configuration
To set the default host and port used by the yum-repo-client, you need to edit (or create) the file `/etc/yum-repo-client.yaml`.
This file may contain any of the following entries :
`DEFAULT_HOST : localhost`
`DEFAULT_PORT : 8000`
`DEFAULT_CONTEXT`: `/yum-repo-server`

### Nicer yum-repo-server error messages
If [the html2text library](https://github.com/mriehl/html2text) is installed in the same environment as yum-repo-client (`pip install html2text` in its most simple form) then yum-repo-client will render yum-repo-server error responses in **markdown** (instead of the pile of inline CSS you usually get with tomcat for example).

If `html2text` is not installed, you'll get the raw HTML/CSS (best effort).
