from typing import TypeAlias


Number: TypeAlias = int | float


class Calculator:
    """Класс калькулятора с базовыми операциями"""

    def add(self, a: Number, b: Number) -> Number:
        """Сложение двух чисел"""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Вычитание двух чисел"""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Умножение двух чисел"""
        return a * b
        # return str(a * b)  # раскомментировать для ошибки проверки типов и pytest

    def divide(self, a: Number, b: Number) -> Number:
        """Деление двух чисел"""
        if b == 0:
            raise ValueError('Cannot divide by zero!')
        return a / b


# раскомментировать для ошибки безопасности bandit
# def insecure_function():
    # """Функция с потенциальными уязвимостями для демонстрации Bandit"""
    # import os
    # import pickle
    # result = os.system('echo "Hello"')

    # data = b"test_data"
    # loaded = pickle.loads(data)
    # return result, data


if __name__ == "__main__":
    # пример использования калькулятора
    calc = Calculator()
    a = 2
    b = 3
    print(f'{a} + {b} = {calc.add(a, b)}')
    print(f'{a} - {b} = {calc.subtract(a, b)}')
