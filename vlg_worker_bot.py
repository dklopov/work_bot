import telebot
from datetime import datetime
import re

bot = telebot.TeleBot("1607313958:AAFyKoJWe7TrDiP0ysplOz8GoYWDnKuZ7Pg")


@bot.message_handler(commands=["create_conf"])
def create_conf_command_start(message):
    bot.send_message(message.from_user.id, 'Укажи количество созданных конфигураций')
    create_conf_message = message
    bot.register_next_step_handler(create_conf_message, create_conf_control)


def create_conf_control(create_conf_message):
    user_id = str(create_conf_message.from_user.id)
    user_name = str(create_conf_message.from_user.username)
    count_create_conf = str(create_conf_message.text)
    date_time = str(datetime.now())
    to_chat_id = -1001427883840  # id чата vlg_worker_bot_report
    check_message_text = int(re.sub('\D', '', count_create_conf))  # вырезаем все символы и приводим к int
    if isinstance(check_message_text, int) and check_message_text > 0:  # проверяем, что введеное значение > 0
        bot.send_message(to_chat_id,
                         'count_create_conf: ' + str(check_message_text) +
                         '\nuser_id: ' + user_id +
                         '\nuser_name: ' + user_name +
                         '\ndate_time: ' + date_time
                         )
        bot.send_message(create_conf_message.from_user.id, 'Принято')
    else:
        bot.send_message(create_conf_message.from_user.id, 'Запусти команду заново и введи целое число > 0')


@bot.message_handler(commands=["change_conf"])
def change_conf_command_start(message):
    bot.send_message(message.from_user.id, 'Укажи количество измененных конфигураций ')
    change_conf_message = message
    bot.register_next_step_handler(change_conf_message, change_conf_control)


def change_conf_control(change_conf_message):
    user_id = str(change_conf_message.from_user.id)  # id юзера, написавшего в бота
    user_name = str(change_conf_message.from_user.username)  # нейм юзера, написавшего в бота
    count_change_conf = str(change_conf_message.text)  # текст юзера, написавшего в бота
    date_time = str(datetime.now())  # текущий datetime
    to_chat_id = -1001427883840  # id чата vlg_worker_bot_report
    check_message_text = int(re.sub('\D', '', count_change_conf))  # вырезаем все символы и приводим к int
    if isinstance(check_message_text, int) and check_message_text > 0:  # проверяем, что введеное значение > 0
        bot.send_message(to_chat_id,
                         'count_change_conf: ' + str(check_message_text) +
                         '\nuser_id: ' + user_id +
                         '\nuser_name: ' + user_name +
                         '\ndate_time: ' + date_time
                         )  # отправляем сообщение в чат vlg_worker_bot_report
        bot.send_message(change_conf_message.from_user.id, 'Принято')  # Сообщаем пользователю, что все прошло успешно
    else:
        bot.send_message(change_conf_message.from_user.id,
                         'Запусти команду заново и введи целое число > 0')  # Сообщаем пользователю о некорректном воде


@bot.message_handler(commands=["notify_all"])
def notify_all(message):
    bot.send_message(message.from_user.id, 'Что нужно сообщить?')
    notify_all_message = message
    bot.register_next_step_handler(notify_all_message, send_notify_all)


def send_notify_all(notify_all_message):
    bot.send_message(380895469, notify_all_message.text)  # Клопов
    bot.send_message(676190873, notify_all_message.text)  # Спиридонов
    bot.send_message(419881751, notify_all_message.text)  # Ефимов
    bot.send_message(790261504, notify_all_message.text)  # Лисицкий
    bot.send_message(275972221, notify_all_message.text)  # Иванова


bot.polling(none_stop=True, interval=0)
