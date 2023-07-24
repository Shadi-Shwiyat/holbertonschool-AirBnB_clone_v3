#!/usr/bin/python3
"""View for State objects that handles all default RESTFul API actions"""

import models
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def return_states():
    """Retrieves list of all state objects using GET http method"""
    states = storage.all(State)
    states_list = []
    for key, value in states.items():
        states_list.append(value.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def return_states_id(state_id):
    """Return a specific state based on given id using GET http method"""
    states = storage.all(State)
    for key, value in states.items():
        if states[key].id == state_id:
            return value.to_dict()
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_states_id(state_id):
    """Delete a specific state based on given id using DELETE http method"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def create_states():
    """Create a state object using POST http method"""
    body = request.get_json()
    if body is None:
        return (jsonify({'error': 'Not a JSON'}), 400)
    obj = State(**body)

    if 'name' not in body:
        return (jsonify({'error': 'Missing name'}), 400)
    else:
        storage.new(obj)
        storage.save()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_states(state_id):
    """Update a state objest using PUT http method"""
    body = request.get_json()
    if body is None:
        return (jsonify({'error': 'Not a JSON'}), 400)
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        ignore_key = ['id', 'created_at', 'updated_at']
        for key, value in body.items():
            if key not in ignore_key:
                setattr(state, key, value)
            else:
                pass
        storage.save()
        return (jsonify(state.to_dict()), 200)
