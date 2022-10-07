#!/usr/bin/env python3
"""this is the basic flask app starting with single route"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from os import getenv
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
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index():
    """renders the 1-index template"""
    home_title = _('Welcome to Holberton')
    home_header = _('Hello World')
    not_logged_in = _("You are not logged in")
    if g.user is not None:
        logged_in_as = _('You are logged in as %(username)s',
                         username=g.user.name)
        return render_template('5-index.html', home_title=home_title,
                               home_header=home_header,
                               logged_in_as=logged_in_as)
    return render_template('5-index.html', home_title=home_title,
                           home_header=home_header,
                           not_logged_in=not_logged_in)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(users: dict, num: int) -> dict:
    """grabs user from dictionary"""
    return users.get(num)


@app.before_request
def before_request():
    print('happening first')
    userId = request.args.get('login_as')
    print(f'{userId}')
    if userId:
        user = get_user(users, userId)
        if user:
            ('user')
            g.user = user
        else:
            print('no user')
            g.user = None
            print(f'{g.user} this should be none')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
