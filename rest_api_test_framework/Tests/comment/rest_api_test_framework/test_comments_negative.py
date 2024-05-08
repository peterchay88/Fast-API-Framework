import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall
from rest_api_test_framework.src.utilities.comments_utility import Comments
from rest_api_test_framework.src.helpers.random_generator import generate_random_sentence, generate_random_number

pytestmark = [pytest.mark.comments]
api_request_call = RequestsApiCall()
comments = Comments()
