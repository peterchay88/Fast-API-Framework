from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers
from rest_api_test_framework.src.helpers.url_encoding import url_encode_string
from rest_api_test_framework.src.utilities.logging_utility import logger
import json


class Comments:

    def __init__(self):
        self.endpoint = "comments"
        self.text_header = "/?text="
        self.api_request = RequestsApiCall()

    def get_all_comments(self, access_token):
        request_headers = build_request_headers(access_token)
        response = self.api_request.get(endpoint=self.endpoint, api_headers=request_headers)
        self.api_request.expected_status_code(status_code=response.status_code)
        return response

    def create_comment(self, access_token, string):
        request_headers = build_request_headers(access_token)
        encoded_string = url_encode_string(string)
        response = self.api_request.post(endpoint=f"{self.endpoint}{self.text_header}{encoded_string}",
                                         api_headers=request_headers)
        self.api_request.expected_status_code(status_code=response.status_code, expected_status_code=201)
        return response

    def update_comment(self, access_token, comment_id, comment_payload):
        request_headers = build_request_headers(access_token, content_type="application/json")
        logger.debug(f"Sending the following headers: {request_headers}")
        json_data = json.dumps(comment_payload)
        response = self.api_request.put(endpoint=f"{self.endpoint}/{comment_id}", api_data=json_data,
                                        api_headers=request_headers)
        self.api_request.expected_status_code(status_code=response.status_code)
        return response

    def delete_comment(self, access_token, comment_id):
        requests_headers = build_request_headers(access_token)
        logger.debug(f"Sending the following headers: {requests_headers}")
        response = self.api_request.delete(endpoint=f"{self.endpoint}/{comment_id}", api_headers=requests_headers)
        self.api_request.expected_status_code(status_code=response.status_code)
        return response
