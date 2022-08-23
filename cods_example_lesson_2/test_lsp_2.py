import unittest


# Прямоугольник, неизменяемый
class RectangleImmutable:
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        super().__setattr__('_width', width)
        super().__setattr__('_height', height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        raise AttributeError('attributes are immutable')

    @property
    def area(self):
        return self._width * self._height


# Квадрат, неизменяемай
class SquareImmutable(RectangleImmutable):
    def __init__(self, size):
        super().__init__(size, size)


class SquareTest(unittest.TestCase):
    def test_area(self):
        rectangle = SquareImmutable(4)
        # тест пройден
        self.assertEqual(rectangle.area, 16)

        rectangle1 = RectangleImmutable(4,4)

        rectangle1.width = 5
        # пытаемся изменить атрибуты
        # with self.assertRaises(AttributeError):
        #     rectangle.width = 5
        #
        # with self.assertRaises(AttributeError):
        #     rectangle.height = 4
        #
        # self.assertEqual(rectangle.area, 16)


from abc import ABC, abstractmethod


# class Notification(ABC):
#     @abstractmethod
#     def notify(self, message, email):
#         pass
#
#
# class Email(Notification):
#     def notify(self, message, email):
#         print(f'Send {message} to {email}')
#
#
# class SMS(Notification):
#     def notify(self, message, phone):
#         print(f'Send {message} to {phone}')
#
#
# if __name__ == '__main__':
#     notification = SMS()
#     notification.notify('Hello', 'john@test.com')


from abc import ABC, abstractmethod


class Notice(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notice):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notice):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Data:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NoticeManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Data('Николай Нагорный', 'test@mail.ru', '+7-900-000-00-00')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NoticeManager(sms_notification)
    notification_manager.send('Привет Николай')

    notification_manager.notification = email_notification
    notification_manager.send('Здорова Николай')