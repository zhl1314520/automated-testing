from test_foocompare import Foo
"""
自定义错误断言
"""
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   values: {left.val} != {right.val}",
        ]