# -*- coding: UTF-8 -*-

z = zip(['a', 'b', 'c'], ['x', 'y'])

print (next(z))
print (next(z))
# print (next(z))


m = map(lambda x, y: max([x, y]), [4, 1, 7], [3, 4, 5])

print (next(m))
print (next(m))
print (next(m))
