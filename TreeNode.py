from abc import ABC, abstractmethod


# 抽象基类
class TreeNode(ABC):
    def __init__(self, iconFamily=None):
        self.iconFamily = iconFamily

    @abstractmethod
    def draw(self, level, prefix=""):
        pass


# 绘制中间节点
class ContainerNode(TreeNode):
    def __init__(self, name, level=0, icon_family=None):
        super().__init__(icon_family)
        self.name = name
        self.level = level
        self.children = []

    def Add_ChildNode(self, child):
        self.children.append(child)

    def draw(self, flag, level=0, prefix=""):
        icon = self.iconFamily.composite_icon if self.iconFamily else ""
        if flag:
            prefix = "└─ "
        print(f"{prefix}{icon}{self.name}")
        if self.children:
            last_child = self.children[-1]
            for child in self.children[:-1]:
                if not flag:
                    prefix_next = "| " + "  " * level + "   ├─ "
                else:
                    prefix_next = "  " * level + "   ├─ "
                child.draw(flag, level + 1, prefix_next)
            if flag:
                prefix_next = "  " * level + "   └─ "
            else:
                prefix_next = "| " + "  " * level + "   └─ "
            last_child.draw(flag, level + 1, prefix_next)


# 绘制矩形风格的中间节点
class RectangleContainer(ContainerNode):
    def draw(self, flag, level=0, prefix=""):
        icon = self.iconFamily.composite_icon if self.iconFamily else ""
        if level == 0 and not flag:
            print(f"┌─ {icon}{self.name} {'─' * (41 - len(self.name))}┐")
        else:
            print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")
        if self.children:
            last_child = self.children[-1]
            for child in self.children[:-1]:
                prefix_next = "|   " + "|" * level + " ├─ "
                child.draw(False, level + 1, prefix_next)
            if flag:
                prefix_next = "└─" + "─" * level + "───┴─ "
            else:
                prefix_next = "|   " + "| " * level + "├─ "
            last_child.draw(False, level + 1, prefix_next)


# 绘制叶子节点
class LeafNode(TreeNode):
    def __init__(self, name, value=None, icon_family=None):
        super().__init__(icon_family)
        self.name = name
        self.value = value

    # 绘图方法
    def draw(self, flag, level, prefix=""):
        icon = self.iconFamily.leaf_icon if self.iconFamily else ""
        if self.value:
            print(f"{prefix}{icon}{self.name}: {self.value}")
        else:
            print(f"{prefix}{icon}{self.name}")


# 绘制矩形风格的叶子节点
class RectangleLeaf(LeafNode):
    def draw(self, flag, level, prefix=""):
        icon = self.iconFamily.leaf_icon if self.iconFamily else ""
        if self.value:
            print(f"{prefix}{icon}{self.name}: {self.value} {'─' * (44 - len(self.name) - len(str(self.value)) - len(prefix) - 2)}┤")
        else:
            if prefix[0] == "└":
                print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┘")
            else:
                print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")
