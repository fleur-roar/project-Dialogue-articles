# эта программа пишет в файлы рекомендации по кей словам
# то есть при запросе определённой статьи она выводит для каждого её кей слова список где ещё оно есть

import json

for i in range (1, 62):
    toprint = '' # сюда будем писать выдачу
    
    with open('key_words_result.json', encoding='utf-8') as file:
        w = json.load(file) # сюда выгружаем ключевые слова по номерам
    if str(i) not in w.keys(): # если так получилось, что у статьи нет кей вордс
        toprint += 'Здравствуйте! К сожалению, у этой статьи нет ключевых слов... или они не отображаются...\n'

    else:
        words = w[str(i)] # достали список её кей вордс
            
        with open('find_key_words_result.json', encoding='utf-8') as file:
            k = json.load(file) # сюда выгружаем списки статей по ключевым словам

        with open('authors_and_titles_result.json', encoding='utf-8') as file:
            t = json.load(file) # сюда выгружаем авторов и названия
            title = t[str(i)][1] # название этой статьи
            author = t[str(i)][0] # автор этой статьи

        toprint += 'Здравствуйте! В этой статье следующие ключевые слова:\n'
        toprint += str(words)[1:len(str(words))-1] # вывели список, удалив значки [ ]
        toprint += '\nНам кажется, что вам было бы интересно почитать и другие статьи с этими ключевыми словами :)\n\n'

        for word in words: # для каждого ключевого слова
            toprint += 'Статьи с keyword \'' + word + '\':\n'
            new = '' # будем собирать сюда всех авторов и названия
            for article in k[word]:
                if article[1] == title and article[0] == author:
                    pass # если нашли ту же самую статью, что и это=а, то в рекомендации она не попадает
                else:
                    new += article[1] + ', ' + article[0] + '\n' # если другая, то добавили сюда
            if len(new) > 0:
                toprint += new # если хоть что-то другое с этим кей словом нашлось, т.е. оно встречается где-то ещё
            else:
                toprint += 'Ой, больше статей с этим ключевым словом нет :(\n'
            toprint += '\n'

        toprint += 'Надеемся, эти статьи будут интересны вам!'

    with open('key_words_' + str(i) + '.txt', 'w', encoding='utf-8') as new_file:
                    new_file.write(toprint) # открыли новый файл, записали туда всё это

