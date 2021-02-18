import telebot
from datetime import datetime

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
    check_message_text = int(create_conf_message.text)
    if isinstance(check_message_text, int) and check_message_text > 0:
        bot.send_message(to_chat_id,
                         'count_create_conf: ' + count_create_conf +
                         '\nuser_id: ' + user_id +
                         '\nuser_name: ' + user_name +
                         '\ndate_time: ' + date_time
                         )
        bot.send_message(create_conf_message.from_user.id, 'Принято')
    else:
        bot.send_message(create_conf_message.from_user.id, 'Запусти команду заново и введи целое число > 0')


@bot.message_handler(commands=["change_conf"])
def change_conf_command_start(message):
    bot.send_message(message.from_user.id, 'Укажи количество измененных конфигураций')
    change_conf_message = message
    bot.register_next_step_handler(change_conf_message, change_conf_control)


def change_conf_control(change_conf_message):
    user_id = str(change_conf_message.from_user.id)
    user_name = str(change_conf_message.from_user.username)
    count_change_conf = str(change_conf_message.text)
    date_time = str(datetime.now())
    to_chat_id = -1001427883840  # id чата vlg_worker_bot_report
    check_message_text = int(change_conf_message.text)
    if isinstance(check_message_text, int) and check_message_text > 0:
        bot.send_message(to_chat_id,
                         'count_change_conf: ' + count_change_conf +
                         '\nuser_id: ' + user_id +
                         '\nuser_name: ' + user_name +
                         '\ndate_time: ' + date_time
                         )
        bot.send_message(change_conf_message.from_user.id, 'Принято')
    else:
        bot.send_message(change_conf_message.from_user.id, 'Запусти команду заново и введи целое число > 0')


bot.polling(none_stop=True, interval=0)
