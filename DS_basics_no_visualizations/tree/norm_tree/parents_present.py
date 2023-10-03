class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

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
        return [n for n in self.nodes if n.parent == node]

    def get_root(self):
        return self.root