import random
import requests
from string import Template

from hw_04.src.base_api import BaseApi


class DogApi(BaseApi):
    BASE_URL = 'https://dog.ceo'
    IMAGES_URL = 'https://images.dog.ceo/breeds'

    ALL_BREEDS_METHOD = '/api/breeds/list/all'
    RANDOM_IMAGE_METHOD = '/api/breeds/image/random'
    RANDOM_MULTIPLE_IMAGE_METHOD = Template('/api/breeds/image/random/$count_image')
    RANDOM_IMAGE_BY_BREED_METHOD = Template('/api/breed/$breed/images/random')
    RANDOM_MULTIPLE_IMAGE_BY_BREED_METHOD = Template('/api/breed/$breed/images/random/$count_image')

    SUCCESS_STATUS = 'success'
    ERROR_STATUS = 'error'

    def __init__(self):
        super().__init__(DogApi.BASE_URL)

    @staticmethod
    def get_image(image_url):
        return requests.get(image_url)

    def get_random_breeds(self, count=3):
        json_data = self.get(DogApi.ALL_BREEDS_METHOD).json()
        breeds = json_data['message'].keys()
        return random.sample(breeds, k=min(count, len(breeds)))
