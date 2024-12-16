import sqlite3
from main import DB_FILE, TABLE_NAME

# CONNECTION CREATE
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL
# FETCHALL
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()
# FETCHONE
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = 3'
)

_id, name, weight = cursor.fetchone()
print(_id, name, weight)

# CLOSE CURSOR AND CONNECTION
cursor.close()
connection.close()
