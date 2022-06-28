#!/usr/bin/env python3
""" module to hash a password """

from uuid import uuid4
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from flask import jsonify


def _hash_password(password: str):
    """
    It takes a password as a string, generates a salt, and then hashes the
    password using the salt

    :param password: The password to hash
    :type password: str
    :return: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        "Register a new user with the given email and password."

        The first thing we do is check that the email and password are not
        empty. If they are, we raise a ValueError

        :param email: str
        :type email: str
        :param password: str
        :type password: str
        :return: User object
        """
        try:
            self._db.find_user_by(email=email)
            raise(ValueError)
        except NoResultFound:
            hashed_password = _hash_password(password)
            created_user = self._db.add_user(email, hashed_password)
            return created_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        "Check if the given email and password are valid."

        :param email: str
        :type email: str
        :param password: str
        :type password: str
        :return: True if the email and password are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def _generate_uuid(self):
        """
        "Generate a new UUID."

        :return: str
        """
        return str(uuid4())

    def create_session(self, email: str) -> str:
        """ Create a new session for the user with the given email."""

        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
