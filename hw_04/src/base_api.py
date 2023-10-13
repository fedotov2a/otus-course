import requests


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, **kwargs):
        url = self.base_url + endpoint
        return requests.get(url, params, **kwargs)

    def post(self, endpoint, data=None, json_=None, **kwargs):
        url = self.base_url + endpoint
        return requests.post(url, data, json_, **kwargs)

    def put(self, endpoint, data=None, json_=None, **kwargs):
        url = self.base_url + endpoint
        return requests.put(url, data, json_, **kwargs)

    def delete(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        return requests.delete(url, **kwargs)
