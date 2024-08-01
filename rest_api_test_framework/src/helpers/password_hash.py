import bcrypt
from rest_api_test_framework.src.utilities.logging_utility import logger


class EncryptPassword:

    def __init__(self, password):
        self.password = password

    def encrypt_password(self):
        """
        This function takes in a password argument and returns the hashed value
        :param password:
        :return:
        """
        encrypted_password = bcrypt.hashpw(password=self.password.encode(), salt=bcrypt.gensalt())
        return encrypted_password

    def check_password_hash(self, hashed_password):
        """
        This function compares a hashed value with a password and checks to see if they match
        :param password:
        :param hashed_password:
        :return:
        """
        if bcrypt.checkpw(password=self.password.encode(), hashed_password=hashed_password):
            result = 200
        else:
            result = 400
            logger.debug(hashed_password)
        return result
