#!/usr/bin/env python3
"""Authentication module for the API."""

from flask import request
from typing import List, TypeVar
from os import getenv


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
        # Check if the path matches any of the excluded paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def session_cookie(self, request=None):
        """Returns a cookie value from a request."""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        if session_name is None:
            return None
        return request.cookies.get(session_name)

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user."""
        return None
