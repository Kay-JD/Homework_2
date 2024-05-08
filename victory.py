# Словарь с именами знаменитостей и их годами рождения
celebrities = {
    "Эйнштейн": 1879,  # Правильный ответ: 1879
    "Михаэль Джексон": 1958,  # Правильный ответ: 1958
    "Александр Солженицын": 1918,  # Правильный ответ: 1918
    "Мария Кюри": 1867,  # Правильный ответ: 1867
    "Стив Джобс": 1955  # Правильный ответ: 1955
}

def play_quiz(celebrities):
    correct_answers = 0
    wrong_answers = 0

    # Итерируемся по словарю с вопросами
    for celebrity, birth_year in celebrities.items():
        guess = input(f"Введите год рождения {celebrity}: ")
        
        # Проверяем ответ
        if guess.isdigit() and int(guess) == birth_year:
            print("Верно!")
            correct_answers += 1
        else:
            print("Неверно.")
            wrong_answers += 1

    total_questions = len(celebrities)
    print("\nРезультаты:")
    print("Количество правильных ответов:", correct_answers)
    print("Количество неправильных ответов:", wrong_answers)
    print("Процент правильных ответов:", correct_answers * 100 / total_questions, "%")
    print("Процент неправильных ответов:", wrong_answers * 100 / total_questions, "%")

# Запускаем игру
play_quiz(celebrities)

# Спрашиваем пользователя, хочет ли он начать игру заново
while True:
    repeat = input("Хотите ли вы начать игру заново? (да/нет): ")
    if repeat.lower() == "да":
        play_quiz(celebrities)
    elif repeat.lower() == "нет":
        print("Спасибо за игру! До свидания!")
        break
    else:
        print("Некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")
