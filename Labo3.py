# person = [['Трус', 1993], ['Балбес', 1992], ['Бывалый', 1991]]
person = [['Трус', 1993], ['Балбес', 1992], ['Бывалый', 1991]]
a = [[0, 0]]
command = input("номер лабы:")
match command.split():
    case ["1"]:  # 3.1 выбрать "самого какого-то" персонажа, перебрав всех циклом 1-список
        for i in range(len(person) - 1):
            for j in range(0, i):
                if person[i][j] < person[i + 1][j]:
                    a = person[i][2]
                else:
                    a = person[i + 1][2]
        print(a)
    #            print(person[i])
    case ["2"]:  # 3.2 выбрать "самого какого-то" персонажа, перебрав всех циклом 2-словарь
        print('2')
    case ["3"]:  # 3.3 Сделать запрос данных от пользователя (input())
        output = input("Введите Фамилию(id) персонажа:")
        if output == '1' or output == "Кожанов":
            print(person)
