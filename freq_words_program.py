from collections import Counter

language = input('Введите en, если ваша статья на английском, и ru, если на русском: ')
file = input('Пожалуйста, введите путь к файлу: ')
n = int(input('Введите, сколько слов вы бы хотели получить: '))

with open('stop_' + language + '.txt', encoding='utf-8') as f:
    my_words = f.read() # это мы стоп-лист нужный прочитали
stop_words = []
for word in my_words.split():
    word = word.strip('!~./\\"\'*(),;:?%^<>&-=+\n»«')
    stop_words.append(word) # токенизировали его
# токенизация - чтобы в конце слов не было всяких \n и подобного
# просто очистили от всего, сделали сам список стоп-слов

with open(file, encoding='utf-8') as f:
    article = f.read() # а здесь будет статья
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

