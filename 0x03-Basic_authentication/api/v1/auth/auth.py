#!/usr/bin/env python3
""" Module for authentication
"""

from flask import request
from typing import TypeVar, List


class Auth():
    """class used for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if requiring auth is true"""
        return False

    def authorization_header(self, request=None) -> str:
        """sets the auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns current user"""
        return None
