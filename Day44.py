class class2:
    def __init__(self,name):
        self.name=name
    def func1(self):
        print('my name is '+self.name)

class class3(class2):
    def __init__(self,name,year):
        super().__init__(name)
        self.year=year
    def fun(self):
        print(self.year,self.name)
x=class3('amani',2000)
x.fun()
