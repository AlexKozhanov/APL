# См. актуальную версию Labo3.1
def person_db_dict():
    # dictionary словарь
    person_dict = {
        "courses": "Ресурсное",
        "age": 36,
        "name": "Андрейченко Игорь Леонардович",
        "sex": "male",
        "position": "Доцент",
        "science": ""
    }
    return person_dict


def load_and_parse_data_dict(person_db):
    data = person_db
    people_dict2 = {}  # dictionary словарь
    for url in data:
        fio = data['name']
        courses = data['courses']
        age = data['age']
        sex = data['sex']
        position = data['position']
        science = data['science']

        people_dict2.update({fio: {
            'courses': courses,
            'age': age,
            'sex': sex,
            'position': position,
            'science': science,
        }
        })
    return people_dict2


def person_db_list():
    # list список
    person_list = [
        ["https:2.1", "courses1.1", 36, "Андрейченко Игорь Леонардович", "male", "Доцент", ""],
        ["https:2.2", "courses1.2", 34, "Балакирев Александр Андреевич", "male", "Старший преподаватель", ""],
        ["https:2.3", "courses1.3", 91, "Белослудцев Иван Михайлович", "male", "Доцент", ""]
    ]
    return person_list


def load_and_parse_data_list(person_db):
    data = person_db
    people_list2 = []  # list список
    for url in data['staff']:
        fio = data['staff'][url]['name']
        courses = data['staff'][url]['courses']
        age = data['staff'][url]['age']
        sex = data['staff'][url]['sex']
        position = data['staff'][url]['position']
        science = data['staff'][url]['science']

        people_list2 += [(
            fio,
            courses,
            age,
            sex,
            position,
            science,
        )]
    return people_list2


def find_teacher_in_dict(a_dict):
    sorted_dict = {
        k: v for k, v in sorted(a_dict.items(), key=lambda x: x[1]['courses'].count(','))
    }
    last = list(sorted_dict.keys())[-1]
    return last, a_dict[last]


def find_teacher_in_list(a_list):
    rez = sorted(a_list, key=lambda x: x[1].count(','))[-1]
    return rez


if __name__ == '__main__':
    people_dict = load_and_parse_data_dict(person_db_dict())
    people_list = load_and_parse_data_list(person_db_list())

    the_most_erudite_teacher = find_teacher_in_dict(people_dict)
    print(the_most_erudite_teacher)
    the_most_erudite_teacher = find_teacher_in_list(people_list)
    print(the_most_erudite_teacher)

# if __name__ == "__main__":
#     command = input("Номер задания:")
#     match command.split():
#         case ["1"]:
#             task1()
#         case ["2"]:
#             task2()
#         case ["3"]:
#             task3()

# person = [['Трус', 1993], ['Балбес', 1992], ['Бывалый', 1991]]


# 3.1 выбрать "самого какого-то" персонажа, перебрав всех циклом 1-список
# 3.2 выбрать "самого какого-то" персонажа, перебрав всех циклом 2-словарь
# 3.3 Сделать запрос данных от пользователя (input())

# person_dict = {
#     "первый": {
#         "courses": "Ресурсное проектирование авиационных двигателей и энергетических установок",
#         "age": 36,
#         "name": "Андрейченко Игорь Леонардович",
#         "sex": "male",
#         "position": "Доцент",
#         "science": ""
#     },
#     "второй": {
#         "courses": " Общая теория авиационных и ракетных двигателей, Учебно-исследовательская работа",
#         "age": 34,
#         "name": "Балакирев Александр Андреевич",
#         "sex": "male",
#         "position": "Старший преподаватель",
#         "science": ""
#     },
#     "третий": {
#         "courses": "Технология, Технология производства авиационных и ракетных двигателей",
#         "age": 91,
#         "name": "Белослудцев Иван Михайлович",
#         "sex": "male",
#         "position": "Доцент",
#         "science": ""
#     },
# }
# def load_and_parse_data_dict(person_db):
#     data = person_db
#     people_dict2 = {}  # dictionary словарь
#     for url in data['staff']:
#         fio = data['staff'][url]['name']
#         courses = data['staff'][url]['courses']
#         age = data['staff'][url]['age']
#         sex = data['staff'][url]['sex']
#         position = data['staff'][url]['position']
#         science = data['staff'][url]['science']
#
#         people_dict2.update({fio: {
#             'courses': courses,
#             'age': age,
#             'sex': sex,
#             'position': position,
#             'science': science,
#         }
#         })
#     return people_dict2
