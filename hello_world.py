from telebot import TeleBot

bot = TeleBot('7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(['start'])


def hello_world(message):
    bot.send_message(message.chat.id, 'Hello,World')
    print(message)

bot.polling()
