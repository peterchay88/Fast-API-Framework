import requests
import logging as logger


class RequestsApiCall:

    def __init__(self):
        self.url = "http://localhost:8080/docs#/"

    def expected_status_code(self, status_code, expected_status_code=200):
        """
        This method is used to assert if the expected status code was returned from the API response call
        :param status_code:
        :param expected_status_code:
        :return:
        """
        logger.debug(f"Checking to see if expected status code {expected_status_code} satisfied")
        assert status_code == expected_status_code, \
            f"Unexpected status code. Expected {expected_status_code}. Actual {status_code}."

    def get(self, endpoint):
        """
        API wrapper for the GET response call
        :param endpoint:
        :return:
        """
        logger.debug("huh?")
        response = requests.get(url=f"{self.url}{endpoint}")
        self.expected_status_code(status_code=response.status_code)
        logger.info("WHAT")
        return response
