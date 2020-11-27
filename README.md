# EzPyZ ![Travis (.com) branch](https://img.shields.io/travis/com/EGuthrieWasTaken/EzPyZ/main) ![PyPI](https://img.shields.io/pypi/v/EzPyZ) ![PyPI - License](https://img.shields.io/pypi/l/EzPyZ) ![PyPI - Status](https://img.shields.io/pypi/status/EzPyZ)

Welcome to EzPyZ! This project seeks to provide an easy-to-use statistical library for Python 3. This project was inspired in concept by the [ez](https://github.com/mike-lawrence/ez) library available in R.  

**This project is under development, and will likely not work as intended. You have been warned.**

## Installation ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/EGuthrieWasTaken/EzPyZ) ![PyPI - Downloads](https://img.shields.io/pypi/dw/EzPyZ) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/EzPyZ) ![PyPI - Format](https://img.shields.io/pypi/format/EzPyZ)

This package is installed using pip. Pip should come pre-installed with all versions of Python for which this package is compatible. Nonetheless, if you wish to install pip, you can do so by downloading [get-pip.py](https://pip.pypa.io/en/stable/installing/) and running that python file (Windows/MacOS/Linux/BSD), or you can run the following command in terminal (Linux/BSD):

```bash
sudo apt install python3-pip
```

If you're using brew (most likely for MacOS), you can install pip (along with the rest of Python 3) using brew:

```bash
brew install python3
```

**Note: The creator of this software does not recommend the installation of python or pip using brew, and instead recommends that pip be installed using [get-pip.py](https://pip.pypa.io/en/stable/installing/), or that Python 3.7+ be installed using the installation candidates found on [python.org](https://www.python.org/downloads/), which include pip by default.**

### Using Pip to install from PyPi

Fetching this repository from PyPi is the recommended way to install this package. From your terminal, run the following command:

```bash
pip3 install EzPyZ
```

And that's it! Now you can go right ahead to the quick-start guide!

### Install from Source

Not a big fan of pip? Well, you're weird, but weird is OK! I've written a separate script to help make installation from source as easy as possible. To start, download the installation script and run it:

```bash
wget https://raw.githubusercontent.com/EGuthrieWasTaken/EzPyZ/main/source_install.py
python3 source_install.py
```

After completing, the script will have downloaded the latest tarball release and extracted it into the working directory. Now, all you have to do is switch into the newly-extracted directory and run the install command:

```bash
cd EGuthrieWasTaken-EzPyZ-[commit_id]/
python3 setup.py install
```

Congratulations, you just installed EzPyZ from source! Feel free to check out the quick-start guide!

## Quick-Start Guide

Now that you have the package installed, getting started with the package should be easy! You can start with importing the package and creating a ``DataFrame``:

```python
import EzPyZ as ez

# Create new dataframe.
raw_data = {
    'height (cm)': [134, 168, 149, 201, 177],
    'weight (kg)': [32.2, 64.3, 59.9, 95.4, 104.2]
}
df = ez.DataFrame(data=raw_data)
```

Already have a ``pandas.DataFrame`` object? Great! You can create an ``EzPyZ.DataFrame`` object with an existing ``pandas.DataFrame``:

```python
import EzPyZ as ez
import pandas as pd

# Create new dataframe.
raw_data = {
    'height (cm)': [134, 168, 149, 201, 177],
    'weight (kg)': [32.2, 64.3, 59.9, 95.4, 104.2]
}
pandas_df = pd.DataFrame(raw_data)
df = ez.DataFrame(data=pandas_df)
```

Of course, most of the time you will not be hard-coding your data directly. Fortunately this package comes with tools to help with that as well! Check it out:

```python
import EzPyZ as ez
from EzPyZ.tools import read_file

df = ez.DataFrame(data=read_file("bmi_data.csv")) # A bmi_data.xlsx would also work here.
```

That should be enough to get you off the ground! To learn more, check out the documentation.

**Note: the creator(s) of this software will not be liable for any unintended results from using EzPyZ software. For complete information regarding liability, see the [License](https://github.com/EGuthrieWasTaken/EzPyZ/blob/main/LICENSE).**  

## Documentation

Documentation for this project can be found in the GitHub Repository. Each folder has it's own documentation for the class files it contains. The documentation tree is below:

* [EzPyZ](https://github.com/EGuthrieWasTaken/EzPyZ/tree/main/EzPyZ)
  * [tools](https://github.com/EGuthrieWasTaken/EzPyZ/tree/main/EzPyZ/tools)
