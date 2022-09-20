#!/usr/bin/env python3
"""defines the basic auth class
"""
from mimetypes import init
from auth import Auth


class BasicAuth(Auth):
    def __init__(self) -> None:
        super().__init__()
