#!/usr/bin/env python3
""" basic Auth Module """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ class BasicAuth """

    def __init__(self):
        """ __init__ """
        super().__init__()

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        It takes a string that looks like this:
        `Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`
        and returns this:
        `QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

        :param authorization_header: The value of the Authorization header
        :type authorization_header: str
        :return: The base64 encoded string is being returned.
        """
        import re
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        match_pattern = re.compile(r'^Basic (.*)$')
        match = match_pattern.match(authorization_header)
        if match is None:
            return None
        return match.group(1)

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        It takes a base64 encoded string and returns the decoded string

        :param base64_authorization_header: The base64 encoded authorization
        header
        :type base64_authorization_header: str
        :return: The decoded base64 string.
        """
        import base64
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header
            ).decode('utf-8')
        except Exception:
            return None
