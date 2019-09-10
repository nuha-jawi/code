d={}
print(d)
d1={'brand':'ford','model':'Mustang','Year':1964}
print(d1)
print(d1['model'])
print(d1.get('brand'))
d1['Year']=2019
print(d1)
for x in d1 :
    print(x)
for x in d1 :
    print(d1[x])
print(d1.values())
print(d1.items())
for x,y in d1.items():
    print(x,y)