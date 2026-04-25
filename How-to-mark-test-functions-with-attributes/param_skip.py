import pytest
import sys


@pytest.mark.skip(reason="功能未开发完成")
def test_login():
    pass


# 有条件的跳过
@pytest.mark.skipif(sys.platform == "win32", reason="Windows不支持")
def test_linux_only():
    pass