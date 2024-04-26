#!/bin/bash

python setup.py install
echo
echo
echo
echo

if [ $# -eq 0 ]; then
  echo "Error! Please provide test ID/Tag as an argument. Example: bash test_runner.sh tcid01"
  echo "If you want to run all of the tests specify all as the argument"
# Automatically append the reports argument
elif [ "$1" = "all" ]; then
    pytest --html=rest_api_test_framework/Results/reports/report.html --self-contained-html
else
  pytest -m "$1" --html=rest_api_test_framework/Results/reports/report.html --self-contained-html
fi


