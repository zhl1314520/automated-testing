import pytest


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        data = None
    else:
        data = marker.args[0]

    return data


@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt == 42