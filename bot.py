from telebot import TeleBot

bot = TeleBot(token='7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(commands=['start','help'])
def main(message):
    id = message.chat.id
    if message.text == '/start':
        bot.send_message(id,'welcome to our bot')
    elif message.text == '/help':
        bot.send_message(id,'do you need help?')
@bot.message_handler(content_types=['text'],regexp=r'\bMohammad\b')
def mohammad_reaction(message):
    id = message.chat.id
    bot.send_message(id,'nice to meet you Mohammad')

@bot.message_handler(func=lambda m : 'ali' in m.text.lower())
def ali_reaction(message):
    bot.send_message(message.chat.id,'nice to meet you Ali')

@bot.message_handler(commands=['info'],chat_types=['private'])
def info_command(message):
    bot.send_message(message.chat.id,'this is our command \n1./start\n2./help')

@bot.message_handler(regexp=r'^\/')
def unknown_command(message):
    bot.send_message(message.chat.id,'its unknown command you can use /info can tell our command')

@bot.message_handler(chat_types=['private'])
def Echo_message(message):
    bot.send_message(message.chat.id,message.text)

bot.polling()