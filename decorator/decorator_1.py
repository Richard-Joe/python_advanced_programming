# -*- coding: UTF-8 -*-

def decorated_1(func):
    func.__doc__ += '\nDecorator one'
    print ("This is decorated one")
    return func

def decorated_2(func):
    func.__doc__ += '\nDecorator two'
    print ("This is decorated two")
    return func

@decorated_2
@decorated_1
def add(x, y):
    """Return the sum of x and y."""
    return x + y

if __name__ == '__main__':
    print (add(3, 5))
    print (help(add))
