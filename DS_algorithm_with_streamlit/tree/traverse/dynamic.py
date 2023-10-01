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


def preorder_traversal(root, result=[], explanation=[], depth=0):
    indent = "  " * depth
    if root:
        result.append(root.value)
        explanation.append(f"{indent}访问节点 {root.value}")
        explanation.append(f"{indent}向左递归遍历子树")
        preorder_traversal(root.left, result, explanation, depth + 1)
        explanation.append(f"{indent}向右递归遍历子树")
        preorder_traversal(root.right, result, explanation, depth + 1)
    else:
        explanation.append(f"{indent}遇到空节点，返回")
    return result, explanation

# 添加节点的简单实现


def add_node(root, value):
    if not root:
        return TreeNode(value)
    else:
        # 这里可以实现添加节点的逻辑，例如添加为左子节点或右子节点
        # 暂时为简单起见，我们添加到左子节点
        if not root.left:
            root.left = TreeNode(value)
        elif not root.right:
            root.right = TreeNode(value)
    return root


def main():
    st.title("二叉树可视化与交互")

    # 使用session state存储二叉树
    if 'tree_root' not in st.session_state:
        st.session_state.tree_root = TreeNode(
            1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    # 添加节点
    add_value = st.text_input("请输入要添加的节点值:")
    if st.button("添加节点"):
        if add_value:
            st.session_state.tree_root = add_node(
                st.session_state.tree_root, int(add_value))
            st.write(f"添加了节点: {add_value}")
            st.pyplot(draw_binary_tree(st.session_state.tree_root))

    # 删除节点功能可以类似地实现

    # 遍历二叉树
    traversal_type = st.selectbox("选择遍历方式", ["先序遍历", "中序遍历", "后序遍历"])
    if st.button("开始遍历"):
        explanation = []
        result = []
        if traversal_type == "先序遍历":
            result, explanation = preorder_traversal(
                st.session_state.tree_root, [], explanation)
        # 中序和后序遍历的递归过程也可以类似地进行修改
        st.write(f"{traversal_type}结果: {result}")
        for step in explanation:
            st.text(step)


if __name__ == "__main__":
    main()
