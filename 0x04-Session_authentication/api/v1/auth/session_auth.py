#!/usr/bin/env python3
""" Module of session_auth class
"""
from api.v1.auth.basic_auth import BasicAuth


class SessionAuth(BasicAuth):
    def __init__(self) -> None:
        super().__init__()
