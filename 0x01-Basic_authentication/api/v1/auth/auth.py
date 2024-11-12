#!/usr/bin/env python3
"""Authentication module for the API."""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if authentication is required."""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        # Ensure path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'
        # Check if the path is in the list of excluded paths
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user."""
        return None
