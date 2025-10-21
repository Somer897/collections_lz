dicto = {'Oleg': 'Domeyko 14', 'Dima': 'Lenin 7', 'Sanya': 'Kozlov 12'}
choice = 0
print('Адреса: ', dicto)
while choice != 4:
    choice = int(input('Удалить(0), Изменить адресс(1), Просмотреть словарь(2), Выйти(3) : '))
    match choice:
        case 0:
            delete = int(input('Кого хотите удалить: Олег(1), Дима(2), Саня(3), Никого(любая клавиша) : '))
            match delete:
                case 1:
                    del dicto['Oleg']
                case 2:
                    del dicto['Dima']
                case 3:
                    del dicto['Sanya']
        case 1:
            change = int(input('Кого адресс хотите изменить: Олег(1), Дима(2), Саня(3), Никого(любая клавиша) : '))
            match change:
                case 1:
                    dicto['Oleg'] = str(input('Новый адресс Олега: '))
                case 2:
                    dicto['Dima'] = str(input('Новый адресс Димы: '))  
                case 3:
                    dicto['Sanya'] = str(input('Новый адресс Сани: '))
        case 2:
            print('Адресса: ', dicto)
        case 3:
            choice = 4
