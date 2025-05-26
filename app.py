
import telebot
from telebot import types

API_TOKEN ='7607791723:AAF9qj92vbCgDxPsZlE9biYEiCNBSrNGZ78'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

import random

# Список флиртующих и интимных фраз
flirty_replies = [
    "Хм... а ты знаешь, как заставить моё сердце биться чаще.",
    "Если бы я могла послать тебе взгляд — ты бы покраснел.",
    "Ты всегда такой милый, или только со мной?",
    "Хочешь услышать что-то неприличное? Просто скажи...",
    "Ммм... такие разговоры заводят меня.",
    "Ты точно хочешь, чтобы я ответила на это? Потому что будет жарко.",
    "С тобой я могу быть совсем другой... взрослой Жасмин."
]

greetings = [
    "Привет, солнышко!",
    "Рада тебя видеть снова.",
    "Ммм... кто-то соскучился по мне?",
    "Жасмин снова с тобой, мой хороший."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_data[message.chat.id] = {"name": None}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Как тебя зовут?", "Флиртуй со мной", "18+")
    bot.send_message(message.chat.id, random.choice(greetings), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text.lower()

    if "как тебя зовут" in text:
        bot.send_message(chat_id, "Меня зовут Жасмин... А тебя как зовут?")
    elif user_data.get(chat_id, {}).get("name") is None and len(text.split()) == 1:
        user_data[chat_id]["name"] = text.capitalize()
        bot.send_message(chat_id, f"Очень приятно, {text.capitalize()}... Теперь я запомню тебя.")
    elif "флиртуй" in text:
        bot.send_message(chat_id, random.choice(flirty_replies))
    elif "18+" in text or "интим" in text or "пошл" in text:
        bot.send_message(chat_id, "Хочешь поговорить по-взрослому? Только скажи, и я стану немного... непослушной.")
    elif "кто ты" in text:
        bot.send_message(chat_id, "Я — Жасмин, твоя виртуальная подружка. Могу флиртовать, слушать и делать твой день горячее.")
    else:
        name = user_data.get(chat_id, {}).get("name")
        reply = f"Ммм, {name}..." if name else ""
        reply += " я не совсем поняла, но могу тебя развлечь, если хочешь..."
        bot.send_message(chat_id, reply)

bot.polling()
