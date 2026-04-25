import pytest

"""
提前标记用例数据
"""
@pytest.fixture
def fixt(request):  # request: 获取当前用例 test_fixt所有信息
    marker = request.node.get_closest_marker("fixt_data")   # 获取当前用例 test_fixt的 fixt_data 标记
    if marker is None:
        data = None
    else:
        data = marker.args[6]   # index[6]

    yield data


@pytest.mark.fixt_data(42, 43, 44, 45, 46, 47, 48, 49, 50, 51)
def test_fixt(fixt):
    assert fixt == 48