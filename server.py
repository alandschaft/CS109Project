import os
from flask import Flask, jsonify
import uuid
from random import shuffle
import pandas as pd

app = Flask(__name__)

sessions = {}
data = {}


def init_search_server():
    terms = pd.read_pickle(os.path.join('data', 'terms.pckl'))
    documents = pd.read_pickle(os.path.join('data', 'trials.pckl'))
    data['terms'] = terms.term.values.tolist()
    data['trials'] = documents[['nct_id', 'title', 'url']].to_dict('records')


def get_current_terms(num=50):
    shuffle(data['terms'])
    return data['terms'][:num]


def create_session():
    session_data = {
        'session_id': uuid.uuid4(),
        'current_terms': get_current_terms(),
        'skipped_terms': [],
        'clicked_terms': [],
        'current_documents': data['trials']
    }
    sessions[session_data['session_id']] = session_data

    return {
        'session_id': session_data['session_id'],
        'current_terms': session_data['current_terms'],
        'current_documents': session_data['current_documents'][:20]
    }


def on_next(session_id):
    session_data = sessions.get(session_id, None)
    if not session_data:
        session_id = create_session()['session_id']
        session_data = sessions[session_id]
    session_data['skipped_terms'] += session_data['current_terms']
    session_data['current_terms'] = get_current_terms()
    return {
        'session_id': session_data['session_id'],
        'current_terms': session_data['current_terms'],
        'current_documents': session_data['current_documents'][:20]
    }


def on_select_term(session_id, term):
    session_data = sessions.get(session_id, None)
    if not session_data:
        session_id = create_session()['session_id']
        session_data = sessions[session_id]
    session_data['clicked_terms'].append(term)
    session_data['current_terms'] = get_current_terms()
    return {
        'session_id': session_data['session_id'],
        'current_terms': session_data['current_terms'],
        'current_documents': session_data['current_documents'][:20]
    }


@app.route('/sessions/new', methods=['GET'])
def new():
    return jsonify(create_session()), 201


@app.route('/sessions/<session_id>/next', methods=['GET'])
def next(session_id):
    return jsonify(on_next(session_id)), 200


@app.route('/sessions/<session_id>/select/<term>', methods=['GET'])
def select(session_id, term):
    return jsonify(on_select_term(session_id, term)), 200

if __name__ == '__main__':
    init_search_server()
    app.run(debug=True)