import pytest

"""
filterwarnings: 过滤警告
"""
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_api():
    pass