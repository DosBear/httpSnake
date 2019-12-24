import os

tmpPath = os.path.join(os.path.dirname(__file__), "tmp")

if not os.path.exists(tmpPath):
    os.makedirs(tmpPath)
    
webURL= {
    "Specificstion": "http://customs.ru/folder/757",
    "Albom": "http://customs.ru/folder/6432"
}


MAIL_USERNAME = "test@yandex.ru"
MAIL_PASSWORD = "pass"
SMTP_SERVER_ADDR = "smtp.yandex.ru"
MAIL_FROM_ADDR = "Info Bot <test@yandex.ru>"
