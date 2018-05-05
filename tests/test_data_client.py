from panoramix_backend.data_client import DataClient
import json

test_data = json.load(open('tests/sample_movie.json'))


class MockCollection:
    def __init__(self):
        self.test_data = [test_data]

    def find(self, _dict_1: dict, _dict_2: dict):
        return self.test_data


def test_get_data():
    data_client = DataClient(MockCollection())
    assert data_client.get_all_movies() == [test_data]
