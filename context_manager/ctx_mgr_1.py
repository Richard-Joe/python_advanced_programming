# -*- coding: UTF-8 -*-

class ContextManager(object):
    def __init__(self):
        print ("__init__")

    def __enter__(self):
        print ("__enter__")

    def __exit__(self, exc_type, exc_instance, traceback):
        print ("__exit__")


if __name__ == '__main__':
    with ContextManager() as cm:
        print ("hello")
