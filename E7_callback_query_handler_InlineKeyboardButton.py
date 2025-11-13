from telebot import TeleBot, types

bot = TeleBot('7951234207:AAE1keTBO3b2E6dqWAwWaFVUv3lIV4IE_9Y')

@bot.message_handler(['start'])
def start_cmd(message):
    id = message.chat.id
    ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn_AboutUs = types.KeyboardButton('AboutUs')
    btn_ProductsCatagory = types.KeyboardButton('ProductsCatagory')
    ReplyKeyboardMarkup.add(btn_AboutUs,btn_ProductsCatagory)
    bot.send_message(id,'Welcome to our bot please enter on Provided ReplyKeyboard',reply_markup=ReplyKeyboardMarkup)

@bot.message_handler(func=lambda m : True)
def handler_reply_keyboard(message):
    id = message.chat.id
    if message.text == 'AboutUs':
        bot.send_message(id,'We are best Tech Online shop')
    elif message.text == 'ProductsCatagory':
        InlineKeybordMarkup = types.InlineKeyboardMarkup(row_width=2)
        btn_phone = types.InlineKeyboardButton('Phone',callback_data='Phone')
        btn_laptop = types.InlineKeyboardButton('Laptop',callback_data='Laptop')
        InlineKeybordMarkup.add(btn_phone,btn_laptop)
        bot.send_message(id,'Choose a Catagory from Provided Catagory',reply_markup=InlineKeybordMarkup)
    else:
        bot.send_message(id,'Its Unknown Cmd plese Choose from provided Reply Button')
@bot.callback_query_handler(func=lambda cb : True)
def handler_CallBack(CallBack):
    if CallBack.data == 'Phone':
        bot.answer_callback_query(CallBack.id,'you press on Phone Catagory')
    elif CallBack.data == 'Laptop':
        bot.answer_callback_query(CallBack.id,'you press on Laptop Catagory')

bot.polling()