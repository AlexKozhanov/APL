if __name__ == '__main__':
    pass
    print('Hello, world!')

    # todoо: Players

    # region important
    print('1)сtrl + shift + F10 - запускает код')
    print('2)колёсико мыши находит использование объекта,')
    print('ctrl + лкм - момент объявления ')
    print('shift + F6 - реформат переменных и не только')
    print('alt + лкм - позволяет создавать любое кол-во синхронизированных курсоров')
    print('ctrl + alt + s - открывает настройки')
    print('ctrl + alt + t - реформат кода в файле')
    print('ctrl + alt + о - оптимизация импортов в файле')
    print('ctrl + alt + F12 - быстрый переход в проводник')
    # endregion

    # структура программы отсутствует, главное чтоб понятно было
    # В реальности:
    # Все импорты - сначала
    # Потом - описания констант
    # Потом - функции
    # В конце - волшебная конструкция,
    # if __name__ == '__main__':
    #     main()

    # Заслонение - наименование переменной совпадает с именами функции, типов, ...

    # import x                # получить х
    # import x as y           # получить х как у
    # from x import y         # только у из х
    # from x import y as z    # только у из х как z
    # from x import *         # Так плохо! Но можно, но перед этим нужно извиниться
    # пример
    #
    # x = numpy.array(range(100))
    # print(numpy.mean(x))
    # import numpy as np  # 2)- так короче
    #
    # x = np.array(range(100))
    # print(np.mean(x))
    # from numpy import array  # 3) - можно через запятую
    #
    # x = array(range(100))
    # print(x.mean())
    # print(np.mean())       - не работает, т.к. имя numpy не импортировано
    # print(numpy.mean())    - не работает, т.к. имя numpy не импортировано
