"""
Модуль для демонстрации различных операций в Python.
"""

def demo_operations(x: int, y: int):
    """
    Функция для демонстрации различных операций.
    Параметры:
    x (int): первое число
    y (int): второе число
    """
    print(f"\nВыполняется demo_operations с параметрами x={x}, y={y}:\n")

    # Арифметические операции
    print(x + y)
    print(x - y)
    print(x * y)

    if y != 0:
        print(x / y)
        print(x // y)
    else:
        print("Деление на ноль невозможно")

    print(x % y)  # Остаток от деления
    print(x ** y)

    # Логические операции
    print(x > 0 and y > 0)
    print(x > 0 or y > 0)
    print(not x > 0)

    # Преобразование типов
    print(float(x))  # в float
    print(str(y))    # в строку
    print(int("10"))  # строку в число

    # Условная конструкция с вложенным if
    if x > y:
        print("x больше y")
        if x > 10:
            print("x больше 10")
    else:
        print("x не больше y")

    # Условная конструкция if-elif-else
    if x > y:
        print("x больше y")
    elif x == y:
        print("x равно y")
    else:
        print("x меньше y")

    # Циклы
    for i in range(x):
        print(i, end=" ")
    print()

    while y > 0:
        print(y, end=" ")
        y -= 1
    print()

    # Цикл for внутри for
    array = [1, 2, 3]
    for i in range(x):
        for j in array:
            print(f"{i} {j}", end=" ")
        print()

    # Простая версия switch-case
    def switch_case_simple(value):
        if value == 1:
            return "1"
        elif value == 2:
            return "2"
        elif value == 3:
            return "3"
        return "неправильно"

    print(switch_case_simple(2))

print("\n=== Вызов demo_operations с явным указанием параметров x=7, y=4 ===\n")
demo_operations(x=7, y=4)

def switch_case_match(value: int):
    """
    Простая функция для демонстрации работы оператора match-case.
    Параметры:
    value (int): значение для проверки
    """
    match value:
        case 1:
            return "один"
        case 2:
            return "два"
        case 3:
            return "три"
        case _:
            return "неправильно"

print(switch_case_match(3))

def sum_all(*args):
    """
    Функция для суммирования всех переданных аргументов.
    Параметры:
    *args: произвольное количество аргументов
    """
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

if __name__ == "__main__":
    print("\n=== Вызов demo_operations с переменными A=5, B=3 ===\n")
    A = 5
    B = 3
    demo_operations(A, B)
