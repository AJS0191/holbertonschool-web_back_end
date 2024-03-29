#!/usr/bin/env python3
""" Module of session_auth class
"""
from api.v1.auth.basic_auth import BasicAuth
import uuid
from models.user import User


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
            self.user_id_by_session_id.update({sessionId: user_id})
            return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """gets a user_id based on session"""
        if not session_id or type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns the current user based on session id cookie"""
        uID = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(uID)
