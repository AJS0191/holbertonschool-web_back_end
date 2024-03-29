#!/usr/bin/env python3
"""this is the basic flask app starting with single route"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """renders the 0-index template"""
    return render_template('0-index.html')
