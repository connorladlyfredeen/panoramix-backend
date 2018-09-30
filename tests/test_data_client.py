from panoramix_backend.data_client import DataClient
import json

test_data = json.load(open('tests/sample_movie.json'))
expected_data = {
    'page': 1,
    'limit': 1,
    'total_pages': 1,
    'movies': [test_data]
}


class MockCollection:
    def __init__(self):
        self.test_data = [test_data]

    def find(self, _dict_1: dict, _dict_2: dict):
        return self.test_data

    def count(self):
        return len(self.test_data)

    def find_one(self, filter):
        for movie in self.test_data:
            if movie['imdbID'] == filter['imdbID']:
                return movie
        return None


def test_get_data():
    data_client = DataClient(MockCollection())
    assert data_client.get_movies() == expected_data


def test_get_single_movie_exists():
    data_client = DataClient(MockCollection())
    assert data_client.get_movie('tt0468569') == test_data


def test_get_single_movie_not_exists():
    data_client = DataClient(MockCollection())
    assert data_client.get_movie('123') is None
