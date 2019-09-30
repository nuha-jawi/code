class class2:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def func1(self):
        print('my name is '+self.name)


b=class2(20,'Nuha')
b.age=30
print(b.age)
b.func1()
del b
print(b)