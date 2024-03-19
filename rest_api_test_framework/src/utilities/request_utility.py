import requests
import logging as logger


class RequestsApiCall:

    def __init__(self):
        self.url = "http://localhost:8080/"
        self.session = requests.session()

    @staticmethod
    def expected_status_code(status_code, expected_status_code=200):
        """
        This method is used to assert if the expected status code was returned from the API response call
        :param status_code: Status code passed in
        :param expected_status_code: Expected status code
        :return:
        """
        logger.debug(f"Checking to see if expected status code {expected_status_code} satisfied")
        assert status_code == expected_status_code, \
            f"Unexpected status code. Expected {expected_status_code}. Actual {status_code}."

    def get(self, endpoint, api_headers=None):
        """
        API wrapper for the GET response call
        :param api_headers: Headers to be passed to the Get call. Default is None if there are no arguments.
        :param endpoint: API endpoint to be hit
        :return:
        """
        logger.debug(f"Running GET API call on endpoint {endpoint}")
        logger.debug(f"Passing the following params for headers {api_headers}")
        response = self.session.get(url=f"{self.url}{endpoint}", headers=api_headers)
        return response

    def post(self, endpoint, api_data=None, api_headers=None):
        """
        API wrapper for the POST response call
        :param api_headers: Headers to be passed to the Post call. Default is None if there are no arguments.
        :param api_data: data to be passed to the Post call. Default is None if there are no arguments.
        :param endpoint: API endpoint to be hit
        :return:
        """
        logger.debug(f"Running POST API call on endpoint {endpoint}")
        logger.debug(f"Passing the following params for data {api_data}")
        logger.debug(f"Passing the following params for headers {api_headers}")
        response = self.session.post(url=f"{self.url}{endpoint}", data=api_data, headers=api_headers)
        return response
