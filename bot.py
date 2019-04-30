# -*- coding: utf-8 -*-
import telebot

TOKEN = "545763190:AAG2iUQDQVmxUjUzUnhLdATafnHcwkv0SJQ"
bot = telebot.TeleBot(TOKEN)

# Приветственная надпись
@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def hello(message):
    name = message.text
    if name == "Bohdan":
        sent = bot.send_message(message.chat.id, name + ' , you are /|0X')
    else:
        sent = bot.send_message(message.chat.id, 'Привет, ' + name + '. Рад тебя видеть.')

@bot.message_handler(func=lambda message: True, content_types=['photo', 'sticker'])
def handle_images(message):
	bot.send_message(message.chat.id, "Nahuy mnie tvoyi kartinki?!")

bot.polling()
