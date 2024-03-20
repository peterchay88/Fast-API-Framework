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

`Note this framework is still underconstruction. Will update readme file as I get further in the 
framework :)`
