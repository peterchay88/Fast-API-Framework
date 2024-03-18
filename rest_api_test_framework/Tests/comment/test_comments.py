import pytest
import logging as logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.build_request_headers_utility import build_request_headers

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()


class TestCommentsEndpoint:

    @pytest.mark.tcid02
    def test_get_comments(self, get_auth_token):
        """
        This test checks to see if we can successfully run a get call on the comments endpoint
        :return:
        """
        token_header = build_request_headers(access_token=get_auth_token)
        api_response = api_request_call.get(endpoint="comments/", api_headers=token_header)
        api_request_call.expected_status_code(status_code=api_response.status_code)
