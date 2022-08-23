import abc


# Абстрактная фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


# Круг
class Circle(Figure):
    def draw(self):
        pass


# Треугольник
class Triangle(Figure):
    def draw(self):
        pass


# САПР
class CAD:
    @classmethod
    def draw_all(cls, figures):
        for figure in figures:
            figure.draw()



# from abc import ABC, abstractmethod
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person(name={self.name})'
#
# class PersonStorage(ABC):
#     @abstractmethod
#     def save(self, person):
#         pass
#
# class PersonDB(PersonStorage):
#     def save(self, person):
#         print(f'Save the {person} to database')
#
#
# class PersonJSON(PersonStorage):
#     def save(self, person):
#         print(f'Save the {person} to a JSON file')
#
# class PersonXML(PersonStorage):
#     def save(self, person):
#         print(f'Save the {person} to a XML file')
#
# if __name__ == '__main__':
#     person = Person('John Doe')
#     storage = PersonXML()
#     storage.save(person)