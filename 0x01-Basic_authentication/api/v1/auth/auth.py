#!/usr/bin/env python3
"""Basic authentication module """
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class """

    def __init__(self):
        """ Initializer """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ """
        pass

    def authorization_header(self, request=None) -> str:
        """ """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """ """
        pass
