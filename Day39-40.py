def fun (p,n):
    if p > 0:
        r = n * fun(p-1,n)
    else:
        r = 1
    return r
print(fun(3,5))
list =[-4,-6,-5,-1,2,3,7,9,88]
x=lambda a : a>0
for n in list:
    if x(n):
        print(n)