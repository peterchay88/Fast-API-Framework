import pytest
import requests

pytestmark = [pytest.mark.health]


class TestHealthEndpoint:

    @pytest.mark.tcid01
    def test_get_health_endpoint(self):
        pass
