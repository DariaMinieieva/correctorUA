"""
This module contains functions that work
directly with a telegram bot
"""
from token import token
import telebot
from main_logic import check_for_mistake, check_conjunctions, correct_msg, main_check

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_command(message):
    """
    Initial message
    """
    bot.reply_to(message, "Привіт! Я бот - українізатор!")


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    """
    Send messages to the bot
    """
    special_word(message, message.text)
    mess = message.text
    correct = check_for_mistake(mess)
    correctes_sentence = correct_msg(mess)
    errors = check_conjunctions(correctes_sentence)
    hyphen = main_check(correctes_sentence)

    if correct:
        for i in correct:
            bot.reply_to(message, i)

    if errors:
        for i in errors:
            bot.reply_to(message, i)

    if hyphen:
        for i in hyphen:
            bot.reply_to(message, i)


def special_word(message, text):
    """
    Special cases
    """
    if "українізатор" in text:
        bot.reply_to(message, "Це я!")
    if "україна" in text:
        bot.reply_to(message, "Україна - лише з великої.")

    if ("Тернопіль" in text) or ("тернопіль" in text):
        bot.reply_to(message, "Файне місто")

    if "сумно" in text:
        bot.reply_to(message, "не сумуй!")

    if ("важко" in text) or ("тяжко" in text):
        bot.reply_to(message, "нічого, буде ще важче.")

    if "БА" in text:
        bot.reply_to(message, "ні, КН")


bot.polling()
