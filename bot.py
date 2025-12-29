from telebot import TeleBot,types
from dotenv import load_dotenv
"""  """
import os 
import query
"""  """
load_dotenv()
bot_token = os.getenv('bot_token')

bot = TeleBot(bot_token)

user_state = {} 
""" Start """
admins = ['6618292400']
@bot.message_handler(['start'])
def start_cdm(message):
    chat_id = message.chat.id
    user_id = str(message.from_user.id)
    user_name = message.from_user.username
    query.insert_user(user_id,user_name)
    
    MarkUp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    MarkUp.row('Available Servises','My Appointments')

    if user_id in admins:
        MarkUp.row('Add service')

    bot.send_message(chat_id,f'Welcome to our bot {user_name} \n please choose an option',reply_markup=MarkUp)
""" Service """
@bot.message_handler(func=lambda message : message.text=='Available Servises')
def choose_service(message):
    services = query.get_services()
    markup = types.InlineKeyboardMarkup()
    for sid, name in services:
        markup.add(types.InlineKeyboardButton(name, callback_data=f"service_{sid}"))
    bot.send_message(message.chat.id, "Choose a service:", reply_markup=markup)
""" Date """
@bot.callback_query_handler(func=lambda call:call.data.startswith('service_'))
def choose_date(call):
    service_id = int(call.data.split("_")[1])    
    user_state[call.from_user.id] = {'service_id':service_id}
    dates = query.get_dates(service_id)
    markup = types.InlineKeyboardMarkup()
    for date in dates:
        markup.add(types.InlineKeyboardButton(date,callback_data=f"date_{date}"))
    bot.send_message(call.message.chat.id,'choose your date',reply_markup=markup)
"""  """
@bot.callback_query_handler(func=lambda call:call.data.startswith('date_'))
def choose_date(call):
    date = call.data.split('_')[1]
    user_state[call.from_user.id]['date'] = date
    service_id = user_state[call.from_user.id]['service_id']
    times = query.get_times(service_id,date)
    markup = types.InlineKeyboardMarkup()
    for slot_id,time in times:
        markup.add(types.InlineKeyboardButton(time,callback_data=f"time_{slot_id}"))
    bot.send_message(call.message.chat.id,'choose your time',reply_markup=markup)
""" confirm """
@bot.callback_query_handler(func=lambda call:call.data.startswith('time_'))
def confirm(call):
    user_id = str(call.from_user.id)
    slot_id = int(call.data.split('_')[1])
    query.book_appointments(user_id,slot_id)
    query.update_slots_status(slot_id)
    bot.send_message(call.message.chat.id,'Appoinments books and time reserved')
    user_state.pop(call.from_user.id,None)
"""  """
bot.polling()