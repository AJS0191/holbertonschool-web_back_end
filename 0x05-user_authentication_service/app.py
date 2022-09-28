#!/usr/bin/env python3
"""flask app module"""
from flask import Flask, jsonify, request
from auth import Auth
import sys

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
    return jsonify({"email": f'{email}'}, {"message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
