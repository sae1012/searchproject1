import telebot
import random
from telebot import types
token = "7043472916:AAE4VE3JPaLS46uSruhmleSRpguMjEK7E4k"
bot = telebot.TeleBot(token=token)
ankets = {}
users = {}
"""exit = types.KeyboardButton("Я больше не хочу никого искать")"""


@bot.message_handler(commands=['start'])
def Start(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton('Начать✔')
    markup.add(start)
    bot.send_message(user_id, text="Привет,{0.first_name}! Нажми на кнопку 'Начать✔', чтобы начать заполнять анкету".format(message.from_user), reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def knopke(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if(message.text == "Начать✔"):
        member = types.KeyboardButton("Ищу проект!")
        project = types.KeyboardButton("Ищу участников!")
        markup.add(member, project)
        choose = bot.send_message(user_id, text="Вы ищите проект или участников в него?".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(choose, choice)
    if(message.text != "Начать✔"):
        start = types.KeyboardButton('/start')
        markup.add(start)
        eror1 = bot.send_message(user_id, text="Такого ответа нет, нажмите /start, чтобы возобновить бота".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(eror1, Start)


@bot.message_handler(content_types=['text'])
def choice(message):
    user_id = message.chat.id
    users[user_id] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if users[user_id] == "Ищу проект!":
        bot.send_message(user_id, "Напиши свои навыки и предпочтения о проекте который ты ищешь!\nА так же:\nКласс\nКакой опыт в твоей деятельности\nВСЕ ЭТО ОДНИМ СООБЩЕНИЕМ!!!")
    elif users[user_id] == "Ищу участников!":
        bot.send_message(user_id, "Напиши о своем проекте и навыки участника, которого ты ищешь, и свои предпочтения нём!\n" "А так же:\n", "Класс\n", "Сколько участников уже состоят в проекте\n", "Сколько участников надо?\n", "ВСЕ ЭТО ОДНИМ СООБЩЕНИЕМ!!!")
    else:
        start = types.KeyboardButton('/start')
        markup.add(start)
        eror2 = bot.send_message(user_id, text="Такого ответа нет, нажмите /start, чтобы возобновить бота".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(eror2, Start)


@bot.message_handler(content_types=['text'])
def Fork(message):
    user_id = message.chat.id
    ankets[user_id] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if  ankets[user_id] == "Ищу проект!": 
        search = types.KeyboardButton("Начать поиск проектов")
        profile = types.KeyboardButton("Изменить свою анкету")
        markup.add(search, profile)
        bot.send_message(user_id, text="Начнем?".format(message.from_user), reply_markup=markup)
    elif ankets[user_id] == "Ищу участников!": 
        search = types.KeyboardButton("Начать поиск участников")
        profile = types.KeyboardButton("Изменить свою анкету")
        markup.add(search, profile)
        bot.send_message(user_id, text="Начнем?".format(message.from_user), reply_markup=markup)
    else:
        start = types.KeyboardButton('/start')
        markup.add(start)
        eror2 = bot.send_message(user_id, text="Такого ответа нет, нажмите /start, чтобы возобновить бота".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(eror2, Start)
"""
@bot.message_handler(content_types=['text'])
def Searching(message):
"""
@bot.message_handler(content_types=['text'])
def MyProfile(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == "Изменить свою анкету":
        bot.send_message(user_id, text = "Вот ваша анкета")
        bot.send_message(user_id, text = ankets[user_id])
        yes = types.KeyboardButton("Да")
        no = types.KeyboardButton("Нет")
        markup.add(yes, no)
        bot.send_message(user_id, text="Вы точно хотите изменить свою анкету?".format(message.from_user), reply_markup=markup)
        if message.text == "Да":
            bot.send_message(user_id, "Напиши свои навыки и предпочтения о проекте который ты ищешь!\nА так же:\nКласс\nКакой опыт в твоей деятельности\nВСЕ ЭТО ОДНИМ СООБЩЕНИЕМ!!!")
            ankets[user_id] = 0
            update = bot.send_message(user_id, "Анкета успешно обновлена!")
            bot.register_next_step_handler(update, Fork)
        elif message.text == "Нет":
            Fork(message)
        else:
            start = types.KeyboardButton('/start')
            markup.add(start)
            eror3 = bot.send_message(user_id, text="Такого ответа нет, нажмите /start, чтобы возобновить бота".format(message.from_user), reply_markup=markup)
            bot.register_next_step_handler(eror3, Start)





bot.polling(none_stop=True)

