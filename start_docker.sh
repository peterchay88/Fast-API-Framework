#!/bin/bash

# Create Docker Image
echo
echo "-------------------------------------------------"
echo "Creating Docker Image rest_api:v1"
echo "-------------------------------------------------"
docker build -t rest_api:v1 .

# If a container named fast_api exists. Stop it and then remove it.
echo
echo "-------------------------------------------------"
echo "If container fast_api exists already stopping it and deleting it"
echo "-------------------------------------------------"
docker stop fast_api
docker rm fast_api

# Run the docker compose file
echo
echo "-------------------------------------------------"
echo "Running the docker compose file"
echo "-------------------------------------------------"
docker compose -f docker-compose.yml down
docker compose -f docker-compose.yml up
echo
