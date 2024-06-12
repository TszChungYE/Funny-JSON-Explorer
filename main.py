import json
import argparse
from Factory import TreeStyleFactory, RectangleStyleFactory


class FJEBuilder:
    def __init__(self, factory):
        self.factory = factory

    # 构建根节点
    def build_root(self, data, level=0):
        if isinstance(data, dict):
            composite_node = self.factory.build_Container("", level)
            for key, value in data.items():
                composite_node.Add_ChildNode(self.build_child(key, value, level + 1))
            return composite_node
        elif isinstance(data, list):
            composite_node = self.factory.build_Container("", level)
            for index, item in enumerate(data):
                composite_node.Add_ChildNode(self.build_child(f"[{index}]", item, level + 1))
            return composite_node
        else:
            raise ValueError("Value Error")

    # 构建子节点
    def build_child(self, name, value, level=0):
        if isinstance(value, dict) or isinstance(value, list):
            composite_node = self.factory.build_Container(name, level)
            if isinstance(value, dict):
                for key, val in value.items():
                    composite_node.Add_ChildNode(self.build_child(key, val, level + 1))
            else:
                for index, item in enumerate(value):
                    composite_node.Add_ChildNode(self.build_child(f"[{index}]", item, level + 1))
            return composite_node
        else:
            return self.factory.build_leaf(name, value)


class FJE:
    def __init__(self, filepath, factory):
        self.filepath = filepath
        self.factory = factory
        self.root = None

    # 加载并构建树结构
    def _load(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
        builder = FJEBuilder(self.factory)
        self.root = builder.build_root(data)

    # 绘制结果
    def show(self):
        self._load()
        if self.root:
            i = 0
            for child in self.root.children:
                if i < len(self.root.children) - 1:
                    child.draw(False, 0, "├─ ")
                else:
                    child.draw(True, 0, "├─ ")
                i += 1


class IconFamily:
    def __init__(self, composite_icon, leaf_icon):
        self.composite_icon = composite_icon
        self.leaf_icon = leaf_icon


poker_face_icon_family = IconFamily(composite_icon="♢", leaf_icon="♤")

if __name__ == "__main__":
    # 解析命令：fje -f <json file> -s <style> -i <icon family>
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-s', '--style', type=str, choices=['tree', 'rectangle'], required=True)
    parser.add_argument('-i', '--icon', type=str, choices=['default', 'poker'], default='default')
    args = parser.parse_args()

    # 选择图标族
    if args.icon == 'default':
        icon_family = IconFamily(composite_icon="", leaf_icon="")
    else:
        icon_family = IconFamily(composite_icon="♢", leaf_icon="♤")

    # 选择风格
    if args.style == 'tree':
        factory = TreeStyleFactory(iconFamily=icon_family)
    elif args.style == 'rectangle':
        factory = RectangleStyleFactory(iconFamily=icon_family)

    # 运行fje
    fje = FJE(args.file, factory)
    fje.show()
