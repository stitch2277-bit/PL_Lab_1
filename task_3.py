import random
from string import ascii_lowercase, ascii_uppercase

# Глобальная строка символов для генерации паролей
CHARS = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def password_generator(n):
    """
    Генератор случайных паролей заданной длины.
    
    Аргументы:
        n (int): Длина генерируемого пароля
        
    Возвращает:
        Генератор, выдающий бесконечную последовательность паролей
    """
    if n <= 0:
        raise ValueError("Длина пароля должна быть положительным числом")
    
    while True:
        # Генерируем пароль случайным выбором символов
        password = ''.join(random.choice(CHARS) for _ in range(n))
        yield password


def main():
    """Основная функция для демонстрации генератора паролей."""
    N = 8  # Длина пароля по условию задачи
    
    print(f"\nИспользуемые символы ({len(CHARS)} шт.):")
    print(f"  Строчные буквы: {ascii_lowercase}")
    print(f"  Заглавные буквы: {ascii_uppercase}")
    print(f"  Цифры и спецсимволы: 0123456789!?@#$*")
    
    # Создаем генератор
    gen = password_generator(N)
    
    # Выводим первые 5 паролей
    print("\nПервые 5 сгенерированных паролей:")
    print("-" * 60)
    for i in range(1, 6):
        password = next(gen)
        print(f"{i}. {password}")
    
    # Дополнительная демонстрация: генерация еще 3 паролей
    print("\nДополнительная генерация (еще 3 пароля):")
    print("-" * 60)
    for i in range(1, 4):
        password = next(gen)
        print(f"Доп. {i}. {password}")
    
    print("\n Генератор работает корректно: пароли генерируются бесконечно")


if __name__ == "__main__":
    main()