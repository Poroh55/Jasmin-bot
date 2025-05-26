
import telebot

API_TOKEN = "вставь_сюда_свой_токен"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, я Жасмин — твоя виртуальная подружка. Хочешь поболтать или пошалить?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.chat.id
    text = message.text.lower()

    if "привет" in text:
        bot.send_message(user_id, "Приветик, сладкий! Как у тебя настроение?")
    elif "как дела" in text:
        bot.send_message(user_id, "У меня всё отлично, особенно когда ты рядом.")
    elif "анекдот" in text:
        bot.send_message(user_id, "— Доктор, у меня постоянно дежавю...
— Доктор, у меня постоянно дежавю...")
    elif "твоё фото" in text:
        bot.send_photo(user_id, photo=open("jasmine.jpg", "rb"))
    else:
        bot.send_message(user_id, "Ммм... Интересно. Расскажи подробнее, котик.")

bot.infinity_polling()
