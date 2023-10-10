import random
import pytest

from hw_04.src.dog_api import DogApi
from http import HTTPStatus


@pytest.fixture
def dog_api():
    return DogApi()


class TestDogApi:
    def test_all_breeds(self, dog_api):
        response = dog_api.get(DogApi.ALL_BREEDS_METHOD)

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert json_data['message']

        assert 'status' in json_data
        assert json_data['status'] == DogApi.SUCCESS_STATUS

    def test_random_image(self, dog_api):
        response = dog_api.get(DogApi.RANDOM_IMAGE_METHOD)

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert json_data['message']

        assert 'status' in json_data
        assert json_data['status'] == DogApi.SUCCESS_STATUS

        image_url = json_data['message']
        assert image_url.startswith(DogApi.IMAGES_URL), f'url [{image_url}] does not contain a prefix [{DogApi.IMAGES_URL}]'

        response = dog_api.get_image(image_url)
        assert response.status_code == HTTPStatus.OK, f'Not found image by url [{image_url}]'

    @pytest.mark.parametrize(
        'breed',
        DogApi().get_random_breeds()
    )
    def test_get_random_image_by_breed(self, dog_api, breed):
        response = dog_api.get(DogApi.RANDOM_IMAGE_BY_BREED_METHOD.substitute(breed=breed))

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert json_data['message']

        assert 'status' in json_data
        assert json_data['status'] == DogApi.SUCCESS_STATUS

        image_url = json_data['message']
        assert image_url.startswith(DogApi.IMAGES_URL), f'url [{image_url}] does not contain a prefix [{DogApi.IMAGES_URL}]'

        response = dog_api.get_image(image_url)
        assert response.status_code == HTTPStatus.OK, f'Not found image by url [{image_url}]'

    @pytest.mark.parametrize(
        'breed',
        [
            'superdog',
            123,
            None
        ]
    )
    def test_get_random_image_by_breed_negative(self, dog_api, breed):
        response = dog_api.get(DogApi.RANDOM_IMAGE_BY_BREED_METHOD.substitute(breed=breed))

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert 'Breed not found' in json_data['message']

        assert 'status' in json_data
        assert json_data['status'] == DogApi.ERROR_STATUS

    @pytest.mark.parametrize(
        'breed, count_image, expected_count_image',
        [
            (DogApi().get_random_breeds(count=1).pop(), 3, 3),
            (DogApi().get_random_breeds(count=1).pop(), 1, 1),
            (DogApi().get_random_breeds(count=1).pop(), 0, 1),
            (DogApi().get_random_breeds(count=1).pop(), 1.1, 1),
            pytest.param(DogApi().get_random_breeds(count=1).pop(), -1, 1, marks=pytest.mark.skip(reason='Returns 10 images. Should be 1.')),
            (DogApi().get_random_breeds(count=1).pop(), '"5"', 1),
            (DogApi().get_random_breeds(count=1).pop(), None, 1)
        ]
    )
    def test_get_random_multiple_images_by_breed(self, dog_api, breed, count_image, expected_count_image):
        response = dog_api.get(DogApi.RANDOM_MULTIPLE_IMAGE_BY_BREED_METHOD.substitute(breed=breed, count_image=count_image))

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert len(json_data['message']) == expected_count_image

        assert 'status' in json_data
        assert json_data['status'] == DogApi.SUCCESS_STATUS

        image_url = random.choice(json_data['message'])
        assert image_url.startswith(DogApi.IMAGES_URL), f'url [{image_url}] does not contain a prefix [{DogApi.IMAGES_URL}]'

        response = dog_api.get_image(image_url)
        assert response.status_code == HTTPStatus.OK, f'Not found image by url [{image_url}]'

    @pytest.mark.parametrize(
        'count_image, expected_count_image',
        [
            (3, 3),
            (1, 1),
            (0, 1),
            (1.1, 1),
            (-1, 1),
            ('"5"', 1),
            (None, 1)
        ]
    )
    def test_get_random_images(self, dog_api, count_image, expected_count_image):
        response = dog_api.get(DogApi.RANDOM_MULTIPLE_IMAGE_METHOD.substitute(count_image=count_image))

        assert response.status_code == HTTPStatus.OK
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers['Content-Type']

        json_data = response.json()

        assert json_data
        assert 'message' in json_data
        assert len(json_data['message']) == expected_count_image

        assert 'status' in json_data
        assert json_data['status'] == DogApi.SUCCESS_STATUS

        image_url = random.choice(json_data['message'])
        assert image_url.startswith(DogApi.IMAGES_URL), f'url [{image_url}] does not contain a prefix [{DogApi.IMAGES_URL}]'

        response = dog_api.get_image(image_url)
        assert response.status_code == HTTPStatus.OK, f'Not found image by url [{image_url}]'

