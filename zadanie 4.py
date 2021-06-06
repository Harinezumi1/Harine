z = input('enter number :')
i = int(z)
ls = []
while i > 10:
    ls.append(i % 10)
    i //= 10
r = max(ls)
print(r)