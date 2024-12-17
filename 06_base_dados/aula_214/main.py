"""
PyMySQL - um cliente MySQL feito em Python Puro
Doc: https://pymysql.readthedocs.io/en/latest/
Pypy: https://pypi.org/project/pymysql/
GitHub: https://github.com/PyMySQL/PyMySQL
"""
import os
import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    # cursorclass=pymysql.cursors.Cursor,
    cursorclass=pymysql.cursors.DictCursor,
    # cursorclass=pymysql.cursors.SSCursor,
    # cursorclass=pymysql.cursors.SSDictCursor,
)

# SQL
with connection:
    with connection.cursor() as cursor:
        # CREATE TABLE customers
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )

        # TRUNCATE
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

    connection.commit()

    with connection.cursor() as cursor:
        # INSERT INTO without biding
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("Giovani", 27)'
        )

        cursor.execute(sql)

        # INSERT INTO with biding (%s)
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES (%s, %s)'
        )
        data = ('Luanna', 24)

        cursor.execute(sql, data)

        # INSERT INTO with biding (%(item)s)
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES (%(name)s, %(age)s)'
        )
        data2 = {
            "name": "Mel",
            "age": 11
        }

        cursor.execute(sql, data2)

        # INSERT INTO with biding (%(item)s) MANY ITEMS
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES (%(name)s, %(age)s)'
        )
        data3 = (
            {"name": "Alex", "age": 9},
            {"name": "Malu", "age": 3},
            {"name": "Georgete", "age": 55},
        )

        cursor.executemany(sql, data3)

        # INSERT INTO with biding (%s) MANY ITEMS
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES (%s, %s)'
        )
        data4 = (
            ("Maria", 32),
            ("João", 74),
        )

        cursor.executemany(sql, data4)

    connection.commit()

    with connection.cursor() as cursor:
        # SELECT without biding
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)
        print(cursor.mogrify(sql))

        response1 = cursor.fetchall()
        for _id, name, age in response1:
            print(_id, name, age)

        print()

        # SELECT with biding (%s)
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = %s '
        )
        data5 = 3

        cursor.execute(sql, data5)
        print(cursor.mogrify(sql, data5))

        response2 = cursor.fetchone()
        print(response2)

        print()

        # SELECT with biding (%(item)s)
        # try:
        #     lowest_id = int(input('Digite o menor id: '))
        #     biggest_id = int(input('Digite o maior id: '))
        # except Exception:
        #     lowest_id = 1
        #     biggest_id = 5
        lowest_id = 1
        biggest_id = 5
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %(lowest_id)s AND %(biggest_id)s '
        )
        data6 = {"lowest_id": lowest_id, "biggest_id": biggest_id}

        cursor.execute(sql, data6)
        print(cursor.mogrify(sql, data6))

        response3 = cursor.fetchall()
        for _id, name, age in response3:
            print(_id, name, age)

    connection.commit()

    print()

    with connection.cursor() as cursor:
        # DELETE
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %(id)s'
        )
        data7 = {
            "id": 7
        }

        cursor.execute(sql, data7)
        print(cursor.mogrify(sql, data7))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)
        print(cursor.mogrify(sql))

        response4 = cursor.fetchall()
        for _id, name, age in response4:
            print(_id, name, age)

        print()

    connection.commit()

    with connection.cursor() as cursor:
        # UPDATE
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%(name)s, age=%(age)s '
            'WHERE id = %(id)s'
        )
        data8 = {
            "id": 8,
            "name": "Carlos",
            "age": 33
        }

        cursor.execute(sql, data8)
        print(cursor.mogrify(sql, data8))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)
        print(cursor.mogrify(sql))

        response5 = cursor.fetchall()
        for _id, name, age in response5:
            print(_id, name, age)

        print()

    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)
        print(cursor.mogrify(sql))

        response6 = cursor.fetchall()
        print('CURSOR')
        for _id, name, age in response6:
            print(_id, name, age)

        print()

        print('DICTCURSOR')
        for items in response6:
            print(items)

        print('\nFOR 1 (-2 RELATIVE)')
        # cursor.scroll(-2, 'relative')
        for items in cursor.fetchall():
            print(items)

        print('\nFOR 2 (O ABSOLUTE)')
        # cursor.scroll(0, 'absolute')
        for items in cursor.fetchall():
            print(items)

        print()

        cursor.execute(sql)
        print('SSDICTCURSOR')
        for items in cursor.fetchall():
            print(items)

        # cursor.execute(sql)
        # print('\nFOR 1')
        # for items in cursor.fetchall_unbuffered():
        #     print(items)
        #     if items['id'] >= 4:
        #         break

        # print('\nFOR 2')
        # for items in cursor.fetchall_unbuffered():
        #     print(items)

        print()

    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        resultFromSelect = cursor.execute(sql)
        print(cursor.mogrify(sql))

        response7 = cursor.fetchall()
        for items in response7:
            print(items)

        print()

        print('resultFromSelect', resultFromSelect)
        print('len(response7)', len(response7))
        print('rowcount', cursor.rowcount)
        print('rownumber', cursor.rownumber)

        print()

        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("Mariana", 42), '
            '("Luciano", 22)'
        )

        cursor.execute(sql)
        print(cursor.mogrify(sql))

        print('lastrowid', cursor.lastrowid)

        print()

        sql = (
            f'SELECT id FROM {TABLE_NAME} '
            'ORDER BY id DESC '
            'LIMIT 1'
        )

        resultFromSelect = cursor.execute(sql)
        print(cursor.mogrify(sql))

        response8 = cursor.fetchone()

        if response8 is not None:
            print('Last id with SELECT', response8['id'])

    connection.commit()
