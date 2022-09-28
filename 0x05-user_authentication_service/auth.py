#!/usr/bin/env python3
"""authentication module"""
from base64 import encode
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm import sessionmaker, scoped_session
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
            self._db.add_user(email, password)
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
            user.session_id = i
            return i
