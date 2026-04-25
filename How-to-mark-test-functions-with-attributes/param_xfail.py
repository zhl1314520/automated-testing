import pytest

"""
xfail: 预期失败
"""
@pytest.mark.xfail(reason="已知bug")
def test_bug():
    assert 1 == 2