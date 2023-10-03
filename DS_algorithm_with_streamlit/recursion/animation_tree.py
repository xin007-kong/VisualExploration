"""
使用Matplotlib可视化二叉树遍历：

1. Node：一个简单的类，表示二叉树节点，包含值、左子节点和右子节点。
2. build_sample_tree：构建一个用于可视化的示例二叉树。
3. plot_tree：递归绘制二叉树。返回线条列表（表示树的边缘）和文本列表（表示树的节点）。
4. animate_tree_traversal：动画演示先序遍历的过程。一个红点沿着树的边缘移动，节点在被访问时被揭示。

脚本的主要部分构建了一个示例树，绘制它，然后动画演示了遍历过程。
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def plot_tree(tree, ax):
    lines = []
    texts = []

    def draw(node, x, y, dx):
        if not node:
            return
        txt = ax.text(x, y, str(node.value), ha='center',
                      va='center', visible=False)
        texts.append(txt)
        if node.left:
            line, = ax.plot([x, x-dx], [y-1, y-2], 'k-', visible=False)
            lines.append(line)
            draw(node.left, x-dx, y-2, dx/2)
        if node.right:
            line, = ax.plot([x, x+dx], [y-1, y-2], 'k-', visible=False)
            lines.append(line)
            draw(node.right, x+dx, y-2, dx/2)
    draw(tree, x=0, y=0, dx=4)
    ax.axis('off')
    ax.set_aspect('equal')
    return lines, texts


def animate_tree_traversal(tree, ax, lines, texts):
    path = []

    def traverse_pre_order(node, parent_coords=None):
        if node is None:
            return
        x, y = parent_coords if parent_coords else (0, 0)
        path.append((x, y, node.value))
        if node.left:
            traverse_pre_order(node.left, (x-2, y-2))
        if node.right:
            traverse_pre_order(node.right, (x+2, y-2))
    traverse_pre_order(tree)

    point, = ax.plot([], [], 'ro')

    def init():
        point.set_data([], [])
        for line in lines:
            line.set_visible(False)
        for txt in texts:
            txt.set_visible(False)
        return point, *lines, *texts

    def update(num):
        x, y, val = path[num]
        point.set_data(x, y)
        for txt in texts:
            if txt.get_text() == str(val):
                txt.set_visible(True)
                break
        if num > 0:
            _, _, prev_val = path[num-1]
            for line in lines:
                xdata, ydata = line.get_xdata(), line.get_ydata()
                if (xdata[0], ydata[0]) == (x, y):
                    line.set_visible(True)
                    break
        return point, *lines, *texts

    ani = animation.FuncAnimation(ax.figure, update, frames=len(
        path), init_func=init, interval=1000, blit=True)
    plt.show()


fig, ax = plt.subplots()
root = build_sample_tree()
lines, texts = plot_tree(root, ax)
animate_tree_traversal(root, ax, lines, texts)
