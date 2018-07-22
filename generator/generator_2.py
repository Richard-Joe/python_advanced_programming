# -*- coding: UTF-8 -*-

import time

def fibonacci():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]

if __name__ == '__main__':
    for i in fibonacci():
        print (i)
        time.sleep(0.5)
