#!/usr/bin/env python3
""" Module for authentication
"""

from flask import request
from typing import TypeVar, List


class Auth():
    """class used for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if requiring auth is true"""
        if excluded_paths is None or path is None:
            return True

        if path in excluded_paths or path + '/' in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """sets the auth header"""

        if request is None:
            return None
        
        if request.form.get("Authorization"):
            return request.form.get("Authorization")
        
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns current user"""
        return None
