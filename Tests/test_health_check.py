import pytest
from src.utilities.request_utility import RequestsApiCall

pytestmark = [pytest.mark.health]


class TestHealthEndpoint:

    def __init__(self):
        self.api_call = RequestsApiCall()
        self.health_endpoint = "health"

    @pytest.mark.tcid01
    def test_get_health_endpoint(self):
        response = self.api_call.get(endpoint=self.health_endpoint)
