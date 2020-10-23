#!/usr/bin/env python3

import pickle
from flask import escape
from sklearn.feature_extraction.text import CountVectorizer


def process_input(req: 'flask_request') -> list:
    '''This function extracts a value from a POST request and returns the value as a list.'''
    snippet = escape(req.form['snippet'])
    return [snippet]


def classify_text(req: 'flask_request') -> int:
    '''This function classifies a snippet extracted from a POST request as spam or ham.'''

    data = process_input(req)

    transformer = pickle.load(open("tfr.pkl", "rb"))
    vec = transformer.transform(data)

    model = pickle.load(open("model.pkl", "rb"))
    pred = model.predict(vec)
    print('type of pred is:', type(pred), pred)
    return pred, data
