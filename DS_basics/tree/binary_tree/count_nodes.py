"""
下面的例子树是：
         1
        / \
       2   3
      / \
     4   5
    /
   6
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_separator(char="@", length=50):
    """打印分隔符"""
    print(char * length)


def count_nodes(root, parent=None, direction=None):
    if not root:
        if parent:
            print_separator("=")
            print(f"count_nodes(None)开始递归，此为节点{parent.value}的{direction}子树")
        else:
            print_separator("=")
            print("count_nodes(None)开始递归")
        print("count_nodes(None)结束，返回值为：0")
        print_separator("=")
        return 0

    if parent:
        print_separator()
        print(f"从节点{parent.value}进入其{direction}子节点{root.value}")
    print_separator("=")
    print(f"count_nodes({root.value})开始递归")

    left_count = count_nodes(root.left, root, "左")
    right_count = count_nodes(root.right, root, "右")
    result = left_count + right_count + 1
    print(f"节点{root.value}的左子树节点总数为：{left_count}")
    print(f"节点{root.value}的右子树节点总数为：{right_count}")
    print(f"加上节点{root.value}本身，所以节点{root.value}的节点总数为：{result}")
    print(f"count_nodes({root.value})结束，返回值为：{result}")
    if parent:
        print(f"从节点{root.value}返回节点{parent.value}，继续调用count_nodes")
    print_separator("=")
    return result


# 示例用法
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print("计算二叉树节点总数：")
print_separator("*", 60)
print("二叉树的节点总数为：", count_nodes(root))
print_separator("*", 60)
