from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers
from rest_api_test_framework.src.utilities.url_encoding_utility import url_encode_string


class Comments:

    def __init__(self):
        self.endpoint = "comments"
        self.api_request = RequestsApiCall()

    def get_all_comments(self, access_token):
        request_headers = build_request_headers(access_token)
        response = self.api_request.get(endpoint=self.endpoint, api_headers=request_headers)
        return response

    def create_comment(self, access_token, string):
        request_headers = build_request_headers(access_token)
        encoded_string = url_encode_string(string)
        response = self.api_request.post(endpoint=f"{self.endpoint}/?{encoded_string}", api_headers=request_headers)
        return response
