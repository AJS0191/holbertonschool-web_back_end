#!/usr/bin/env python3
""" Module of session_auth class
"""
from api.v1.auth.basic_auth import BasicAuth
import uuid


class SessionAuth(BasicAuth):
    """class for session authorizations"""
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """creates a session id for a user id"""
        if not user_id or type(user_id) != str:
            return None
        else:
            sessionId = str(uuid.uuid4())
            self.user_id_by_session_id.update({user_id: sessionId})