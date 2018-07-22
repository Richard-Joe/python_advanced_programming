# -*- coding: UTF-8 -*-

# __init__ 方法并没有创建新对象，该方法旨在为创建后的对象提供初始化数据。
# 
# 实际上，__init__ 方法并不返回任何值，在Python中所有的__init__都不返回值，如果用return返回值则会导致TypeError错误。
# 
# __new__方法实际上在__init__方法之前执行，用于创建类的实例。
# 
# __new__方法永远是静态的。

class MyClass(object):
    def __new__(cls):
        instance = super(MyClass, cls).__new__(cls)
        print ("__new__")
        return instance

    def __init__(self):
        print ("__init__")

    def __del__(self):
        print ("__del__")

    def __enter__(self):
        print ("__enter__")

    def __exit__(self, exc_type, exc_instance, traceback):
        print ("__exit__")

if __name__ == '__main__':
    with MyClass() as m:
        pass
