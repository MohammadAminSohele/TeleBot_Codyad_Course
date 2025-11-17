import sqlite3

def ConnectUser_TO_DB():
    conn = sqlite3.connect('Connect_To_Bot.db')
    return conn

def CreateUser(user_chatID,user_username,user_name):
    conn = ConnectUser_TO_DB()
    cursor = conn.cursor()

    cursor.execute(
    '''

    INSERT OR IGNORE INTO users (user_chatID,user_username,user_name) VALUES (?,?,?)

    ''',
    (user_chatID,user_username,user_name)
    )

    conn.commit()
    conn.close()

def SelectUser(ChatID):
    conn = ConnectUser_TO_DB()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT user_username,user_name,user_join_date FROM users WHERE user_chatID=?
        ''',
        (ChatID,)
    )
    Row = cursor.fetchone()

    conn.commit()
    conn.close()
    
    return Row
