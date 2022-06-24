#!/usr/bin/env python3
""" Session Auth module"""

import uuid


class SessionAuth():
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session for the user with the given user_id,
        and return the session_id.

        :param user_id: The user ID of the user to create a session for
        :type user_id: str
        :return: A session ID
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
