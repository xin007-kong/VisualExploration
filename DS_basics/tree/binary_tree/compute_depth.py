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


def max_depth(root, depth=1):
    print("-----" * depth)
    if not root:
        print("max_depth(None)开始递归")
        print("max_depth(None)结束，返回值为：0")
        print("-----" * depth)
        return 0
    print(f"max_depth({root.value})开始递归")
    left_depth = max_depth(root.left, depth + 1)
    right_depth = max_depth(root.right, depth + 1)
    result = max(left_depth, right_depth) + 1
    print(f"max_depth({root.value})结束，返回值为：{result}")
    print("-----" * depth)
    return result


# 示例用法
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print("计算二叉树深度：")
print("二叉树的深度为：", max_depth(root))
