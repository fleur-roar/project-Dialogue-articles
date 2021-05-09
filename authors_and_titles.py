# эта программа вытаскивает из всех статей автора и название и кладет их в json
# кладет словарем в формате "номер статьи" : "(автор, название)"

import fitz, json

d = {} # это словарь, где будут лежать метаданные - авторы и названия всех статей по номерам
# формат словаря "номер статьи" : "(автор, название)"

for i in range(1, 327):
    doc = fitz.open(str(i) + '.pdf') # открываем их подряд просто все
    x = doc.metadata
    a = x['author'] # вытаскиваем автора
    if a is None or a == '':
        a = 'ой, автор не определяется...'
    t = x['title'] # вытаскиваем название
    if t is None or t == '':
        t = 'ой, название не определяется...'
    d[i] = (a, t)

with open('authors_and_titles_result.json', 'w') as write_file:
    json.dump(d, write_file) # запишем всё это в json-файл
