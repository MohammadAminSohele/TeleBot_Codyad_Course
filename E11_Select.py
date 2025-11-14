import sqlite3

conn = sqlite3.connect('shop.db')

cursor = conn.cursor()

cursor.execute(
    '''

    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT ,
    user_family TEXT,
    user_age INTEGER,
    user_date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
    )

    '''
)

cursor.execute(
    '''
    INSERT INTO users(user_name,user_family,user_age) VALUES (?,?,?)
    ''',
    ('Ali','Alimi',40)
)
cursor.execute(
    '''
    INSERT INTO users(user_name,user_family,user_age) VALUES (?,?,?)
    ''',
    ('Hassan','Hassani',20)
)
cursor.execute(
    '''
    INSERT INTO users(user_name,user_family,user_age) VALUES (?,?,?)
    ''',
    ('Hossen','Hosseni',50)
)
cursor.execute(
    '''
    INSERT INTO users(user_name,user_family,user_age) VALUES (?,?,?)
    ''',
    ('Sajad','Babayee',30)
)

cursor.execute(
    '''

    SELECT user_family,user_age FROM users

    '''
)

row = cursor.fetchall()
for r in row:
    print(r)

conn.commit()
conn.close()