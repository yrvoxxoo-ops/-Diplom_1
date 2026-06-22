import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("black bun", 100)

@pytest.fixture
def sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50
    return sauce

@pytest.fixture
def filling():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 70
    return filling