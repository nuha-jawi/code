x=300
def func():
    x=900
    def funcc():
        print(x)
    funcc()
func()
print(x)
def funccc():
    print(x)
funccc()