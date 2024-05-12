from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers


class Users:

    def __init__(self):
        self.endpoint = "users/"
        self.api_request = RequestsApiCall()

    def get_users(self, access_token):
        requests_header = build_request_headers(access_token=access_token)
        response = self.api_request.get(endpoint=self.endpoint, api_headers=requests_header)
        self.api_request.expected_status_code(status_code=response.status_code)
        return response

