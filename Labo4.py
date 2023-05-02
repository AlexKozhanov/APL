def main():
    pass

    # import x                # получить х
    # import x as y           # получить х как у
    # from x import y         # только у из х
    # from x import y as z    # только у из х как z
    # from x import *         # Так плохо! Но можно, но перед этим нужно извиниться
    # пример
    import numpy  # 1)

    x = numpy.array(range(100))
    print(numpy.mean(x))
    import numpy as np  # 2)- так короче

    x = np.array(range(100))
    print(np.mean(x))
    from numpy import array  # 3) - можно через запятую

    x = array(range(100))
    print(x.mean())
    # print(np.mean())       - не работает, т.к. имя numpy не импортировано
    # print(numpy.mean())    - не работает, т.к. имя numpy не импортировано

    main()
