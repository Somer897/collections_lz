dicto = {'Oleg': 'Domeyko 14', 'Dima': 'Lenin 7', 'Sanya': 'Kozlov 12'}   #our dict
choice = 0                                                              #переменная для операций 
print('Адреса: ', dicto)
while choice != 4:                                                  #цикл операций

    #выбор операций
    choice = int(input('Удалить(0), Изменить адресс(1), Просмотреть словарь(2), Выйти(3) : '))
    match choice:

        #1 операция
        case 0:
            a = str(input('Кого хотите удалить? '))

            #проверка нахождения элемента
            if a in dicto:
                del dicto[a]
            else:
                print('Error: такого человека и так нет в списке')

        #2 операция
        case 1:
            b = str(input('Кого адресс хотите изменить? '))
            c = str(input('Какой его новый адресс? '))

            #проверка нахождения элемента
            if b in dicto:
                dicto(b) == c
            else:
                print('Error: такой человек не найден')

        #операция 3
        case 2:
            print('Адресса: ', dicto)
            
        #операция 4(выход)
        case 3:
            choice = 4  #переменная к выходу
