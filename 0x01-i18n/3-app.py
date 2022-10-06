#!/usr/bin/env python3
"""this is the basic flask app starting with single route"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config():
    """config class for flask"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """uses best match from request with config.languages to get best locale"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index():
    """renders the 1-index template"""
    home_title = _('Welcome to Holberton')
    home_header = _('Hello World')
    return render_template('3-index.html', home_title=home_title,
                           home_header=home_header)
