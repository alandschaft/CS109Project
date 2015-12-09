import os
from operator import itemgetter
from random import shuffle

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def init_data():
    data = {}
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    terms = pd.read_pickle(os.path.join(path, '..', 'data', 'terms.pckl'))
    docs = pd.read_pickle(os.path.join(path, '..', 'data', 'trials.pckl'))
    data['candidate_terms_init'] = terms.term.values.tolist()
    data['candidate_docs_init'] = init_ui_docs_full(docs)
    # Holds the initial terms / docs lists we present with new sessions
    data['ui_terms_init'] = get_terms(data['candidate_terms_init'], data['candidate_docs_init'])
    return data

def init_ui_docs_full(docs_df):
    _docs = docs_df[['nct_id', 'title', 'url', 'terms']].to_dict('records')
    for doc in _docs:
        doc['terms'] = doc['terms'].tolist()
    return _docs

def get_freqs(terms, docs):
    _docs = ('|'.join(doc['terms']) for doc in docs)
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
        doc for doc in docs if len(set(doc['terms']).intersection(set(curr_terms))) < m
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

def get_tfidf_matrix_and_vectorizer(docs):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
        return tfidf_matrix, tfidf_vectorizer

def get_docs(docs, selected_terms, ui_terms, n_docs=20):
    '''
        Returns a list of doc indices (indices in docs) that is sorted:
        based on relevance to selected_terms and ui_terms
        
        Parameters:
        docs - The target list of documents. Each document is a string. Words are separated by spaces.
        selected_terms, ui_terms - The lists of terms. (each term is a string in the list)
        n_docs - the number of document indices to output
    '''
    if not docs:
        return []
    total_terms = selected_terms + ui_terms;
    # Create tf-idf vectorizer and matrix from the documents table
    tfidf_matrix, tfidf_vectorizer = get_tfidf_matrix_and_vectorizer(docs)
    # Vectorize the list of terms
    tfidf_total_terms = tfidf_vectorizer.transform([' '.join(total_terms)])
    # Calculate cosine similarities between the list of terms and each document
    score = cosine_similarity(tfidf_total_terms, tfidf_matrix)
    # Sort based on cosine similarities and return the indices of documents with higher scores
    return score.argsort().flatten()[-n_docs:][::-1]