import sqlite3
from main import DB_FILE, TABLE_NAME

# CONNECTION CREATE
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL
# REGISTER VALUES ON THE TABLE
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES ("First Person", 75.5)'
)
print(sql)

# WITHOUT BIDING ONE OR MANY VALUES
cursor.execute(sql)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (?, ?)'
)
print(sql)

# WITH BIDING (?) ONE VALUE
cursor.execute(sql, ['Giovani', 107.1])

# WITH BIDING (?) MANY VALUES
cursor.executemany(
    sql, (
        ('Luanna', 145.6), ('Ezon', 137.3)
    )
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (:name, :weight)'
)
print(sql)

# WITH BIDING (:item) ONE VALUE
cursor.execute(
    sql, {'name': "Georgete", 'weight': 80.5}
)

# WITH BIDING (:item) MANY VALUES
cursor.executemany(
    sql, (
        {'name': 'Mel', 'weight': 4.5},
        {'name': 'Alex', 'weight': 7.8},
        {'name': 'Malu', 'weight': 10.9}
    )
)
connection.commit()

# CLOSE CURSOR AND CONNECTION
cursor.close()
connection.close()
