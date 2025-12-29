import sqlite3
from dotenv import load_dotenv
import os 

load_dotenv()
bot_db = os.getenv('bot_db')

def connect():
    conn = sqlite3.connect(bot_db)
    cursor = conn.cursor()
    return conn , cursor

def insert_user(user_id, username):
    conn ,cursor = connect()

    cursor.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))

    conn.commit()
    conn.close()

def get_services():
    conn, cursor = connect()

    cursor.execute("SELECT service_id, name FROM services")
    services = cursor.fetchall()

    conn.close()
    return services

def get_dates(service_id):
    conn, cursor  = connect()

    cursor.execute("SELECT DISTINCT date FROM slots WHERE service_id = ?", (service_id,))
    dates = [row[0] for row in cursor.fetchall()]

    conn.close()
    return dates

def get_times(service_id, date):
    conn, cursor  = connect()

    cursor.execute("""
        SELECT slot_id, time FROM slots
        WHERE service_id = ? AND date = ? AND status = 'available'
        ORDER BY time ASC
    """, (service_id, date))
    times = cursor.fetchall()

    conn.close()
    return times

def insert_service(name, admin_id):
    conn, cursor  = connect()
    cursor.execute("INSERT INTO services (name, admin_id) VALUES (?, ?)", (name, admin_id))
    service_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    return service_id

def insert_slots(slot_id,date,times):
    conn,cursor = connect()
    for time in times:
        cursor.execute(
            'INSERT INTO slots(slot_id,date,time,status) VALUES(?,?,?,?)',(slot_id,date,time,'available')
        )

    conn.commit()
    conn.close()

""" book appointments """
def book_appointments(user_id,slot_id):
    conn,cursor = connect()

    cursor.execute("INSERT INTO appointments (user_id,slot_id) VALUES(?,?)",(user_id,slot_id))

    conn.commit()
    conn.close()

""" Update slot status """
def update_slots_status(slot_id):
    conn,cursor = connect()

    cursor.execute("UPDATE slots SET status = 'booked' WHERE slot_id=? ",(slot_id,))

    conn.commit()
    conn.close()