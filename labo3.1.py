def main():
    # dictionary �������
    person = {
        "courses": "���������",
        "age": 36,
        "name": "����������� ����� �����������",
        "sex": "male",
        "position": "������",
        "science": ""
    }
    for k, v in person.items():
        print(f"{k} >>> {v}")


if __name__ == '__main__':
    main()
