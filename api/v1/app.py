#!/usr/bin/python3
""" An instance of Flask for API """

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv  # to use environmental variables
from flask import jsonify
from werkzeug.exceptions import HTTPException  # to use errorhandler
from flask_cors import CORS


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
