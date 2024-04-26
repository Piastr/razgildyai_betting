import time

import telebot
from telebot import types
import schedule
from PIL import Image
import os

import footballAPI
import make_photos

token = "7192918265:AAG9Syec4CazlgYv3ij5dkQudQIIKBxFKdw"
bot = telebot.TeleBot(token)
id = 678484052

test = """2024-04-24 12:00:00+03:00 SKA-Khabarovsk vs Rodina Moskva 12 @ 1.32
2024-04-24 16:00:00+03:00 FC Tyumen vs Chernomorets Novorossiysk 1X @ 1.36
2024-04-24 16:00:00+03:00 FC Orenburg vs Dinamo Moskva 1X @ 1.67
2024-04-24 17:00:00+03:00 Volgar Astrakhan vs Torpedo Moskva 1X @ 1.38
2024-04-24 17:00:00+03:00 Alania Vladikavkaz vs Kuban Krasnodar 1 @ 1.77
2024-04-24 17:00:00+03:00 Zvijezda 09 Bijeljina vs Tuzla City 2 @ 1.727
2024-04-24 17:30:00+03:00 Tatran Liptovsky Mikulas vs Slavoj Trebisov 1 @ 1.407
2024-04-24 18:00:00+03:00 Sokol Saratov vs Yenisey Krasnoyarsk 12 @ 1.3
2024-04-24 18:00:00+03:00 Neftekhimik Nizhnekamsk vs Shinnik Yaroslavl 1 @ 1.73
2024-04-24 18:00:00+03:00 FK Panevezys vs Dziugas Telsiai 1X @ 1.255
2024-04-24 19:00:00+03:00 FK Khimki vs KAMAZ Chelny 1 @ 1.56
2024-04-24 19:00:00+03:00 Kauno Zalgiris vs Banga Gargzdai 1 @ 1.4
2024-04-24 19:00:00+03:00 Borac Banja Luka vs Posusje 1 @ 1.255
2024-04-24 19:00:00+03:00 Znicz Pruszkow vs Arka Gdynia 2 @ 1.74
2024-04-24 19:00:00+03:00 Wisla Plock vs Miedz Legnica 12 @ 1.29
2024-04-24 19:00:00+03:00 AEL Limassol vs Nea Salamina Famagusta 1X @ 1.365
2024-04-24 19:00:00+03:00 Seinajoen JK vs HJK Helsinki 2 @ 1.938
2024-04-24 19:30:00+03:00 Dynamo Makhachkala vs Arsenal Tula 1X @ 1.35
2024-04-24 19:30:00+03:00 Austria Klagenfurt vs Red Bull Salzburg 2 @ 1.362
2024-04-24 20:00:00+03:00 AIK Stockholm vs IFK Varnamo 1 @ 1.538
2024-04-24 20:00:00+03:00 Lorient vs Paris Saint Germain 2 @ 1.38
2024-04-24 20:00:00+03:00 Zalgiris Vilnius vs Dainava Alytus 1 @ 1.367
2024-04-24 20:00:00+03:00 Brommapojkarna vs Sirius 12 @ 1.262
2024-04-24 20:00:00+03:00 IFK Goteborg vs Hacken 12 @ 1.278
2024-04-24 20:00:00+03:00 Spartak Myjava vs Pohronie Dolna Zdana 12 @ 1.245
2024-04-24 20:30:00+03:00 Zenit Sankt Peterburg vs Rubin Kazan 1 @ 1.39
2024-04-24 20:30:00+03:00 Stade Nyonnais vs Vaduz 12 @ 1.247
2024-04-24 21:30:00+03:00 Zrinjski Mostar vs FK Sarajevo 1 @ 1.46
2024-04-24 21:45:00+03:00 Wolverhampton vs Bournemouth 12 @ 1.284
2024-04-24 21:45:00+03:00 Coventry vs Hull City 12 @ 1.272
2024-04-24 22:00:00+03:00 Monaco vs Lille 12 @ 1.286
2024-04-24 22:00:00+03:00 Crystal Palace vs Newcastle 1X @ 1.558
2024-04-24 22:00:00+03:00 Marseille vs Nice 1X @ 1.34
2024-04-24 22:00:00+03:00 Ajax Amsterdam vs Excelsior 1 @ 1.277
2024-04-24 22:00:00+03:00 Everton vs Liverpool 2 @ 1.423
2024-04-24 22:00:00+03:00 Manchester United vs Sheffield United 1 @ 1.353"""

#print(test.split('\n'))

"""for i in test.split('\n'):
    team1, team2, ishod = make_photos.icon_parsing(i)
    print(team1, team2, ishod)
    files = os.listdir('temp')
    for file_name in files:
        file_path = os.path.join('temp', file_name)
        os.remove(file_path)
"""
#team1, team2, ishod = make_photos.icon_parsing(test.split('\n')[-1])
#print(team1, team2, ishod)

"""def compress_image(input_path, output_path, target_size=(800, 640)):
    # Открываем изображение
    image = Image.open(input_path)

    # Меняем размер изображения до указанных размеров
    image.thumbnail(target_size)

    # Сохраняем изображение
    image.save(output_path)


# Пример использования
input_path = "photo_and_logo/FF.jpeg"
output_path = "photo_and_logo/background.jpeg"
compress_image(input_path, output_path)
"""


#matches = footballAPI.get_matches()
#print(matches)

matches = ['2024-04-25 16:00:00+03:00\tUral Sverdlovskaya Oblast vs FK Rostov\t12 @ 1.37', '2024-04-25 18:15:00+03:00\tFakel Voronezh vs Krylya Sovetov Samara\t1X @ 1.41', '2024-04-25 19:00:00+03:00\tTermalica Nieciecza vs Odra Opole\t12 @ 1.273', '2024-04-25 19:45:00+03:00\tHeerenveen vs PSV Eindhoven\t2 @ 1.33', '2024-04-25 20:00:00+03:00\tDjurgardens vs Malmo\t2 @ 2.112', '2024-04-25 20:00:00+03:00\tNorrkoping vs Elfsborg\t2 @ 2.144', '2024-04-25 20:00:00+03:00\tKalmar vs GAIS Goteborg\t1X @ 1.358', '2024-04-25 20:00:00+03:00\tHalmstads vs Hammarby\t2 @ 1.91', '2024-04-25 20:30:00+03:00\tAkhmat Grozny vs PFC Sochi\t1X @ 1.39', '2024-04-25 20:30:00+03:00\tCSKA Moskva vs Spartak Moskva\t1X @ 1.49', '2024-04-25 21:00:00+03:00\tUdinese vs Roma\t1X @ 1.512', '2024-04-25 21:30:00+03:00\tGKS Katowice vs Gornik Leczna\t1 @ 1.8', '2024-04-25 21:45:00+03:00\tUniversitatea Craiova vs CFR Cluj\t1X @ 1.434', '2024-04-25 22:00:00+03:00\tBrighton vs Manchester City\t2 @ 1.37', '2024-04-25 22:00:00+03:00\tGo Ahead Eagles vs Feyenoord\t2 @ 1.465', '2024-04-25 22:15:00+03:00\tKeflavik IF vs Breidablik Kopavogur\t2 @ 1.287']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(id, 'hi')


for i in matches:
    team1, team2, ishod, date, time = make_photos.icon_parsing(i)
    print(team1, team2, ishod, date, time)
    ishod = ishod.strip()
    photo = open(f'temp/match{team1}.png', 'rb')
    verdict = ''
    if ishod == '1':
        verdict = '1 (считаем что победит первая команда)'
    if ishod == '12':
        verdict = '12 (считаем что ничьи в матче не будет)'
    if ishod == '1X':
        verdict = '1Х (считаем что у первой команды двойной шанс)'
    if ishod == '2':
        verdict = '2 (считаем что победит вторая команда)'
    if ishod == '2X':
        verdict = '2X (считаем что у второй команды двойной шанс)'
    if ishod == 'X':
        verdict = 'X (считаем что в матче будет ничья)'

    bot.send_photo(id, photo, caption=f"⚽ Футбол\n\n🏟 {team1} VS {team2}\n\n📅 Дата: {date}\n🕒 Время: {time}\n\n📊 Прогноз: {verdict}")

time.sleep(10)

files = os.listdir('temp')
for file_name in files:
    file_path = os.path.join('temp', file_name)
    os.remove(file_path)