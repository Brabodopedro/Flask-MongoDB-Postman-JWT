from flask import Flask
from database.db import initialize_db
from database.models import Movie
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from json import JSONEncoder
from bson import json_util
from json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return json_util.default(obj)

app.json_encoder = JSONEncoder


MONGODB_SETTINGS = {
    'host': 'mongodb://localhost/27017/teste1'
}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)
