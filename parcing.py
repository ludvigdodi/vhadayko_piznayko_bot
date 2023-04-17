import requests
import os
import random
import sqlite3 as sq
from bs4 import BeautifulSoup as bs

# прописываем свой хедер чтоб не приняи нас за бота
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
# }

# # url_1 = "https://kidadl.com/quotes/best-2-word-quotes-and-phrases"
# # url_2 = "https://motivationalwizard.com/4-word-short-inspirational-quotes/"
# # # url_3 = "https://thejohnfox.com/2021/08/100-beautiful-sentences/"

# # def first_level_parser(url):
# #     req = requests.get(url_1, headers=header)
# #     soup = bs(req.text, 'html.parser')
# #     text = soup.find('div', class_="rich-text-article-body")
# #     sentences = text.find_all('p')
# #     return [c.text for c in sentences ]

# # list_of_sentences = first_level_parser(url_1)

# # Парсимо текст загадок
# url = 'https://np.pl.ua/2021/10/zahadky-dlia-ditey-100-zahadok-dlia-riznoho-viku/'


# def parser(url):
#     req = requests.get(url)
#     soup = bs(req.text, 'html.parser')
#     zagadky_list = soup.find('div', class_="entry-content")
#     zagadky = zagadky_list.find_all('li')
#     return [c.text for c in zagadky]


# list_of_zagadky = parser(url)
# random.shuffle(list_of_zagadky)


# with sq.connect('sentences.db') as con:
#     cur = con.cursor()

#     # cur.execute("DROP TABLE sentences_2")
#     cur.execute('''CREATE TABLE IF NOT EXISTS zahadky(
#         sentence INTEGER
#         )''')
#     for s in list_of_zagadky:
#         if s:
#             cur.execute("INSERT INTO zahadky VALUES (?)", (s,))

# cur.execute("SELECT * FROM users WHERE score < 1000 AND old IN(19, 32)")
# result = cur.fetchall()
# print(result)

# fatchmany(3) перші три записи
# fetchone() - перша запись
with sq.connect('sentences.db') as con:
    cur = con.cursor()

    sentences = cur.execute("SELECT * FROM  zahadky")

for sentence in sentences:
    print(sentence)
