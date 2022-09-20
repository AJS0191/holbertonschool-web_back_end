#!/usr/bin/env python3
"""defines the basic auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """the BasicAuth"""
    def __init__(self) -> None:
        super().__init__()
