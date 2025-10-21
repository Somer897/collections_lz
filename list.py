a = 0
b = 1
fib = 0
spisok = list()
summa = 0
n = int(input('Номер конечного элемента: '))
for i in range (0, n):
    spisok.append(a)
    fib = a + b
    a = b
    b = fib

print('Элементы: ', spisok)

for i in range(0, len(spisok), 2):
    spisok[i] = spisok[i]*2
for i in range(1, len(spisok), 2):
    spisok[i] = spisok[i] ** 2

mini = min(spisok)
maxi = max(spisok)
lenth = len(spisok)

mid = sum(spisok) / n
for i in range(0, len(spisok)):
    if spisok[i] > mid:
        summa += 1

print(spisok)
print(maxi)
print(mini)
print(lenth)
print(summa)