"""
智慧校园导航系统
-----------------
这是一个允许用户按照满二叉树的序号添加节点的导航系统。

学习目标：
1. 了解满二叉树的基本结构。
2. 学习如何按照满二叉树的序号添加节点。
3. 使用Streamlit进行数据可视化。
"""

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

class Building:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def insert_node(root, name, index):
    if index == 1:
        if not root:
            return Building(name)
        else:
            return root
    else:
        if index % 2 == 0:
            root.left = insert_node(root.left, name, index // 2)
        else:
            root.right = insert_node(root.right, name, index // 2)
    return root

def visualize_tree(root, graph, pos=None, x=0, y=0, layer=1):
    if root is not None:
        graph.add_node(root.name, pos=(x, y))
        if root.left:
            graph.add_edge(root.name, root.left.name)
            l = x - 1 / 2 ** layer
            visualize_tree(root.left, graph, pos, x=l, y=y-1, layer=layer+1)
        if root.right:
            graph.add_edge(root.name, root.right.name)
            r = x + 1 / 2 ** layer
            visualize_tree(root.right, graph, pos, x=r, y=y-1, layer=layer+1)
    return graph

def main():
    st.title("智慧校园导航系统")

    st.sidebar.header("添加建筑物")
    name = st.sidebar.text_input("建筑物名称:")
    index = st.sidebar.number_input("满二叉树序号:", min_value=1, value=1, step=1)
    add_button = st.sidebar.button("添加")

    if 'tree_root' not in st.session_state:
        st.session_state.tree_root = None

    if add_button and name:
        st.session_state.tree_root = insert_node(st.session_state.tree_root, name, index)

    if st.session_state.tree_root:
        G = nx.Graph()
        visualize_tree(st.session_state.tree_root, G)
        pos = nx.get_node_attributes(G, 'pos')
        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", ax=ax)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
