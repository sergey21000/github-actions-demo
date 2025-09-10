import pytest
from src.calculator import Calculator


def test_add(calc: Calculator) -> None:
    """Тест сложения"""
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract(calc: Calculator) -> None:
    """Тест вычитания"""
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(10, 10) == 0


def test_multiply(calc: Calculator) -> None:
    """Тест умножения"""
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0


def test_divide(calc: Calculator) -> None:
    """Тест деления"""
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5


def test_divide_by_zero(calc) -> None:
    """Тест деления на ноль."""
    # если блок кода под with вызовет исключение то тест будет успешным
    with pytest.raises(ValueError):
        calc.divide(10, 0)
