import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.request_utility import RequestsApiCall

pytestmark = [pytest.mark.health]
api_request_call = RequestsApiCall()


class TestHealthEndpoint:

    @pytest.mark.tcid01
    def test_get_health_endpoint(self):
        """
        This test checks to see if we can hit the health endpoint via a GET api call
        :return:
        """
        logger.info("Running test_health_endpoint...")
        response = api_request_call.get(endpoint="health")
        api_request_call.expected_status_code(response.status_code, expected_status_code=200)
