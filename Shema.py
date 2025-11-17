import sqlite3

conn = sqlite3.connect('Connect_To_Bot.db')

cursor = conn.cursor()

cursor.execute(
    '''

    CREATE TABLE IF NOT EXISTS users(
    user_chatID INTEGER PRIMARY KEY,
    user_username TEXT,
    user_name TEXT,
    user_join_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )


    '''
)

conn.commit()
conn.close()