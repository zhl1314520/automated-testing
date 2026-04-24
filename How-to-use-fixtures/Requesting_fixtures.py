import pytest

"""
依赖注入
"""
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False  # 默认未切块

    def cube(self):
        """
        是否切块
        :return:
        """
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        """
        *fruit_bowl: 表示接收多个参数(会变成一个 tuple)，如：FruitSalad(f1, f2) == self.fruit = (f1, f2)
        :param fruit_bowl:
        """
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


@pytest.fixture
def fruit_bowl():
    """
    提供测试数据
    :return: 返回一个“水果列表”
    """
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):   # 依赖注入fruit_bowl, 把返回值传入函数中
    fruit_salad = FruitSalad(*fruit_bowl)

    # 验证 FruitSalad 在初始化时，是否会把所有水果都切块
    for fruit in fruit_salad.fruit:
        assert fruit.cubed is True