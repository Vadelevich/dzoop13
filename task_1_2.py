class Item:

    def __init__(self, name, price, quantity=0):
        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __check (self,name, price,quantity):
        if not isinstance(name,str) : raise TypeError('Название товара должно быть строкой.')
        if not isinstance(price,(int, float)) : raise TypeError ('Цена товара должна быть числом.')
        if not isinstance(quantity, int) : raise TypeError ('Количество товара должно быть целым числом.')

    def __str__(self):
        return f'{self.__class__.__name__} ({self.name}, {self.price}, {self.quantity})'


class Phone(Item):
    def __init__(self,name, price, quantity,broken_phones):
        super().__init__(name, price, quantity,)
        self.__check_broken_phones(broken_phones)
        self.broken_phones = broken_phones

    def __check_broken_phones(self,broken_phones):
        if  not isinstance(broken_phones,int): raise TypeError ('  Количество неисправных телефонов на складе должно быть целым числом.')

phone1 = Phone("iPhone 10", 500, 5, 1)
print(Item('phone', 18000, 5))
print(phone1.__dict__)
# Item(phone, 18000, 5)
# print(Item(18000, 'phone', 5))
# TypeError: Название товара должно быть строкой.
# print(Item('phone', '18000', 5))
# TypeError: Цена товара должна быть числом.
# print(Item('phone', 18000, 5.5))
# TypeError: Количество товара должно быть целым числом.
