import json
import logging
import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANEL_ID = os.environ.get('CHANEL_ID')
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64)"
}
LINK = 'https://vc.ru/new'
TG_REQUEST = 'https://api.telegram.org/bot{}/sendMessage'


def main():
    old_news = ''
    headers = HEADERS
    link = LINK
    while link != 0:
        time.sleep(10)
        try:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
            news = soup.find('a', class_='content-link').get('href')
            logging.info('request completed')
        except Exception as e:
            logging.error(f'Error: {e} request error')
        try:
            with open('data.json') as f:
                old_news = json.load(f)
                print(f'Колесо сансары дало оборот, новость в БД: {old_news}')
        except Exception as e:
            logging.error(f'Error: {e} BD clear!')

        if news != old_news:
            requests.get(TG_REQUEST.format(BOT_TOKEN),
                         params=dict(chat_id=CHANEL_ID, text=news))
            logging.info('message send')

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(news, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
