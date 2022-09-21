#!/usr/bin/env python3
"""defines the basic auth class
"""

import base64
import binascii
from api.v1.auth.auth import Auth
import re
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """the BasicAuth"""
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns base64 part of auth header"""
        if not authorization_header or type(authorization_header) != str:
            return None

        basicSearch = re.search("^Basic ", authorization_header)

        if basicSearch is None:
            return None

        return re.split('^Basic ', authorization_header)[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns user credintials"""
        if not decoded_base64_authorization_header:
            return (None, None)

        if type(decoded_base64_authorization_header) != str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        eNP = re.split(':', decoded_base64_authorization_header)
        return (eNP[0], eNP[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        """returns User instance"""
        if not user_email or type(user_email) != str:
            return None

        if not user_pwd or type(user_pwd) != str:
            return None

        try:
            userMatch = User.search({'email': user_email})
            for user in userMatch:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the user"""
        try:
            authHeader = self.authorization_header(request)
            b64 = self.extract_base64_authorization_header(authHeader)
            decode = self.decode_base64_authorization_header(b64)
            userC = self.extract_user_credentials(decode)
            return self.user_object_from_credentials(userC[0], userC[1])
        except Exception:
            return None
