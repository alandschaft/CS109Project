"""
Routes and views for the flask application.
"""

import uuid
from flask import Flask
from flask.ext.jsonpify import jsonify
from flask import render_template, request
import os
import redis
import imp    
import pickle
actions = imp.load_source('core.actions', 'core/actions.py')
import json
from flask import Flask

app = Flask(__name__)

#sessions = {}

redis_url = os.getenv('REDISCLOUD_URL')
redis = redis.from_url(redis_url)

def get_session(session_id):
    redis_session_data = redis.get(session_id)
    if redis_session_data is None:
        return None
    session_data = pickle.loads(redis_session_data)
    return session_data

def new_session(session_data):
    session_id = str(uuid.uuid4())
    redis.set(session_id, pickle.dumps(session_data))
    return session_id
    
def save_session(session_id, session_data):
    redis.set(session_id, pickle.dumps(session_data))
    return session_id

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sessions/new', methods=['GET'])
def new():
    #TODO: call end_session
    new_session_data = actions.create_session_data()
    session_id = new_session(new_session_data)
    session_data = get_session(session_id)
    session_data['session_id'] = session_id
    response = actions.session_response(session_data)
    #res_json = json.dumps(response)
    return jsonify(response), 200

@app.route('/sessions/<session_id>/end', methods=['GET'])
def end_session(session_id):
    #TODO: call end_session
    return None, 200

@app.route('/sessions/<session_id>/next', methods=['GET'])
def next(session_id):
    session_data = get_session(session_id)
    if not session_data:
        return jsonify({'message': 'Session not found'}), 404
    session_data['session_id'] = session_id
    new_data = actions.on_next(session_data)
    save_session(session_id, new_data)
    res_json = json.dumps(new_data)
    return jsonify(res_json), 200


@app.route('/sessions/<session_id>/select_term', methods=['GET'])
def select(session_id):
    session_data = get_session(session_id)
    if not session_data:
        return jsonify({'message': 'Session not found'}), 404
    term = request.args.get('term')
    if not term:
        return jsonify({'message': 'Specify term query param'}), 400
    new_data = actions.on_select_term(session_data, term)
    save_session(session_id, new_data)
    new_data['session_id'] = session_id
    response = actions.session_response(new_data)
    #res_json = json.dumps(response)
    return jsonify(response), 200
