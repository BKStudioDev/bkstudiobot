# -*- coding: utf-8 -*-
import telebot

TOKEN = "545763190:AAG2iUQDQVmxUjUzUnhLdATafnHcwkv0SJQ"
bot = telebot.TeleBot(TOKEN)

# Приветственная надпись
@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, 'Як тебе звати?')
    bot.register_next_step_handler(sent, hello)
	
def hello(message):
    name = message.text
    if name == "Bohdan":
        sent = bot.send_message(message.chat.id, name + ' , you are /|0X')
    else:
        sent = bot.send_message(message.chat.id, 'Привіт, ' + name + '. Радий тебе бачити!')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    text = message.text
    if name != "Bohdan":
        bot.send_message(message.chat.id, 'Ти сказав(-ла) ' + text + ' ?')

@bot.message_handler(func=lambda message: True, content_types=['photo', 'sticker'])
def handle_images(message):
	bot.send_message(message.chat.id, "Нахуй мені твої картинки?!")

bot.polling()
