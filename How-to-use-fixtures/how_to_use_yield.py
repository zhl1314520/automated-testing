import pytest

"""
yield 的使用
"""
@pytest.fixture
def db_session():
    # --- 第一阶段：Setup (测试前) ---
    print("\n[连接数据库] 正在建立连接...")
    db = {"data": "初始数据", "connected": True}

    yield db  # 这里的 db 会传给下面的测试函数

    # --- 第二阶段：Teardown (测试后) ---
    print("\n[断开数据库] 正在清理数据并关闭连接...")
    db["connected"] = False
    db["data"] = None


def test_db_update(db_session):
    print("  -> 执行测试：正在修改数据...")
    db_session["data"] = "新数据"
    assert db_session["data"] == "新数据"
    # 注意：即便这里 assert 失败，下面的 Teardown 依然会执行！

"""
yield 和 return 的区别：
    特性              return                              yield
测试前准备（setup）	✅ 支持	                            ✅ 支持
测试后清理(teardown)	❌ 不支持（代码在 return 后就不执行了）	✅ 支持
异常安全性	        ❌ 测试崩了，清理代码跑不到	            ✅ 测试崩了，清理代码依然跑
"""