import re
str='The rain in Spain'
x=re.sub("\s","9",str,1)
print(x)
y=re.search(r"\bS\w+",str)
print(y.span())
print(y.string)
print(y.group())