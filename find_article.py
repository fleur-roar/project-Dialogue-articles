# эта программа принимает на вход название статьи или его часть
# в ответ она печатает ссылки на все статьи, в которых есть это название или эта часть названия
# программа игнорирует шрифт
# т.е. если в названии статьи написано RuREBus, то по запросу rurebus или RUrebUS она его найдет

import csv
links = csv.DictReader(open('links_to_articles.csv', encoding='utf-8'))
# csv-файл имеет колонки number,title,link

links_list = [] # здесь будет список найденных нами ссылок

title = input('Введите, пожалуйста, название или его часть: ')
title = title.lower() # привели к нижнему шрифту

for row in links: # идём по всем строчкам
    new = str(row['title']) # сюда достали заголовок
    new = new.lower() # привели к нижнему шрифту
    if title in new: # если там есть введённый кусок названия
        links_list.append(str(row['link'])) # прибавляем ссылку на него в список ссылок

if len(links_list) > 0: # если такие статьи нашлись, т.е. в списке что-то лежит
    for link in links_list:
        print(link) # печатаем с новой строчки каждую ссылку
else: # если нет статей с таким названием
    print('К сожалению, статей с таким названием не нашлось :(')
