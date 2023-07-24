#!/usr/bin/python3
""" Index route """

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns the status of GET request """
    status = {"status": "OK"}
    return jsonify(status)
