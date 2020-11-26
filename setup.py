"""
setup.py
~~~~~~~~

"""

import setuptools
import versioneer

with open("README.md", "r") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

# These should all remain the same.
NAME = "EzPyZ"
DESCRIPTION = ""
AUTHOR = "Ethan Guthrie"
PACKAGES = setuptools.find_packages()

# These should change.
version = versioneer.get_version()
cmdclass = versioneer.get_cmdclass()

# Setup will be done using the information in setup.cfg
setuptools.setup()
