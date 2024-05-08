bornyear = int(input('Введите год рождения Пушкина: '))
while bornyear != 1799:
    print('Неверно!')
    bornyear = int(input('Введите год рождения Пушкина: '))
    if bornyear == 1799: break
print('Верно!')