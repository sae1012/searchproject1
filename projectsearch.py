import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
import json

bot = telebot.TeleBot(token=token)

projects = {}
profiles = {}
users = []

try:
    with open('file.json', 'w') as file:
        users = json.loads(file.read())
except:
    users = []
try:
    with open('file.json', 'w') as file:
        projects = json.loads(file.read())
except:
    projects = {}
try:
    with open('file.json', 'w') as file:
        profiles = json.loads(file.read())
except:
    profiles = {}

def create_empty_profile():
    return {
        "name": "",
        "class": "",
        "technologies": [],
        "interests" : []
    }


def create_empty_project():
    return {
        "name": "",
        "class": "",
        "languages": [],
        "idea" : []
    }


@bot.message_handler(commands=['start'])
def send_menu(user_id):
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton("Посмотреть резюме 👀"))
    keyboard.add(KeyboardButton('Создать проект ✒️'))
    keyboard.add(KeyboardButton('Создать резюме ✒️'))
    keyboard.add(KeyboardButton('Посмотреть проекты 👀'))
    bot.send_message(user_id.chat.id, "Что хочешь?", reply_markup=keyboard)



def receive_name(message):
    profiles[message.from_user.id]['name'] = message.text
    msg = bot.send_message(message.chat.id, "В каком ты классе?")
    bot.register_next_step_handler(msg, receive_class)


def receive_class(message):
    profiles[message.from_user.id]['class'] = message.text
    msg = bot.send_message(message.chat.id, "Какие языки ты знаешь? Напиши через запятую...")
    bot.register_next_step_handler(msg, receive_technologies)


def receive_technologies(message):
    technologies = list(map(lambda x: x.strip(), message.text.split(',')))
    profiles[message.from_user.id]['technologies'] = technologies
    msg = bot.send_message(message.chat.id, "Напиши о своих интересах🤔")
    bot.register_next_step_handler(msg, receive_interests)
    
def receive_interests(message):
    interests = list(map(lambda x: x.strip(), message.text.split(',')))
    profiles[message.from_user.id]['interests'] = interests
    send_menu(message.chat.id)

    

@bot.message_handler(content_types=['text'])
def process_message(message):
    if message.text == "Посмотреть резюме 👀":
        for user_id in profiles:
            profile = profiles[user_id]
            resume = f"Имя: {profile['name']}\nКласс: {profile['class']}\nНавыки: {', '.join(profile['technologies'])}\nИнтересы: {', '.join(profile['interests'])}"
            bot.send_message(message.chat.id, resume)
    if message.text == "Посмотреть проекты 👀":
        for user_id in projects:
            project = projects[user_id]
            resume2 = f"Имя: {project['name']}\nКласс: {project['class']}\nНеобходимые навыки: {', '.join(project['languages'])}\nИдея проекта: {', '.join(project['idea'])}"
            bot.send_message(message.chat.id, resume2)
    if message.text == "Создать проект ✒️":
        projects[message.from_user.id] = create_empty_profile()
        msg = bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
        bot.register_next_step_handler(msg, receive_name_project)
    if message.text == "Создать резюме ✒️":
        profiles[message.from_user.id] = create_empty_profile()
        msg = bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
        bot.register_next_step_handler(msg, receive_name)


def receive_name_project(message):
    projects[message.from_user.id]['name'] = message.text
    msg = bot.send_message(message.chat.id, "В каком ты классе?")
    bot.register_next_step_handler(msg, receive_class_project)


def receive_class_project(message):
    projects[message.from_user.id]['class'] = message.text
    msg = bot.send_message(message.chat.id, "Какие языки ты будешь использовать в создании проекта? Напиши через запятую...")
    bot.register_next_step_handler(msg, receive_languages_project)


def receive_languages_project(message):
    languages = list(map(lambda x: x.strip(), message.text.split(',')))
    projects[message.from_user.id]['languages'] = languages
    msg = bot.send_message(message.chat.id, "Напиши о проекте и его сути🤔")
    bot.register_next_step_handler(msg, receive_idea_project)
    
def receive_idea_project(message):
    idea = list(map(lambda x: x.strip(), message.text.split(',')))
    projects[message.from_user.id]['idea'] = idea
    send_menu(message)


bot.polling(non_stop=True)
