import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.comments_utility import Comments
from rest_api_test_framework.src.helpers.random_generator import generate_random_sentence, generate_random_number

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()
comments = Comments()


class TestCommentsEndpointNegative:

    @pytest.mark.tcid07
    def test_create_comments_over_max_char_limit(self, get_auth_token):
        """
        This test case is to confirm that you cannot create a comment that is greater than 140 characters
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid07 'test_create_comments_over_max_char_limit'")
        # Generate a Random sentence with 141 or More characters. 140 is the limit.
        random_sentence = generate_random_sentence(char_length=141)
        import pdb; pdb.set_trace()
