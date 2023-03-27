import telebot
import requests
import os
import random
import config
from telebot import types
from dotenv import load_dotenv
import sqlite3 as sq

load_dotenv()
bot = telebot.TeleBot(os.environ.get("TOKEN"))


# *******FROM DB EXTRACTING TABLES*******
with sq.connect('sentences.db') as con:
    cur = con.cursor()

list_of_zagadky = cur.execute("SELECT * FROM zahadky")
zagadky = [list(i) for i in list_of_zagadky]

list_of_prysl = cur.execute("SELECT * FROM pryslivya")
pryslivya = [list(i) for i in list_of_prysl]


# *******БOT*******
@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("☝ Прислів'я")
    button2 = types.KeyboardButton("❓ Загадка")
    markup.add(button1, button2)
    bot.send_message(
        message.chat.id, "Привіт! 👋\n\nОбери прислів'я чи загадку, надіславши 1 або 0\n\n\n☝  ПРИСЛІВ'Я  -  1\n\n❓  ЗАГАДКА  -  0", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sending_answer(message):

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("☝ Прислів'я")
    button2 = types.KeyboardButton("❓ Загадка")
    markup.add(button1, button2)
    if (message.text == "❓ Загадка"):
        bot.send_message(
            message.chat.id, zagadky[0], reply_markup=markup)
        random.shuffle(zagadky)
    elif (message.text == "☝ Прислів'я"):
        bot.send_message(
            message.chat.id, pryslivya[0], reply_markup=markup)
        random.shuffle(pryslivya)
    elif message.text.lower() in '0':
        bot.send_message(
            message.chat.id, zagadky[0], reply_markup=markup)
        del zagadky[0]
    elif message.text.lower() in '1':
        bot.send_message(
            message.chat.id, pryslivya[0], reply_markup=markup)
        del pryslivya[0]
    elif message.text.lower() in '23456789':
        bot.send_message(message.chat.id, '⛔ Введи 0 або 1',
                         reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id, '⛔ Ти ввів слово або число більше за 1', reply_markup=markup)


bot.polling()
