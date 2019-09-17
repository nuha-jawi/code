l=['banana','cherry','apple']
for x in l:
    print(x)
s='banana'
for a in s:
    print(a)
for b in l:
    print(b)
    if b=='cherry':
        break
for m in l:
    print(m)
    if m=='banana':
        continue