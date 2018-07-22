# -*- coding: UTF-8 -*-

import time


def squares_1():
    cursor = 1
    while True:
        yield cursor ** 2
        cursor += 1


def squares_2(cursor=1):
    while True:
        response = yield cursor ** 2
        if response:
            cursor = int(response)
        else:
            cursor += 1


if __name__ == '__main__':
    # for i in squares_1():
    #     print (i)
    #     time.sleep(0.5)

    sq = squares_2()
    print (next(sq))
    print (next(sq))
    sq.send(10)
    print (next(sq))
    print (next(sq))
