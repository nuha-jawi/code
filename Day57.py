import re
text='the rain in Mecca'
x=re.search('^the.*Mecca$',text)
if (x):
    print('yess')
else:
    print('noo')
