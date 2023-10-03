from prettytable import PrettyTable

class HuffmanNode:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

def build_huffman_tree(weights):
    # 构建哈夫曼树
    nodes = [HuffmanNode(i, w) for i, w in enumerate(weights)]
    index = len(nodes)
    while len(nodes) > 1:
        # 选取权值最小的两个节点
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        # 将它们作为左右子节点，构建一个新的节点作为它们的父节点
        parent = HuffmanNode(index, left.freq + right.freq, left, right)
        index += 1

        # 将新节点插入到列表中
        nodes.append(parent)

        # 打印信息
        print(f"合并节点 {left.value} 和 {right.value}，生成新节点 {parent.value}，权重为 {parent.freq}")

    # 返回哈夫曼树的根节点
    return nodes[0]

def print_huffman_tree(root):
    # 创建表格
    table = PrettyTable()
    table.field_names = ["Index", "Weight", "Parent", "Left Child", "Right Child"]

    # 遍历哈夫曼树，将每个节点添加到表格中
    queue = [(root, None)]
    while queue:
        node, parent = queue.pop(0)
        table.add_row([node.value, node.freq, parent.value if parent else '', node.left.value if node.left else '', node.right.value if node.right else ''])
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))

    # 打印表格
    print(table)

# 测试代码
weights = [5, 29, 7, 8, 14, 23, 3, 11]
root = build_huffman_tree(weights)
print_huffman_tree(root)