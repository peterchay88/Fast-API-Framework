import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.users_utility import Users
from rest_api_test_framework.Tests.conftest import get_auth_token

pytestmark = [pytest.mark.users]
user = Users()


class TestUsersPositive:

    @pytest.mark.tcid09
    def test_get_users(self, get_auth_token):
        logger.info("Running tcid09 'test_get_users'")
        response = user.get_users(access_token=get_auth_token)
        logger.debug(f"retrieved all users: {response.json()}")
        assert response.ok, f"Unexpected response. {response.status_code} "
