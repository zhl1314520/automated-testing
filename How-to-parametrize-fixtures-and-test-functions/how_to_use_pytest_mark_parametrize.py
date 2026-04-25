import pytest

"""
参数化
"""
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected # eval() 函数用来将str转为数字计算


# 类参数化
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


# 加上预期结果预判
@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 52, marks=pytest.mark.xfail)],
)   # marks=pytest.mark.xfail 预期失败（6*9 ！= 52）
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# 多个参数
"""
笛卡尔积：
    (0,2)
    (1,2)
    (0,3)
    (1,3)
"""
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    assert (x, y)