# -*- coding: cp1251 -*-
from pprint import pprint
def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2)) > 0.6
class Person:
    "Класс создания переменной типа dic"
    def __init__(self, name=None, age=None, height=None, address=None): # метод конструктор
        self.name, self.age, self.height, self.address = name, age, height, address
        # self.key = (name, address)
    def __repr__(self): # метод вывода / возвращает представление, которое максимально похожа на Питоновский код
        return "Person('%s',%s,%s,'%s')" % (self.name, self.age, self.height, self.address)
        # return f"Person('{self.name}',{self.age},{self.height},'{self.address}')"
    def __eq__(self, obj): # метод сравнения персоны с чем-либо
        return (obj.name == None or self.name == None or compare(obj.name, self.name)) \
           and (obj.age == None or self.age == None or abs(obj.age - self.age) <= 2) \
           and (obj.height == None or self.height == None or abs(obj.height - self.height) <= 10) \
           and (obj.address == None or self.address == None or compare(obj.address, self.address))

to_search = Person("Helenaa", 40, 157, "Мильчакова, 17, 100")
to_search_list = [to_search]

print(to_search_list)
# name = Person("name","age","height","address")
andrey = Person("Andrey", 36, 180, "Пушкина, 12, 115")
alex = Person("Alexsander", 40, 170, "Ленского, 10, 5")
olga = Person("Olga", 30, 165, "Ленина, 1, 1")
helena = Person("Helena", 42, 167, "Мильчакова, 17, 95")

people = [
    andrey,
    alex,
    olga,
    helena,
]
pprint(people)
from itertools import product
for p1, p2 in product(people, to_search_list):
    print(p1, p2, p1 == p2)

# for username, userinfo in people.items():
#     print(f"username: {username}")
#     print(f"userinfo: {userinfo}")

# print(people.get("name"))
# print(people.get("имя", "Что это?"))
# print(people.setdefault(2)) # нетолько возвращает значение  ключа, но и создаёт новую пару
# people_copy = people.copy() # копия словаря
# print(people_copy)
# people.update({helena.key: helena}) # новые пары в словарь
# people.update({olga.key: helena}) # также если ключ есть, то перезапишет значение
# print(people.pop(olga.key)) # удаляет ключ и возвращает значение
# print(people.pop(helena.key, "No key!")) # если нет ключа, то возвращает переданное дефолтное значение
# print(people.popitem()) # удаляет и возвращает случайную пару ключ-значение
# print(people.keys()) возвращает список ключей словаря
# print(people.values()) возвращает список значений
# print(people.items()) возвращает кортежа с парами ключ-значение
# people.clear() # очищает словарь
# pprint(people)

# if __name__ == "__main__":

    # getattr(odj, name,[, default]) -
    # hasattr(odj, name) - проверяет на наличие атрибута name в obj
    # setattr(odj, name, value) - зкадает значение атрибута (если атрибут не существует, то он создается)
    # delattr(obj, name) - удаляет атрибут с именем name
    # class.__doc__ - содержит строку с описанием класса
    # *.__dict__  - содержит набор атрибутов экзэмпляра класса