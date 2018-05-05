from flask import Flask, jsonify
import os
from pymongo import MongoClient
from panoramix_backend.data_client import DataClient

app = Flask(__name__)
data_client = DataClient(MongoClient(os.environ['MONGODB_URI']).movies.imdb_movies)


@app.route('/movies')
def movies():
    return jsonify(data_client.get_all_movies())
