#!/usr/bin/env python3
"""Authentication module for the API."""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if authentication is required."""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user."""
        return None
