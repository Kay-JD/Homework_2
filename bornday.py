bornyear = int(input('Введите год рождения Пушкина: '))
if bornyear == 1799:
    print('Верно')
    bornday = int(input('Введиет день рождения Пушкина: '))
    if bornday == 6:
        print('Верно')
    else:
        print('Неверно')
else:
    print('Неверно')