# -*- coding: UTF-8 -*-

import functools
import time

"""
decorate class
"""

def sortable_by_creation_time(cls):
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self,  *args, **kwargs)
        self._created = time.time()
        print (self._created)
    cls.__init__ = new_init

    cls.__lt__ = lambda self, other : self._created < other._created
    cls.__gt__ = lambda self, other : self._created > other._created

    return cls

@sortable_by_creation_time
class Sortable(object):
    def __init__(self, identifier):
        self.identifier = identifier
    def __repr__(self):
        return self.identifier

if __name__ == '__main__':
    one = Sortable('first')
    two = Sortable('second')
    three = Sortable('third')

    sortables = [three, one, two]
    print (sortables)
    sorted(sortables)
    print (sortables)

    table = [5, 6, 1, 9, 3]
    print (sorted(table))
