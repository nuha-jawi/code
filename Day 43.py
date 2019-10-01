class class2:
    def __init__(self,name):

        self.name=name
    def func1(self):
        print('my name is '+self.name)

class class3(class2):
    #pass
    def __init__(self,name):
        class2.__init__(self,name)

x=class3('amani')
x.func1()
