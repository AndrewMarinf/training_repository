easy = {'say':'сказать','get':'получать','take':'брать','think':'думать','look':'смотреть'}
medium = {'use':'ипользовать','find':'находить','tell':'рассказывать','seem':'казаться','try':'пытаться'}
hard = {'leave':'оставлять','because':'потому что ','it depends':'это завист','lately':'недавно','open':'открыть'}

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

if user_answers == 'легкий':
        words = easy 

if user_answers == 'средний':
        words = medium 

if user_answers == 'сложный':
        words = hard 
else:
        print("Не знаю такой сложности")

        