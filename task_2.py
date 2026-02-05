class CyclicSetIterator:
    """
    Итератор по множеству (set) с циклическим повторением.
    После достижения конца начинает итерацию сначала.
    """
    
    def __init__(self, iterable_set):
        """
        Инициализация итератора.
        
        Аргументы:
            iterable_set (set): Множество для итерации
        """
        if not isinstance(iterable_set, set):
            raise TypeError("Ожидается множество (set)")
        
        self.original_set = iterable_set
        self.elements = list(iterable_set)  # Фиксируем порядок элементов
        self.index = 0
        self.iteration_count = 0  # Счетчик итераций для демонстрации цикличности
    
    def __iter__(self):
        """Возвращает сам объект итератора."""
        return self
    
    def __next__(self):
        """
        Возвращает следующий элемент. При достижении конца начинает сначала.
        
        Возвращает:
            Элемент множества
            
        Вызывает:
            StopIteration: никогда не вызывается (бесконечная итерация)
        """
        if not self.elements:
            raise StopIteration("Множество пусто")
        
        # Если достигли конца списка - начинаем сначала
        if self.index >= len(self.elements):
            self.index = 0
            self.iteration_count += 1
        
        element = self.elements[self.index]
        self.index += 1
        return element
    
    def get_state(self):
        """Возвращает текущее состояние итератора для отладки."""
        return {
            'current_index': self.index,
            'iteration_count': self.iteration_count,
            'total_elements': len(self.elements)
        }


def test_cyclic_iterator():
    """Тестирование работы циклического итератора."""
    
    # Тест 1: Обычное множество
    test_set = {3, 1, 4, 1, 5, 9, 2, 6}
    print(f"\nИсходное множество: {test_set}")
    print("Элементы в порядке итерации (первые 15 элементов):")
    
    iterator = CyclicSetIterator(test_set)
    results = []
    for i in range(15):
        elem = next(iterator)
        results.append(elem)
        print(f"  Шаг {i+1:2d}: {elem} (состояние: {iterator.get_state()})")
    
    print(f"\nРезультат первых 15 итераций: {results}")
    
    # Тест 2: Пустое множество
    print("\n" + "-" * 60)
    print("Тест с пустым множеством:")
    try:
        empty_iterator = CyclicSetIterator(set())
        print(next(empty_iterator))
    except (StopIteration, TypeError) as e:
        print(f"Ожидаемая ошибка: {type(e).__name__}: {e}")
    
    # Тест 3: Множество из одного элемента
    print("\n" + "-" * 60)
    print("Тест с множеством из одного элемента:")
    single_set = {'A'}
    single_iterator = CyclicSetIterator(single_set)
    print("Первые 5 итераций:", [next(single_iterator) for _ in range(5)])


if __name__ == "__main__":
    test_cyclic_iterator()