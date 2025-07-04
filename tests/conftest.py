import pytest

from roman_converter.converter import RomanToInt


@pytest.fixture
def converter():
    return RomanToInt()
