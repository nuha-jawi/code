def func(n):
    return lambda a : a*n
d=func(2)
d1=func(3)
print(d1(11))
print(d(11))