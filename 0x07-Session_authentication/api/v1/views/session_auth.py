#!/usr/bin/env python3
# """ Module of Session Auth Routes """

import os
from models.user import User
from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    It checks if the email and password are in the request, if not it
    returns an error, if they are, it checks if the email is in the
    database, if not it returns an error, if it is, it checks if the
    password is valid, if not it returns an error, if it is, it creates
    a session and returns the user's information
    :return: A JSON object with the user information.
    """

    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
        users = User.search({"email": email})
        if not users:
            return jsonify(error="no user found for this email"), 404
        for user in users:
            if not user.is_valid_password(password):
                return jsonify({"error": "wrong password"}), 401
            else:
                from api.v1.app import auth
                session_id = auth.create_session(user.id)
                session_name = os.getenv("SESSION_NAME")
                user_dict = jsonify(user.to_json())
                user_dict.set_cookie(session_name, session_id)
                return user_dict


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    It destroys the session and returns a 200 status code if the
    session was destroyed, otherwise it returns a 404 status code
    :return: A JSON object with an empty dictionary and a 200 status code.
    """

    destroy_session = auth.destroy_session(request)

    if destroy_session:
        return jsonify({}), 200
    abort(404)
