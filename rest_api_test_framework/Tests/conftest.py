import pytest
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
import logging as logger

api_request = RequestsApiCall()


@pytest.fixture(scope="session")
def get_auth_token():
    logger.debug("Fetching API token")
    payload = {"username": "admin", "password": "admin"}
    logger.debug(f"sending following payload: {payload}")
    api_token = api_request.post(endpoint="auth/login", api_data=payload)
    api_request.expected_status_code(status_code=api_token.status_code)
    logger.debug(f"API token fetched: {api_token.json()['access_token']}")
    yield api_token.json()['access_token']
