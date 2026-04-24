import pytest

"""
关于预期异常的断言
"""
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    # 如果代码真的抛出了指定的异常，测试通过，match 匹配异常，刚好 123 匹配上Exception 123 raised
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

def test_exception_in_group():
    with pytest.RaisesGroup(ValueError):
        raise ExceptionGroup("group msg", [ValueError("value msg")])
    with pytest.RaisesGroup(ValueError, TypeError):
        raise ExceptionGroup("msg", [ValueError("foo"), TypeError("bar")])


def test_raisesgroup_match_and_check():
    with pytest.RaisesGroup(BaseException, match="my group msg"):
        raise BaseExceptionGroup("my group msg", [KeyboardInterrupt()])
    with pytest.RaisesGroup(
        Exception, check=lambda eg: isinstance(eg.__cause__, ValueError)
    ):
        raise ExceptionGroup("", [TypeError()]) from ValueError()

"""
ExceptionGroup: 支持python 3.11以上
"""
import sys
if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup   # 3.10 版本

def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:  # 把捕获到的异常组包装在 excinfo 对象里
        raise ExceptionGroup(
            "Exception Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)

def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Exception Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    # depth 指的是 ExceptionGroup 的嵌套层级
    """
    ExceptionGroup: depth=0
    RuntimeError、名为”Nested group“的容器：depth = 1
    TypeError: depth = 2
    """
    assert excinfo.group_contains(RuntimeError, depth=1)    # 主异常组直接包含的内容
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)

def f():
    raise ExceptionGroup("索引异常", [IndexError()])
# xfail: 告诉 pytest：“这个测试用例我知道它会失败（会抛出异常），请不要把它当成普通的 Bug（Failure）来处理。
@pytest.mark.xfail(raises=ExceptionGroup)
def test_f():
    f()