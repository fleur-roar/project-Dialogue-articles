import telebot
from telebot import types

bot = telebot.TeleBot('1752493898:AAGgYdZWuhtdQh3baJPCRl-nUXs72ZWp-kc')

@bot.message_handler(commands = ['start'])
def starter(message):
    bot.send_message(message.from_user.id, "Смотрите, что мы умеем! \nНаприме\
р,введите /start \nа чтобы идти дальше нажмите /menu 🌾")
    chat_id = message.chat.id

def obrabotchic(tex):
    lex = tex.lower()
    lex = lex.replace("статья:","", 1)
    lex = lex.strip(' ')
    var_final = 0
    count_in = 0
    links_2_articles = {'название 1 статьи': 'https://drive.google.com/drive/\
folders/1VkJC9bR2zyyrSEclgQcyroyxPmwOSUUg?usp=sharing', '2я статья': '2я ссыл\
ка', '3я статья': '3я ссылка и тд.'}
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


@bot.message_handler(commands=['menu'])
def menu(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('Обработка статьи 🤍')
    start_menu.row('Достать статью Диалога ❤')
    start_menu.row('Интересные факты 🤍')
    bot.send_message(message.chat.id, 'Стартовое меню', reply_markup=start_menu)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Обработка статьи 🤍':
        source_language_menu = types.ReplyKeyboardMarkup(True, True)
        source_language_menu.row('Английский', 'Русский')
        source_language_menu.row('🌾', '🌾')
        source_language_menu.row('Назад')
        bot.send_message(message.chat.id, 'Уупс.. похоже, этот раздел ещё не \
доделан, приходите позже!🌾  ', reply_markup=source_language_menu)

    elif message.text == 'Достать статью Диалога ❤':
        B_menu = types.ReplyKeyboardMarkup(True, True)
        B_menu.row('Назад')
        bot.send_message(message.chat.id, 'Напишите, пожалуйста, название ста\
тьи вот в таком формате🌾 \n \nстатья: название статьи', reply_markup=B_menu)

    elif message.text == 'Интересные факты 🤍':
        C_menu = types.ReplyKeyboardMarkup(True, True)
        C_menu.row('Авторы', 'Key-words')
        C_menu.row('Назад')
        bot.send_message(message.chat.id, 'Уупс.. похоже, этот раздел ещё не \
доделан, приходите позже!🌾 ', reply_markup=C_menu)
    
    elif "статья:" in message.text or "Статья:" in message.text:
        k = message.text
        answer = obrabotchic(message.text)[0]
        line = obrabotchic(message.text)[1]
        if line == 1:
            bot.send_message(message.chat.id, "Простите, у нас нет статьи с т\
аким названием \nПопробуйте проверить, вдруг в вашем сообщении есть опечатки \
\n🌾")
        if line == 2:
            bot.send_message(message.chat.id, "Ой.. Ой.. у нас несколько стат\
ей с таким названием! \nУточните, пожалуйста, какую вы хотите \n🌾")
        else:
            markup = types.InlineKeyboardMarkup()
            btn_article= types.InlineKeyboardButton(text='материальчики', url\
                                                    = answer)
            markup.add(btn_article)
            bot.send_message(message.chat.id, "Ура, тыкните на кнопку, чтобы \
забрать материалы 🌾", reply_markup = markup)
            bot.send_message(message.chat.id, "Теперь вы можете попросить инф\
ормацию по другим статьям или вернуться назад в меню 🌾")
       

    elif message.text == 'Назад':
        menu(message)

    else:
        bot.send_message(message.chat.id, 'Прости, я не понимаю, попробуй нач\
ать с /menu')


        
bot.polling(none_stop=True, interval=0) 
















