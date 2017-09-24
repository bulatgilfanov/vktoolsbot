"""
?
Описание бота
?
"""

import telebot
import constants
from telebot import types

bot = telebot.TeleBot(constants.token)

print(bot.get_me())

##### Логирование #####
### Логирование сообщений ###
def log_text(message, answer):
    print("\n --------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print("Ваш ответ: ", answer)

### Логирование команд ###
def log_commands(message):
    print("\n --------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n  Команда - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
### Логирование команд ###
##### Логирование #####

##### Команды #####
@bot.message_handler(commands=['help'])
def hendle_text(message):
    log_commands(message)
    bot.send_message(message.chat.id, constants.answer_help)

@bot.message_handler(commands=['start'])
def hendle_text(message):
    log_commands(message)

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Помощь')
    user_markup.row(' ')
    bot.send_message(message.from_user.id, "Добро пожаловать.", reply_markup=user_markup)

    markup = telebot.types.InlineKeyboardMarkup()
    link_markup = telebot.types.InlineKeyboardButton(text='Открыть ссылку для авторизации.', url='https://vk.cc/78N1SL')
    markup.add(link_markup)
    bot.send_message(message.from_user.id, constants.info_authorization, reply_markup=markup)


##### Команды #####


@bot.message_handler(content_types=['text'])
def hendle_text(message):
    if message.text == "Помощь" or message.text == "помощь":
        log_commands(message)
        bot.send_message(message.chat.id, constants.answer_help)

@bot.message_handler(content_types=['text'])
def hendle_text(message):
    answer = "Пошел нахуй!"
    if message.text == "Ты пидор!" or message.text == "ты пидор!" or message.text == "Ты пидор" or message.text == "ты пидор" or message.text == "пидор" or message.text == "Пидор":
        answer = "Нет ТЫ!!!"
        log_text(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Я пидор" or message.text == "я пидор":
        answer = "Ну ОК!"
        log_text(message, answer)
        bot.send_message(message.chat.id, answer)
    else:
        log_text(message, answer)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
