class Library:
    def __init__(self,book,shelf):
        self.book=book
        self.shelf=shelf
obj=Library(300,45)
class science_section(Library):
    def __init__(self,book,shelf,name):
        super().__init__(book,shelf)
        self.name=name
    def func(self):
        print(self.shelf)
        print(self.book)
        print(self.name)
x=science_section(300,45,'physics books')
x.func()
x.shelf=4
x.book=20
print('after changing information')
x.func()

