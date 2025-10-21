a = 0
b = 1        #переменные для фибоначчи
fib = 0

spisok = list()      #список с которым мы будем работать

summa = 0        #будущая сумма элементов

n = int(input('Номер конечного элемента: '))      #кол-во элементов

for i in range (0, n):              #создание фибоначчи
    spisok.append(a)
    fib = a + b
    a = b
    b = fib

print('Элементы: ', spisok)                #вывод начального списка

for i in range(0, len(spisok)):            #изменения четных и нечетных 
    if spisok[i] % 2 == 0:                  #четных
        spisok[i] = spisok[i]*2
    else:                                  #не четных
        spisok[i] = spisok[i] ** 2

mini = min(spisok)
maxi = max(spisok)               #мин и макс значения и кол-во элементов
lenth = len(spisok)

mid = sum(spisok) / n                 #мид значение
for i in range(0, len(spisok)):         #высчитывание элементов больше мида 
    if spisok[i] > mid:
        summa += 1                   #высчитывание кол-ва этих элементов

print(spisok)                      #итоги
print(maxi)
print(mini)
print(lenth)
print(summa)