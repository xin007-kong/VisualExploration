import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.value, pos=(x, y))
        if node.left:
            graph.add_edge(node.value, node.left.value)
            l = x - 1 / 2 ** layer
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            r = x + 1 / 2 ** layer
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_binary_tree(tree_root):
    graph = nx.DiGraph()
    graph = add_edges(graph, tree_root, pos={})
    pos = nx.get_node_attributes(graph, 'pos')
    fig, ax = plt.subplots()
    nx.draw(graph, pos=pos, with_labels=True, arrows=False, ax=ax)
    return fig


def main():
    st.title("二叉树可视化")

    # 示例树
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    # 使用Streamlit显示图形
    st.pyplot(draw_binary_tree(root))


if __name__ == "__main__":
    main()
