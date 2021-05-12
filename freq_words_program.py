# эта программа принимает на вход файл pdf, читает его и составляет список самых частотных слов
# частотные слова очищены от стоп-слов русского и английского языков
# на вход пользователь дает сколько слов он хочет и саму статью

import pdfminer.high_level
from collections import Counter

n = int(input('Введите, сколько слов вы бы хотели получить: '))

pdfdir = input('Введите путь к файлу: ')

textpdf = pdfminer.high_level.extract_text(pdfdir) # здесь текст из неё
textpdf = textpdf.replace('\n', ' ') # все абзацы превратили в пробелы, текст теперь - сплошная строка

# очистка от переносов
if '- ' in textpdf: # если они вообще есть
    j = 0
    k = len(textpdf)
    while j < k-2:
        if textpdf[j] == '-' and textpdf[j+1] == ' ': # если перенос с пробелом
            textpdf = textpdf[:j] + textpdf[j+2:] # делитнули позиции j и j+1
            k -= 2 # длина уменьшилась
        else:
            j += 1 # если не перенос с пробелом подряд - увеличили j, идем дальше

with open('stop_all.txt', encoding='utf-8') as f:
    stop_list = f.read() # это мы стоп-лист нужный прочитали
stop_words = []
for word in stop_list.split():
    word = word.strip('!~./\\"\'*(),;:?%^<>&-=+\n»«')
    stop_words.append(word) # токенизировали его
# токенизация - чтобы в конце слов не было всяких \n и подобного
# просто очистили от всего, сделали сам список стоп-слов

article = textpdf
words = []
for word in article.split():
    word = word.strip('!~./\\"\'*(),;:?%^<>&-=+\n»«')
    if word.lower() not in stop_words and word != '':
        words.append(word)
        # слово не пустое и слова нет в стоп-словах
        # важно, что именно word.lower() нет в стоп-словах

mostnwithfreq = [] # словарь для n самых частотных слов
mostn = [] # здесь он будет очищен от самих частотностей
mostnwithfreq = Counter(words).most_common(n)
for t in mostnwithfreq: # будем чистить словарь, доставая без частотностей
    mostn.append(t[0]) # сюда почистили
# если же мы хотим список слов с частотами, то нам нужен mostnwithfreq

print(mostn)

