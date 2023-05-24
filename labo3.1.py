def find_persons_in_dict(persons):
    people_dict = {} # dictionary словарь
    for username, userinfo in persons.items():
        age = userinfo["age"]
        height = userinfo["height"]
        sex = userinfo["sex"]
        position = userinfo["position"]

        people_dict.update({username: {
            'age': age,
            'height': height,
            'sex': sex,
            'position': position,
        }})
    # print(persons)
    # print(people_dict)
    sorted_dict = { # сортировка словаря по возрастанию возраста
        k: v for k, v in sorted(people_dict.items(), key=lambda x:x[1]['age'])
    }
    last = list(sorted_dict.keys())[-1]
    # print(sorted_dict)
    # print(last)
    # print(people_dict[last])
    return last, people_dict[last]

def find_teacher_in_list(persons):
    persons_list = [] # list список
    for username, userinfo in persons.items():
        age = userinfo["age"]
        height = userinfo["height"]
        sex = userinfo["sex"]
        position = userinfo["position"]

        persons_list += [( # конвертируем словарь в список с кортежами
            username,
            age,
            height,
            sex,
            position,
        )]
    # print(persons_list)
    rez = sorted(persons_list, key=lambda x: x[1])[-1] # сортировка списка по возрастанию возраста
    # persons_list = sorted(persons_list, key=lambda x: x[1])
    # print(persons_list)
    return rez

def main():
    persons = {
        "Andriy":{
            "age": 36,
            "height": 180,
            "sex": "male",
            "position": "docent"
        },
        "Alexsander": {
            "age": 40,
            "height": 170,
            "sex": "male",
            "position": "docent"
        },
        "Olga": {
            "age": 30,
            "height": 165,
            "sex": "woman",
            "position": "senior lecturer"
        }
    }
    the_oldest_person = find_persons_in_dict(persons)
    print('Max old from dictionary - ', the_oldest_person)
    the_oldest_person = find_teacher_in_list(persons)
    print("Max old from list - ", the_oldest_person)


if __name__ == '__main__':
    main()

    # for username, userinfo in persons.items():
    #     print(f"Имя пользователя: {username}")
    #     age = userinfo["age"]
    #     sex = userinfo["sex"]
    #
    #     print(f"Возраст пользователя {username} : {age} лет.")
    #     print(f"Пол пользователя {username} : {sex}.\n")

    # for k, v in person.items():
    #     print(f"{k} >>> {v}")