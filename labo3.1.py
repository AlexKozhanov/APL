# -*- coding: cp1251 -*-
def main():
    # dictionary �������
    persons = {
        "������":{
            "age": 36,
            "height": 180,
            "sex": "male",
            "position": "������"
        },
        "���������": {
            "age": 36,
            "height": 170,
            "sex": "male",
            "position": "������"
        },
        "�����": {
            "age": 36,
            "height": 165,
            "sex": "woman",
            "position": "��.�������������"
        }
    }
    for username, userinfo in persons.items():
        print(f"��� ������������: {username}")
        age = userinfo["age"]
        sex = userinfo["sex"]

        print(f"������� ������������ {username} : {age} ���.")
        print(f"��� ������������ {username} : {sex}.\n")

    # for k, v in person.items():
    #     print(f"{k} >>> {v}")


if __name__ == '__main__':
    main()
