def task2(x):
    print('Введите значение: ')
    input(x)


def main():
    import numpy as np
    array1 = np.array(range(101))
    # sum_array = array1.sum()
    print(array1.sum())


if __name__ == "__main__":
    main()
    # 1) Сумма ряда 0-100
    # 2) Сумма ряда 0-input
    # 3) Среднее среди 100 случайных чисел
  