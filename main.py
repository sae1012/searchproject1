import json
import telebot
from telebot import types
role = {}
who = {}
about = {}
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
        answer1 =  bot.send_message(message.chat_id, "Напиши о своем проекте")
        bot.register_next_step_handler(answer1, about)
    elif(message.text == "Участник"):
        user_id = message.from_user.id
        who[user_id] = message.text
        answer2 = bot.send_message(message.chat.id, "Напиши о себе")
        bot.register_next_step_handler(answer2, about1)


def about1(message):
    user_id = message.from_user.id
    about[user_id] = message.text


bot.polling(none_stop=True)

