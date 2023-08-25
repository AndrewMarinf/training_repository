questions = ["My name __ Vova\n", "I __ a coder\n", "I live __ Moscow\n"]
answers = ["is", "am", "in"]
while True:
    print ('Hello! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать')
    user_answers = input() 
    if user_answers == 'ready':
        print('Поехали')
    else:
        print('Кажеться, вы не хотите играть.Очень жаль.')
    break

#СЧЕТЧИК БАЛЛОВ
correct_answers = 0
uncorrect_answer = 0

# тут цикл для вопроcам

for list_questions in range(len(questions)):
    # ВЫВЕСТИ ВОПРОС
    print(questions[list_questions])
    # ОТВЕТ
    user_answer = input()
    if user_answer == answers[list_questions]:
        print('Красавчик')
        correct_answers +=1
    else:
        for attempts in range(1,-3):
            print(f'Осталось попыток:{attempts},попробуй еще раз')
        print(f'ЛОХ! Правильный ответ {answers[list_questions]}')
uncorrect_answer +=1  
    
print (f"Everything! Your answered  {correct_answers} from question {len(questions)}, this {round (correct_answers / len(questions) * 100 )}")

