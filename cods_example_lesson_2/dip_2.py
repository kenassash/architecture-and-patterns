import abc


# абстракция товара
class ItemInterface(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        '''returns the price'''


# превосходный  товар наследуем от абстрактного товара
class PerfectItem(ItemInterface):
    def get_price(self):
        pass


class SuperItem(ItemInterface):
    def get_price(self):
        pass


class Order:
    ...

    # добавить абстрактный товар, детали реализации товара не интересуют
    def add(self, item: ItemInterface):
        self.total += item.get_price()



# from abc import ABC
#
#
# class CurrencyConverter(ABC):
#     @abc.abstractmethod
#     def convert(self, from_currency, to_currency, amount) -> float:
#         pass
#
# class FXConverter(CurrencyConverter):
#     def convert(self, from_currency, to_currency, amount) -> float:
#         print('Converting currency using FX API')
#         print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
#         return amount * 2
#
# class AlphaConverter(CurrencyConverter):
#     def convert(self, from_currency, to_currency, amount) -> float:
#         print('Converting currency using Alpha API')
#         print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
#         return amount * 1.2
#
# class App:
#     def __init__(self, converter: CurrencyConverter):
#         self.converter = converter
#
#     def start(self):
#         self.converter.convert('EUR', 'USD', 100)
#
# if __name__ == '__main__':
#     converter = FXConverter()
#     converterAlpha = AlphaConverter()
#     app = App(converter)
#     app.start()
#
#     app = App(converterAlpha)
#     app.start()