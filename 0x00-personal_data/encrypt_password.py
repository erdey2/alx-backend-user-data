#!/usr/bin/env python3
""" Encrypting passwords using bcrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns encripted password """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
