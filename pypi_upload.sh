#!/usr/bin/env bash
# 'set -e' stops the execution of a script if a command or pipeline has an error.
# This is the opposite of the default shell behaviour, which is to ignore errors in scripts.
set -e

echo -e "\nCleaning up existing pieces"
rm -rf dist *.egg-info

echo -e "\nUpgrading pip"
python -m pip install --upgrade pip

echo -e "\nInstalling dependencies"
pip install build twine

echo -e "\nCreating package"
python -m build

echo -e "\nRunning twine check"
twine check dist/*

read -p "Are you sure you want to proceed uploading to pypi? <Y/N> " prompt
if [[ $prompt =~ [yY](es)* ]]
  then
    echo -e "\nUploading to pypi"
    twine upload dist/*.whl
    echo -e "\nRunning cleanup"
    rm -rf dist *.egg-info
  else
      echo -e "BUILD PROCESS TERMINATED\n"
fi
