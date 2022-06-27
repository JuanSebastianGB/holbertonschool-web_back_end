#!/usr/bin/env python3

""" app module """

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """
    It returns a JSON object with a key called "message"
    and a value of "Bienvenue"
    :return: A JSON object with a message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    It returns a JSON object with a key called "message"
    and a value of "User created"
    :return: A JSON object with a message
    """

    try:
        new_user = AUTH.register_user(**request.form)
        response = {
            "email": new_user.email,
            "message": "user created"
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"message": 'email already registered'}), 400


if __name__ == "__main__":
    """ Running the app on port 5000 """
    app.run(host="0.0.0.0", port="5000")
