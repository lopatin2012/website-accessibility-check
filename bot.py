import datetime
import time
import telebot
#sudo pip3 install pyTelegramBotAPI
import requests
# from bot_id import bot_id, chat_id, web_site
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Пинг")
root.geometry("200x100")

# Переменные кнопок
bot_id_value = StringVar()
chat_id_value = IntVar()
web_site_value = StringVar()
text_ready = StringVar()
text_ready_ping = StringVar()

# Глобальные переменные. Фу-фу-фу
bot_id = ''
chat_id = ''
bot = ''
website = ''
flag = True


def load_option():
    global website, bot_id, chat_id, bot
    with open('config.txt', 'r', encoding='utf-8') as f:
        list_config = f.read().split(',')
        website = str(list_config[0])
        bot_id = str(list_config[1])
        chat_id = str(list_config[2])
        bot = telebot.TeleBot(bot_id)
        text_ready.set('Настройки загружены')


def log_file(text):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(f'{text}')


def flag_false():
    flag = False
    return flag

# цифра отсутствия соединения
def time_down_func():
    time_down_error = str(datetime.datetime.now().strftime("%H:%M:%S"))
    time_list_down = list(map(int, time_down_error.split(':')))
    return (time_list_down[0] * 60 * 60) + (time_list_down[1] * 60) + time_list_down[2]

# итоговое время отсутствия соединения с сервером
def time_error_summa(now=datetime.datetime.now(), difference_time=1):
    time_now = str(now.strftime("%H:%M:%S"))
    time_list = list(map(int, time_now.split(':')))
    summa_total_time_off = (time_list[0] * 60 * 60) + (time_list[1] * 60) + time_list[2]
    return abs(summa_total_time_off - difference_time)


def ping(error='NO', check=True):
    time_down = datetime.datetime.now()
    now = datetime.datetime.now()
    time.sleep(1)
    text_ready_ping.set('Программа работает')
    while check:
        time.sleep(0.5)
        try:
            response = requests.get(website)
            if response.status_code == 200 and error == 'YES':
                pass
                send = f'\n{website}\n{str(now.strftime("%H:%M:%S"))} - OFF' \
                       f'\n{time_down_error} - ON' \
                       f'\n*{time_error_summa(now=now, difference_time=time_down)} - LOST sec.*\n'
                bot.send_message(chat_id=chat_id, text=send, parse_mode="Markdown")
                log_file(send)
                error = 'NO'
                pass
            elif response.status_code == 200 and error == 'YES-YES-YES':
                send = f'!!ERROR!!\n{website}\n{str(now.strftime("%H:%M:%S"))} - OFF' \
                       f'\n{time_down_error} - ON' \
                       f'\n*{time_error_summa(now=now, difference_time=time_down)} - LOST sec.*\n'
                bot.send_message(chat_id=chat_id, text=send, parse_mode="Markdown")
                log_file(send)
                error = 'NO'
                pass
            elif response.status_code != 200 and error == 'NO':
                error = 'YES'
                time_down = time_down_func()
            else:
                now = datetime.datetime.now()
                time_down_error = str(datetime.datetime.now().strftime("%H:%M:%S"))
        except requests.ConnectionError:
            error = 'YES-YES-YES'
            time_down = time_down_func()
            time_down_error = str(datetime.datetime.now().strftime("%H:%M:%S"))


load_option_entry = ttk.Button(text="Загрузить настройки", command=load_option)
load_option_entry.pack()

button_on_ping = ttk.Button(text="Запуск",  command=ping)
button_on_ping.pack()

field_option_ready = ttk.Label(textvariable=text_ready)
field_option_ready.pack()

field_option_ready_ping = ttk.Label(textvariable=text_ready_ping)
field_option_ready_ping.pack()

root.mainloop()
bot.polling(none_stop=True)