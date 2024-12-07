def ask_question(question):

    print(question[0])
    user_answer = input("Ваш ответ: ")
    if user_answer == question[1]:
        print(f"Правильно! +{question[2]}\n")
        return question[2]
    else:
        print(f"Неправильно!\n")
        return 0


def run_ege_test():

    print("Добро пожаловать в экспертную систему по определения вашего балла на ЕГЭ по математике'!")

    # Список вопросов, правильных ответов и их ценность
    questions = [
        ("Сколько будет 7 * 8?", "56", 1),
        ("Чему равен корень из 49?", "7", 1),
        ("Решите уравнение: 5x = 20. Найдите x.", "4", 1),
        ("3/12 в % = ", "25", 2),
        ("Чему равна сумма углов треугольника?", "180", 2),
        ("sin^2x + cos^2x = ", "1", 3),
        ("log2(16) = ", "4", 3),
        ("При каких значения a уравнение не имеет корней y = x^2 + 4*x + a = 0")
    ]

    # Считаем баллы
    total_score = 0
    max_score = 0
    for question in questions:
        total_score += ask_question(question)
        max_score += question[2]
    total_score /= max_score
    your_ball = int(100*total_score)
    # Оценка результатов
    print(f"Вы бы набрали {your_ball}")

    if your_ball > 80:
        print('Отличный результат!')
    elif your_ball > 60:
        print('Хорошо!')
    elif your_ball > 30:
        print('Слабовато!')
    else:
        print('Плохо!')



# Запускаем тест
if __name__ == "__main__":
    run_ege_test()
