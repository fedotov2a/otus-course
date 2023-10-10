from hw_04.src.base_api import BaseApi


class OpenBrewDbApi(BaseApi):
    BASE_URL = 'https://api.openbrewerydb.org'
    RANDOM_BREWERIES_METHOD = '/v1/breweries/random'
    BREWERIES_METHOD = '/v1/breweries'

    def __init__(self):
        super().__init__(OpenBrewDbApi.BASE_URL)
