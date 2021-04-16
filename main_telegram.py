import telebot
from main_logic import check_for_mistake

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot")


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    mess = message.text
    correct = check_for_mistake(mess)
    for i in correct:
        bot.reply_to(message, i)


bot.polling()
