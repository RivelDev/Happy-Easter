#Easter - Пасха
import random
import time

eggs = 0
eggs_give = random.randint(1, 2)
language = input('Русский or English? [RU|EN]: ') #выбор языка

if language == 'RU': #программа на русском
    inf_ru = input('Идем? [Да|Нет]: ')
    while inf_ru == 'Да':
        for i in range(1):
            print('Христос Воскрес!')
        answer_ru = input('Что нужно ответить?: ')
        if answer_ru == 'Воистину воскрес':
            print(answer_ru)
            eggs += (eggs_give)
            print(f'Вам дали яйца. Всего у вас {eggs} яиц.')
            if language == 'RU':
                if eggs >= 50:
                    print('-----------------------------')
                    print('Вы победили, получив 50 яиц! Чтобы играть дальше перезапустите игру. С пасхой!')
                    quit()
        elif answer_ru == 'quit':
            print('------------------------------------')
            print('Вы ввели команду выхода.')
            print('------------------------------------')
            time.sleep(5)
            quit()
        elif answer_ru == 'hack':
            print('------------------')
            print('Взлом пентагона... Подождите')
            time.sleep(5)
            eggs_give = eggs
            eggs_give += 3
            print('------------------')
            print(f'Успешный взлом. Теперь вам вам могут дать по 3 яйца')
        else: 
            print('Ты ответил неправильно. Яиц не дали')
        for y in range(1):
            print('--------------------------------')
    else:
        quit()
    
elif language == 'EN': #программа на англйиском
    inf_en = input('Lets go? [Yes|No]: ')
    while inf_en == 'Yes':
        for i in range(1):
            print('Happy Easter!')
        answer_en = input('What will you answer?: ')
        if answer_en == 'Truly he is risen':
            print(answer_en)
            eggs += (eggs_give)
            print(f'You got an eggs. Total you have {eggs} eggs.')
            if language == 'EN':
                if eggs >= 50:
                    print('-----------------------------')
                    print('You won by getting 50 eggs! Restart the game to continue playing. Easter!')
                    quit()
        elif answer_en == 'quit':
            print('-----------------------------')
            print('Quit command activated')
            print('-----------------------------')
            time.sleep(5)
            quit()
        elif answer_en == 'hack':
            print('------------------')
            print('Hack... Please wait')
            time.sleep(5)
            eggs_give = eggs
            eggs_give += 3
            print('------------------')
            print(f'Done. Now you can take {eggs_give} eggs')
        else: 
            print('Invalid answer. Try later :)')
        for y in range(1):
            print('--------------------------------')
    else:
        quit()