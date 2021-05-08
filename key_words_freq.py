# эта программа открывает json с названием 'key_words_result.json'
# в нем лежит словарь key words в формате "номер статьи" : "список key words"
# далее программа составляет частотные словари key words, нужные пользователю
# варианты - год от 2016 до 2020 или за все годы

import json
from pprint import pprint
from collections import Counter

c = Counter()

with open('key_words_result.json', encoding='utf-8') as file:
    d = json.load(file) # сюда выгружаем содержимое

# сейчас мы примем на вход нужный год
answer = input('За какой год вы бы хотели получить key words? Если за все, то введите "за все": ')

if answer == '2016':
    i = 259
    j = 327
elif answer == '2017':
    i = 189
    j = 259
elif answer == '2018':
    i = 125
    j = 189
elif answer == '2019':
    i = 62
    j = 125
elif answer == '2020':
    i = 1
    j = 62
elif answer == 'за все':
    i = 1
    j = 327

# в зависимости от года мы определили диапазон статей, из которых нам нужно делать словарь
for key in d.keys(): # здесь мы делаем то, что просит пользователь - составляем нужный словарь
    if int(key) in range(i, j):
        for word in d[key]:
            c[word] += 1

pprint(c) # выводим то, что попросил пользователь
