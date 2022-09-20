#!/usr/bin/env python3
"""defines the basic auth class
"""
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """the BasicAuth"""
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns base64 part of auth header"""
        if not authorization_header or type(authorization_header) != str:
            return None

        basicSearch = re.search("^Basic ", authorization_header)

        if basicSearch is None:
            return None

        return re.split('^Basic ', authorization_header)[0]
