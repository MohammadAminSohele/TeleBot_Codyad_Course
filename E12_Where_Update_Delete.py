import sqlite3

conn = sqlite3.connect('shop.db')

cursor = conn.cursor()

cursor.execute(
    '''
    
    DELETE FROM users WHERE user_id=?

    ''',
    (4,)
)

# cursor.execute(
#     '''
    
#     UPDATE users SET user_family =? WHERE user_id=? 

#     ''',
#     ('Sajadi',4)
# )

# cursor.execute(
#     '''
    
#     SELECT user_id,user_family,user_age FROM users WHERE user_age < 30

#     '''
# )

rows = cursor.fetchall()
for r in rows:
    print(r)

conn.commit()
conn.close()