from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import yaml

app = Flask(__name__)

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

app.config.update(config)

db = SQLAlchemy(app)
jwt = JWTManager(app)
cache = Cache(app)
limiter = Limiter(app, key_func=get_remote_address)

from routes import register_routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
