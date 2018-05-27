# -*- coding: UTF-8 -*-

import functools

"""
User Authentication
"""

class User(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AnonymousUser(User):
    def __init__(self):
        self.username = None
        self.email = None

    def __nonzero__(self):
        return False;

def requires_ints(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to run this.')
    return inner