questions = ["My name __ Vova\n", "I __ a coder\n", "I live __ Moscow\n"]
answers = ["is", "am", "in"]

print('Привет! Предлагаю проверить свои знания английского!')
word = 'ready'
ans = input("Наберите 'ready', чтобы начать!")
if str(ans) == word:
    print('Поехали')
else:
    print('Кажется, вы не хотите играть Очень жаль.')
    while True:

        # Счетчик баллов
        correct_answers = 0
        uncorrect_answer = 0

        # Первый вопрос
        first_question = input(questions[0])
        if str(first_question) == (answers[0]):
            print("Ответ верный!")
            correct_answers += 1
        else:
            for i in range(-3, -0):
                print(f'Осталось попыток', [i], 'попробуй еще раз ')
                w = input(questions[0])
        print('Увы, но нет.Правильный ответ' + ' ' + answers[0])

        # Второй вопрос
        second_question = input(questions[1])
        if str(second_question) == (answers[1]):
            print("Ответ верный!")
            correct_answers += 1
        else:
            print('Непрвильно.Правильный ответ' + ' ' + answers[1])

            # Третий вопрос
        third_question = input(questions[2])
        if str(third_question) == (answers[2]):
            print("Ответ верный!")
            correct_answers += 1
        else:
            print('Непрвильно.Правильный ответ' + ' ' + answers[2])
        break

    # Колличесво баллов пользователя.
user_score = correct_answers * 10
# Количество процентов
user_percentage = int((correct_answers / 3) * 100)

# Подсчет всех вопрос
print("Вот и все!\n"
      f"Вы ответили на {correct_answers} вопросов из {len(questions)} верно,\n"
      f"Это {user_percentage} процентов.\n")
