# -*- coding: UTF-8 -*-

# 生成器是一种迭代器，迭代器是包含__next__方法的任何对象。
# 
# 迭代对象是任何定义了__iter__方法的对象。可迭代对象的__iter__方法负责返回一个迭代器。

r = range(0, 5)   # 迭代对象
it = iter(r)      # 迭代器

print (next(it))
print (next(it))
print (next(it))

# 生成器可以是迭代器，但不一定是迭代对象。
