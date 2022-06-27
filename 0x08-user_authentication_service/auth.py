#!/usr/bin/env python3
""" module to hash a password """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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

        if not email or not password:
            raise ValueError("Email and password are required.")
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        new_user = {
            'email': email,
            'hashed_password': _hash_password(password)
        }
        user = self._db.add_user(**new_user)
        return user
