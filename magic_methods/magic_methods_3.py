# -*- coding: UTF-8 -*-

class MyClass(object):
    def __str__(self):
        return 'My Class string'

    def __unicode__(self):
        return u'unicode'

    def __bytes__(self):
        return b'bytes'

    def __bool__(self):
        return True

    def __int__(self):
        return int(999)

    def __float__(self):
        return float(77.77)

    def __complex__(self):
        return complex(1, 2)

if __name__ == '__main__':
    print (MyClass())

    print (bytes(MyClass()))

    print (bool(MyClass()))

    print (int(MyClass()))

    print (float(MyClass()))

    print (complex(MyClass()))
