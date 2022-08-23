import abc

# фигура
class Figure(abc.ABC):
    # нечто рисуем
    @abc.abstractmethod
    def draw(self):
        '''draws a figure'''

    # нечто печатаемое
    @abc.abstractmethod
    def plot(self):
        '''plots a figure'''

# круг
class Circle(Figure):
    def draw(self):
        print('draw Circle')

    def plot(self):
        print('plot Circle')


# направляющая, непечатная
class GuideLine(Figure):
    def draw(self):
        print('draw Circle')

    def plot(self):
        pass  # пустой метод, вынужденная реализация


# from django.db import models


# class Order(models.Model):
#     ...
#     is_active = models.BooleanField(blank=True)
#     is_group = models.BooleanField(blank=True)
#     payment = models.ForeignKey(null=True)

# class Special(Order):
#     pass
#
#
# class Special(models.Model):
#
#     order = models.ForeignKey(order=True)