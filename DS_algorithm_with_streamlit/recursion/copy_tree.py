import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def plot_tree(tree, pos=None, ax=None, depth=0, width=2):
    if pos is None:
        pos = {tree.value: (0, 0)}
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 12))
    if tree.left:
        pos[tree.left.value] = (pos[tree.value][0] -
                                width/2**depth, pos[tree.value][1] - 1)
        ax.plot([pos[tree.value][0], pos[tree.left.value][0]],
                [pos[tree.value][1], pos[tree.left.value][1]], 'k-')
        plot_tree(tree.left, pos, ax, depth+1)
    if tree.right:
        pos[tree.right.value] = (
            pos[tree.value][0] + width/2**depth, pos[tree.value][1] - 1)
        ax.plot([pos[tree.value][0], pos[tree.right.value][0]],
                [pos[tree.value][1], pos[tree.right.value][1]], 'k-')
        plot_tree(tree.right, pos, ax, depth+1)
    ax.text(pos[tree.value][0], pos[tree.value][1], str(tree.value),
            ha='center', va='center', bbox=dict(facecolor='white'))
    return pos


def copy_tree(tree, ax_orig, ax_copy, pos_orig, pos_copy=None, depth=0):
    if tree is None:
        return None

    if pos_copy is None:
        pos_copy = {tree.value: (0, 0)}

    new_node = Node(tree.value)
    ax_copy.text(pos_copy[tree.value][0], pos_copy[tree.value][1], str(tree.value),
                 bbox=dict(facecolor='cyan', edgecolor='black'))

    if tree.left:
        pos_copy[tree.left.value] = (
            pos_copy[tree.value][0] - 1 / (2 ** (depth + 1)), pos_copy[tree.value][1] - 1)
        ax_copy.plot([pos_copy[tree.value][0], pos_copy[tree.left.value][0]],
                     [pos_copy[tree.value][1], pos_copy[tree.left.value][1]], 'k-')
        new_node.left = copy_tree(
            tree.left, ax_orig, ax_copy, pos_orig, pos_copy, depth+1)

    if tree.right:
        pos_copy[tree.right.value] = (
            pos_copy[tree.value][0] + 1 / (2 ** (depth + 1)), pos_copy[tree.value][1] - 1)
        ax_copy.plot([pos_copy[tree.value][0], pos_copy[tree.right.value][0]],
                     [pos_copy[tree.value][1], pos_copy[tree.right.value][1]], 'k-')
        new_node.right = copy_tree(
            tree.right, ax_orig, ax_copy, pos_orig, pos_copy, depth+1)

    return new_node


# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 12))
ax1.set_title("Original Tree")
ax2.set_title("Copied Tree")
pos_orig = plot_tree(root, ax=ax1)
copy_tree(root, ax1, ax2, pos_orig)
plt.show()
