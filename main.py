import json
import telebot
from telebot import types
role = {}
who = {}
projects = {}
bot = telebot.TeleBot('6977407912:AAH2ov_sx0MlUIaQsXu49ZrAXldaCCYYG70')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    role[user_id] = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Автор")
    btn2 = types.KeyboardButton("Участник")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Ты Участник/Автор", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Автор"):
        user_id = message.from_user.id
        who[user_id] = message.text
        answer1 =  bot.send_message(message.chat.id, "Напиши о своем проекте в одно сообщение:\n 1.Название проекта\n 2.Описание проекта\n 3.Участники\n 4.Кто нужен?\n 5.Контакный данные участников")
        bot.register_next_step_handler(answer1, createprojects)
    elif(message.text == "Участник"):
        user_id = message.from_user.id
        who[user_id] = message.text
        answer2 = bot.send_message(message.chat.id, "Напиши о себе в одно сообщение:\n 1.Изученные языки\n 2.Что лучше всего делаешь(фронтенд/бэкенд/дизайн)\n 3.Контакный данные")
        bot.register_next_step_handler(answer2, createprojects)


def createprojects(message):
    user_id = message.from_user.id
    projects[user_id] = message.text
    answer3 = bot.send_message(message.chat.id, "Напишите ключевые слова, связанные с проектом, который потенциально, Вам, понравится ")


bot.polling(none_stop=True)
