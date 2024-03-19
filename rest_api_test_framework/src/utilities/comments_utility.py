from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers


class Comments:

    def __init__(self):
        self.endpoint = "comments"
        self.api_request = RequestsApiCall()

    def get_all_comments(self, access_token):
        request_headers = build_request_headers(access_token)
        response = self.api_request.get(endpoint=self.endpoint, api_headers=request_headers)
        return response
