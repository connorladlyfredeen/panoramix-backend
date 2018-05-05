from flask import Flask, jsonify
import os
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(os.environ['MONGODB_URI'])


@app.route('/movies')
def movies():
    return jsonify(list(client.movies.imdb_movies.find({}, {'_id': 0})))
