#!/usr/bin/env python3
"""authentication module"""
from base64 import encode
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes a password as a string and returns hashed bytes"""
    password = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
