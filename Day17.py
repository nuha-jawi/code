t=(1,2,3,4,5,6)
if 1 not in t:
    print('one is not in tuple')
else:
    print('one is already in the tuple')
t2=('melon',)
print(t2*3)
t3=t+t2
print(t3)
print(len(t3))
t4=tuple(('watermelon','lemon','orange','lemon'))
print(t4)
print(t4.count('lemon'))
print(t4.index('orange'))
