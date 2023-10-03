from prettytable import PrettyTable
from collections import Counter
class HuffmanNode:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right


# def build_huffman_tree(data):
#     # 统计每个字符出现的频率
#     freq = {}
#     for c in data:
#         if c in freq:
#             freq[c] += 1
#         else:
#             freq[c] = 1

#     # 将每个字符和其频率封装成节点
#     nodes = []
#     for c in freq:
#         node = HuffmanNode(c, freq[c])
#         nodes.append(node)

#     # 构建Huffman树
#     while len(nodes) > 1:
#         # 按照频率从小到大排序
#         # lambda x: x.freq 作为函数，返回x.freq
#         nodes = sorted(nodes, key=lambda x: x.freq)
#         # 取出频率最小的两个节点
#         # pop是从列表中取出元素，pop(0)是从列表左边取出元素，sorted是python内置函数，sorted(iterable, key, reverse)，iterable是可迭代对象，key是排序函数，reverse是排序规则，reverse=True是降序，reverse=False是升序
#         left = nodes.pop(0)
#         right = nodes.pop(0)

#         # 构建新节点，新节点的频率为两个子节点的频率之和
#         parent = HuffmanNode(None, left.freq + right.freq)
#         parent.left = left
#         parent.right = right

#         nodes.append(parent)

#     # 返回根节点
#     return nodes[0]
def build_huffman_tree(data):
    # 统计每个字符在原始数据中出现的次数
    freq = Counter(data)

    # 将每个字符和其出现次数封装成一个节点
    nodes = [HuffmanNode(char, freq[char]) for char in freq]

    # 构建哈夫曼树
    while len(nodes) > 1:
        # 从节点列表中选出权值最小的两个节点
        left = min(nodes, key=lambda node: node.freq)
        nodes.remove(left)
        right = min(nodes, key=lambda node: node.freq)
        nodes.remove(right)

        # 将它们作为左右子节点，构建一个新的节点作为它们的父节点
        parent = HuffmanNode(None, left.freq + right.freq, left, right)

        # 将新节点添加到节点列表中
        nodes.append(parent)

        # 打印节点信息
        print(f"Combine {left.value}:{left.freq} and {right.value}:{right.freq} to {parent.freq}")

    # 返回哈夫曼树的根节点
    return nodes[0]


def print_huffman_tree(root):
    # 创建表格
    table = PrettyTable()
    table.field_names = ["Value", "Freq", "Parent", "Left Child", "Right Child"]

    # 遍历哈夫曼树，将每个节点的信息添加到表格中
    stack = [(root, None)]
    while stack:
        node, parent = stack.pop()
        table.add_row([node.value, node.freq, parent.value if parent else None, node.left.value if node.left else None, node.right.value if node.right else None])
        if node.left:
            stack.append((node.left, node))
        if node.right:
            stack.append((node.right, node))

    # 打印表格
    print(table)

def test_build_huffman_tree():
    data = "hello worldwwwwwwwwwwwwwwwwwwwwwww"
    root = build_huffman_tree(data)
    print_huffman_tree(root)

if __name__ == '__main__':
    # test_build_huffman_tree()
    data = ['a'] * 7 + ['b'] * 5 + ['c'] * 5 + ['d'] * 2 + ['e'] * 4
    root = build_huffman_tree(data)
    print_huffman_tree(root)


