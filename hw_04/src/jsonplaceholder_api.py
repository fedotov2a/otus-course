from string import Template
from hw_04.src.base_api import BaseApi


class JsonPlaceHolderApi(BaseApi):
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    USERS_METHOD = '/users'
    USERS_BY_ID_METHOD = Template('/users/$user_id')
    CREATE_POST_METHOD = '/posts'
    GET_POST_METHOD = Template('/posts/$post_id')
    DELETE_POST_METHOD = Template('/posts/$post_id')

    def __init__(self):
        super().__init__(JsonPlaceHolderApi.BASE_URL)
