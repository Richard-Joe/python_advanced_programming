# -*- coding: UTF-8 -*-

import contextlib

@contextlib.contextmanager
def tag(name):
    print ("<%s>" % name)
    yield
    print ("/%s>" % name)

if __name__ == '__main__':
    with tag("h1"):
        print ("\thello")
