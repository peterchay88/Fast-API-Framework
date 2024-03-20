import pytest
import logging as logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.comments_utility import Comments

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()
comments = Comments()


class TestCommentsEndpoint:

    @pytest.mark.tcid02
    def test_get_comments(self, get_auth_token):
        """
        This test checks to see if we can successfully run a get call on the comments endpoint
        :return:
        """
        logger.info("Running tcid02 'test_get_comments'")
        response = comments.get_all_comments(access_token=get_auth_token)
        assert response.ok, \
            f"Error! Unexpected status code returned. Expected OK status. Actual {response.status_code}"

