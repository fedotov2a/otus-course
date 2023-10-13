import random

import pytest
from http import HTTPStatus

from hw_04.src.openbrewdb_api import OpenBrewDbApi


@pytest.fixture
def openbrewdb_api():
    return OpenBrewDbApi()


class TestOpenBrewDbApi:
    def test_get_random_breweries(self, openbrewdb_api):
        response = openbrewdb_api.get(OpenBrewDbApi.RANDOM_BREWERIES_METHOD)

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert json_data, 'Breweries list is empty'

        brewery = json_data[0]
        assert brewery['id'], 'id is empty'
        assert brewery['name'], 'name is empty'
        assert brewery['state'], 'state is empty'
        assert brewery['city'], 'city is empty'
        assert brewery['street'], 'street is empty'

    @pytest.mark.parametrize(
        'size, expected_size',
        [
            (1, 1),
            (49, 49),
            (50, 50),
            (51, 50),
            (0, 1),
            pytest.param(-1, 1, marks=pytest.mark.skip(reason='Returns 500'))
        ]
    )
    def test_get_random_breweries(self, openbrewdb_api, size, expected_size):
        response = openbrewdb_api.get(OpenBrewDbApi.RANDOM_BREWERIES_METHOD, params={'size': size})

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert len(json_data) == expected_size

    @pytest.mark.parametrize(
        'city',
        [
            'San Diego',
            'Miami',
            'Moscow'
        ]
    )
    def test_get_breweries_by_city(self, openbrewdb_api, city):
        response = openbrewdb_api.get(OpenBrewDbApi.BREWERIES_METHOD, params={'by_city': city})

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert json_data, 'Breweries list is empty'

        brewery = random.choice(json_data)
        assert brewery['city'] == city

    @pytest.mark.parametrize(
        'per_page, expected_per_page',
        [
            (1, 1),
            (10, 10),
            (100, 100),
            (0, 0),
            pytest.param(-1, 0, marks=pytest.mark.skip(reason='Returns 50 elements'))
        ]
    )
    def test_get_breweries_by_city(self, openbrewdb_api, per_page, expected_per_page):
        response = openbrewdb_api.get(OpenBrewDbApi.BREWERIES_METHOD, params={'per_page': per_page})

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert len(json_data) == expected_per_page

    @pytest.mark.parametrize(
        'name',
        [
            'Broken Clock Brewing Cooperative',
            '4th Tap Brewing Cooperative',
            '3cross Fermentation Cooperative'
        ]
    )
    def test_get_breweries_by_name(self, openbrewdb_api, name):
        response = openbrewdb_api.get(OpenBrewDbApi.BREWERIES_METHOD, params={'by_name': name})

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert json_data, 'Breweries list is empty'

        brewery = random.choice(json_data)
        assert brewery['name'] == name
