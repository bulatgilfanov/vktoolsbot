# -*- coding: utf-8 -*-

import telebot
import constants
import vk
import sqlite3
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
@bot.message_handler(func=lambda message: message.text in ["Помощь", "помощь", "/help"])
def help(message):
    log_commands(message)
    bot.send_message(message.chat.id, constants.answer_help)

@bot.message_handler(func=lambda message: message.text in ["Оценить", "оценить", "/rate"])
def rate(message):
    log_commands(message)
    bot.send_message(message.chat.id, constants.rateforbot)

@bot.message_handler(func=lambda message: message.text in ["/check", "check"])
def rate(message):
    log_commands(message)

    if len(user_token) > 0:
        log_commands(message)
        bot.send_message(message.chat.id, constants.error_token)
    else:
        print(len(user_token))

@bot.message_handler(func=lambda message: message.text in ["/all", "all"])
def rate(message):
    log_commands(message)

    if len(user_token) > 0:
        log_commands(message)
        bot.send_message(message.chat.id, constants.error_token)
    else:
        print(len(user_token))

@bot.message_handler(func=lambda message: message.text in ["/dialogs", "dialogs"])
def rate(message):
    log_commands(message)

    if len(user_token) > 0:
        log_commands(message)
        bot.send_message(message.chat.id, constants.error_token)
    else:
        print(len(user_token))

@bot.message_handler(func=lambda message: message.text in ["/start"])
def start(message):

    log_commands(message)

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('check', 'all', 'dialogs')
    user_markup.row('Назад')
    user_markup.row('Иинформация о текущем аккаунте')
    user_markup.row('settoken','Помощь','Оценить')
    bot.send_message(message.from_user.id, constants.info_hello, reply_markup=user_markup)

@bot.message_handler(func=lambda message: message.text in ["/settoken", "settoken"])
def token(message):
    log_commands(message)

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('check', 'all', 'dialogs')
    user_markup.row('Назад')
    user_markup.row('Иинформация о текущем аккаунте')
    user_markup.row('settoken','Помощь','Оценить')
    bot.send_message(message.from_user.id,"\u26A0Внимательно прочитайте всю инструкцию", reply_markup=user_markup)

    markup = telebot.types.InlineKeyboardMarkup()
    link_markup = telebot.types.InlineKeyboardButton(text='Открыть ссылку для авторизации.', url='https://vk.cc/78N1SL')
    markup.add(link_markup)
    bot.send_message(message.from_user.id, constants.info_settoken, reply_markup=markup)


##### Команды #####


@bot.message_handler(content_types=['text'])
def commands_menu(message):

    if message.text == "Помощь" or message.text == "помощь":
        log_commands(message)
        bot.send_message(message.chat.id, constants.answer_help)

    elif len(message.text) > 150:
        user_token = message.text[45:130]
        user_id = message.text.split('=')[-1]
        print("Token -", user_token, "Id -", user_id)
        bot.send_message(message.chat.id, "Ваш token установлен.")

    else:
        log_text(message, constants.answer)
        bot.send_message(message.chat.id, constants.answer)
        print(len(message.text))


@bot.message_handler(content_types=['text'])
def commands_menu(message):
    user_token = message.text[45:130]
    user_id = message.text.split('=')[-1]
    print("Token -", user_token, "Id -", user_id)
    bot.send_message(message.chat.id, "Ваш token установлен.")

bot.polling(none_stop=True, interval=0)