#!/usr/bin/env python3
"""
Encrypts passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that a provided password matches a hash.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
