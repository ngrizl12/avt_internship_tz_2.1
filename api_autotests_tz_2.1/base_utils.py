from enum import Enum
import requests


class APIConfig:
    def __init__(self):
        self.base_host = "https://qa-internship.avito.com"

    @property
    def base_url(self):
        return self.base_host


config = APIConfig()


class Endpoint(Enum):
    CREATE_ITEM = "/api/1/item"
    GET_ITEM_BY_ID = "/api/1/item/{id}"
    GET_ITEMS_BY_SELLER = "/api/1/{sellerID}/item"
    GET_STATISTIC = "/api/1/statistic/{id}"

def send_request(method, endpoint, json=None, params=None):
    url = config.base_url + endpoint
    return requests.request(method, url, json=json, params=params)


class RequestBuilder:

    def __init__(self):
        self.method = "GET"
        self.endpoint = ""
        self.json_body = None
        self.params = None

    def with_method(self, method):
        self.method = method
        return self

    def with_endpoint(self, endpoint):
        self.endpoint = endpoint
        return self

    def with_json(self, json_body):
        self.json_body = json_body
        return self

    def with_params(self, params):
        self.params = params
        return self

    def send(self):
        return send_request(
            method=self.method,
            endpoint=self.endpoint,
            json=self.json_body,
            params=self.params
        )
