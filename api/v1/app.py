#!/usr/bin/python3
""" An instance of Flask for API """

from api.v1.views import app_views
from flask import Flask, jsonify
import requests
from models import storage
from werkzeug.exceptions import HTTPException
from os import getenv


# Create an instance of flask as app
app = Flask(__name__)
# Register blueprint 'app_views' to Flask instance 'app'
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ Remove current SQLAlchemy session """
    storage.close()

@app.errorhandler(HTTPException)
def not_found(error):
    """ Display 404 page if route not found """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
