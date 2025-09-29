from telebot import TeleBot

bot = TeleBot('7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(['start', 'help'])


def hello_world(message):
    id = message.chat.id
    if message.text == '/start':
        bot.send_message(id, 'Welcome to our bot')
    elif message.text == '/help':
        bot.send_message(id, 'do you need help?')

@bot.message_handler(content_types=['text'], regexp=r'\bMohammad\b')
def message_on_pattern_detected(message):
    bot.send_message(message.chat.id, 'Mohammad,Its nice Name')

@bot.message_handler(func=lambda m: 'ali' in m.text.lower())
def func_handler(message):
    bot.send_message(message.chat.id, 'its beautifual name and related to 1st Imam of Sheee')

@bot.message_handler(chat_types=['private'], func=lambda m: 'info' in m.text.lower())
def info_handler(message):
    bot.send_message(message.chat.id, '1.option1\n2.option2\n3.option3\n4.option4')

# @bot.message_handler(func=lambda m: m.text.startswith('/'))
# def unknown_handler(message):
#     bot.send_message(message.chat.id, 'Unknown command, you can use /start or /help to get assistent')

@bot.message_handler(regexp=r'^\/')
def unknown_handler(message):
    bot.send_message(message.chat.id, 'Unknown command, you can use /start or /help to get assistent this handler work with regex arg')

# its should be to be last of all func 
@bot.message_handler(chat_types=['private'])
def private_handler(message):
    bot.send_message(message.chat.id, 'Its private Chat be Easy we Garanty that is secure be easy')

bot.polling()
