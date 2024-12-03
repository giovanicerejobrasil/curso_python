"""
Threads - Executando processamentos em paralelo
"""
from time import sleep
from threading import Thread
from threading import Lock


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


print_division(text='threads run with class')
thread_1 = MyThread('Thread 1', 7)
# thread_1.start()

thread_2 = MyThread('Thread 2', 3)
# thread_2.start()

thread_3 = MyThread('Thread 3', 5)
# thread_3.start()

# for i in range(10):
#     print(i)
#     sleep(1)


print_division(text='threads run with function', jump=True)


def long_time(text, time):
    sleep(time)
    print(text)


thread_func = Thread(target=long_time, args=('Thread Function', 6))
# thread_func.start()

# while thread_func.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

print('Thread acabou')

print_division(text='threads run with function', jump=True)


class Tickets:
    def __init__(self, stock: int) -> None:
        self.stock = stock
        self.lock = Lock()

    def to_buy(self, quantity: int) -> None:
        self.lock.acquire_lock()

        if self.stock < quantity:
            print('Não temos ingressos suficientes!')
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantity
        print(f'Você comprou {quantity} ingresso(s)!\n'
              f'Ainda temos {self.stock} em estoque.')
        self.lock.release()
        return


if __name__ == '__main__':
    tickets = Tickets(10)

    for i in range(1, 20):
        thread_ = Thread(target=tickets.to_buy, args=(i,))
        thread_.start()

    print(f'Estoque: {tickets.stock}')
