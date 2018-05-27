# -*- coding: UTF-8 -*-

import functools
import logging
import time

"""
Log Management
"""

def logged(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        start = time.time()
        return_values = method(*args, **kwargs)
        end = time.time()
        delta = end - start

        logger = logging.getLogger('decorated.logged')
        logger.warn('Called method %s at %.02f; execution time %.02f seconds; resukt %r.'
                    % (method.__name__, start, delta, return_values))
        return return_values
    return inner

@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value

if __name__ == '__main__':
    sleep_and_return(42)