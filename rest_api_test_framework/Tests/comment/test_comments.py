import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
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
        logger.debug(f"Returned comments {response.json()}")
        logger.debug(f"Returned comments count: {len(response.json())}")
        assert response.ok, \
            f"Error! Unexpected status code returned. Expected OK status. Actual {response.status_code}"

    @pytest.mark.tcid03
    def test_cud_comment(self, get_auth_token):
        """
        This test checks the ability to create a new comment, update it, and delete it
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid03 'test_cud_comment'")
        # create comment
        # update comment
        # post comment


