import pytest
import logging as logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()


class TestCommentsEndpoint:

    @pytest.mark.tcid02
    def test_get_comments(self):
        """
        This test checks to see if we can successfully run a get call on the comments endpoint
        :return:
        """
        # Authenticate
        
        # Get comments
