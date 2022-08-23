# bad
class Order:
    def get_items(self):
        pass

    def get_total(self):
        pass

    def validate(self):
        pass

    def save(self):
        pass

    def load(self):
        pass


# good
class Order:
    def get_items(self):
        pass

    def get_total(self):
        pass

    def validate(self):
        pass


class OrderRepository:
    def save(self):
        pass

    def load(self):
        pass




# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person(name={self.name})'
#
#     @classmethod
#     def save(cls,person):
#         print(f'Save the {person} to the database')
#
#
# if __name__ == '__main__':
#     p = Person('John Doe')
#     Person.save(p)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person(name={self.name})'
#
#
# class PersonDB:
#     def save(self, person):
#         print(f'Save the {person} to the database')
#
#
# if __name__ == '__main__':
#     p = Person('John Doe')
#
#     db = PersonDB()
#     db.save(p)