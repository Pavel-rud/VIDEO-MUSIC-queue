import telebot
import json
from telebot import types
from telegram_bot.services_bot import *

link = "http://127.0.0.1:8000"

TOKEN = '5529060438:AAENrDJS7yA96lZrN63Zr_q0QOou_NMnA_I'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_help(message):
    user_tg = message.from_user.username
    create_user_tg(user_tg)
    if tg_tied(user_tg):  # если пользователь привязал телеграмм
        info = get_all_info(user_tg)
        username = get_user_name(user_tg)
        bot.send_message(message.chat.id, f"Привет, этот аккаунт телеграмма привязан "
        f"к профилю {username} на нашем сайте😌\n"
        f"Введите ID комнаты в которой вы хотите добавить видео/музыку в очередь\n"
        f"/help - список команд")
    else:
        markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton("Наш сайт", url=link)
        # markup.add(button1)
        bot.send_message(message.chat.id, f"Привет, этот аккаунт телеграмма не привязан "
        f"к какому-либо профилю на нашем сайте😢\nНо вы всё равно можете пользоваться ботом😉"
        f" Добавленные вами видео/музыка в очереди будут подписаны вашим телеграммом\n"
        f"Если вы всё-таки хотите привязать свой телеграмм, то зарегистрируйтесь на сайте, если вы это ещё не сделали."
        f"Введите ID комнаты в которой вы хотите добавить видео/музыку в очередь\n"
        f"/help - список команд", reply_markup=markup)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "Cписок команд:\n/leave_room - покинуть комнату\n"
                                      "/state - вывести всю информацию на данный момент")


@bot.message_handler(commands=['leave_room'])
def leave_room_command(message):
    user_tg = message.from_user.username
    if not is_password_tied(user_tg):
        leave_room(user_tg)
        bot.send_message(message.chat.id, "Вы и так не находитесь в какой-либе комнате")
    else:
        leave_room(user_tg)
        bot.send_message(message.chat.id, "Вы вышли из комнаты")


@bot.message_handler(commands=['state'])
def state_command(message):
    user_tg = message.from_user.username
    if tg_tied(user_tg):  # если пользователь привязал телеграмм
        info = get_all_info(user_tg)
        username = get_user_name(user_tg)
        bot.send_message(message.chat.id, f"Этот аккаунт телеграмма привязан "
        f"к профилю {username} на нашем сайте😌")
    else:
        info = get_all_info(user_tg)
        bot.send_message(message.chat.id,  f"Этот аккаунт телеграмма не привязан "
        f"к какому-либо профилю на нашем сайте😢")
    if info[3]:
        info = get_all_info(user_tg)
        room_info = get_info_about_room(user_tg, info[2])
        owner = get_owner(room_info[3])
        is_music = "Музыкальная" if room_info[2] else "Видеокомната"
        bot.send_message(message.chat.id, f"Вы находитесь в комнате с id {info[2]}\n"
        f"Название комнаты: {room_info[1]}\n"
        f"Владелец комнаты: {owner}\n"
        f"Тип комнаты: {is_music}")
    elif info[2]:
        bot.send_message(message.chat.id, f"Чтоб войти в комнату с id {info[2]} введите пароль")
    else:
        bot.send_message(message.chat.id, f"Введите ID комнаты в которой вы хотите добавить видео/музыку в очередь")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    chat_id = message.chat.id
    user_tg = message.from_user.username
    if is_password_tied(user_tg):
        # link
        if add_link(user_tg, message.text):
            bot.send_message(chat_id, "Вы успешно добавили в очередь!")
        else:
            bot.send_message(chat_id, "Что-то пошло не так, попробуйте ещё раз...")
    elif is_room_tied(user_tg):
        # password
        if password_is_valid(user_tg, message.text):
            info = get_all_info(user_tg)
            room_info = get_info_about_room(user_tg, info[2])
            owner = get_owner(room_info[3])
            is_music = "Музыкальная" if room_info[2] else "Видеокомната"
            bot.send_message(chat_id, f"Вы успешно присоеднились к комнате c id {info[2]}😌\n"
            f"Название комнаты: {room_info[1]}\n"
            f"Владелец комнаты: {owner}\n"
            f"Тип комнаты: {is_music}")
        else:
            info = get_all_info(user_tg)
            bot.send_message(chat_id, f"Неверный пароль для комнаты с id {info[2]}, попробуйте ещё раз")
        bot.delete_message(chat_id, message.message_id)
    else:
        # room
        if room_exist(user_tg, message.text):
            bot.send_message(chat_id, f"Введите пароль для входа в комнату с id {message.text}")
        else:
            bot.send_message(chat_id, f"Комната с таким id {message.text} не найдена")


def run_bot():
    try:
        print("TelegramBot is ready")
        bot.infinity_polling()
    except Exception as error:
        print(error)