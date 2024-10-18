"""
method vs @classmethod vs @staticmethod

method - self, método de instância

@classmethod - cls, método de classe

@staticmethod - método estático (❌self, ❌cls)
"""


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, host, user, password):
        connection = cls(host)
        # connection.user = user
        # connection.password = password
        connection.set_user(user)
        connection.set_password(password)

        return connection

    @staticmethod
    def log(msg):
        print(f'LOG: {msg}')


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division('METHOD')

conn1 = Connection()
conn1.set_user('giovani.brasil')
conn1.set_password('senha123')

print(conn1.user)
print(conn1.password)

print_division('CLASS METHOD')

conn2 = Connection.create_with_auth('localhost', 'giovani.brasil', 'senha123')
print(conn2.user)
print(conn2.password)

print_division('STATIC METHOD')
Connection.log('Esse é um método estático')
