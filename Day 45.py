t=('apple','banana','cherry')
tt = iter(t)
print(next(tt))
print(next(tt))
print(next(tt))
for v in t:
    print(v)
str = 'pinapple'
str2=iter(str)
print(next(str2))
print(next(str2))
print(next(str2))
print(next(str2))
print(next(str2))
print(next(str2))
print(next(str2))
print(next(str2))
for x in str :
    print(x)
class class2:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<6:
            x=self.num
            self.num+=1
            return x
        else:
            raise StopIteration
c=class2()
cc=iter(c)
print(next(cc))
print(next(cc))
print(next(cc))
print(next(cc))
print(next(cc))