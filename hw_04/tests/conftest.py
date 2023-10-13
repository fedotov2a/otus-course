def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='Url for testing')
    parser.addoption('--status_code', default=200, type=int, help='Expected status code')
