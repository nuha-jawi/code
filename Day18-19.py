fruits=['cherry','apple','orange','melon']
#append
fruits.append('watermelon')
print(fruits)
#reverse
fruits.reverse()
print(fruits)
#remove
fruits.remove(fruits[2])
print(fruits)
#count
print(fruits.count('apple'))
tuple=("java","python","swift")
if 'python' in tuple:
    print('python in a tuple')
else:
    print('python not in a tuple')