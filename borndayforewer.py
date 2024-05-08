bornyear = int(input('Введите год рождения Пушкина: '))
while bornyear != 1799:
    print('Неверно!')
    bornyear = int(input('Введите год рождения Пушкина: '))
    if bornyear == 1799: break
print('Верно!')

bornday = int(input('Введиет день рождения Пушкина: '))
while bornday != 6:
    print('Неверно!')
    bornday = int(input('Введиет день рождения Пушкина: '))
    if bornday == 6: break
print('Верно')