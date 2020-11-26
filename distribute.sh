#!/bin/zsh

# Getting new version.
currVersion=$( cat VERSION )
echo "Current version: $currVersion"
echo "Enter new version name: "
read newVersion
echo $newVersion > VERSION
echo "Version: $currVersion -> $newVersion"

# Adding and commit new version.
git add VERSION
git commit -m "Update version number"
git push origin master

# Tagging newest version and uploading tarball to GitHub.
git tag $newVersion
git push; git push --tags

# Uploading to PyPi.
sudo python3 setup.py develop
sudo python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
