import pytest

"""
usefixtures: 自动使用 fixture
"""
@pytest.mark.usefixtures("driver")
class TestLogin:
    pass