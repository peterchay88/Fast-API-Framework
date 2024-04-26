#!/bin/bash

custom_datetime=$(date +"%Y_%m_%d_%H:%M:%S")

# Access the container
echo Acessing the container

if [ $# -eq 0 ]; then
  echo "Error! Please provide test ID/Tag as an argument. Example: bash test_runner.sh tcid01"
  echo "If you want to run all of the tests specify all as the argument"
# Automatically append the reports argument
elif [ "$1" = "all" ]; then
  docker exec fast_api pytest \
  --html /rest_api_test_framework/Tests/reports/results_$1_$custom_datetime.html \
  --self-contained-html \
  --color=yes
else
  docker exec fast_api pytest -m $1 \
  --html /rest_api_test_framework/Tests/reports/results_$1_$custom_datetime.html \
  --self-contained-html \
  --color=yes
fi

