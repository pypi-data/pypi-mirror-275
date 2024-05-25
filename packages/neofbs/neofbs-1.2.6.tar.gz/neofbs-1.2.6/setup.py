long_de = """
Neofbs is a fork of fbs. The original project is locked to Python 3.5 and 3.6, which are not supported anymore. To have the more recent versions, you have to pay €50.
Obviously, the paid versions have a lot more features, but atleast with neofbs you can start a project, package it into a .exe and then package it into an installer.

To download it, simply use pip:

```
pip install neofbs
```

And then, follow the guide in the original fbs website --- the commands are the same.

See for a guide of how to use:
https://build-system.fman.io

The git repo:
https://github.com/albano-a/neofbs
"""

from os.path import relpath, join
from setuptools import setup, find_packages

import os


def _get_package_data(pkg_dir, data_subdir):
    result = []
    for dirpath, _, filenames in os.walk(join(pkg_dir, data_subdir)):
        for filename in filenames:
            filepath = join(dirpath, filename)
            result.append(relpath(filepath, pkg_dir))
    return result


description = "Create cross-platform desktop applications with Python and Qt with support for the most recent Python versions"
setup(
    name="neofbs",
    # Also update fbs/_defaults/requirements/base.txt when you change this:
    version="1.2.6",
    description=description,
    long_description=description + long_de,
    author="Andre Albano",
    author_email="geof.aalbano@gmail.com",
    url="https://albano-dev.netlify.app",
    packages=find_packages(exclude=("tests", "tests.*")),
    package_data={
        "fbs": _get_package_data("fbs", "_defaults"),
        "fbs.builtin_commands": _get_package_data(
            "fbs/builtin_commands", "project_template"
        ),
        "fbs.builtin_commands._gpg": ["Dockerfile", "genkey.sh", "gpg-agent.conf"],
        "fbs.installer.mac": _get_package_data("fbs/installer/mac", "create-dmg"),
    },
    install_requires=["PyInstaller==5.13.2"],
    extras_require={
        # Also update requirements.txt when you change this:
        "licensing": ["rsa>=3.4.2"],
        "sentry": ["sentry-sdk>=0.6.6"],
        "upload": ["boto3"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"console_scripts": ["fbs=fbs.__main__:_main"]},
    license="GPLv3 or later",
    keywords="PyQt",
    platforms=["MacOS", "Windows", "Debian", "Fedora", "CentOS", "Arch"],
    test_suite="tests",
)
