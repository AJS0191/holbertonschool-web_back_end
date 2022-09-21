#!/usr/bin/env python3
"""defines the basic auth class
"""
import base64
import binascii
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

        return re.split('^Basic ', authorization_header)[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """decodes base64"""
        if not base64_authorization_header:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None
        else:
            return decoded.decode('utf-8')
