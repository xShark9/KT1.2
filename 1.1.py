x = ''
a = input("Введите строку: ").lower().split()
for i in range(len(a)):
 a [i] = sorted(a[i])
 x += ''.join(a[i]) + ' '
a = x
print(a)