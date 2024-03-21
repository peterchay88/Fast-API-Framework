import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.comments_utility import Comments
from rest_api_test_framework.src.helpers.random_generator import generate_random_sentence, generate_random_number

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

        # step 1: create comment w/ a random comment
        random_string = generate_random_sentence()
        logger.debug(f"Creating new comment with string: {random_string}")
        response = comments.create_comment(access_token=get_auth_token, string=random_string)
        logger.debug(f"Generated comment: {response.json()}")
        assert response.ok, f"Error! Unexpected status code returned. {response.status_code}"
        assert response.json()['comment_text'] == random_string, \
            (f"Error! Comment string does not match generated string. Expected {random_string}. "
             f"Actual {response.json()['comment_text']}")

        # step 2: update comment via comment id. We also need to pass in number of likes to update to
        comment_id = response.json()["id"]
        logger.debug(f"Now updating the comment with ID : {comment_id}")
        likes = generate_random_number()
        new_random_string = generate_random_sentence()
        payload = {"comment_text": new_random_string, "likes": likes}
        logger.debug(f"updating the comment with ID : {comment_id} with the following payload: {payload}")
        response = comments.update_comment(access_token=get_auth_token, comment_id=comment_id, comment_payload=payload)
        import pdb;pdb.set_trace()
        # step 3: delete comment

        # trying to figure out why tcid03 won't run. I suspect the issue is somewhere in the headers

