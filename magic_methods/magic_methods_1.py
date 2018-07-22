# -*- coding: UTF-8 -*-

class MyClass(object):
    def __init__(self):
        pass

    def __eq__(self, other):
        return type(self) == type(other)

if __name__ == '__main__':
    print (MyClass())
    print (MyClass())
    print (MyClass() == MyClass())
    print (MyClass() == 42)
