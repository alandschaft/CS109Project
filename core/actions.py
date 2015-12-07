import imp
lib = imp.load_source('core.lib', 'core/lib.py')

data = lib.init_data()
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
        'candidate_terms': data['candidate_terms_init'],
        'candidate_docs': data['candidate_docs_init'],
        'ui_terms': data['ui_terms_init'],
        'ui_docs': data['ui_docs_init'],
        'selected_terms': []
    }
    return session_data


def on_next(session_data):
    print('1')
    session_data['candidate_terms'] = filter_terms(
        session_data['candidate_terms'],
        [t['text'] for t in session_data['ui_terms']]
    )
    print('2')
    session_data['ui_terms'] = get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )
    print('3')
    session_data['ui_docs'] = get_docs(session_data['ui_docs'])
    print('4')
    return session_response(session_data)


def on_select_term(session_data, term):

    session_data['selected_terms'].append({'text': term})
    session_data['candidate_terms'].remove(term)

    session_data['candidate_docs'] = [
        doc for doc in session_data['candidate_docs'] if term in doc
    ]

    session_data['ui_terms'] = get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )

    session_data['ui_docs'] = get_docs(session_data['ui_docs'])
    return session_response(session_data)
