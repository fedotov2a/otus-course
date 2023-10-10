import random

import pytest
from http import HTTPStatus

from hw_04.src.jsonplaceholder_api import JsonPlaceHolderApi


@pytest.fixture
def jsonplaceholder_api():
    return JsonPlaceHolderApi()


@pytest.fixture
def create_post(jsonplaceholder_api):
    response = jsonplaceholder_api.post(
        JsonPlaceHolderApi.CREATE_POST_METHOD,
        data={
            'title': 'test_title',
            'body': 'test_body',
            'userId': random.randint(1, 10)
        }
    )
    assert response.status_code == HTTPStatus.CREATED

    json_data = response.json()
    assert json_data, 'Post is empty'
    assert 'id' in json_data, 'no post id'

    return json_data


class TestJsonPlaceHolderApi:
    def test_get_all_users(self, jsonplaceholder_api):
        response = jsonplaceholder_api.get(JsonPlaceHolderApi.USERS_METHOD)

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()
        assert json_data, 'Users list is empty'

        user = json_data[0]
        assert user['id'], 'id is empty'
        assert user['name'], 'name is empty'
        assert user['email'], 'email is empty'
        assert user['phone'], 'phone is empty'

    @pytest.mark.parametrize(
        'user_id, expected_status_code',
        [
            (1, HTTPStatus.OK),
            (10, HTTPStatus.OK)
        ]
    )
    def test_get_user_by_id(self, jsonplaceholder_api, user_id, expected_status_code):
        response = jsonplaceholder_api.get(JsonPlaceHolderApi.USERS_BY_ID_METHOD.substitute(user_id=user_id))

        assert response.status_code == expected_status_code
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        user = response.json()
        assert user, 'Users list is empty'
        assert user['id'] == user_id

    @pytest.mark.parametrize(
        'user_id, expected_status_code',
        [
            (11, HTTPStatus.NOT_FOUND),
            (0, HTTPStatus.NOT_FOUND),
            (-1, HTTPStatus.NOT_FOUND)
        ]
    )
    def test_get_user_by_id_negative(self, jsonplaceholder_api, user_id, expected_status_code):
        response = jsonplaceholder_api.get(JsonPlaceHolderApi.USERS_BY_ID_METHOD.substitute(user_id=user_id))

        assert response.status_code == expected_status_code
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

    @pytest.mark.parametrize(
        'data',
        [
            {
                'title': 'test_title',
                'body': 'test_body',
                'userId': random.randint(1, 10)
            }
        ]
    )
    def test_create_post(self, jsonplaceholder_api, data):
        response = jsonplaceholder_api.post(
            JsonPlaceHolderApi.CREATE_POST_METHOD,
            data=data
        )
        assert response.status_code == HTTPStatus.CREATED

        post = response.json()
        assert post, 'Post is empty'
        assert post['title'] == data['title']
        assert post['body'] == data['body']
        assert post['userId'] == str(data['userId'])

        return response

    def test_delete_post(self, jsonplaceholder_api, create_post):
        post_id = create_post['id']

        response = jsonplaceholder_api.delete(JsonPlaceHolderApi.DELETE_POST_METHOD.substitute(post_id=post_id))
        assert response.status_code == HTTPStatus.OK

        response = jsonplaceholder_api.get(JsonPlaceHolderApi.GET_POST_METHOD.substitute(post_id=post_id))
        assert response.status_code == HTTPStatus.NOT_FOUND
