#!/usr/bin/env python3
"""authentication module"""
from base64 import encode
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm import sessionmaker, scoped_session


def _hash_password(password: str) -> bytes:
    """takes a password as a string and returns hashed bytes"""
    password = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """hashes a users password and saves it in database"""
        if self._db._session is None:
            Base.metadata.create_all(self._db._engine)
            sessionF = sessionmaker(bind=self._db._engine,
                                    expire_on_commit=False)
            Session = scoped_session(sessionF)
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f'{user.email} already exists')
        else:
            password = _hash_password(password)
            self._db.add_user(email, password)
            return user
