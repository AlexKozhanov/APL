command = input("номер лабы:")
match command.split():
    case ["1"]:  # 2.1 Опишите себя, используя список
        about_me = [
            'Кожанов Александр', 1998, 'магистр', 'ПНИПУ',
            'ООО Интеллектуальные системы', 'младший специалист'
        ]
        print(about_me)
    case ["2"]:  # 1.2 Опишите себя, используя словарь
        about_me2 = {
            'Кожанов Александр':
                {'род.': 1998,
                 'обучение':
                     {'Универ': 'ПНИПУ',
                      'специальность': 'магистр', },
                 'работа':
                     {'организация': 'ООО Интеллектуальные системы',
                      'должность': 'младший специалист', },
                 },
        }
        print(about_me2)
