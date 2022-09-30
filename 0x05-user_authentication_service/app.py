#!/usr/bin/env python3
"""flask app module"""
from crypt import methods
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first_route():
    """returns a jsonified message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST', 'GET'], strict_slashes=False)
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f'{email}', "message": "user created"}), 200


@app.route('/sessions', methods=['POST', 'GET'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        sess = AUTH.create_session(email)
        response = make_response(jsonify({"email": f'{email}',
                                          "message": "logged in"}), 200)
        response.set_cookie('session_id', sess)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH._db.update_user(user.id, session_id=None)
        redirect('/', 200)
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
