# часть с вытаскиванием ссылки на информацию по статье
# одна (а может не одна) часть сильно костыльная, но так вполне работает

# после нажатия кнопки пользователю выводится уточнение, в каком формате писать название стати

    elif message.text == 'Достать статью Диалога ❤':
        B_menu = types.ReplyKeyboardMarkup(True, True)
        B_menu.row('Назад')
        bot.send_message(message.chat.id, 'КоРоЧе пиши вот в таком формате\nСтатья: название стати ', reply_markup=B_menu)

# функция, которая определит
# I было несколько/0/1 вхождение => разные ответы
# II если "хорошо" совпало - вернёт нужную ссылку

def obrabotchic(tex):
    lex = tex.lower()
    lex = lex.replace("статья:","", 1)
    lex = lex.strip(' ')
    var_final = 0
    count_in = 0
    links_2_articles = {'название 1 статьи': 'https://vos.olimpiada.ru/', '2я статья': '2я ссылка', '3я статья': '3я ссылка и тд.'}
    keys = list(links_2_articles.keys())
    for i in keys:
        if lex in i:
            count_in += 1
            var_final = i
    if count_in == 0:
        line = 1
        a = 0
    elif count_in > 1:
        line = 2
        a = 0
    elif count_in == 1:
        line = 3
        a = links_2_articles[var_final]
    return a, line

# из-за триггерного кусочка запустится функция, что сверху
# и в зависимости от её результатов будет вывод


    elif "статья:" in message.text or "Статья:" in message.text:
        k = message.text
        answer = obrabotchic(message.text)[0]
        line = obrabotchic(message.text)[1]
        if line == 1:
            bot.send_message(message.chat.id, "Простите, у нас нет статьи с таким названием\nПопробуйте проверить, вдруг у вас в сообщении опечатки")
        if line == 2:
            bot.send_message(message.chat.id, "Ой.. Ой.. у нас несколько статей с таким названием!\nУточните, пожалуйста, какую вы хотите")
        else:
            markup = types.InlineKeyboardMarkup()
            btn_article= types.InlineKeyboardButton(text='материальчики', url = answer)
            markup.add(btn_article)
            bot.send_message(message.chat.id, "Ура, тыкните на кнопку, чтобы забрать материалы", reply_markup = markup)
            bot.send_message(message.chat.id, "Теперь вы можете попросить информацию по другим статьям или вернуться назад в меню")
















