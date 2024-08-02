#!/usr/bin/env python3
""" Encrypting passwords using bcrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns encripted password """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed
