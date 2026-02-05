def insertion_sort(arr):
    """
    Сортировка вставками (самостоятельная реализация).
    Возвращает новый отсортированный список без изменения исходного.
    
    Аргументы:
        arr (list): Список для сортировки
        
    Возвращает:
        list: Отсортированный список
    """
    if not arr:
        return []
    
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


def check_positive_exists(lst):
    """
    Проверяет наличие хотя бы одного положительного числа через any().
    
    Аргументы:
        lst (list): Список для проверки
        
    Возвращает:
        bool: True если есть положительное число, иначе False
    """
    return any(x > 0 for x in lst if isinstance(x, (int, float)))


def check_all_numbers(lst):
    """
    Проверяет, состоят ли все элементы только из чисел через all().
    
    Аргументы:
        lst (list): Список для проверки
        
    Возвращает:
        bool: True если все элементы - числа, иначе False
    """
    return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in lst)


def main():
    """Основная функция для демонстрации работы программы."""
    
    # Получение списка от пользователя
    try:
        user_input = input("Введите элементы списка через пробел: ")
        elements = []
        for item in user_input.strip().split():
            # Пытаемся преобразовать в число, иначе оставляем как строку
            try:
                # Проверяем, является ли число целым или вещественным
                if '.' in item:
                    elements.append(float(item))
                else:
                    elements.append(int(item))
            except ValueError:
                elements.append(item)
        
        print(f"\nИсходный список: {elements}")
        
        # Проверка 1: наличие положительного числа
        has_positive = check_positive_exists(elements)
        print(f"\n1. Содержит ли список хотя бы одно положительное число?")
        print(f"   Результат (any): {has_positive}")
        
        # Проверка 2: все ли элементы - числа
        all_numeric = check_all_numbers(elements)
        print(f"\n2. Состоят ли все элементы списка только из чисел?")
        print(f"   Результат (all): {all_numeric}")
        
        # Проверка 3: сортировка вставками
        if all_numeric:
            sorted_list = insertion_sort(elements)
            print(f"\n3. Отсортированный список (вставками): {sorted_list}")
        else:
            print("\n3. Сортировка невозможна: список содержит нечисловые элементы")
            
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"\nОшибка: {e}")


if __name__ == "__main__":
    main()