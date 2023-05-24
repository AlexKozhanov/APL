import numpy as np
def task1():
    # 1) ����� ���� 0-100
    array1 = np.array(range(101))
    # sum_array = array1.sum()
    print(array1.sum())


def task2():
    # 2) ����� ���� 0-input
    x = int(input('������� ��������: '))
    array2 = np.array(range(0, x + 1))
    # array2 = np.arange(0, x + 1)
    print(array2.sum())


def task3():
    # 3) ������� ����� 100 ��������� �����
    np.random.seed(1000)
    a = np.random.random(100)
    # print(a)
    # print(a.sum(), ' / ', a.size, ' = ', a.sum() / a.size)
    print('������� �������� ������� �� 100 ��������� ����� = ', a.sum() / a.size)


if __name__ == "__main__":
    command = input("����� �������:")
    match command.split():
        case ["1"]:
            task1()
        case ["2"]:
            task2()
        case ["3"]:
            task3()
