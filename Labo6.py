# -*- coding: cp1251 -*-
from pprint import pprint
class Person:
    "Класс создания БД"
    def __init__(self, name, age, height, address):
        self.name, self.age, self.height, self.address = name, age, height, address
        self.key = (name, address)
    def __repr__(self):
        return "Person('%s',%s,%s,'%s')" % (self.name, self.age, self.height, self.address)

# def people_bd():
# name = Person("name","age","height","address")
andrey = Person("Andrey", 36, 180, "Пушкина, 12, 115")
alex = Person("Alexsander", 40, 170, "Ленского, 10, 5")
olga = Person("Olga", 30, 165, "Ленина, 1, 1")
people = {
    andrey.key: andrey,
    alex.key: alex,
    olga.key: olga,
}
    # return people, people[olga.key]
pprint(people)
pprint(people[olga.key])
# a = people[2]


# if __name__ == "__main__":

    # getattr(odj, name,[, default]) -
    # hasattr(odj, name) - проверяет на наличие атрибута name в obj
    # setattr(odj, name, value) - зкадает значение атрибута (если атрибут не существует, то он создается)
    # delattr(obj, name) - удаляет атрибут с именем name
    # class.__doc__ - содержит строку с описанием класса
    # *.__dict__  - содержит набор атрибутов экзэмпляра класса