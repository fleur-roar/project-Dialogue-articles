import telebot
from telebot import types
bot = telebot.TeleBot('<мой токен>')


   #вот так можно создавать команды
   #тут чел пишет /article, ему отвечают с просьбой написать название
@bot.message_handler(commands = ['article'])
def helper(message):
    bot.send_message(message.from_user.id, "Введите название (можно неполное) статьи, информацию по которой хотите получить 💚")

#КАПЕЦ ВАЖНО !!! команды должны быть расположены ВЫШЕ в коде, чем примитивный ответ на текст
#иначе на /article ответится просто как на текстовое сообщение


   #кноооопкииии
   #но нужно чтобы они не на сайт перебрасывали, а например
   # ЗапУсКаЛи КоМаНдУ !!!
@bot.message_handler(commands = ['ururu'])
def ururu(message):
    markup = types.InlineKeyboardMarkup()
    btn_vseros_site= types.InlineKeyboardButton(text='первый сайт', url='https://vos.olimpiada.ru/')
    markup.add(btn_vseros_site)
    btn_A= types.InlineKeyboardButton(text='второй сайт', url='https://vos.olimpiada.ru/')
    markup.add(btn_A)
    bot.send_message(message.chat.id, "Хотите посмотреть на сайт всероса?👍👍", reply_markup = markup)


  #тот самый примитивный ответ на текст
  #сообщения в ответ на сообщения
  #вытягивание текста из сообщения пользователя
  #просто отправка сообщений
@bot.message_handler(content_types=['text'])
def echo_all(message):
#    print(message)
#    bot.reply_to(message, message.text)
    bot.send_message(message.from_user.id, '👍👍👍\n👍👍👍')
   #это будет отвечать на каждое сообщение
   #но ещё можно внутри сообщений навешивать условия
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Нет блин Пока")

        
  #создание нижнего меню, но его закавычу, ибо оно НЕ ИСЧЕЗАЕТ потом
  #и тут аккуратнее надо с иерархией!
  #мне не очень нравится визуально, но тут хоть какой-то переход от команды к команде

"""@bot.message_handler(commands=['start'])
def menu(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row('Обработка статьи', 'Достать статью Диалога', 'Интересные факты')
    bot.send_message(message.chat.id, 'Стартовое меню', reply_markup=start_menu)"""

# первой идёт команда, по "появлению этого меню"
# а потом всё устроено просто через
# нажал на кнопку => отправилось сообщение => через примитивную обработку текста сообщений вывелось что-то новое + разве что кнопки меняются интересно, надо прописывать


"""@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Обработка статьи':
        A_menu = types.ReplyKeyboardMarkup(True, True)
        A_menu.row('Кнопка1', 'Кнопка2')
        A_menu.row('Кнопка3', 'Кнопка4')
        A_menu.row('Назад')"""
#вот тут ооочень неплохо, что можно по рядам кнопки расположить!!
     """bot.send_message(message.chat.id, 'Обработка статьи - меню', reply_markup=source_language_menu)

    elif message.text == 'Достать статью Диалога':
        B_menu = types.ReplyKeyboardMarkup(True, True)
        B_menu.row('к1', 'к2')
        B_menu.row('к3', 'к4')
        B_menu.row('Назад')
        bot.send_message(message.chat.id, 'Достать статью Диалога - меню', reply_markup=translation_language_menu)

    elif message.text == 'Получить интересные факты по годам':
        C_menu = types.ReplyKeyboardMarkup(True, True)
        C_menu.row('b1', 'b2')
        C_menu.row('b3', 'b4')
        C_menu.row('Назад')
        bot.send_message(message.chat.id, 'Интересные факты - меню', reply_markup=translation_language_menu)

    elif message.text == 'Назад':
        menu(message)"""




#это нужно оставлять, чтобы бот реагировал на сообщения
bot.polling(none_stop=True, interval=0) #способ связи с с серв для полу сообщ
