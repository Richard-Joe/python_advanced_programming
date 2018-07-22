# -*- coding: UTF-8 -*-

# 一个生成器调用其他生成器也是可行的。
# 
# Python3.3 引入了新的 yield from 语句

import itertools

def gen1():
    yield 'foo'
    yield 'bar'

def gen2():
    yield 'spam'
    yield 'eggs'

def full_gen_1():
    for word in gen1():
        yield word
    for word in gen2():
        yield word


def full_gen_2():
    for word in itertools.chain(gen1(), gen2()):
        yield word


def full_gen_3():
    """
    生成器委托
    """
    yield from gen1()
    yield from gen2()


if __name__ == '__main__':
    for i in full_gen_1():
        print (i)
    print ('')

    for i in full_gen_2():
        print (i)
    print ('')

    for i in full_gen_3():
        print (i)
    print ('')
