import pytest
"""
在测试函数中返回非None值(参数化：parametrize)
"""
def foo(a, b):
    return a + 2 * b

@pytest.mark.parametrize(
    ["a", "b", "result"],
    [
        [1, 2, 5],
        [2, 3, 8],
        [5, 3, 11],
    ],
)
def test_foo(a, b, result):
    return foo(a, b) == result