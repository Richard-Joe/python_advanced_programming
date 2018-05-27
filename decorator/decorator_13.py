# -*- coding: UTF-8 -*-

class Task(object):
    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement `run`.')

    def identify(self):
        return 'I am a task.'

def task1(decorated):
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass # 返回类本身

def task2(decorated):
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass() # 返回类的实例

@task1
def foo1():
    return 2 + 2

@task2
def foo2():
    return 2 + 2

if __name__ == '__main__':

    print (type(foo1))
    print (type(foo2))

    f = foo1()
    print (f.run())
    print (f.identify())

    print (foo2.run())
    print (foo2.identify())
