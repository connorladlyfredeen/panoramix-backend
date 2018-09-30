from pymongo.collection import Collection
from math import ceil


class DataClient(object):
    def __init__(self, client: Collection):
        self.movies = client

    def get_movies(self, limit: int=-1, page: int=-1):
        total_movies = self.movies.count()
        low = 0
        high = total_movies
        if limit > 0 and page > 0:
            high = min(limit * page, high)
            low = min(high, limit * (page - 1))
        else:
            limit = -1
            page = -1
        movies = list(self.movies.find({}, {'_id': 0})[low:high])
        ret_limit = limit if limit != -1 else total_movies
        ret_page = page if page != -1 else 1
        total_pages = int(ceil(total_movies / float(ret_limit)))
        return {
            'page': ret_page,
            'limit': ret_limit,
            'total_pages': total_pages,
            'movies': movies
        }

    def get_movie(self, imdb_id: str):
        return self.movies.find_one(filter={'$eq': {'imdbID': imdb_id}})
