import requests


class RequestsApiCall:

    def __init__(self):
        self.url = "http://localhost:8080/docs#/"

    def get(self, endpoint):
        response = requests.get(url=f"{self.url}{endpoint}")
        return response
