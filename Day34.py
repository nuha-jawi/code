def func1(food):
    for x in food :
        print(x)
fruit=['apple','banana','pinapple']
func1(fruit)

def func2 (x):
    return x*2
print(func2(3))

def func3(child1,child2,child3):
    print('the youngest child is '+child2)
func3(child1='a',child2='aa',child3='aaa')

def func4(*kids):
    print('the smallest one is '+kids[1])
func4('Nuha','Heba','Abdullah')

def func5(k):
    if k>0:
        result=k+func5(k-1)
        print(result)
    else:
        result=0
    return result
print(func5(6))