#!/usr/bin/env python3
"""this is the basic flask app starting with single route"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """config class for flask"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """renders the 1-index template"""
    return render_template('1-index.html')
