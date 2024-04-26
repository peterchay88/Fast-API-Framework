# REST API Project 

This project is a test framework that tests the endpoints created from
the API created by Jose Lopez. The source code and instructions for the REST API can be found
[here](https://github.com/jllopez/basic-restapi-app)!

### Prerequisites
Docker \
Python \
Make

## How to Spin up the API server
1. Launch Docker Desktop
2. Navigate to the folder `/Rest_API_Project/API/basic-restapi-app` in terminal
3. Run the command `make run`
4. Visit URL http://localhost:8080/docs#/

User admin/admin is preloaded in the DB. Leverage this user to authenticate and perform admin-only operations 
(i.e. create/delete/list-all users, delete comments)

## How to run tests
### Docker
First you will need to spin up the docker image. 
```commandline
bash start_docker.sh
```
Next open another terminal and navigate to the `test_runners` folder. From there run the docker test runner script with
an argument after calling the script. Specify all if you wish to run all the tests.
```commandline
bash docker_test_runner.sh <argument>
```
If you need to run tests with more than one marker use the "and/or" operator
For example `bash docker_test_runner.sh "tcid01 and tcid34"`

### Local
If you wish to run tests on the local env you will need to edit the value in `secrets.env` for the key `API_URL` 
currently it`s pointed to work for a docker env. Please change that value to local host.

After making this change please run tests using the local test runner in the `test_runners` folder
```commandline
bash local_test_runner.sh <argument>
```
----
 ### TO DO
1. Write more test.
2. re-vist if Docker YAML file is the best way to do this. After running the docker script that uses the yaml file
its a bit annoying that you have to use another terminal.