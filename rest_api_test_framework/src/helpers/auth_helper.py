from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
import logging as logger


class GetAuthToken:

    def __init__(self):
        self.api_request = RequestsApiCall()
        self.auth_endpoint = "auth/login"
        self.api_payload = {"username": "admin", "password": "admin"}

    def get_auth_token(self):
        logger.debug("Fetching API token")
        api_token = self.api_request.post(endpoint=self.auth_endpoint, api_data=self.api_payload)
        self.api_request.expected_status_code(status_code=api_token.status_code)
        logger.debug(f"API token fetched: {api_token.json()['access_token']}")
        return api_token.json()['access_token']
