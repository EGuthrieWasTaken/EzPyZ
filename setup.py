"""
setup.py
~~~~~~~~

"""

import setuptools
import versioneer

with open("README.md", "r") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

# Setup will be done using the information in setup.cfg
setuptools.setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
