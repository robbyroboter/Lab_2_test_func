# test_my_library.py
import pytest
from my_library import fibonacci, bubble_sort, calculator

# Тесты для функции fibonacci
def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3], "Ошибка при вычислении первых 5 чисел Фибоначчи"
    assert fibonacci(1) == [0], "Ошибка при вычислении первых 1 числа Фибоначчи"
    assert fibonacci(2) == [0, 1], "Ошибка при вычислении первых 2 чисел Фибоначчи"

    # Граничные значения и некорректные данные
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-5)

# Тесты для функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3], "Ошибка в пузырьковой сортировке"
    assert bubble_sort([1, 2, 3]) == [1, 2, 3], "Ошибка при сортировке уже отсортированного списка"
    assert bubble_sort([1]) == [1], "Ошибка при сортировке списка с одним элементом"
    assert bubble_sort([]) == [], "Ошибка при сортировке пустого списка"
    assert bubble_sort([5, -2, 0, 12]) == [-2, 0, 5, 12], "Ошибка при сортировке списка с отрицательными числами"

# Тесты для функции calculator
def test_calculator():
    assert calculator(1, 1, '+') == 2, "Ошибка при сложении"
    assert calculator(10, 5, '-') == 5, "Ошибка при вычитании"
    assert calculator(3, 4, '*') == 12, "Ошибка при умножении"
    assert calculator(10, 2, '/') == 5, "Ошибка при делении"

    # Тестирование деления на ноль
    with pytest.raises(ZeroDivisionError):
        calculator(10, 0, '/')

    # Тестирование некорректного оператора
    with pytest.raises(ValueError):
        calculator(10, 5, '%')
    with pytest.raises(ValueError):
        calculator(10, 5, 'invalid_operator')

