#!/usr/bin/env python3
""" Module of Auth Class """

from typing import List, TypeVar
from flask import request


class Auth:
    """ class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        If the path is not in the list of excluded paths, then require
        authentication

        :param path: The path of the request
        :type path: str
        :param excluded_paths: A list of paths that do not require
        authentication
        :type excluded_paths: List[str]
        :return: A boolean value.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path + '/' if path[-1] != '/' else path
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
