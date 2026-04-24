import pytest
import numpy

"""
关于近似相等的断言
"""
def test_floats():
    assert (0.1 + 0.2) == pytest.approx(0.3)


def test_arrays():
    a = numpy.array([1.0, 2.0, 3.0])    # 原生列表 -> 为一个 NumPy 数组
    b = numpy.array([0.9999, 2.0001, 3.0])
    assert a == pytest.approx(b), "arrays are not equal，抛出 AssertionError"  # approx 近似相等函数
    # 输出报错的原因
    """
    a == pytest.approx(b)：本质上会有三个 bool 值，但是 assert 只会比较一个 bool 值，assert 不知道比较哪个。
    """