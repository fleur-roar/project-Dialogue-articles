# эта программа нужна для генерации случайной статьи с Диалога
# она открывает json "номер" : "автор и название"
# далее генерирует номер и берет из json-а автора и название по этому номеру

import json
from random import randint # randint(a, b) генерирует число N такое, что a <= N <= b

with open('authors_and_titles_result.json', encoding='utf-8') as file:
    at = json.load(file) # сюда выгружаем авторов и названия

r = randint(1, 326) # сгенерировали число r такое, что 1 <= r <= 326
result = at[str(r)] # по этому номеру вытащили автора и название
print('Советуем почитать следующую статью:', result)
