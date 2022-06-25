a = input('Введите строку:')
b = a.split(' ')
c = []
for item in b:
    if item[0] == item[-1]:
        c.append(item)
    else:
        pass
print(c)
