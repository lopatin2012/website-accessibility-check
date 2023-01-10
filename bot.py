import datetime
import time
import telebot
#sudo pip3 install pyTelegramBotAPI
import requests
from bot_id import bot_id, chat_id, web_site


bot = telebot.TeleBot(bot_id)
#Присваивание токена

def ping_web(domain):
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
                send = f'Домашний\nОшибка доступа к сайту\n{domain} \nс {str(now.strftime("%H:%M:%S"))}\nпо {time_down}\nИтого: {total_time_off} секунд'
                bot.send_message(chatId, text=send)
                count = 0
            elif response.status_code == 200 and count == 2:
                time_now = str(now.strftime("%H:%M:%S"))
                time_list = list(map(int, time_now.split(':')))
                summa_total_time_off = (time_list[0] * 60 * 60) + (time_list[1] * 60) + time_list[2]
                total_time_off = abs(summa_total_time_off - difference_time)
                print(f'{domain} упал в {str(now.strftime("%H:%M:%S"))}\nЕго работы была восстановлена в {time_down}\nИтоговое время простоя: {total_time_off} секунд')
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
                



print(ping_web(web_site))


bot.polling(none_stop=True)
