import json

import pytest
from rest_api_test_framework.src.utilities.logging_utility import logger
from rest_api_test_framework.src.utilities.users_utility import Users
from rest_api_test_framework.Tests.conftest import get_auth_token
from rest_api_test_framework.src.helpers.random_generator import generate_random_word
from rest_api_test_framework.src.helpers.password_hash import EncryptPassword

pytestmark = [pytest.mark.users]
user = Users()


class TestUsersPositive:

    @pytest.mark.tcid09
    def test_get_users(self, get_auth_token):
        """
        This test confirms that we can hit the users endpoint and return all users
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid09 'test_get_users'")
        response = user.get_users(access_token=get_auth_token)
        logger.debug(f"retrieved all users: {response.json()}")
        assert response.ok, f"Unexpected response. {response.status_code} "

    @pytest.mark.tcid10
    def test_create_user(self, get_auth_token):
        """
        This test confirms that we can hit the users endpoint and create a user with the user role
        :param get_auth_token:
        :return:
        """
        logger.info("Running tcid10 'create_user'")
        # Generate Username and password
        username = generate_random_word()
        password = generate_random_word()
        logger.debug(f"Creating a user with the username {username}")

        # Encrypt Password
        hash_pw = EncryptPassword(password)
        encrypted_pw = hash_pw.encrypt_password()
        logger.debug(f"Encrypted Password: {encrypted_pw}")

        # Create User
        data = {
            "username": username,
            "password_hash": str(encrypted_pw),
            "roles": "user"
        }
        logger.debug(f"Sending payload: {data}")
        created_user = user.create_user(access_token=get_auth_token, data=json.dumps(data))

        assert created_user.json()['username'] == username, \
            f"Unexpected Value for username. Expected {username}. Actual {created_user.json()['username']}"

        check_pw = hash_pw.check_password_hash(hashed_password=encrypted_pw)
        assert check_pw == 200, f"Unexpected value for password. Expected 200. Actual {check_pw} "

