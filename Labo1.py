command = input("номер задания:")
match command.split():
    case ["1"]: # 1.1 заменить буквы на цифры
        str = "zxcvbnhy yhnbvcxz xxx yyy"
        str_new = ""
        for x in str:
            if x == "x":
                str_new += "y"
            else:
                str_new += x
        print("№1")
        print(str)
        print(str_new)
    case ["2"]: # 1.2 сосчитать произведение чисел, кратных 3 и 5
        num = [1,2,3,4,5,6,7,8,9,10,11,12]
        #          ^   ^ ^     ^ ^^    ^^ - кратны, сумм=97200
        prod = 1
        for x in num:
            if (x // 3 == x / 3) or (x // 5 == x / 5):
                prod *= x
        print("№2")
        print(prod)
    case ["3"]: #Заменить все буквы "x" на "y" в исходной строке без использования дополнительной
        str = "zxcvbnhy yhnbvcxz xxx yyy"
        out = str.replace("x", "y")
        print(str)
        print(out)



# command = input("What are you doing next? ")
# match command.split():
#     case ["quit"]:  # введено одно слово "quit"
#         print("Goodbye!")
#         quit_game()
#     case ["look"]:  # введено одно слово "look"
#         current_room.describe()
#     case ["get", obj]:  # введено два слова - "get" и какое-то другое, которое будет записано в переменную obj
#         character.get(obj, current_room)
#     case ["go", direction]:
#         current_room = current_room.neighbor(direction)
#     case ["drop", *objects]:  # введено слово "drop" и еще несколько слов, которые будут записаны в переменную objects
#         for obj in objects:
#             character.drop(obj, current_room)
#     case _:  # Аналогично default в других языках
#         print(f"Sorry, I couldn't understand {command!r}")