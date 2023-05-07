def main():
    # dictionary словарь
    person = {
        "courses": "Ресурсное",
        "age": 36,
        "name": "Андрейченко Игорь Леонардович",
        "sex": "male",
        "position": "Доцент",
        "science": ""
    }
    for k, v in person.items():
        print(f"{k} >>> {v}")


if __name__ == '__main__':
    main()
