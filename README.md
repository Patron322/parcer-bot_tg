Как запустить проект:

    Cоздать и активировать виртуальное окружение:
        python -m venv venv
        .\venv\Scripts\Activate.ps1

    Установить зависимости из файла requirements.txt:

        python -m pip install —upgrade pip
        pip install -r requirements.txt

    В файл .env записать токен бота и id телеграмм канала:

        BOT_TOKEN = 'your_token_bot'
        CHANEL_ID = '@your_chat_id_tg_chanel'

Скрипт отправляет последнюю новость с сайта https://vc.ru/new в телеграмм канал.
    Для корректной работы необходимо выдать боту права администратора в канале.