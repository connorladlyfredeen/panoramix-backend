from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from pymongo import MongoClient
from panoramix_backend.data_client import DataClient

app = Flask(__name__)
CORS(app)
data_client = DataClient(MongoClient(os.environ['MONGODB_URI']).get_database().imdb_movies)


@app.route('/movies')
def movies():
    limit = int(request.args.get('limit', -1))
    page = int(request.args.get('page', -1))
    return jsonify(data_client.get_movies(limit=limit, page=page))


@app.route('/movie/<string:imdb_id>')
def movie(imdb_id: str):
    res = data_client.get_movie(imdb_id=imdb_id)
    if res is None:
        return jsonify({}), 404
    return jsonify(res)
