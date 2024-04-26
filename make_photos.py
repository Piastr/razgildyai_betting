import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import datetime
import re



def find_teams_link(team):
    try:
        url = f"https://soccer365.ru/?a=search&q={team}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        element = soup.find("a", attrs={'rel': 'nofollow'})
        link = "https://soccer365.ru" + element.get('href')
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        text = soup.find("h1", class_='profile_info_title red').get_text()
        team_attr_list = [link, text]
        return team_attr_list

    except:
        team = team.split()
        url = f"https://soccer365.ru/?a=search&q={team[0]}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        element = soup.find("a", attrs={'rel': 'nofollow'})
        link = "https://soccer365.ru" + element.get('href')
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        text = soup.find("h1", class_='profile_info_title red').get_text()
        team_attr_list = [link, text]
        return team_attr_list


# Функция для создания градиентного фона


def icon_parsing(string):
    date = string[:10]
    time = string[11:16]
    teams = string.split(" vs ")
    ishod = string[string.find("@") - 3: string.find('@')].replace(' ', '')
    team1 = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', ' ', teams[0]).strip()
    team2 = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', ' ', teams[1]).strip()


    team1_attr_list = find_teams_link(team1)
    team2_attr_list = find_teams_link(team2)

    #['https://soccer365.ru/clubs/10605/', 'Стад Нионас']

    url_team1 = team1_attr_list[0]
    response = requests.get(url_team1)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_element = soup.find('img', src=True, attrs={"alt":f"{team1_attr_list[1]}"})
    icon_url = img_element['src']
    icon_response = requests.get(icon_url)
    with open(f"temp/{team1_attr_list[1]}.png", "wb") as f:
        f.write(icon_response.content)

    url_team2 = team2_attr_list[0]
    response = requests.get(url_team2)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_element = soup.find('img', src=True, attrs={"alt":f"{team2_attr_list[1]}"})
    icon_url = img_element['src']
    icon_response = requests.get(icon_url)
    with open(f"temp/{team2_attr_list[1]}.png", "wb") as f:
        f.write(icon_response.content)
    create_match_card(f"temp/{team1_attr_list[1]}.png", f"temp/{team2_attr_list[1]}.png", team1_attr_list[1], team2_attr_list[1], time, date)

    return team1_attr_list[1], team2_attr_list[1], ishod, date, time




def draw_text_center(image, text, font_path, font_size, color, text_height=None):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Получение координат и размеров текста
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_height or text_bbox[3] - text_bbox[1]

    # Вычисляем координаты центра изображения
    image_width, image_height = image.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    # Рисуем текст на изображении
    draw.text((x, y), text, font=font, fill=color)


def create_match_card(logo1_path, logo2_path, team1_name, team2_name, time, date):
    background = Image.open("photo_and_logo/background.jpeg")

    # Вставка логотипов команд с прозрачным фоном
    logo1 = Image.open(logo1_path).resize((200, 200))
    logo2 = Image.open(logo2_path).resize((200, 200))
    background.paste(logo1, (50, 90), mask=logo1.convert('RGBA').split()[3])
    background.paste(logo2, (550, 90), mask=logo2.convert('RGBA').split()[3])

    # Добавление названий команд
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("Naga.ttf", 30)  # Путь к вашему шрифту

    team1_name_split = team1_name.split()
    for i in range(len(team1_name.split())):
        text_bbox1 = draw.textbbox((0, 0), team1_name_split[i], font=font)
        text_width1 = text_bbox1[2] - text_bbox1[0]
        text_height1 = text_bbox1[3] - text_bbox1[1]
        text_x1 = 50 + (200 - text_width1) / 2
        text_y1 = 300
        second_word_y = text_y1 + text_height1 * i + 10
        text_y1 = second_word_y
        draw.text((text_x1, text_y1), team1_name_split[i], fill="white", font=font)

    team2_name_split = team2_name.split()
    for i in range(len(team2_name.split())):
        text_bbox2 = draw.textbbox((0, 0), team2_name_split[i], font=font)
        text_width2 = text_bbox2[2] - text_bbox2[0]
        text_height2 = text_bbox2[3] - text_bbox2[1]
        text_x2 = 550 + (200 - text_width2) / 2
        text_y2 = 300
        second_word_y = text_y2 + text_height2 * i + 10
        text_y2 = second_word_y
        draw.text((text_x2, text_y2), team2_name_split[i], fill="white", font=font)

    # Добавление времени матча и даты
    draw_text_center(background, 'VS', "Naga.ttf", 50, "white")
    draw_text_center(background, time, 'Naga.ttf', 30, 'white', text_height=-220)
    draw_text_center(background, date, 'Naga.ttf', 30, 'white', text_height=-300)

    background.save(f'temp/match{team1_name}.png')

    #background.show()


#icon_parsing("2024-04-24 20:30:00+03:00 Stade Nyonnais vs Vaduz 12 @ 1.247")



