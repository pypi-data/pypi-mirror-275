#!/usr/bin/env python
"""The setup script."""
import os
import re
import sys

from hatchling.metadata.plugin.interface import MetadataHookInterface


class MetaDataHook(MetadataHookInterface):
    """Custom Meta Data Hook to intercept in Hatch build system."""

    def update(self, metadata):
        """Provide dynamic values of package meta data."""
        metadata["version"] = get_version()
        metadata["license"] = "MIT"
        metadata["authors"] = [
            {"name": "Franck Nijhof", "email": "frenck@frenck.dev"},
            {"name": "Aäron Munsters"},
        ]
        metadata["maintainers"] = [{"name": "Aäron Munsters"}]
        metadata["description"] = "Asynchronous Python client for the Fumis WiRCU API."
        metadata["classifiers"] = [
            "Framework :: AsyncIO",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Home Automation",
        ]
        metadata["readme"] = {"file": "README.md", "content-type": "text/markdown"}
        metadata["requires-python"] = ">=3.10"

        # TODO: compute this automatically
        metadata["dependencies"] = ["aiohttp>=3.9.5", "async-timeout>=4.0.3", "yarl"]
        metadata["keywords"] = ["fumis", "wircu", "api", "async", "client"]


def get_version():
    """Get current version from code."""
    regex = r"__version__\s=\s\"(?P<version>[\d\.]+?)\""
    path = ("fumis_wircu", "__version__.py")
    return re.search(regex, read(*path)).group("version")


def read(*parts):
    """Read file."""
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)
    sys.stdout.write(filename)
    with open(filename, encoding="utf-8") as fp:
        return fp.read()
