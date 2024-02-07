#!/bin/bash

python setup.py install
echo
echo

if [ $# -eq 0 ]; then
  echo "Error! Please provide test ID/Tag as an argument. Example: bash test_runner tcid01"
else
  pytest -m $1
fi