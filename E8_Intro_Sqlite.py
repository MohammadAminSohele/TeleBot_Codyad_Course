import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER,
    user_name TEXT,
    user_age INTEGER
    )
    '''
)

cursor.execute(
    '''
    INSERT INTO users(user_id,user_name,user_age) values(?,?,?)
    ''',
    (2,'Ali',22)
)

conn.commit()
conn.close()