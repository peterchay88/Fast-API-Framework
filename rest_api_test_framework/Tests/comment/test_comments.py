import pytest
import logging as logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()
# auth_token = GetAuthToken()


class TestCommentsEndpoint:

    @pytest.mark.tcid02
    def test_get_comments(self, auth_token):
        """
        This test checks to see if we can successfully run a get call on the comments endpoint
        :return:
        """
        token_header = {"Authorization": f"Bearer {auth_token}"}
        api_response = api_request_call.get(endpoint="comments/", api_headers=token_header)
        api_request_call.expected_status_code(status_code=api_response.status_code)
