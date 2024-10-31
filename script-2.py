"""
Первая версия реализации задания Мегатрйдер
"""

def calculate_income(N, lot):
    """
    Функция рассчитывает доход от одного лота.

    Аргументы:
    N (int): количество предложений облигаций на рынке за N дней + 30 дней
    day (int): день погашения облигации
    name (str): название облигации
    price (float): цена лота
    quantity (int): количество лотов
    """
    day, name, price, quantity = lot  # распаковка кортежа лота в отдельные переменные
    bond_value = 1000  # номинал облигации
    daily_coupon = 1  # ежедневная выплата
    lot_price = price / bond_value * 100 * quantity  #
    income_from_redemption = bond_value * quantity  # цена облигации * количество лотов
    coupon_income = daily_coupon * quantity * (N + 30 - day + 1)  # количество лотов * дней до конца срока * 1
    total_income = income_from_redemption + coupon_income  # доход от погашения + доход от купонов
    return total_income, lot_price  # доход от лота и стоимость лота


def maximize_income(N, M, S, lots):
    """
    Функция для нахождения максимального дохода и выбора лотов.

    Аргументы:
    N (int): количество предложений облигаций на рынке за N дней
    M (int): каждый день на рынке может быть от 0 до M лотов
    S (int): трейдер располагает суммой денежных средств в количестве S.

    Возвращает:
    tuple: кортеж из двух элементов: максимальный доход и список лотов, которые следует купить,
    чтобы получить этот доход.
    lots (list): список лотов, каждый лот представлен кортежем (day, name, price, quantity)
    """
    income_lots = []  # Список кортежей (доход, стоимость, название лота)
    for lot in lots:
        income, cost = calculate_income(N, lot)  # Рассчитываем доход и стоимость лота
        income_lots.append((income, cost, lot))  # Добавляем кортеж (доход, стоимость, лот) в список
    
    # Сортируем список лотов по отношению доход/стоимость, в порядке убывания
    income_lots.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    selected_lots = []
    total_spent = 0
    total_income = 0

    # Выбираем лоты, чтобы максимизировать доход
    for income, cost, lot in income_lots:
        # Проверяем, что общая сумма денег, потраченная на покупку лотов, не превышает максимальную сумму
        if total_spent + cost <= S:
            selected_lots.append(lot)
            total_spent += cost  # Обновляем общую сумму денег, потраченную на покупку лотов
            total_income += income  # Обновляем общий доход
    
    return total_income, selected_lots


def main():
    import random

    def generate_lots():
        """
        Генерирует случайные лоты для тестирования
        :return: список лотов в формате [(day, name, price, quantity), ...]
        """
        lots = []
        for _ in range(random.randint(1, 10)):
            day: int = random.randint(1, 31)
            name: str = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))  # Название облигации
            percent: float = random.randint(1, 1000) / 1000 * 100  # Цена в процентах от номинала
            percent = round(percent, 2)  # Округляем до 2 знаков после запятой
            quantity: int = random.randint(1, 10)  # Количество
            lots.append((day, name, percent, quantity))
        return lots

    test_cases = []

    for _ in range(100):
        """
        Генерируем случайные тестовые случаи
        N (int): количество предложений облигаций на рынке за N дней
        M (int): каждый день на рынке может быть от 0 до M лотов
        S (int): трейдер располагает суммой денежных средств в количестве S.
        """
        N = random.randint(1, 365)
        M = random.randint(1, 100)
        S = random.randint(1, 100000)  # баланс условных едениц

        lots = generate_lots()

        test_cases.append((N, M, S, lots))

    # Write test cases to a file
    with open('test_cases.py', 'w') as f:
        f.write('test_cases = [\n')
        for case in test_cases:
            f.write(f'    {case},\n')
        f.write(']\n')


def test_main():
    from test_cases import test_cases
    for i, case in enumerate(test_cases):
        N, M, S, lots = case
        total_income, selected_lots = maximize_income(N, M, S, lots)
        # print(f"Тестовый  набор {i+1}: Кол-во предложений за N дней={N}, Кол-во лотов на день=M={M} S={S}, Кол-во выбранных лотов={len(lots)}")
        print(f"Сумма дохода: {total_income}")
        # <день> <название облигации> <цена> <количество>
        print(f"Выбранные лоты: {selected_lots}")
        print()


#test_main() # Генерация тестовых данных
main() # Вызов основной функции