"""
Вторая версия реализации задания Мегатрйдер
"""

def parse_input(txt):
    """
    Функция для парсинга входных данных
    Сложность алгоритма O(n), где n - количество лотов
    :param txt: входные данные в виде строки
    :return: кортеж (n, m, s, lots) где n, m, s - значения N, M, S, lots - список лотов
    """
    data = txt.strip().splitlines()

    # Значения N, M, S
    n, m, s = map(int, data[0].split())

    lots = []

    # Остальные строки - данные о лотах
    for line in data[1:]: 
        if line.strip() == '':
            break
        day, name, price, quantity = line.split()
        day = int(day)
        price = float(price)
        quantity = int(quantity)
        lots.append((day, name, price, quantity))
    return n, m, s, lots

def calculate_income(n, lot):
    """
    Функция для расчета дохода от лота

    :param n: количество предложений облигаций на рынке за N дней
    :param lot: лот (day, name, price, quantity)
    :return: кортеж (total_income, lot_price)
    """
    day, name, price, quantity = lot
    bond_value = 1000
    daily_coupon = 1
    lot_price = price / 100 * bond_value * quantity  # цена лота равна цена лота / 100 * цена облигации * количество лотов
    income_from_redemption = bond_value * quantity  # доход от выкупа равен номиналу облигации * количество лотов
    # доход от купонов равен ежедневная выплата по купону * количество лотов * количество дней до конца срока * 1
    coupon_income = daily_coupon * quantity * (n + 30 - day + 1)
    total_income = income_from_redemption + coupon_income  # доход от погашения + доход от купонов
    return total_income, lot_price


def maximize_income(n, s, lots):
    """
    Функция для нахождения максимального дохода и выбора лотов

    :param n: количество предложений облигаций на рынке за N дней
    :param s: общая сумма денег
    :param lots: список лотов
    :return: кортеж (total_income, selected_lots)
    """
    income_lots = []
    for lot in lots:
        #
        income, cost = calculate_income(n, lot)  # доход
        income_lots.append((income, cost, lot))

    income_lots.sort(key=lambda x: x[0] / x[1], reverse=True)

    selected_lots = []
    total_spent = 0
    total_income = 0

    for income, cost, lot in income_lots:
        if total_spent + cost <= s:
            selected_lots.append(lot)
            total_spent += cost
            total_income += income

    return total_income, selected_lots

def main():
    """
    Основная функция программы
    Комплексность алгоритма O(n log n), где n - количество лотовб
    .т.е наибольшая возрастающая подпоследовательность за o(n*log(n))
    :param txt: входные данные в виде строки
    :return: ничего не возвращает, только выводит результаты
    """
    # txt = '\n2 2 8000\n1 alfa-05 100.2 2\n2 alfa-05 101.5 5\n2 gazprom-17 100.0 2\n\n'
    # n, m, s, lots = parse_input(txt)

    n, m, s, lots = 2, 2, 8000, [(1, 'alfa-05', 100.2, 2), (2, 'alfa-05', 101.5, 5), (2, 'gazprom-17', 100.0, 2)]
    total_income, selected_lots = maximize_income(n, s, lots)

    print(int(total_income)) # выводим максимальный доход
    for lot in selected_lots:
        # выводим выбранные лоты
        print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}", end='\n')

main()

"""
Ожидаемый вывод из ТЗ, но не совпадает с полученными данными.

Ожидаемый вывод:
--
135
2 alfa-05 101.5 5
2 gazprom-17 100.0 2

Мой вывод:
--
4126
2 gazprom-17 100.0 2
1 alfa-05 100.2 2
"""
