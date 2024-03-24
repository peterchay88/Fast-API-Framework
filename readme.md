# REST API Project 

This project is a test framework that tests the endpoints created from
the API created by Jose Lopez. The source code and instructions for the REST API can be found
[here](https://github.com/jllopez/basic-restapi-app)!

### Prerequisites
Docker \
Python \
Make

### How to Spin up the API server
1. Launch Docker Desktop
2. Navigate to the folder `/Rest_API_Project/API/basic-restapi-app` in terminal
3. Run the command `make run`
4. Visit URL http://localhost:8080/docs#/

User admin/admin is preloaded in the DB. Leverage this user to authenticate and perform admin-only operations 
(i.e. create/delete/list-all users, delete comments)

### How to run tests
Tests should be run using the test runner shell script followed by the test tag after as an argument. \
For example `bash test_runner.sh tcid01` will run the test with the tag tcid01. 

If you need to run tests with more than one marker use the "and/or" operator
For example `bash test_runner.sh "tcid01 and tcid34"`

```commandline
Need to update this information with Docker once the it clears up how I want to run this with docker
```

### Important information for troubleshooting issues
Line 10 in `rest_api_test_framework/Tests/conftest.py` load dotenv is set to use an absolute path \
please make sure to update it with your machines specific absolute path
----
 ### TO DO
1. Need to create a shell script that streamlines the docker steps. Currently manually issuing the commands is tedious.
2. Create a runner script that easily executes tests from your local machine to the docker instance. That way
   a user doesn't have to log into the docker container to run tests
3. See if there is an easy way to access reports that are generated from the tests in the docker container