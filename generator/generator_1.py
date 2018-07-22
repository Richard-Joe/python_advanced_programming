# -*- coding: UTF-8 -*-

def fibonacci():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8
    yield 13

if __name__ == '__main__':
    for i in fibonacci():
        print (i)
