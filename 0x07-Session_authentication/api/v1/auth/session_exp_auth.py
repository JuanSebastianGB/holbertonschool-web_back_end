#!/user/bin/env python3

import datetime
import os
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):

    def __init__(self) -> None:
        super().__init__()
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """
        It creates a session for a user, and returns the session ID

        :param user_id: The user_id of the user who is logging in
        :type user_id: str
        :return: session_id
        """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = user_id
        self.user_id_by_session_id['created_at'] = datetime.now()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        If the session ID is valid, return the user ID

        :param session_id: The session ID of the user
        :return: The user_id for the session_id
        """
        if not session_id:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return user_id
        created_at = self.user_id_by_session_id.get('created_at')
        if created_at is not None:
            return None
        duration_in_seconds = datetime.timedelta(seconds=self.session_duration)
        if duration_in_seconds < datetime.now():
            return None
        return user_id
