from telebot import TeleBot

bot = TeleBot('7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(['start', 'help'])


def hello_world(message):
    global id 
    id = message.chat.id
    if message.text == '/start':
        bot.send_message(id, 'Hello,World')
    elif message.text == '/help':
        bot.send_message(id, 'do you need help?')

@bot.message_handler(content_types=['text'], regexp=r'\bMohammad\b')
def message_on_pattern_detected(message):
    bot.send_message(id, 'Nice to meet you')

bot.polling()
