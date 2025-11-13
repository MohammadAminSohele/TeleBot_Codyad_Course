from telebot import TeleBot,types

bot = TeleBot(token='7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(commands=['start'])
def start(m):
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn_info = types.KeyboardButton('Info')
    btn_help = types.KeyboardButton('Help')
    btn_readme = types.KeyboardButton('Readme')
    keybord.add(btn_info,btn_help,btn_readme)
    bot.send_message(m.chat.id,'Welcome to our Bot',reply_markup=keybord)

readme_text = 'readme'
help_text = 'help'
info_text = 'info'

@bot.message_handler(func=lambda m : True)
def handle_message(m):
    id = m.chat.id
    if m.text == 'Info':
        bot.send_message(id,info_text)
    elif m.text == 'Help':
        bot.send_message(id,help_text)
    elif m.text == 'Readme':
        bot.send_message(id,readme_text)
    else:
        bot.send_message(id,'Unknown command! please use buttons provided')

bot.polling()