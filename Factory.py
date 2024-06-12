from abc import ABC, abstractmethod
from TreeNode import ContainerNode, LeafNode
from TreeNode import RectangleContainer, RectangleLeaf


# 抽象工厂
class StyleFactory(ABC):
    def __init__(self, iconFamily=None):
        self.iconFamily = iconFamily

    @abstractmethod
    def build_Container(self, name, level=0):
        pass

    @abstractmethod
    def build_leaf(self, name, value=None):
        pass


# 具体工厂（树形风格）
class TreeStyleFactory(StyleFactory):
    def build_Container(self, name, level=0):
        return ContainerNode(name, level, self.iconFamily)

    def build_leaf(self, name, value=None):
        return LeafNode(name, value, self.iconFamily)


# 具体工厂（矩形风格）
class RectangleStyleFactory(StyleFactory):
    def build_Container(self, name, level=0):
        return RectangleContainer(name, level, self.iconFamily)

    def build_leaf(self, name, value=None):
        return RectangleLeaf(name, value, self.iconFamily)
