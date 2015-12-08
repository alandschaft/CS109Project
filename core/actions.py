import imp
lib = imp.load_source('core.lib', 'core/lib.py')

data = lib.init_data()
default_fields = ['session_id', 'ui_terms', 'ui_docs', 'selected_terms']


def session_response(session_data, fields=default_fields):
    print("res1")
    res={}
    print("res2")
    res['ui_docs']=session_data['ui_docs']
    print("res3")
    # filter terms with zero score
    res['ui_terms']=[x for x in session_data['ui_terms'] if x['score'] > 0]
    print("res4")
    res['N_candidate_docs']=len(session_data['candidate_docs'])
    print("res5")
    res['session_id']=session_data['session_id']
    print("res6")
    res['selected_terms']=session_data['selected_terms']
    print("res7")
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
    print("next1")
    session_data['candidate_terms'] = lib.filter_terms(
        session_data['candidate_terms'],
        [t['text'] for t in session_data['ui_terms']]
    )
    print("next2")
    session_data['ui_terms'] = lib.get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )
    print("next3")
    session_data['ui_docs'] = lib.get_docs(session_data['ui_docs'])
    print("next4")
    return session_response(session_data)


def on_select_term(session_data, term):

    session_data['selected_terms'].append({'text': term})
    session_data['candidate_terms'].remove(term)

    session_data['candidate_docs'] = [
        doc for doc in session_data['candidate_docs'] if term in doc
    ]

    session_data['ui_terms'] = lib.get_terms(
        session_data['candidate_terms'],
        session_data['candidate_docs']
    )

    session_data['ui_docs'] = lib.get_docs(session_data['ui_docs'])
    return session_response(session_data)
