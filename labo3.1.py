# -*- coding: cp1251 -*-
def main():
    # dictionary словарь
    persons = {
        "Андрей":{
            "age": 36,
            "height": 180,
            "sex": "male",
            "position": "Доцент"
        },
        "Александр": {
            "age": 36,
            "height": 170,
            "sex": "male",
            "position": "Доцент"
        },
        "Ольга": {
            "age": 36,
            "height": 165,
            "sex": "woman",
            "position": "Ст.преподаватель"
        }
    }
    for username, userinfo in persons.items():
        print(f"Имя пользователя: {username}")
        age = userinfo["age"]
        sex = userinfo["sex"]

        print(f"Возраст пользователя {username} : {age} лет.")
        print(f"Пол пользователя {username} : {sex}.\n")

    # for k, v in person.items():
    #     print(f"{k} >>> {v}")


if __name__ == '__main__':
    main()
