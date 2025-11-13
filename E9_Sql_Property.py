import sqlite3 

conn = sqlite3.connect('Shop.db')

cursor = conn.cursor()

cursor.execute(
    '''

    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT ,
    user_family TEXT , 
    user_age INTEGER , 
    user_join_date DATETIME DEFAULT CURRENT_TIMESTAMP 
    )

    '''
)

cursor.execute(
    '''

    INSERT INTO USERS (user_name,user_family,user_age) VALUES (?,?,?)

    ''',
    ('ali','alimi',30)
)

conn.commit()
conn.close()