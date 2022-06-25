#!/usr/bin/env python3
""" Session db Auth module"""

from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ It's a session manager that uses the
    database to store session information"""

    def create_session(self, user_id=None):
        """
        It creates a session for a user.

        :param user_id: The user_id of the user to create a session for
        :return: The session_id is being returned.
        """

        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        new_user = UserSession(user_id=user_id, session_id=session_id)
        new_user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        If the session_id is valid, return the user_id associated with it

        :param session_id: The session ID that you want to look up
        :return: The user_id for the session_id
        """

        if session_id is None:
            return None
        try:
            matches = UserSession.search({session_id: session_id})
            if matches is None:
                return None
            for match in matches:
                created_at = match.get('created_at')
                if not created_at:
                    return None
                if created_at + timedelta(self.session_duration) <\
                        datetime.now():
                    return None
                return match.get('user_id')
            return None
        except Exception as e:
            return e

    def destroy_session(self, request=None):
        """
        It deletes the session id from the dictionary

        :param request: The request object
        :return: A boolean value.
        """

        if request is None:
            return None
        session_cookie = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_cookie)
        if session_id is None:
            return None
        try:
            UserSession.delete(session_id)
            return True
        except Exception as e:
            return e
