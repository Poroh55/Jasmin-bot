
import telebot
from telebot import types

API_TOKEN = '7607791723:AAF9qj92vbCgDxPsZlE9biYEiCNBSrNGZ78'

bot = telebot.TeleBot(API_TOKEN)

user_names = {}

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Как тебя зовут?", "Пошалим", "Расскажи анекдот", "Покажи фото", "Спроси меня что-нибудь")
    bot.send_message(user_id, "Привет, я Жасмин. Хочешь познакомиться поближе?", reply_markup=markup)

# Ответы на команды и кнопки
@bot.message_handler(func=lambda message: True)
def reply(message):
    user_id = message.from_user.id
    text = message.text.lower()

    if "как тебя зовут" in text:
        bot.send_message(user_id, "Я Жасмин. А тебя как зовут?")
    elif "меня зовут" in text:
        name = message.text.split("меня зовут")[-1].strip().capitalize()
        user_names[user_id] = name
        bot.send_message(user_id, f"Очень приятно, {name}. Хочешь, пошалим?")
    elif "спроси меня" in text:
        bot.send_message(user_id, "Что бы ты сделал, если бы я оказалась рядом сейчас?")
    elif "пошалим" in text:
        bot.send_message(user_id, "Ты точно готов к этому?.. Я люблю, когда нежно, но с огоньком.")
    elif "анекдот" in text:
        bot.send_message(user_id, "— Доктор, у меня постоянно дежавю...
— Я это уже слышал.")
    elif "фото" in text:
        with open("jasmine.jpg", "rb") as photo:
            bot.send_photo(user_id, photo, caption="Вот как я могу выглядеть, если ты мечтал...")
    else:
        name = user_names.get(user_id, "милый")
        responses = [
            f"Ты знаешь, {name}, я люблю, когда меня вызывают часто...",
            "Спроси меня что-нибудь пикантное, я не укушу (пока)",
            "Ты сегодня особенно возбуждающий...",
            "Знаешь, у меня тоже есть фантазии. Хочешь узнать какие?",
            "Я люблю, когда меня настраивают на волну удовольствия..."
        ]
        import random
        bot.send_message(user_id, random.choice(responses))

print("Бот запущен")
bot.polling()
