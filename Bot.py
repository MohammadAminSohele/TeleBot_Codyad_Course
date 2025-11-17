from telebot import TeleBot 
from Database import CreateUser,SelectUser

bot = TeleBot('7951234207:AAH9eMY_2l2jEoOlL-7XJYxBir11hXDacqY')

@bot.message_handler(['start'])
def start_cmd(message):
    ChatId = message.chat.id
    username = message.from_user.username
    name = message.from_user.first_name
    CreateUser(ChatId,username,name)
    bot.send_message(ChatId,'Welcome to our bot')

@bot.message_handler(['Report'])
def ReportUserInfo_To_User(message):
    ChatId = message.chat.id
    User = SelectUser(ChatId)
    bot.send_message(ChatId,f'Username:{User[0]}\nFirstName:{User[1]}\nJoinDate:{User[2]}')

bot.polling()
