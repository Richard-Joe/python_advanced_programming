# -*- coding: UTF-8 -*-

class BubbleExceptions(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        if exc_instance:
            print ('exception: %s.' % exc_instance)
        return False    # 抛出异常
        # return True   # 不抛出异常

if __name__ == '__main__':
    with BubbleExceptions() as ex:
        5 / 0
