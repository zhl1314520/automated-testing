import pytest

"""
fixture 里面使用其他 fixture 
"""
@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return [first_entry]    # [a]


def test_string(order):
    order.append("b")   # [a, b]

    assert order == ["a", "b"]