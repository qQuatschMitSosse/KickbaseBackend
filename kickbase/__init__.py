from flask_cors import CORS
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient(
    'mongodb+srv://businesskurzmann:fQVSiklMVQbJRyLI@kickbase.did416a.mongodb.net/?retryWrites=true&w=majority')
db = client.kickbase
collection = db.players

from kickbase import routes
