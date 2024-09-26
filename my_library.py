# my_library.py

# Функция для вычисления первых n чисел Фибоначчи
def fibonacci(n):
    """
    Возвращает список из первых n чисел Фибоначчи.
    :param n: количество чисел Фибоначчи
    :return: список чисел Фибоначчи
    """
    if n <= 0:
        raise ValueError("n должно быть положительным числом")

    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list[:n]


# Функция для сортировки пузырьком
def bubble_sort(lst):
    """
    Сортирует список чисел по возрастанию с использованием алгоритма пузырьковой сортировки.
    :param lst: список чисел
    :return: отсортированный список чисел
    """
    sorted_list = lst.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


# Калькулятор для выполнения арифметических операций
def calculator(num1, num2, operator):
    """
    Выполняет арифметическую операцию между двумя числами.
    :param num1: первое число
    :param num2: второе число
    :param operator: арифметическая операция ('+', '-', '*', '/')
    :return: результат вычисления
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return num1 / num2
    else:
        raise ValueError("Некорректный оператор!")

