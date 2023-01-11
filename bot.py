import datetime
import sys
import time
import telebot
#sudo pip3 install pyTelegramBotAPI
import requests
# from bot_id import bot_id, chat_id, web_site
from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.title("Приложения для проверки доступа к веб-сайту")
root.geometry("300x250")

#Присваивание токена


bot_id_value = StringVar()
chat_id_value = IntVar()
web_site_value = StringVar()
text_ready = StringVar()
bot_id = ''
chat_id = 0
web_site = ''



def on_exit(event):
    sys.exit()

def load_optin():
    global web_site, bot_id, chat_id, text_ready, bot
    bot_id = f"{bot_id_value.get()}"
    chat_id = chat_id_value.get()
    web_site = f'{str(web_site_value.get())}'
    text_ready.set('Готово')
    print(bot_id, web_site)
    bot = telebot.TeleBot(bot_id)

def log_file(text):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{text}')



# def save_option():
#     with open('bot_id.py', 'w+', encoding='utf-8') as f:
#         f.write(f'bot_id = {bot_id_value.get()}\n')
#         f.write(f'chat_id = {chat_id_value.get()}\n')
#         f.write(f"web_site = '{str(web_site_value.get())}'\n")

def ping_web():
    domain = web_site
    # Переменная для отвловли ошибки по исключительной ошибке
    count = 0
    chatId = chat_id
    while True:
        time.sleep(1)
        try:
            response = requests.get(domain)
            if response.status_code == 200 and count == 1:
                time_now = str(now.strftime("%H:%M:%S"))
                time_list = list(map(int, time_now.split(':')))
                summa_total_time_off = (time_list[0] * 60 * 60) + (time_list[1] * 60) + time_list[2]
                total_time_off = abs(summa_total_time_off - difference_time)
                send = f'Внимание!\nОшибка доступа к сайту\n{domain} \nс {str(now.strftime("%H:%M:%S"))}\nпо {time_down}\nИтого: {total_time_off} секунд'
                bot.send_message(chatId, text=send)
                text_date = f'Дата: {str(now.strftime("%d.%m.%Y"))}\n{send}'
                log_file(text_date)
                count = 0
            elif response.status_code == 200 and count == 2:
                time_now = str(now.strftime("%H:%M:%S"))
                time_list = list(map(int, time_now.split(':')))
                summa_total_time_off = (time_list[0] * 60 * 60) + (time_list[1] * 60) + time_list[2]
                total_time_off = abs(summa_total_time_off - difference_time)
                send = f'{domain} упал в {str(now.strftime("%H:%M:%S"))}\nЕго работа была\n восстановлена в {time_down}\nИтого: {total_time_off} секунд'
                bot.send_message(chatId, text=send)
                text_date = f'Дата: {str(now.strftime("%d.%m.%Y"))}\n{send}'
                log_file(text_date)
                count = 0
            elif response.status_code != 200 and count == 0:
                time_down = str(datetime.datetime.now().strftime("%H:%M:%S"))
                count = 1
                time_list_down = list(map(int, time_down.split(':')))
                difference_time = (time_list_down[0] * 60 * 60) + (time_list_down[1] * 60) + time_list_down[2]
            else:
                now = datetime.datetime.now()
        except requests.ConnectionError:
            time.sleep(1)
            count = 2
            time_down = str(datetime.datetime.now().strftime("%H:%M:%S"))
            time_list_down = list(map(int, time_down.split(':')))
            difference_time = (time_list_down[0] * 60 * 60) + (time_list_down[1] * 60) + time_list_down[2]
                

button_on_ping = ttk.Button(text="Запустить пинг", command=ping_web)
button_on_ping.pack()

field_domain_line = ttk.Label(text="Введите адрес сайта")
field_domain_line.pack()

field_domain = ttk.Entry(textvariable=web_site_value)
field_domain.pack()

field_bot_id_line = ttk.Label(text="Введите id бота")
field_bot_id_line.pack()

field_bot_id = ttk.Entry(textvariable=bot_id_value)
field_bot_id.pack()

field_chat_id_line = ttk.Label(text="Введите id группового чата")
field_chat_id_line.pack()

field_chat_id = ttk.Entry(textvariable=chat_id_value)
field_chat_id.pack()

# save_option_entry = ttk.Button(text="Сохранить настройки", command=save_option)
# save_option_entry.pack()

load_option_entry = ttk.Button(text="Загрузить настройки", command=load_optin)
load_option_entry.pack()

field_option_ready = ttk.Label(textvariable=text_ready)
field_option_ready.pack()

# print(ping_web(web_site))
root.bind('<Destroy>', on_exit)
root.mainloop()
bot.polling(none_stop=True)

