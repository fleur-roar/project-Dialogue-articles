# эта программа взаимодействует с пользователем
# она принимает на вход ключевое слово и выводит статьи с ним, его частотность и некоторый итог

import json

key_word = input('Введите ключевое слово: ')

with open('find_key_words_result.json', encoding='utf-8') as file:
    key_words = json.load(file) # сюда выгружаем авторов и названия

if key_word not in key_words.keys():
    print('Ой, это ключевое слово нигде не встретилось...')
else:
    print(key_words[key_word])
    print()
    print('Итак, подведём итог! Это слово встретилось', len(key_words[key_word]), 'раз(а)!')

    if len(key_words[key_word]) == 1:
        print('Кажется, оно ооочень редкое...')
    elif len(key_words[key_word]) > 20:
        print('Вау! Оно одно из трёх самых частых!')
    elif len(key_words[key_word]) > 6:
        print('Вау! Оно одно из двадцати самых частых!')
    elif len(key_words[key_word]) > 3:
        print('Хммм... Довольно часто!')
    else:
        print('Хммм... Довольно редко!')
