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
    def test_post_comments(self,get_auth_token):
        """
        This test confirms that we can send a post to a comments endpoint
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid03 'test_post_comments'")
        random_string = generate_random_sentence()
        response = comments.create_comment(access_token=get_auth_token, string=random_string)
        logger.debug(f"Generating a comment with the text: {random_string}")
        assert response.status_code == 201, \
            f"Unexpected Status Code. Expected: 201. Actual:{response.status_code}"
        assert response.json()['comment_text'] == random_string, \
            f"Unexpected Value. Expected: {random_string}. Actual:{response.json()['comment_text']}"

    @pytest.mark.tcid04
    def test_update_comments(self, get_auth_token):
        """
        This test confirms that we can send a PUT request to the comments endpoint
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid04 'test_update_comments'")
        # Get a list of comment ID's and pick a random one
        random_id = comments.get_random_comment_id(access_token=get_auth_token)
        logger.debug(f"Updating comment with the ID of '{random_id}'")

        # Update comment with a random sentence
        random_sentence = generate_random_sentence()
        likes = generate_random_number()
        updated_comment = comments.update_comment(access_token=get_auth_token, comment_id=random_id,
                                                  comment_text=random_sentence, likes=likes)
        assert updated_comment.json()['id'] == random_id, \
            f"Unexpected value. Comment ID Expected: {random_id}. Actual {updated_comment.json()['id']}"
        assert updated_comment.json()['comment_text'] == random_sentence, \
            f"Unexpected value. Comment Text Expected: {random_sentence}. Actual {updated_comment.json()['comment_text']}"
        assert updated_comment.json()['likes'] == likes, \
            f"Unexpected value. Comment Text Expected: {likes}. Actual {updated_comment.json()['likes']}"

    @pytest.mark.tcid05
    def test_delete_comment(self, get_auth_token):
        """
        This test confirms that we can send a DELETE request to the comments endpoint
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid05 'test_delete_comments'")
        # Generate a list of comments ID then randomly pick one to be deleted
        comment_id = comments.get_random_comment_id(access_token=get_auth_token)
        # Delete the comment
        logger.debug(f"Attempting to delete comment {comment_id}")
        response = comments.delete_comment(access_token=get_auth_token, comment_id=comment_id)
        logger.debug(f"Deleted comment {comment_id}")
        assert response.json()['detail'] == f"Deleted comment {comment_id}", \
            f"Unexpected response. Expected {'Deleted comment {comment_id}'}. Actual {response.json()['detail'] }"

    @pytest.mark.tcid00
    def test_cud_comment(self, get_auth_token):
        """
        This test checks the ability to create a new comment, update it, and delete it
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid03 'test_cud_comment'")

        # step 1: create comment w/ a random comment
        logger.info("Running tcid03: Creating new comment.")
        random_string = generate_random_sentence()
        logger.debug(f"Creating new comment with string: {random_string}")
        response = comments.create_comment(access_token=get_auth_token, string=random_string)
        logger.debug(f"Generated comment: {response.json()}")
        assert response.ok, f"Error! Unexpected status code returned. {response.status_code}"
        assert response.json()['comment_text'] == random_string, \
            (f"Error! Comment string does not match generated string. Expected {random_string}. "
             f"Actual {response.json()['comment_text']}")

        # step 2: update comment via comment id. We also need to pass in number of likes to update to
        logger.info("Running tcid03: Updating comment.")
        comment_id = response.json()["id"]
        logger.debug(f"Now updating the comment with ID : {comment_id}")
        likes = generate_random_number()
        new_random_string = generate_random_sentence()
        response = comments.update_comment(access_token=get_auth_token, comment_id=comment_id,
                                           comment_text=new_random_string, likes=likes)
        assert response.json()['comment_text'] == new_random_string, \
            (f"Error! Unexpected string for comment. Expected {new_random_string}. "
             f"Actual {response.json()['comment_text']}")
        assert response.json()['likes'] == likes, \
            f"Error! Unexpected value for likes. Expected {likes}. Actual {response.json()['likes']}."

        # step 3: delete comment
        logger.info("Running tcid03: Deleting comment.")
        response = comments.delete_comment(access_token=get_auth_token, comment_id=comment_id)
        assert response.json()["detail"] == f"Deleted comment {comment_id}", \
            (f"Error! Unexpected value returned. Expected Deleted comment {comment_id}. "
             f"Actual {response.json()['detail']}.")



