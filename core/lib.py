import os
from operator import itemgetter
from random import shuffle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


def init_data():
    data = {}
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    terms = pd.read_pickle(os.path.join(path, '../', 'data', 'terms.pckl'))
    docs = pd.read_pickle(os.path.join(path, '../', 'data', 'trials.pckl'))
    data['candidate_terms_init'] = terms.term.values.tolist()
    data['candidate_docs_init'] = [list(doc['terms']) for doc in docs[['terms']].to_dict('records')]
    data['ui_docs_full'] = docs[['nct_id', 'title', 'url']].to_dict('records')
    data['ui_docs_init'] = get_docs(data['ui_docs_full'])
    data['ui_terms_init'] = get_terms(data['candidate_terms_init'], data['candidate_docs_init'])
    return data


def get_freqs(terms, docs):
    _docs = ('|'.join(doc) for doc in docs)
    cv = CountVectorizer(vocabulary=terms, analyzer=lambda doc: doc.split('|'))
    m = cv.transform(_docs)
    terms_freq = sorted(
        [{'text': term, 'score': int(freq)} for term, freq in zip(terms, m.getnnz(0))],
        key=itemgetter('score'),
        reverse=True
    )
    return terms_freq


def filter_terms(terms, excl_terms):
    _terms = list(set(terms) - set(excl_terms))
    return _terms


def filter_docs(docs, curr_terms, m):
    _docs = [
        doc for doc in docs if len(set(doc).intersection(set(curr_terms))) < m
    ]
    return _docs


def get_terms(terms, docs, n=40, k=10, m=5):
    """
        (n, k, m) realization, which takes terms and docs
        and returns n terms with freqs.
    """
    curr_terms_freq = []
    _terms = terms[:]
    _docs = docs[:]
    while len(curr_terms_freq) < n:
        terms_freq = get_freqs(_terms, _docs)
        curr_terms_freq += terms_freq[:k]
        curr_terms = [t['text'] for t in curr_terms_freq]
        _terms = filter_terms(_terms, curr_terms)
        _docs = filter_docs(_docs, curr_terms, m)

    return curr_terms_freq[:n]


def get_docs(docs, n=40):
    shuffle(docs)
    return docs[:n]
