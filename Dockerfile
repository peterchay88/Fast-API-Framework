FROM python:3.11.4
LABEL authors="peter"

# Installing nano
RUN apt-get update && apt-get install -y nano

# Making a folder named automation to copy all the files into
RUN mkdir /automation
COPY . /automation

# Change the working directory in the docker container to automation
WORKDIR /automation

# Install the setup.py file and the requirements file
RUN python3 setup.py install
RUN pip3 install -r requirements.txt
