import pytest


@pytest.mark.parametrize("email,password", [
    ("a@163.com", "123"),
    ("b@163.com", "456"),
])
def test_login(email, password):
    pass