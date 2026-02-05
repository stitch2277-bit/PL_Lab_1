class BinomialSequence:
    """
    Класс для генерации биномиальных коэффициентов n-й строки
    треугольника Паскаля с минимальными затратами памяти.
    """
    
    @staticmethod
    def generate(n):
        """
        Генерирует n-ю строку треугольника Паскаля (коэффициенты C(n,0)...C(n,n)).
        Использует формулу: C(n,k) = C(n,k-1) * (n-k+1) / k
        
        Аргументы:
            n (int): Номер строки (начиная с 0)
            
        Возвращает:
            Генератор, выдающий коэффициенты по одному
            
        Пример:
            list(BinomialSequence.generate(4)) -> [1, 4, 6, 4, 1]
        """
        if n < 0:
            raise ValueError("Номер строки должен быть неотрицательным")
        
        # Первый коэффициент всегда 1: C(n,0) = 1
        coefficient = 1
        yield coefficient
        
        # Генерируем остальные коэффициенты через рекуррентную формулу
        for k in range(1, n + 1):
            # C(n,k) = C(n,k-1) * (n - k + 1) / k
            coefficient = coefficient * (n - k + 1) // k
            yield coefficient
    
    @staticmethod
    def get_row(n):
        """
        Вспомогательный метод: возвращает всю строку как список.
        Используется для тестирования и сравнения.
        
        Аргументы:
            n (int): Номер строки
            
        Возвращает:
            list: Список коэффициентов
        """
        return list(BinomialSequence.generate(n))


def test_binomial_sequence():
    """Тестирование генератора биномиальных коэффициентов."""
    
    # Тест 1: Строки с малыми n
    test_cases = [0, 1, 2, 3, 4, 5, 8]
    
    print("\nГенерация строк треугольника Паскаля:")
    print("-" * 60)
    for n in test_cases:
        row = BinomialSequence.get_row(n)
        print(f"n = {n:2d}: {row}")
        # Проверка суммы (должна быть 2^n)
        assert sum(row) == 2 ** n, f"Ошибка в строке {n}: сумма != 2^{n}"
    
    # Тест 2: Проверка памяти для больших n
    print("\n" + "-" * 60)
    print("Тест производительности для больших n:")
    large_n = 1000
    print(f"Генерация {large_n}-й строки (без хранения всей строки в памяти)...")
    
    # Используем генератор без преобразования в список
    count = 0
    last_coeff = None
    for coeff in BinomialSequence.generate(large_n):
        count += 1
        last_coeff = coeff
    
    print(f"  Сгенерировано коэффициентов: {count}")
    print(f"  Последний коэффициент C({large_n},{large_n}) = {last_coeff}")
    print(" Генератор работает с минимальными затратами памяти")
    
    # Тест 3: Проверка корректности формулы
    print("\n" + "-" * 60)
    print("Проверка симметрии: C(n,k) == C(n,n-k)")
    n_test = 10
    row = BinomialSequence.get_row(n_test)
    is_symmetric = all(row[i] == row[n_test - i] for i in range(len(row)))
    print(f"n = {n_test}: симметрия {'соблюдена' if is_symmetric else 'НАРУШЕНА'}")
    
    # Тест 4: Обработка ошибок
    print("\n" + "-" * 60)
    print("Тест обработки ошибок:")
    try:
        list(BinomialSequence.generate(-5))
        print("Ошибка: не сработала проверка отрицательного n")
    except ValueError as e:
        print(f"Корректная обработка отрицательного n: {e}")


if __name__ == "__main__":
    test_binomial_sequence()