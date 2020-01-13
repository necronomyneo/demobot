import telebot
from telebot import types  # кнопки
from string import Template
import time, datetime
from datetime import timedelta

from datetime import date

bot = telebot.TeleBot("1037961560:AAEaXbn6a2MwsaH3avwadlvfvBwEFSVMSM8")

all_users_dict = {"Toshkent": "", "Buxoro": ""}

startedUsers = []

users = []

available_in_Tashkent = []
available_in_Bukhara = []

user_dict = {}
markup_taksi_T = types.InlineKeyboardMarkup()
markup_taksi_B = types.InlineKeyboardMarkup()

class User:
    def __init__(self, city):
        self.city = city

        keys = ['id', 'fullname', 'phone', 'passangers', 'price', 'time', 'timeCreated', ]

        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    startedUsers.append(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/Zakaz')
    itembtn3 = types.KeyboardButton('/list')
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(message.chat.id, "Salom "
                     + message.from_user.first_name
                     , reply_markup=markup)

@bot.message_handler(commands=['time'])
def send_about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Time"))
    msg = bot.send_message(message.chat.id, "Time send", reply_markup=markup)
    bot.register_next_step_handler(msg, process_Time_step)
# /about
@bot.message_handler(commands=['help'])
def send_about(message):
    bot.send_message(message.chat.id, "YOUR BEST FRIEND IS FUCKING YOUR GIRLFRIEND AND YOU ARE TOO BIG ASHOLE TO DO ANYTHING .!. .!. .!.")

@bot.message_handler(commands=['about'])
def send_about(message):

    bot.send_message(message.chat.id, "GO FUCK YOURSELF .!. .!. .!.")

@bot.message_handler(commands=['adminmotherfathersend'])
def send_about(message):

    msg = bot.send_message(message.chat.id, "Salom " + message.chat.first_name +"\n\n  Iltimos barcha yubormoqchi \n  bo'lgan xabarizni kiriting")
    bot.register_next_step_handler(msg, admin_send_all)
# /reg
@bot.message_handler(commands=["list"])
def list_taksi(message):
    k = {message.chat.id: message.text}
    users.append(k)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    itembtn5 = types.KeyboardButton('Pochta')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)

    msg = bot.send_message(message.chat.id, 'Number of passangers', reply_markup=markup)
    bot.register_next_step_handler(msg, process_userWsh_step)


@bot.message_handler(commands=["Zakaz"])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Toshkent -> Buxoro')
    itembtn2 = types.KeyboardButton('Buxoro -> Toshkent')

    markup.add(itembtn1, itembtn2)

    msg = bot.send_message(message.chat.id, 'Yo\'nalishni tanlang', reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)

def admin_send_all(message):
    for i in startedUsers:
        bot.send_message(i, message.text)
        bot.send_message(message.chat.id, "Success")

def process_Time_step(message):
    chat_id = message.chat.id
    for i in range(0, len(users)):
        if message.chat.id in users[i].keys():
            users[i]['userTime'] = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Toshkent -> Buxoro')
    itembtn2 = types.KeyboardButton('Buxoro -> Toshkent')
    markup.add(itembtn1, itembtn2)

    msg = bot.send_message(message.chat.id, 'Yo\'nalishni tanlang', reply_markup=markup)
    bot.register_next_step_handler(msg, process_listCity_step)

def process_listCity_step(message):



    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Toshkent -> Buxoro')
    itembtn2 = types.KeyboardButton('Buxoro -> Toshkent')
    markup.add(itembtn1, itembtn2)

    if message.text == "Toshkent -> Buxoro":
        p = 0
        t = 0
        for j in range(0, len(users)):
            if message.chat.id in users[j]:
                if users[j]['userPassangers'] == "Pochta":
                    p = users[j]['userPassangers']
                else:
                    p = int(users[j]['userPassangers'])
                t = users[j]['userTime']
        for i in range(0, len(available_in_Tashkent)):
            if p == "Pochta":
                if (int(t[11: 13]) <= int(available_in_Tashkent[i]['time'][11: 13]) and int(t[0: 2]) == int(
                        available_in_Tashkent[i]['time'][0: 2])) or int(t[0: 2]) < int(
                        available_in_Tashkent[i]['time'][0: 2]):
                    plus = types.InlineKeyboardMarkup()
                    plus.add(types.InlineKeyboardButton(" + ", callback_data=available_in_Tashkent[i]['id']))
                    msg_id = bot.send_message(chat_id,
                                              text=f"ID: {available_in_Tashkent[i]['id']} \n"
                                                   f" Name: {available_in_Tashkent[i]['fullname']} \n"
                                                   f" Phone: +998 {available_in_Tashkent[i]['phone']} \n"
                                                   f" Passangers: {available_in_Tashkent[i]['passangers']} \n"
                                                   f" Price: {available_in_Tashkent[i]['price']} \n"
                                                   f" Time: {available_in_Tashkent[i]['time']}")
                    available_in_Tashkent[i]['message_id'] = msg_id.message_id
            else:
                if available_in_Tashkent[i]['passangers'] != "Pochta":

                    if p >= int(available_in_Tashkent[i]['passangers']):

                        if (int(t[11: 13]) <= int(available_in_Tashkent[i]['time'][11: 13]) and int(t[0: 2]) == int(
                                available_in_Tashkent[i]['time'][0: 2])) or int(t[0: 2]) < int(
                            available_in_Tashkent[i]['time'][0: 2]):
                            plus = types.InlineKeyboardMarkup()
                            plus.add(types.InlineKeyboardButton(" + ", callback_data=available_in_Tashkent[i]['id']))
                            msg_id = bot.send_message(chat_id,
                                                      text=f"ID: {available_in_Tashkent[i]['id']} \n"
                                                           f" Name: {available_in_Tashkent[i]['fullname']} \n"
                                                           f" Phone: +998 {available_in_Tashkent[i]['phone']} \n"
                                                           f" Passangers: {available_in_Tashkent[i]['passangers']} \n"
                                                           f" Price: {available_in_Tashkent[i]['price']} \n"
                                                           f" Time: {available_in_Tashkent[i]['time']}")
                            available_in_Tashkent[i]['message_id'] = msg_id.message_id
                    else:
                        bot.send_message(chat_id, "Bizda hozircha bu zakaz yoq")
                else:
                    if (int(t[11: 13]) <= int(available_in_Tashkent[i]['time'][11: 13]) and int(t[0: 2]) == int(
                            available_in_Tashkent[i]['time'][0: 2])) or int(t[0: 2]) < int(
                        available_in_Tashkent[i]['time'][0: 2]):
                        msg_id = bot.send_message(chat_id,
                                                  text=f"ID: {available_in_Tashkent[i]['id']} \n"
                                                       f" Name: {available_in_Tashkent[i]['fullname']} \n"
                                                       f" Phone: +998 {available_in_Tashkent[i]['phone']} \n"
                                                       f" Passangers: {available_in_Tashkent[i]['passangers']} \n"
                                                       f" Price: {available_in_Tashkent[i]['price']} \n"
                                                       f" Time: {available_in_Tashkent[i]['time']}")
                        available_in_Tashkent[i]['message_id'] = msg_id.message_id

    elif message.text == "Buxoro -> Toshkent":
        p = 0
        for j in range(0, len(users)):
            if message.chat.id in users[j]:
                if users[j]['userPassangers'] == "Pochta":
                    p = users[j]['userPassangers']
                else:
                    p = int(users[j]['userPassangers'])
                t = users[j]['userTime']
        for i in range(0, len(available_in_Bukhara)):
            if p == "Pochta":
                if (int(t[11: 13]) <= int(available_in_Bukhara[i]['time'][11: 13]) and int(t[0: 2]) == int(
                        available_in_Bukhara[i]['time'][0: 2])) or int(t[0: 2]) < int(
                                available_in_Bukhara[i]['time'][0: 2]):
                    msg_id = bot.send_message(chat_id,
                                              text=f"ID: {available_in_Bukhara[i]['id']} \n"
                                                   f" Name: {available_in_Bukhara[i]['fullname']} \n"
                                                   f" Phone: +998 {available_in_Bukhara[i]['phone']} \n"
                                                   f" Passangers: {available_in_Bukhara[i]['passangers']} \n"
                                                   f" Price: {available_in_Bukhara[i]['price']} \n"
                                                   f" Time: {available_in_Bukhara[i]['time']}")
                    available_in_Bukhara[i]['message_id'] = msg_id.message_id
                    plus = types.InlineKeyboardMarkup()
                    plus.add(types.InlineKeyboardButton(" + ", callback_data=available_in_Bukhara[i]['id']))
                    msg_id = bot.send_message(chat_id,
                                              text=f"ID: {available_in_Bukhara[i]['id']} \n"
                                                   f" Name: {available_in_Bukhara[i]['fullname']} \n"
                                                   f" Phone: +998 {available_in_Bukhara[i]['phone']} \n"
                                                   f" Passangers: {available_in_Bukhara[i]['passangers']} \n"
                                                   f" Price: {available_in_Bukhara[i]['price']} \n"
                                                   f" Time: {available_in_Bukhara[i]['time']}")
                    available_in_Bukhara[i]['message_id'] = msg_id.message_id
            else:
                if available_in_Bukhara[i]['passangers'] != "Pochta":
                    if p >= int(available_in_Bukhara[i]['passangers']):
                        if (int(t[11: 13]) <= int(available_in_Bukhara[i]['time'][11: 13]) and int(t[0: 2]) == int(
                                available_in_Bukhara[i]['time'][0: 2])) or int(t[0: 2]) < int(
                            available_in_Bukhara[i]['time'][0: 2]):
                            plus = types.InlineKeyboardMarkup()
                            plus.add(types.InlineKeyboardButton(" + ", callback_data=available_in_Bukhara[i]['id']))
                            msg_id = bot.send_message(chat_id,
                                                      text=f"ID: {available_in_Bukhara[i]['id']} \n"
                                                           f" Name: {available_in_Bukhara[i]['fullname']} \n"
                                                           f" Phone: +998 {available_in_Bukhara[i]['phone']} \n"
                                                           f" Passangers: {available_in_Bukhara[i]['passangers']} \n"
                                                           f" Price: {available_in_Bukhara[i]['price']} \n"
                                                           f" Time: {available_in_Bukhara[i]['time']}")
                            available_in_Bukhara[i]['message_id'] = msg_id.message_id
                    else:
                        bot.send_message(chat_id, "Bizda hozircha bu zakaz yoq")
                else:
                    if (int(t[11: 13]) <= int(available_in_Bukhara[i]['time'][11: 13]) and int(t[0: 2]) == int(
                            available_in_Bukhara[i]['time'][0: 2])) or int(t[0: 2]) < int(
                        available_in_Bukhara[i]['time'][0: 2]):
                        msg_id = bot.send_message(chat_id,
                                                  text=f"ID: {available_in_Bukhara[i]['id']} \n"
                                                       f" Name: {available_in_Bukhara[i]['fullname']} \n"
                                                       f" Phone: +998 {available_in_Bukhara[i]['phone']} \n"
                                                       f" Passangers: {available_in_Bukhara[i]['passangers']} \n"
                                                       f" Price: {available_in_Bukhara[i]['price']} \n"
                                                       f" Time: {available_in_Bukhara[i]['time']}")
                        available_in_Bukhara[i]['message_id'] = msg_id.message_id


    else:
        msg = bot.send_message(chat_id, "Bizda mavjud yo'nalishlar: ", reply_markup=markup)
        bot.register_next_step_handler(msg, process_listCity_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'FIO', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Telefon nomeriz: (+998 )')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_phone_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]

    try:
        if int(message.text) and len(message.text) == 9:
            user.phone = message.text

            markup_time = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
            t = datetime.date.today()
            h = datetime.datetime.now()
            one = timedelta(1)
            if h.hour < 2:
                item24 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 02:00')
                item23 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 04:00')
                item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
                item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
                item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item24, item23, item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7,
                                item8,
                                item9,
                                item10,
                                item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)

            elif h.hour < 4:
                item23 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 04:00')
                item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
                item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
                item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item23, item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8,
                                item9,
                                item10,
                                item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 6:
                item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
                item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
                item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9,
                                item10,
                                item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 8:
                item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
                item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,
                                item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 10:
                item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 12:
                item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,
                                item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 14:
                item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 16:

                item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 18:

                item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 20:

                item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item4, item5, item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 22:

                item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item5, item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)
            elif h.hour < 24:

                item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
                item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
                item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
                item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
                item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
                item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
                item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
                item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
                item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
                item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
                item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
                item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
                item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

                markup_time.add(item6, item7, item8, item9, item10, item11, item12,
                                item13, item14, item15, item16, item17, item18)


            msg = bot.send_message(chat_id, 'Iltimos taxminiy vaqtni tanlang', reply_markup=markup_time)
            bot.register_next_step_handler(msg, process_getTime_step)
        else:
            bot.send_message(chat_id, text="Iltimos qayta kiriting:")
            bot.register_next_step_handler(message, process_phone_step)
    except:
        bot.send_message(chat_id, text="Xatolik")

def process_getTime_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    try:
        print(message.text)
        user.time = message.text

        passenger = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
        passenger.add(types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                      types.KeyboardButton("4"), types.KeyboardButton("Pochta"))


        msg = bot.send_message(chat_id, 'Nechta kishiga buyurtma bermoqchisiz?', reply_markup=passenger)
        bot.register_next_step_handler(msg, process_driverPassangers_step)
    except:
        bot.send_message(chat_id, "Ooops!!")


def process_driverPassangers_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.passangers = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('30 000')
        itembtn2 = types.KeyboardButton('40 000')
        itembtn3 = types.KeyboardButton('100 000')
        itembtn4 = types.KeyboardButton('110 000')
        itembtn5 = types.KeyboardButton('120 000')
        itembtn6 = types.KeyboardButton('130 000')
        itembtn7 = types.KeyboardButton('2X = 220 000')
        itembtn8 = types.KeyboardButton('2X = 240 000')
        itembtn9 = types.KeyboardButton('2X = 250 000')
        itembtn10 = types.KeyboardButton('2X = 260 000')
        itembtn11 = types.KeyboardButton('3X = 330 000')
        itembtn12 = types.KeyboardButton('3X = 350 000')
        itembtn13 = types.KeyboardButton('3X = 360 000')
        itembtn14 = types.KeyboardButton('3X = 380 000')
        itembtn15 = types.KeyboardButton('4X = 460 000')
        itembtn16 = types.KeyboardButton('4X = 480 000')
        itembtn17 = types.KeyboardButton('4X = 500 000')
        itembtn18 = types.KeyboardButton('4X = 520 000')
        itembtn19 = types.KeyboardButton('Boshqa narx')

        if message.text == "Pochta":
            markup.add(itembtn1, itembtn2, itembtn19)
        elif message.text == "1":
            markup.add(itembtn3, itembtn4, itembtn5, itembtn6, itembtn19)
        elif message.text == "2":
            markup.add(itembtn7, itembtn8, itembtn9, itembtn10, itembtn19)
        elif message.text == "3":
            markup.add(itembtn11, itembtn12, itembtn13, itembtn14, itembtn19)
        elif message.text == "4":
           markup.add(itembtn15, itembtn16, itembtn17, itembtn18, itembtn19)
        msg = bot.send_message(chat_id, 'Iltimos taxminiy narxni tanlang. \nTanlagan narxizga qarab sizga taksichilar qo\'ng\'iroq qilishadi',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, process_driverCar_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_driverCar_step(message):
    for i in range(0, len(available_in_Tashkent)):
        if int(available_in_Tashkent[i]['timeCreated'][0: 2]) + 2 <= datetime.datetime.now().day or int(available_in_Tashkent[i]['timeCreated'][3: 5]) < datetime.datetime.now().month or int(available_in_Tashkent[i]['timeCreated'][6: 8]) < datetime.datetime.now().year:
            available_in_Tashkent.remove(available_in_Tashkent[i])
    for i in range(0, len(available_in_Bukhara)):
        if int(available_in_Bukhara[i]['timeCreated'][0: 2]) + 2 <= datetime.datetime.now().day or int(available_in_Bukhara[i]['timeCreated'][3: 5]) < datetime.datetime.now().month or int(available_in_Bukhara[i]['timeCreated'][6: 8]) < datetime.datetime.now().year:
            available_in_Bukhara.remove(available_in_Bukhara[i])


    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == "Boshqa narx":
            msg2 = bot.send_message(chat_id, "Boshqa narx kiritish (minimal summa 1 kishi uchun 60 000")
            bot.register_next_step_handler(msg2, process_driverCar_step)
        else:
            user.price = message.text
            timeCreated = f'{datetime.datetime.now().strftime("%d-%m-%y")} | {datetime.datetime.now().hour}:{datetime.datetime.now().minute}'
            user.timeCreated = timeCreated
            user.id = chat_id
            print(user)
            k = {"id": user.id, "fullname": user.fullname, "phone": user.phone, "passangers": user.passangers,
                 "price": user.price, "city": user.city, "message_id": "", "time": user.time,
                 "timeCreated": timeCreated}

            print(k)
            markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup_cancel.add(types.KeyboardButton("Bekor qilish"))
            if user.city == "Buxoro -> Toshkent":
                all_users_dict['Buxoro'] = k
                available_in_Bukhara.append(k)
                for i in range(0, len(available_in_Bukhara)):
                    print(">>>", available_in_Bukhara[i])
            elif user.city == "Toshkent -> Buxoro":
                all_users_dict['Toshkent'] = k
                available_in_Tashkent.append(k)
                for i in range(0, len(available_in_Tashkent)):
                    print(">>>", available_in_Tashkent[i])

            bot.send_message(chat_id, getRegData(user, 'YOUR APPLICATION', message.from_user.first_name),
                             parse_mode="Markdown")
            msg = bot.send_message(message.chat.id,
                                   f'Hurmatli {user.fullname} taksichi bilan kelishgandan so\'ng so\'rovni '
                                   f'quyidagi tugma orqali bekor qilishizni so\'raymiz, aks holda buyurtangiz '
                                   f'botda 48 soat davomida turadi'
                                   f'\n\n\nSTART - /start\nLIST - /list\nHELP - /help', reply_markup=markup_cancel)
            bot.register_next_step_handler(msg, process_cancel_step)

    except:
        bot.reply_to(message, 'ooops!!')

def process_cancel_step(message):
    try:
        for i in range(0, len(available_in_Tashkent)):
            if message.chat.id == available_in_Tashkent[i]['id']:
                available_in_Tashkent.remove(available_in_Tashkent[i])
        for i in range(0, len(available_in_Bukhara)):
            if message.chat.id == available_in_Bukhara[i]['id']:
                available_in_Bukhara.remove(available_in_Bukhara[i])
        bot.send_message(message.chat.id, "Success")
    except:
        bot.send_message(message.chat.id, "Bekor qilishni iloji yoq.\n\n Iltimos /admin bilan bog'laning")

def process_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text

        msg = bot.send_message(chat_id, 'Дата выдачи водительского удостоверения\nВ формате: День.Месяц.Год')
        bot.register_next_step_handler(msg, process_driverDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')



def process_driverDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Марка автомобиля')
        bot.register_next_step_handler(msg, process_car_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Модель автомобиля')
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Бежевый')
        itembtn2 = types.KeyboardButton('Белый')
        itembtn3 = types.KeyboardButton('Голубой')
        itembtn4 = types.KeyboardButton('Желтый')
        itembtn5 = types.KeyboardButton('Зеленый')
        itembtn6 = types.KeyboardButton('Коричневый')
        itembtn7 = types.KeyboardButton('Красный')
        itembtn8 = types.KeyboardButton('Оранжевый')
        itembtn9 = types.KeyboardButton('Розовый')
        itembtn10 = types.KeyboardButton('Серый')
        itembtn11 = types.KeyboardButton('Синий')
        itembtn12 = types.KeyboardButton('Фиолетовый')
        itembtn13 = types.KeyboardButton('Черный')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
                   itembtn11, itembtn12, itembtn13)

        msg = bot.send_message(chat_id, 'Цвет автомобиля', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text

        msg = bot.send_message(chat_id, 'Гос. номер автомобиля')
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Год выпуска')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")
        # отправить в группу

    except Exception as e:
        bot.reply_to(message, 'ooops!!')
def process_userWsh_step(message):

    for i in range(0, len(users)):
        if message.chat.id in users[i].keys():
            users[i]['userPassangers'] = message.text

    markup_time = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    t = datetime.date.today()
    h = datetime.datetime.now()
    one = timedelta(1)
    if h.hour < 2:
        item24 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 02:00')
        item23 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 04:00')
        item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
        item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
        item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item24, item23, item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7,
                        item8,
                        item9,
                        item10,
                        item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)

    elif h.hour < 4:
        item23 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 04:00')
        item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
        item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
        item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item23, item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8,
                        item9,
                        item10,
                        item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 6:
        item22 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 06:00')
        item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
        item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item22, item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9,
                        item10,
                        item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 8:
        item21 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 08:00')
        item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item21, item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,
                        item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 10:
        item20 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 10:00')
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item20, item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 12:
        item19 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 12:00')
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item19, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,
                        item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 14:
        item1 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 14:00')
        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 16:

        item2 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 16:00')
        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 18:

        item3 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 18:00')
        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 20:

        item4 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 20:00')
        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item4, item5, item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 22:

        item5 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 22:00')
        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item5, item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)
    elif h.hour < 24:

        item6 = types.KeyboardButton(f'{t.strftime("%d-%m-%y")} | 24:00')
        item7 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 02:00')
        item8 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 04:00')
        item9 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 06:00')
        item10 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 08:00')
        item11 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 10:00')
        item12 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 12:00')
        item13 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 14:00')
        item14 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 16:00')
        item15 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 18:00')
        item16 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 20:00')
        item17 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 22:00')
        item18 = types.KeyboardButton(f'{(t + one).strftime("%d-%m-%y")} | 24:00')

        markup_time.add(item6, item7, item8, item9, item10, item11, item12,
                        item13, item14, item15, item16, item17, item18)

    msg = bot.send_message(message.chat.id, 'Iltimos taxminiy vaqtni tanlang', reply_markup=markup_time)

    bot.register_next_step_handler(msg, process_Time_step)

def process_userTEL_step(message):
    print(message.text)
    k = {message.chat.id: message.text}
    users.append(k)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    itembtn5 = types.KeyboardButton('Pochta')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)

    msg = bot.send_message(message.chat.id, 'Number of passangers', reply_markup=markup)
    bot.register_next_step_handler(msg, process_userWsh_step)

# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template(
        '$title *$name* \n CITY: *$userCity* \n NAME: *$fullname* \n PHONE: *$phone* \n Passangers: *$passangers* \n '
        'Price: *$price* \n Time: *$time*')
    if "suxrob" in user.fullname or "Suxrob" in user.fullname:
        return t.substitute({

            'title': title,
            'name': name,
            'userCity': user.city,
            'fullname': f"{user.fullname} G' U L O M",
            'phone': f"+998 {user.phone}",
            'passangers': user.passangers,
            'price': user.price,
            'time': user.time,

        })
    else:
        return t.substitute({

            'title': title,
            'name': name,
            'userCity': user.city,
            'fullname': user.fullname,
            'phone': f"+998 {user.phone}",
            'passangers': user.passangers,
            'price': user.price,
            'time': user.time,

        })


# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'START - /start\nLIST - /list\nHELP - /help')


# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    try:
        for i in range(0, len(available_in_Tashkent)):
            bot.delete_message(call.message.chat.id, available_in_Tashkent[i]['message_id'])
        for i in range(0, len(available_in_Bukhara)):
            bot.delete_message(call.message.chat.id, available_in_Bukhara[i]['message_id'])
        for i in range(0, len(available_in_Tashkent)):
            if str(call.data) == str(available_in_Tashkent[i]['id']):
                bot.send_message(call.message.chat.id,
                                          text=f"ID: {available_in_Tashkent[i]['id']} \n Name: {available_in_Tashkent[i]['fullname']} \n"
                                               f" Phone: +998 {available_in_Tashkent[i]['phone']} \n Passangers: {available_in_Tashkent[i]['passangers']} \n"
                                               f" Car: {available_in_Tashkent[i]['car']}")
        for i in range(0, len(available_in_Bukhara)):
            if str(call.data) == str(available_in_Bukhara[i]['id']):
                bot.send_message(call.message.chat.id,
                                          text=f"ID: {available_in_Bukhara[i]['id']} \n Name: {available_in_Bukhara[i]['fullname']} \n"
                                               f" Phone: +998 {available_in_Bukhara[i]['phone']} \n Passangers: {available_in_Bukhara[i]['passangers']} \n"
                                               f" Car: {available_in_Bukhara[i]['car']}")

        for i in range(0, len(users)):
            if call.message.chat.id in users[i].keys():
                if users[i]['userPassangers'] == "Pochta":
                    bot.send_message(call.data,
                                     "Sizga " + call.message.chat.first_name + " taklif berdi\n TEL: +998 " + users[i][
                                         call.message.chat.id] + "\n" +
                                     users[i]['userPassangers'])
                else:
                    bot.send_message(call.data,
                                     "Sizga " + call.message.chat.first_name + " taklif berdi\n TEL: +998 " + users[i][
                                         call.message.chat.id] + "\n " +
                                     users[i]['userPassangers'] + " ta yo'lovchi")
                time.sleep(3)
                bot.send_message(call.message.chat.id, text="Success")

    except:
        bot.send_message(call.message.chat.id, text="Nothing found(\n for help - /help")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)