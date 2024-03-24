FROM python:3.11.4
LABEL authors="peter"

# Installing nano
RUN apt-get update && apt-get install -y nano

# Making a folder named automation to copy all the files into
RUN mkdir /rest_api_test_framework
COPY ./rest_api_test_framework /rest_api_test_framework
COPY setup.py /rest_api_test_framework
COPY requirements.txt /rest_api_test_framework
COPY pytest.ini /rest_api_test_framework

# Change the working directory in the docker container to automation
WORKDIR /rest_api_test_framework

# Install the setup.py file and the requirements file
RUN python3 setup.py install
RUN pip3 install -r requirements.txt
