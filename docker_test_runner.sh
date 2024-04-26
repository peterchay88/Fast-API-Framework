#!/bin/bash

custom_datetime=$(date +"%Y_%m_%d_%H:%M:%S")

# Access the container
echo Acessing the container
docker exec fast_api pytest -m $1 \
--html /