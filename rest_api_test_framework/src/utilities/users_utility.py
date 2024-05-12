from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers


class Users:

    def __init__(self):
        self.user_endpoint = "users/"
        self.api_request = RequestsApiCall()

    def get_users(self, access_token):
        requests_header = build_request_headers(access_token=access_token)
        response = self.api_request.get(endpoint=self.user_endpoint, api_headers=requests_header)
        self.api_request.expected_status_code(status_code=response.status_code)
        return response

    def create_user(self, access_token, data):
        requests_header = build_request_headers(access_token=access_token, content_type="application/json")
        response = self.api_request.post(endpoint=self.user_endpoint, api_data=data, api_headers=requests_header)
        self.api_request.expected_status_code(status_code=response.status_code, expected_status_code=201)
        return response

