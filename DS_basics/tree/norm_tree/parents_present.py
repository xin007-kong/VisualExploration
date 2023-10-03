class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

class Tree:
    def __init__(self, root=None):
        self.nodes = []
        self.root = root

    def add_node(self, data, parent=None):
        node = TreeNode(data, parent)
        self.nodes.append(node)
        if parent is None:
            self.root = node
        else:
            parent.children.append(node)

    def get_parent(self, node):
        return node.parent

    def get_children(self, node):
        return node.children

    def get_root(self):
        return self.root

if __name__ == '__main__':
    # 创建树
    tree = Tree()
    node1 = TreeNode('A')
    node2 = TreeNode('B', node1)
    node3 = TreeNode('C', node1)
    node4 = TreeNode('D', node2)
    node5 = TreeNode('E', node2)
    node6 = TreeNode('F', node3)
    node7 = TreeNode('G', node3)
    tree.add_node(node1.data)
    tree.add_node(node2.data, node1)
    tree.add_node(node3.data, node1)
    tree.add_node(node4.data, node2)
    tree.add_node(node5.data, node2)
    tree.add_node(node6.data, node3)
    tree.add_node(node7.data, node3)

    # 测试获取父节点
    print("节点 {} 的父节点是 {}".format(node2.data, tree.get_parent(node2).data))
    print("节点 {} 的父节点是 {}".format(node3.data, tree.get_parent(node3).data))
    print("节点 {} 的父节点是 {}".format(node1.data, tree.get_parent(node1)))

    # 测试获取子节点
    children = tree.get_children(node1)
    print("节点 {} 的子节点是：".format(node1.data))
    for child in children:
        print(child.data)

    children = tree.get_children(node2)
    print("节点 {} 的子节点是：".format(node2.data))
    for child in children:
        print(child.data)

    children = tree.get_children(node3)
    print("节点 {} 的子节点是：".format(node3.data))
    for child in children:
        print(child.data)

    # 测试获取根节点
    print("根节点是：{}".format(tree.get_root().data))