# эта программа делает частотный словарь по авторам, т.е. у какого автора сколько статей
# она бежит по метаданным всех статей, вытаскивая из них авторов и кладя в словарь
# она может выдать весь словарь, может выдать n самых частых, может выдать тех, у кого 1 статья

import fitz
from collections import Counter
from pprint import pprint

d = Counter()

for i in range(1, 327):
    doc = fitz.open(str(i) + '.pdf') # открываем их подряд просто все
    x = doc.metadata
    a = x['author'] # вытаскиваем автора
    d[a] += 1 # прибавляем в Counter

answer = input('Хотите ли вы получить весь словарь? ')
if answer == 'yes' or answer == 'да':
    pprint(d) # если нужен словарь - печатаем словарь

answer = input('Хотите ли вы получить список из n самых частых авторов? ')
if answer == 'yes' or answer == 'да':
    n = int(input('А из скольких авторов? '))
    top_n = Counter(d).most_common(n)
    print(top_n) # если нужны топ-n, печатаем их

answer = input('Нужен ли вам список "одноразовых" авторов? ')
if answer == 'yes' or answer == 'да':
    only_one = []
    for key in d.keys():
        if d[key] == 1:
            only_one.append(key)
    print(only_one) # если нужны авторы по одному разу, печатаем их
