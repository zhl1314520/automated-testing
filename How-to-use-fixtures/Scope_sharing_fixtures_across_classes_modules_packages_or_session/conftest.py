import smtplib

import pytest
"""
作用范围：
    function > class > module > package > session
"""




"""
scope 参数：module     (运行 10 个测试文件会创建 10 次)
                        在同一个 .py 文件里，不管有多少个类和函数，固件只创建一次
"""
@pytest.fixture(scope="module") # scope="module": 在同一个模块中只会创建一次
def smtp_connection_module():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # 5秒超时，防止网络卡死时测试无限期挂起




"""
scope 参数：session    ：从输入 pytest 开始，到所有测试结束，它只创建一次
"""
@pytest.fixture(scope="session")
def smtp_connection_session():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # 5秒超时，防止网络卡死时测试无限期挂起




"""
scope 参数：function   (运行 10 个测试文件（每个文件 10 个用例）会创建 100 次)
                        每个测试函数运行前都会新建一个，运行完立刻销毁
"""
@pytest.fixture(scope="function")
def smtp_connection_function():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # 5秒超时，防止网络卡死时测试无限期挂起




"""
scope 参数：class      (每一个 Class 创建一次)
                        如果一个测试类（Class）里有 5 个测试方法，这个固件只会在该类开始时创建一次，全类共享.
"""
@pytest.fixture(scope="class")
def smtp_connection_class():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # 5秒超时，防止网络卡死时测试无限期挂起





"""
scope 参数：package    : 在同一个文件夹（包含 __init__.py 的包）下，所有子目录的所有测试文件共享(创建 1 次)
"""
@pytest.fixture(scope="package")
def smtp_connection_package():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # 5秒超时，防止网络卡死时测试无限期挂起
