import telebot
from telebot import types

TOKEN = '7607791723:AAF9qj92vbCgDxPsZlE9biYEiCNBSrNGZ78'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Просто поговорим")
    item2 = types.KeyboardButton("Лёгкий флирт")
    item3 = types.KeyboardButton("Сделай мне комплимент")
    item4 = types.KeyboardButton("Удиви меня")
    markup.add(item1, item2, item3, item4)

    bot.send_message(
        message.chat.id,
        "Приветик… Я — Жасмин. Хочешь просто поболтать, немного пофлиртовать или, может, хочешь, чтобы я тебя удивила?",
        reply_markup=markup
    )

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == "Просто поговорим":
        bot.send_message(message.chat.id, "О чём хочешь поболтать? У меня полно мыслей, но я слушаю тебя.")
    elif message.text == "Лёгкий флирт":
        bot.send_message(message.chat.id, "Ты знаешь, у тебя такой магнетизм... даже через экран чувствуется. Хочешь продолжим?")
    elif message.text == "Сделай мне комплимент":
        bot.send_message(message.chat.id, "Ты точно хочешь? Я могу заставить тебя покраснеть... Ладно: ты — причина, по которой даже скучный день кажется ярче.")
    elif message.text == "Удиви меня":
        bot.send_message(message.chat.id, "Знаешь, я умею угадывать, кто смотрит на экран с улыбкой... и, кажется, это ты.")
    else:
        bot.send_message(message.chat.id, "Я пока учусь разговаривать, но с тобой — это самое приятное обучение.")

bot.polling(none_stop=True)