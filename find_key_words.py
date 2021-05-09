# эта программа создает из двух словарей один
# она выгружает словарь "номер статьи" : "(автор, название)"
# и словарь "номер статьи" : "список key words"
# и дальше она для каждого ключевого слова делает список статей, в которых оно есть
# после этого она записывает полученный словарь в json 'find_key_words_result.json'

import json
from collections import defaultdict

with open('authors_and_titles_result.json', encoding='utf-8') as file:
    m = json.load(file) # сюда выгружаем авторов и названия

with open('key_words_result.json', encoding='utf-8') as file:
    k = json.load(file) # сюда выгружаем key words

d = defaultdict(list)
# словарь "ключевое слово" : "список авторов и названий статей, где оно есть"

for key in k.keys():
    for word in k[key]:
        d[word].append(m[key])

with open('find_key_words_result.json', 'w') as write_file:
    json.dump(d, write_file) # запишем всё это в json-файл
