# -*- coding: UTF-8 -*-

import functools
import json

"""
decorator parameters

传递给装饰器的参数只被处理一次，即"在函数声明并被装饰时"处理。与之相反，传递给函数"在该函数被调用时"处理。
"""

class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

def json_output(indent=None, sort_keys=False):
    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result =decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator

"""
等价于 @actual_decorator
函数的调用结果被应用到装饰器上
"""
@json_output(indent=4) 
def do_nothing():
    return {'status': 'done'}

"""
考虑如下情况：
@json_output
@json_output()
@json_output(indent=4)
"""

if __name__ == '__main__':
    print (do_nothing())