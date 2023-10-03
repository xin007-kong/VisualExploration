from heapq import heappush, heappop
from collections import defaultdict


class HuffmanNode:
    def __init__(self, value=None, freq=0, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right
        self.index = -1  # 初始化index为-1

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(data):
    # 统计字符频率
    freqs = defaultdict(int)
    for char in data:
        freqs[char] += 1

    # 初始化节点列表
    nodes_list = []

    # 构建哈夫曼树
    heap = [HuffmanNode(char, freq) for char, freq in freqs.items()]
    for i in range(len(heap)):
        heap[i].index = i
        nodes_list.append(heap[i])  # 添加到节点列表
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        parent = HuffmanNode(freq=left.freq + right.freq,
                             left=left, right=right)
        parent.index = len(nodes_list)  # 使用节点列表的长度作为索引
        heappush(heap, parent)
        nodes_list.append(parent)  # 添加新生成的节点到列表

        # 打印信息
        print(f"合并节点 {left.index}({left.value}:{left.freq}) 和 {right.index}({right.value}:{right.freq})，生成新节点 {parent.index}({parent.freq})")

    # 打印哈夫曼树表格
    print_huffman_tree(heap[0])

    # 返回哈夫曼树的根节点
    return heap[0]


def build_huffman_table(root):
    # 构建哈夫曼编码表
    table = {}
    stack = [(root, "")]
    while stack:
        node, code = stack.pop()
        if node.value is not None:
            table[node.value] = code
        if node.left is not None:
            stack.append((node.left, code + "0"))
        if node.right is not None:
            stack.append((node.right, code + "1"))
    return table


def encode(data, table):
    # 哈夫曼编码
    encoded = "".join(table[char] for char in data)

    # 打印信息
    print(f"原始数据：{data}")
    print(f"编码后的数据：{encoded}")

    return encoded


def decode(data, root):
    # 哈夫曼解码
    result = []
    node = root
    for bit in data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.value is not None:
            result.append(node.value)
            node = root

    # 打印信息
    decoded = "".join(result)
    print(f"解码后的数据：{decoded}")

    return decoded

def print_huffman_tree(root):
    # 打印哈夫曼树表格

    # 收集所有节点
    nodes = []
    stack = [(root, root.freq, "", "")]
    while stack:
        node, weight, parent, direction = stack.pop()
        if node is not None:
            nodes.append(node)
            stack.append((node.left, node.left.freq if node.left else 0, str(node.index), direction + "0"))
            stack.append((node.right, node.right.freq if node.right else 0, str(node.index), direction + "1"))

    # 按索引排序
    nodes.sort(key=lambda x: x.index)

    print("-" * 69)
    print("| Index |  Node  | Weight | Parent | Left Child | Right Child |")
    print("-" * 69)

    for node in nodes:
        if node.value is not None:
            node_str = f"'{node.value}'"
        else:
            node_str = ""
        left_str = str(node.left.index) if node.left else ""
        right_str = str(node.right.index) if node.right else ""
        print(f"|{node.index:^7}|{node_str:^8}|{node.freq:^8}|{'':^8}|{left_str:^12}|{right_str:^13}|")

    print("-" * 69)



# 测试代码
data = "This is a test message for Huffman coding."
root = build_huffman_tree(data)
table = build_huffman_table(root)
encoded = encode(data, table)
decoded = decode(encoded, root)
