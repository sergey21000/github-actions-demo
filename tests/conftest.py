import pytest
from src.calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Фикстура для создания экземпляра калькулятора."""
    return Calculator()