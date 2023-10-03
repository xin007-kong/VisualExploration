class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_thread = False
        self.right_thread = False

def inorder_successor(node: Node) -> Node:
    if node.right_thread:
        return node.right
    else:
        node = node.right
        while node is not None and not node.left_thread:
            node = node.left
        return node

def inorder_traversal(root: Node) -> None:
    node = root
    while node.left is not None:
        node = node.left
    while node is not None:
        print(f"当前节点值为：{node.val}")
        if node.left_thread:
            if node.left is not None:
                print(f"节点{node.val}的左子树为空，左子树线索指向节点{node.left.val}")
            else:
                print(f"节点{node.val}的左子树为空，左子树线索指向None")
        if node.right_thread:
            if node.right is not None:
                print(f"节点{node.val}的右子树为空，右子树线索指向节点{node.right.val}")
            else:
                print(f"节点{node.val}的右子树为空，右子树线索指向None")
        node = inorder_successor(node)
    print()

def make_inorder_threaded(node: Node, prev: Node) -> None:
    if node is None:
        return
    make_inorder_threaded(node.left, prev)
    if node.left is None:
        node.left_thread = True
        node.left = prev
        if prev is not None:
            print(f"节点{node.val}的左子树为空，左子树线索指向节点{prev.val}")
        else:
            print(f"节点{node.val}的左子树为空，左子树线索指向None")
    if prev is not None and prev.right is None:
        prev.right_thread = True
        prev.right = node
        print(f"节点{prev.val}的右子树为空，右子树线索指向节点{node.val}")
    prev = node
    make_inorder_threaded(node.right, prev)

# 创建一个二叉树
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

prev = None
make_inorder_threaded(root, prev)

# 中序遍历线索二叉树
print("中序遍历线索二叉树：")
inorder_traversal(root)