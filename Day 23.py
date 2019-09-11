d={'brand':'ford','model':'Mustang','Year':1964}
if 'brand' in d:
    print('yes , brand is one of the keys in d')
print(len(d))
d['color']='red'
print(d)
d.pop('brand')
print(d)
d.popitem()
print(d)
del d['Year']
print(d)
d.clear()
del d