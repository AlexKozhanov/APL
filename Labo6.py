# -*- coding: cp1251 -*-
from pprint import pprint
def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2)) > 0.6
class Person:
    "����� �������� ���������� ���� dic"
    def __init__(self, name=None, age=None, height=None, address=None): # ����� �����������
        self.name, self.age, self.height, self.address = name, age, height, address
        # self.key = (name, address)
    def __repr__(self): # ����� ������ / ���������� �������������, ������� ����������� ������ �� ����������� ���
        return "Person('%s',%s,%s,'%s')" % (self.name, self.age, self.height, self.address)
        # return f"Person('{self.name}',{self.age},{self.height},'{self.address}')"
    def __eq__(self, obj): # ����� ��������� ������� � ���-����
        return (obj.name == None or self.name == None or compare(obj.name, self.name)) \
           and (obj.age == None or self.age == None or abs(obj.age - self.age) <= 2) \
           and (obj.height == None or self.height == None or abs(obj.height - self.height) <= 10) \
           and (obj.address == None or self.address == None or compare(obj.address, self.address))

to_search1 = Person("�����", 42, 167, "����������, 17, 100")
to_search2 = Person(age=40)
to_search3 = Person(name="������")

to_search_list = [
    to_search1,
    to_search2,
    to_search3,
]

# print(to_search_list)
# name = Person("name","age","height","address")
andrey = Person("������", 36, 180, "�������, 12, 115")
alex = Person("���������", 40, 170, "��������, 10, 5")
olga = Person("�����", 30, 165, "������, 1, 1")
helena = Person("�����", 42, 167, "����������, 17, 95")

people = [
    andrey,
    alex,
    olga,
    helena,
]
# pprint(people)
# from itertools import product
# for p1, p2 in product(people, to_search_list):
#     print(p1, p2, p1 == p2)

print('������� �������� ��� ������:')
# z_name = input('���: ')
# z_age = int(input('�������: '))
# z_age = int(z_age)
# z_height = int(input('����: ')) # ������ 120
print('����, �������� �������� (��������� ��������: ������, ������, �����)\n'
      '(������: ������ 120)')
a, b = input().split()
# print(f"a: {a}, b: {b}")
b = int(b)
# print('�����, � ���� (�����, �����, ���) ��� �������\n'
#       '������: �������, 12, 115')
# z_address = input('�����: ')
# z_person = Person(z_name, z_age, b, address=None)
z_person = Person(name=None, age=None, height = b, address=None)
print(z_person)
N = 0
if a == '������':
    for i in people:
        if i.height > b:
            print(i)
            N += 1
if a == '������':
    for i in people:
        if i.height < b:
            print(i)
            N += 1
if a == '�����':
    for i in people:
        if i.height == b:
            print(i)
            N += 1
if N != 0:
    print(f"����������� ���������� '{N}'")
else:
    if N == 0:
        print(f"������� � ����������� {z_person} �� ������")


# for username, userinfo in people.items():
#     print(f"username: {username}")
#     print(f"userinfo: {userinfo}")

# print(people.get("name"))
# print(people.get("���", "��� ���?"))
# print(people.setdefault(2)) # �������� ���������� ��������  �����, �� � ������ ����� ����
# people_copy = people.copy() # ����� �������
# print(people_copy)
# people.update({helena.key: helena}) # ����� ���� � �������
# people.update({olga.key: helena}) # ����� ���� ���� ����, �� ����������� ��������
# print(people.pop(olga.key)) # ������� ���� � ���������� ��������
# print(people.pop(helena.key, "No key!")) # ���� ��� �����, �� ���������� ���������� ��������� ��������
# print(people.popitem()) # ������� � ���������� ��������� ���� ����-��������
# print(people.keys()) ���������� ������ ������ �������
# print(people.values()) ���������� ������ ��������
# print(people.items()) ���������� ������� � ������ ����-��������
# people.clear() # ������� �������
# pprint(people)

# if __name__ == "__main__":

    # getattr(odj, name,[, default]) -
    # hasattr(odj, name) - ��������� �� ������� �������� name � obj
    # setattr(odj, name, value) - ������� �������� �������� (���� ������� �� ����������, �� �� ���������)
    # delattr(obj, name) - ������� ������� � ������ name
    # class.__doc__ - �������� ������ � ��������� ������
    # *.__dict__  - �������� ����� ��������� ���������� ������