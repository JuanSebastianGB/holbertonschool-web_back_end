#!/usr/bin/env python3

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ class BasicAuth """

    def __init__(self):
        """ __init__ """
        super().__init__()
