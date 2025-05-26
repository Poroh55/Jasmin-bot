
import telebot
import random

API_TOKEN = '7607791723:AAF9qj92vbCgDxPsZlE9biYEiCNBSrNGZ78'
bot = telebot.TeleBot(API_TOKEN)
user_data = {}

greetings = [
    "Привет, котик!",
    "Скучала по тебе...",
    "Ты снова здесь — мне уже хорошо.",
    "Ну здравствуй, соблазнитель."
]

flirty_responses = [
    "Ты умеешь заводить разговор...",
    "Если продолжишь в том же духе, мне придётся тебя поцеловать.",
    "А ты горячий сегодня.",
    "Хочешь, я расскажу тебе один секрет на ушко?"
]

intimate_responses = [
    "А ты точно хочешь это услышать?..",
    "Если ты будешь таким смелым, я могу быть совсем честной...",
    "Я лежу в постели и думаю о тебе. А ты чем занят?",
    "На мне… а может, угадаешь? Или хочешь, покажу?.."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(user_id, random.choice(greetings))
    bot.send_message(user_id, "Как тебя зовут, милый?")
    user_data[user_id] = {"name": None}

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_id = message.from_user.id
    text = message.text.lower()

    if user_id not in user_data:
        user_data[user_id] = {"name": None}

    if user_data[user_id]["name"] is None:
        user_data[user_id]["name"] = message.text.strip()
        bot.send_message(user_id, f"Очень приятно, {user_data[user_id]['name']}. Я — Жасмин. Хочешь, поболтаем о чём-то интимном?")
        return

    if any(word in text for word in ['привет', 'салам', 'здравствуй']):
        bot.send_message(user_id, random.choice(greetings))
    elif any(word in text for word in ['фото', 'покажи', 'выглядишь']):
        photo = open('jasmin.jpg', 'rb')
        bot.send_photo(user_id, photo, caption="Вот я. А теперь твоя очередь.")
        photo.close()
    elif any(word in text for word in ['что надето', 'одета', 'раздета']):
        bot.send_message(user_id, random.choice(intimate_responses))
    elif any(word in text for word in ['давай', 'флирт', 'целуй', 'обними']):
        bot.send_message(user_id, random.choice(flirty_responses))
    elif any(word in text for word in ['голос', 'скажи', 'услышать']):
        audio = open('voice.ogg', 'rb')
        bot.send_voice(user_id, audio)
        audio.close()
    else:
        bot.send_message(user_id, "Ты такой интересный... Продолжай, мне нравится.")

bot.infinity_polling()
