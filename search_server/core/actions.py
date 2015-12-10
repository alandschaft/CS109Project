from lib import init_data, get_terms, get_docs, filter_terms
import copy

data = init_data()
default_fields = ['session_id', 'ui_terms', 'ui_docs', 'selected_terms']


def session_response(session_data, fields=default_fields):
    res={}
    res['ui_docs']=session_data['ui_docs']
    # filter terms with zero score
    res['ui_terms']=[x for x in session_data['ui_terms'] if x['score'] > 0]
    res['N_candidate_docs']=len(session_data['candidate_docs'])
    res['session_id']=session_data['session_id']
    res['selected_terms']=session_data['selected_terms']
    return res

def create_session_data():

    session_data = {
        'n_show_docs': 20,
        'candidate_terms': copy.deepcopy(data['candidate_terms_init']),
        'candidate_docs': copy.deepcopy(data['candidate_docs_init']),
        'ui_terms': copy.deepcopy(data['ui_terms_init']),
        'ui_docs': copy.deepcopy(data['candidate_docs_init'][:20]),
        'selected_terms': []
    }
    return session_data


def on_next(session_data):

    session_data['candidate_terms'] = filter_terms(
        session_data['candidate_terms'],
        [t['text'] for t in session_data['ui_terms']]
    )

    session_data['ui_terms'] = get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )

    session_data['ui_docs'] = get_session_docs(session_data)
    return session_response(session_data)


def on_select_term(session_data, term):

    session_data['selected_terms'].append({'text': term})
    if term in session_data['candidate_terms']: session_data['candidate_terms'].remove(term)

    session_data['candidate_docs'] = [
        doc for doc in session_data['candidate_docs'] if term in doc['terms']
    ]

    session_data['ui_terms'] = get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )

    session_data['ui_docs'] = get_session_docs(session_data)
    return session_response(session_data)

def get_session_docs(session_data):
    # Get the indices of the most relevant documents
    indices = get_docs([' '.join(doc) for doc in [doc['terms'] for doc in session_data['candidate_docs']]]
             , [t['text'] for t in session_data['selected_terms']]
             , [t['text'] for t in session_data['ui_terms']])
    # Return the documents in the returned indices 
    return [session_data['candidate_docs'][i] for i in indices]