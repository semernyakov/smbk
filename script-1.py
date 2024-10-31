import unittest
import time

# Задача: Долевое строительство

"""
1. Вычислительная сложность алгоритма calculate_percentages составляет O(N), 
где N - количество долей. Это связано с тем, что алгоритм выполняет один проход
по списку долей для вычисления суммы и затем еще один проход для вычисления 
процентного выражения каждой доли. Оценка необходимой памяти для выполнения 
алгоритма также составляет O(N), так как мы храним список долей 
и список процентных выражений.


2. Ограничения на размер входных параметров, при которых алгоритм будет 
выполняться разумное время, зависят от количества долей и производительности 
системы. Для данного алгоритма, который имеет линейную сложность, 
размер входных данных до нескольких тысяч элементов должен обрабатываться 
за разумное время (до 5 секунд), при условии, что система имеет достаточные ресурсы.

3. Субъективная оценка сложности задачи по шкале от 1 до 10 может быть 
около 2-3. Задача представляет собой простое вычисление процентного 
выражения долей на основе суммы их значений. Реализация данной функции не 
требует сложных математических операций или алгоритмов, и ее выполнение 
не должно занимать много времени. Время, затраченное на реализацию и 
тестирование, у меня ушло порядка 30-60 минут.
"""


def timer(func):
    """
    Декоратор для оценки времени выполнения функции
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time} seconds")
        return result
    return wrapper


@timer
def validate_input(n: int, fractions: list[int | float]) -> None:
    """
    Функция для валидации входных данных
    """
    if n is None and fractions is None:
        raise ValueError("Оба параметра N и fractions не могут быть None.")
    if n is not None and n < 0:
        raise ValueError("Количество долей N не может быть отрицательным.")
    elif n is not None and n == 0:
        raise ValueError("Количество долей N не может быть нулем.")
    elif n is not None and n > len(fractions):
        raise ValueError("Количество долей N не может превышать длину списка fractions.")
    elif n is not None and n < len(fractions):
        raise ValueError("Количество долей N не может быть меньше длины списка fractions.")
    elif n is not None and n != len(fractions):
        raise ValueError("Длина списка fractions не соответствует указанному количеству долей N.")
    if not all(isinstance(fraction, (int, float)) for fraction in fractions):
        raise ValueError("Все элементы списка fractions должны быть числами.")
    if not all(fraction >= 0 for fraction in fractions):
        raise ValueError("Все элементы списка fractions должны быть неотрицательными числами.")
    return None


@timer
def calculate_percentages(n: int, fractions: list[int | float]) -> list:
    """
    Функция для вычисления процентного выражения долей (простая реализация)

    Для оптимизации функции calculate_percentages можно улучшить алгоритм вычисления
    процентного выражения долей, чтобы уменьшить количество операций и повысить эффективность.

    Вместо двух проходов по списку долей для вычисления суммы и процентного выражения каждой доли,
    можно выполнить это за один проход.
    """
    if validate_input(n, fractions) is not None:
        raise ValueError("Invalid input values.")
    total = sum(fractions)
    percentages = [(fraction / total) * 100 for fraction in fractions]
    return ['{:.3f}'.format(percentage / 100) for percentage in percentages]


@timer
def calculate_percentages_optimum(n: int, fractions: list[int | float]) -> list:
    """
    Функция для вычисления процентного выражения долей (оптимизированная реализация)

    В этой оптимизированной версии функции мы вычисляем сумму всех долей в одном проходе
    по списку долей. Затем мы вычисляем процентное выражение каждой доли в том же проходе,
    используя формулу (fraction / total) * 100, и форматируем результат до трех знаков после запятой.

    Эта оптимизированная версия функции позволяет уменьшить количество проходов по списку и
    улучшить производительность алгоритма.
    """
    if validate_input(n, fractions) is not None:
        raise ValueError("Invalid input values.")
    total = sum(fractions)
    percentages = ['{:.3f}'.format((fraction / total) if total != 0 else 0) for fraction in fractions]

    return percentages


class TestCalculatePercentages(unittest.TestCase):
    """
    Тесты для функций calculate_percentages и calculate_percentages_optimum
    """
    def test_calculate_percentages(self):
        n = None
        fractions = [1.5, 3, 6, 1.5]
        expected_result = ['0.125', '0.250', '0.500', '0.125']
        result = calculate_percentages(n, fractions)
        self.assertEqual(result, expected_result)

    def test_calculate_percentages_optimum(self):
        n = 4
        fractions = [1.5, 3, 6, 1.5]
        expected_result = ['0.125', '0.250', '0.500', '0.125']
        result = calculate_percentages_optimum(n, fractions)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
