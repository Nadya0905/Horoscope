import requests
import bs4


def get_today_horo(horo):
    response = requests.get(f"https://horo.mail.ru/prediction/{horo}/today/")

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    raw_description = soup.find(class_="article__item article__item_alignment_left article__item_html")
    return raw_description.text

def get_tomorrow_horo(horo):
    response = requests.get(f"https://horo.mail.ru/prediction/{horo}/tomorrow/")

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    raw_description = soup.find(class_="article__item article__item_alignment_left article__item_html")
    return raw_description.text

def get_week_horo(horo):
    response = requests.get(f"https://horo.mail.ru/prediction/{horo}/week/")

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    raw_description = soup.find(class_="article__item article__item_alignment_left article__item_html")
    return raw_description.text

def get_month_horo(horo):
    response = requests.get(f"https://horo.mail.ru/prediction/{horo}/month/")

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    raw_description = soup.find(class_="article__item article__item_alignment_left article__item_html")
    return raw_description.text

def get_year_horo(horo):
    response = requests.get(f"https://horo.mail.ru/prediction/{horo}/year/")

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    raw_description = soup.find(class_="article__item article__item_alignment_left article__item_html")
    return raw_description.text

