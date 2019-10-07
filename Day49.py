x=200
y=500
def func():
    global x
    x=300
    y=700
    print(y)
    print(x)
func()
print(y)
print(x)