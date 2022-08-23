import abc


# фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        '''draws a figure'''


# нечто печатаемое
class Plottable(abc.ABC):
    @abc.abstractmethod
    def plot(self):
        '''plots a figure'''


# круг, печатаемый - наследуемся от двух классов
class Circle(Figure, Plottable):
    def draw(self):
        print('draw Circle')

    def plot(self):
        print('plot Circle')


# направляющая, просто фигура, непечатная
class GuideLine(Figure):
    def draw(self):
        print('draw Circle')


class Movable(abc.ABC):
    @abc.abstractmethod
    def go(self):
        pass

#################################################################
# class Flyable(abc.ABC):
#
#     @abc.abstractmethod
#     def fly(self):
#         pass
#
#
# class Aircraft(Flyable,Movable):
#     def go(self):
#         print("Taxiing")
#
#     def fly(self):
#         print("Flying")
#
# class Car(Movable):
#     def go(self):
#         print("Going")
#
# Aircraft()
# Car()