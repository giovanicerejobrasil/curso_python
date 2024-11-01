"""
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retorno iguais

SO"L"ID
Princípio da substituição de liskov

Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.

Sobrecarga de métodos (overload)  🐍 = ❌
Sobreposição de métodos (override) 🐍 = ✅
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print(f'E-mail: enviando -> {self.message}')
        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print(f'SMS: enviando -> {self.message}')
        return False


def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


sms_notification = SMSNotification('Testando notificação via SMS')
email_notification = EmailNotification('Testando notificação via E-MAIL')

notify(sms_notification)
print()
notify(email_notification)
