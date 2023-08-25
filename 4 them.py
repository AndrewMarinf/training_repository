words_seasy = {'say':'сказать','get':'получать','take':'брать','think':'думать','look':'смотреть'}
words_medium = {'use':'ипользовать','find':'находить','tell':'рассказывать','seem':'казаться','try':'пытаться'}
words_hard = {'leave':'оставлять','because':'потому что ','it depends':'это завист','lately':'недавно','open':'открыть'}

levels = {
    0:'Нулевой',
    1:'Так себе',
    2:'Можно лучше',
    3:'Норм',
    4:'Хорошо',
    5:'Отлично',
}

answers ={}

print('Выберите уровент сложности')
print('Легкий,средний,сложный')

user_answers = input().lower()
# words = None
if user_answers == 'легкий':
        words = words_seasy 

elif user_answers == 'средний':
        words = words_medium 

elif user_answers == 'сложный':
        words = words_hard 
# else:
#         print("Не знаю такой сложности")

words_count = len(words)

print(f'Выбран уровень сложности,мы предложим {words_count} слов, подберите перевод')

for word_en, word_ru in words.items():
        # print('Поехали')

        litter_count = len(word_ru)
        first_letter = word_ru[1]

print(f' {word_en}, {litter_count} букв,начинается на {first_letter}...')
user_answer = input().lower()

if user_answer == word_ru:
        print(f'Верно,{word_en} это {word_ru}')
        answers[word_en] = True
else:
        print(f'Наверное,{word_en} это {word_ru}')
        answers[word_en] = False