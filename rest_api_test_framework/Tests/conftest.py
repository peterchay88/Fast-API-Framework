import os
import pytest
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
import logging as logger
from dotenv import load_dotenv

api_request = RequestsApiCall()

# Must use absolute path for env variables to work when calling from fixture
load_dotenv("/Users/peter/Desktop/python/udemy/Rest_API_Project/secrets.env")
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")


@pytest.fixture(scope="session")
def get_auth_token():
    logger.debug("Fetching API token")
    payload = {"username": admin_username, "password": admin_password}
    logger.debug(f"sending following payload: {payload}")
    api_token = api_request.post(endpoint="auth/login", api_data=payload)
    api_request.expected_status_code(status_code=api_token.status_code)
    logger.debug(f"API token fetched: {api_token.json()['access_token']}")
    yield api_token.json()['access_token']
