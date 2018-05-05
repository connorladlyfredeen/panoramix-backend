from pymongo.collection import Collection


class DataClient(object):
    def __init__(self, client: Collection):
        self.movies = client

    def get_all_movies(self):
        return list(self.movies.find({}, {'_id': 0}))
