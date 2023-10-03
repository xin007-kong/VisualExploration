# from binarytree import build

# # 生成一个随机的二叉树
# values = [3, 2, 4, 6, 7, 8, 3]
# binary_tree = build(values)

# # 输出二叉树
# print(binary_tree)
from anytree import Node, RenderTree

# 创建节点
root = Node("root")
child1 = Node("child1", parent=root)
child2 = Node("child2", parent=root)
child1_1 = Node("child1_1", parent=child1)
child1_2 = Node("child1_2", parent=child1)
child2_1 = Node("child2_1", parent=child2)

# 打印树
for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
