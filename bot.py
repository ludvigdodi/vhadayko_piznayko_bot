import telebot
import requests
import os
import random
import config
from telebot import types
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.environ.get("TOKEN"))

# Парсимо текст загадок
url = 'https://np.pl.ua/2021/10/zahadky-dlia-ditey-100-zahadok-dlia-riznoho-viku/'
def parser(url):
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    zagadky_list = soup.find('div', class_="entry-content")
    zagadky = zagadky_list.find_all('li')
    return [c.text for c in zagadky]

list_of_zagadky = parser(url)
random.shuffle(list_of_zagadky)

# Парсимо текст прислі'ями
# url = 'https://uk.wikiquote.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D1%96_%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%96_%D0%BF%D1%80%D0%B8%D1%81%D0%BB%D1%96%D0%B2%27%D1%8F_%D1%82%D0%B0_%D0%BF%D1%80%D0%B8%D0%BA%D0%B0%D0%B7%D0%BA%D0%B8:_%D0%BF%D1%80%D0%B0%D1%86%D1%8F,_%D0%B3%D0%BE%D1%81%D0%BF%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%BE'
url = 'https://inlviv.in.ua/suspilstvo/ukrayinski-narodni-prisliv-ya-ta-prikazki-top-300'
def parser_prys(url):
    req = requests.get(url)
    soup = bs(req.text, 'lxml')
    prysl_list = soup.find('div', class_="post-content post-dynamic")
    prysl = prysl_list.find_all('p')
    return [c.text for c in prysl]

list_of_prysl = parser_prys(url)
random.shuffle(list_of_prysl)


# Бот
@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("☝ Прислів'я")
    button2 = types.KeyboardButton("❓ Загадка")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Привіт! 👋\n\nОбери прислів'я чи загадку, надіславши 1 або 0\n\n\n☝  ПРИСЛІВ'Я  -  1\n\n❓  ЗАГАДКА  -  0", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def sending_answer(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("☝ Прислів'я")
    button2 = types.KeyboardButton("❓ Загадка")
    markup.add(button1, button2)
    if (message.text == "❓ Загадка"):
        bot.send_message(message.chat.id, list_of_zagadky[0], reply_markup=markup)
        random.shuffle(list_of_zagadky)
    elif (message.text == "☝ Прислів'я"):
        bot.send_message(message.chat.id, list_of_prysl[0], reply_markup=markup)
        random.shuffle(list_of_prysl)
    elif message.text.lower() in '1':
        bot.send_message(message.chat.id, list_of_zagadky[0], reply_markup=markup)
        del list_of_zagadky[0]
    elif message.text.lower() in '0':
        bot.send_message(message.chat.id, list_of_prysl[0], reply_markup=markup)
        del list_of_prysl[0]
    elif message.text.lower() in '23456789':
        bot.send_message(message.chat.id, '⛔ Введи 0 або 1', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '⛔ Ти ввів слово або число більше за 1', reply_markup=markup)

bot.polling()