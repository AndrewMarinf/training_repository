questions = ["My name __ Vova\n", "I __ a coder\n", "I live __ Moscow\n"]
answers = ["is", "am", "in"]

# Счетчик баллов
correct_count = 0
incorrect_count = 0
question_total = 0

print('Привет! Предлагаю проверить свои знания английского!')
print("Наберите \'ready\',чтобы начать!")
ans = input()

if ans != 'ready':
    print('Кажется, вы не хотите играть Очень жаль.')
    
# запустить цикл по вопросам, используя индексы
# Для каждого индекса
for i in range(len(questions)):
        
  question_text = questions[i]
  answers_text = answers[i]
# Ввести вопрос
  print(questions[i])
#   Получить ответ
  user_input = input()

# Сравнить с правильным ответом
# Ответ совпадает?
  if user_input == answers_text:
        print ('Ответ верный')
        correct_count += 1
  else: 
        print(f'Неправильно.Правильный ответ:{answers_text}')
        incorrect_count +=1

# Почитать процент
question_total = len(questions)
correct_percent =  (correct_count/question_total * 100)

# вывести Вот и Все!
print("Вот и все!\n"
f"Вы ответили на {correct_count} вопросов из {question_total} верно,\n"
f"Это {correct_percent} процентов.\n")