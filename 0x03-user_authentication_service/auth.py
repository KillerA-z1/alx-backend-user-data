#!/usr/bin/env python3
"""Authentication module for the API."""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password string and return the salted hash as bytes.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
