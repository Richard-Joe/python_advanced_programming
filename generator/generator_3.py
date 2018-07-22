# -*- coding: UTF-8 -*-

def my_gen():
    yield 1
    yield 2
    raise StopIteration
    yield 3

if __name__ == '__main__':
    print ([i for i in my_gen()])

    gen = my_gen()
    print (next(gen))
    print (next(gen))
    print (next(gen))
