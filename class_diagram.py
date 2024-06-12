from anytree import Node, RenderTree, AsciiStyle

root = Node("Class Diagram")

style_factory = Node("StyleFactory", parent=root)
tree_style_factory = Node("TreeStyleFactory", parent=style_factory)
rectangle_style_factory = Node("RectangleStyleFactory", parent=style_factory)
fje_builder = Node("FJEBuilder", parent=root)
fje = Node("FJE", parent=root)
icon_family = Node("IconFamily", parent=root)
tree_node = Node("TreeNode", parent=root)
container_node = Node("ContainerNode", parent=tree_node)
rectangle_container = Node("RectangleContainer", parent=container_node)
leaf_node = Node("LeafNode", parent=tree_node)
rectangle_leaf = Node("RectangleLeaf", parent=leaf_node)

# Attributes and methods for each class
# StyleFactory
Node("- iconFamily: IconFamily", parent=style_factory)
Node("+ build_Container(name, level): ContainerNode", parent=style_factory)
Node("+ build_leaf(name, value): LeafNode", parent=style_factory)

# TreeStyleFactory and RectangleStyleFactory inherit StyleFactory
Node("+ build_Container(name, level): ContainerNode", parent=tree_style_factory)
Node("+ build_leaf(name, value): LeafNode", parent=tree_style_factory)
Node("+ build_Container(name, level): ContainerNode", parent=rectangle_style_factory)
Node("+ build_leaf(name, value): LeafNode", parent=rectangle_style_factory)

# FJEBuilder
Node("- factory: StyleFactory", parent=fje_builder)
Node("+ build_root(data, level): ContainerNode", parent=fje_builder)
Node("+ build_child(name, value, level): TreeNode", parent=fje_builder)

# FJE
Node("- filepath: str", parent=fje)
Node("- factory: StyleFactory", parent=fje)
Node("- root: ContainerNode", parent=fje)
Node("+ _load(): None", parent=fje)
Node("+ show(): None", parent=fje)

# IconFamily
Node("- composite_icon: str", parent=icon_family)
Node("- leaf_icon: str", parent=icon_family)

# TreeNode
Node("- iconFamily: IconFamily", parent=tree_node)
Node("+ draw(level, prefix): None", parent=tree_node)

# ContainerNode
Node("- name: str", parent=container_node)
Node("- level: int", parent=container_node)
Node("- children: list", parent=container_node)
Node("+ Add_ChildNode(child): None", parent=container_node)
Node("+ draw(flag, level, prefix): None", parent=container_node)

# RectangleContainer inherits ContainerNode
Node("+ draw(flag, level, prefix): None", parent=rectangle_container)

# LeafNode
Node("- name: str", parent=leaf_node)
Node("- value: any", parent=leaf_node)
Node("+ draw(flag, level, prefix): None", parent=leaf_node)

# RectangleLeaf inherits LeafNode
Node("+ draw(flag, level, prefix): None", parent=rectangle_leaf)

# Render the tree to get a textual representation
for pre, _, node in RenderTree(root, style=AsciiStyle()):
    print(f"{pre}{node.name}")

