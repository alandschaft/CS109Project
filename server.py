import os
from flask import Flask, jsonify
import uuid
from random import shuffle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Hello Indeed!'
