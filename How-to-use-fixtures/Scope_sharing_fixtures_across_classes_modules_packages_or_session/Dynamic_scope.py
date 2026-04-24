import pytest

"""
动态 scope
"""
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"

def spawn_container():
    print("\n[Docker] 正在启动容器...")
    return "Container-ID-123"

@pytest.fixture(scope=determine_scope)
def docker_container():
    container = spawn_container()
    yield container
    print(f"\n[Docker] 正在销毁容器: {container}")