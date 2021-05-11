# эта программа вытаскивает из всех статей key words и записывает их в файл json
# записывает она их в формате словаря "номер статьи" : "список key words"
# она нужна, чтобы не запускать программу из 326 статей каждый раз
# результат выполнения этой программы, т.е. итоговый json, называется 'key_words_result.json'

import pdfminer.high_level, re, json

d = {} # здесь будет сам словарь в формате "номер статьи" : "список key words"

for i in range(1, 327): # будем бежать по статьям подряд
    pdfdir = str(i) + '.pdf' # достаем статью
    textpdf = pdfminer.high_level.extract_text(pdfdir) # здесь текст из неё
    textpdf = textpdf.replace('\n', '    ') # все абзацы превратили в 4 пробела, текст теперь - сплошная строка

    pattern = '[Kk]ey *?-?[wW]ords: *(.*?) {8}' # регулярка: в конце 8 пробелов - после key words пустая строка

    key_words = re.findall(pattern, textpdf) # ищем паттерн
    if len(key_words) > 0: # если нашли, т.е. если есть key words
        key_words = key_words[0]

        # теперь будем обратно внутри key_words превращать несколько пробелов подряд в 1
        j = 0
        k = len(key_words)
        while j < k-1:
            if key_words[j] == ' ' and key_words[j+1] == ' ': # если 2 пробела подряд
                key_words = key_words[:j] + key_words[j+1:] # делитнули позицию j
                k -= 1 # длина уменьшилась
            else:
                j += 1 # если не 2 пробела подряд - увеличили j, идем дальше

        # очистка от переносов
        if '- ' in key_words: # если они вообще есть
            j = 0
            k = len(key_words)
            while j < k-2:
                if key_words[j] == '-' and key_words[j+1] == ' ': # если перенос с пробелом
                    key_words = key_words[:j] + key_words[j+2:] # делитнули позиции j и j+1
                    k -= 2 # длина уменьшилась
                else:
                    j += 1 # если не перенос с пробелом подряд - увеличили j, идем дальше

        list_key_words = [] # а здесь будет список key words
        if ',' in key_words: # если key words в статье были разделены запятыми - разделяем по ним
            list_key_words = re.split(', +', key_words)
        elif ';' in key_words: # если были разделены точкой с запятой - разделяем по ним
            list_key_words = re.split('; +', key_words)
        else: # если же там 1 элемент
            list_key_words = []
            list_key_words.append(key_words) # просто его аппендим

        d[i] = list_key_words # записываем в словарь под ключом номера статьи список key words этой статьи

with open('key_words_result.json', 'w') as write_file:
    json.dump(d, write_file) # запишем всё это в json-файл
