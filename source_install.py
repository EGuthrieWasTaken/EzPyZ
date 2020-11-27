"""
source_install.py
~~~~~~~~~~~~~~~~~
Downloads the tarball of the latest release of EzPyZ and unzips it to install from source.
"""

import requests
import tarfile

try:
    # Download latest tarball.
    print("Downloading latest tarball release...")
    r = requests.get("https://api.github.com/repos/EGuthrieWasTaken/EzPyZ/releases")
    DOWNLOAD_URL = str(r.json()[0]["tarball_url"])
    FILENAME = "EzPyZ-" + DOWNLOAD_URL.split("/")[-1] + ".tar.gz"
    r2 = requests.get(DOWNLOAD_URL)
    if r2.status_code == 200:
        with open(FILENAME, 'wb') as tar_file:
            for chunk in r2.iter_content(chunk_size=128):
                tar_file.write(chunk)
    
    # Extract tarball.
    print("Extracting tarball...")
    tar = tarfile.open(FILENAME, "r:gz")
    tar.extractall()
    tar.close()

    # Print final instructions to install from source.
    print(
        "Extraction complete! To finish installing from source, switch into the extracted directory"
        + " and run \"pip3 install .\" or \"python3 setup.py install\"."
    )
except Exception as e:
    print("An exception has occured. Please try again later.")
    print(e)
