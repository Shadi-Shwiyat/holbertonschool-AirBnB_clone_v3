#!/usr/bin/python3
""" View for State objects that handles all default
    RESTFul API actions """

from models import State
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def return_states():
    """ Retrieves list of all state objects using GET method """
    states = storage.all(State)
    states_list = []
    for key, value in states.items():
        states_list.append(value.to_dict())
    return jsonify(states_list)