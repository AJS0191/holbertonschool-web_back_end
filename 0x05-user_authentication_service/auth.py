#!/usr/bin/env python3
"""authentication module"""
from base64 import encode
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm import sessionmaker
import uuid


def _hash_password(password: str) -> bytes:
    """takes a password as a string and returns hashed bytes"""
    password = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)


def _generate_uuid() -> str:
    """generates a uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """hashes a users password and saves it in database"""
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f'{user.email} already exists')
        else:
            password = _hash_password(password)
            user = self._db.add_user(email, password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """validating password for login"""
        user = self._db.find_user_by(email=email)
        if user:
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        return False

    def create_session(self, email: str) -> str:
        """creates a session id and stores it in user"""
        user = self._db.find_user_by(email=email)
        if user:
            i = _generate_uuid()
            self._db.update_user(user.id, session_id=i)
            return i

    def get_user_from_session_id(self, session_id: str) -> User:
        """gets user from session_id"""
        if not session_id:
            return None
        user = self._db.find_user_by(session_id=session_id)
        if not user:
            return None
        return user

    def destroy_session(self, user_id: int):
        """removes sesssion id from user"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """creates a reset token for user"""
        user = self._db.find_user_by(email=email)
        if user:
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        else:
            raise ValueError

    def update_password(self, reset_token: str, password: str):
        """updates a users password"""
        user = self._db.find_user_by(reset_token=reset_token)
        if not user:
            raise ValueError
        else:
            hashed = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed,
                                 reset_token=None)
