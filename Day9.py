firstName = 'Nuha {}'
salary=5000
a=firstName.format(salary)
print(a)
b='My name is Nuha , my salary is {} , and I am {} years old'
age=20
c=b.format(salary,age)
print(c)
d='My name is Nuha , my salary is {1} , and I am {0} years old'
print(d.format(salary,age))