"""
SQLite Tutorial:
https://www.techonthenet.com/sqlite/index.php

SQLite Doc:
https://www.sqlite.org/doclist.html
"""
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

if __name__ == '__main__':
    # CONNECTION CREATE
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # SQL

    # CRUD - CREAD  READ   UPDATE DELETE
    # SQL -  INSERT SELECT UPDATE DELETE

    # WARNING: MAKING DELETE WITHOUT WHERE
    cursor.execute(
        f'DELETE FROM {TABLE_NAME}'
    )

    # DELETE WITH WHERE
    cursor.execute(
        f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
    )
    connection.commit()

    # CREATE TABLE
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
        ')'
    )
    connection.commit()

    # CLOSE CURSOR AND CONNECTION
    cursor.close()
    connection.close()
