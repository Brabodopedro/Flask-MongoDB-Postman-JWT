from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

from json import JSONEncoder
from bson import json_util
from json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return json_util.default(obj)

app.json_encoder = CustomJSONEncoder


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost: SEU LOCAL'
}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)
