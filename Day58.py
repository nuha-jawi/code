import re
text='the rain in Mecca'
x=re.findall('a',text)
print(x)
if (x):
    print('yess')
else:
    print(noo)
y=re.search('\s',text)
print(y)
z=re.split('\s',text)
print(z)