import streamlit as st
from graphviz import Digraph


class TreeNode:
    """树节点类，每个节点都有一个值和一个子节点列表。"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        """给当前节点添加一个子节点。"""
        self.children.append(child)


def render_tree(node, graph=None):
    """递归函数，用于渲染树。使用Graphviz来创建树的图形表示。"""
    if graph is None:
        graph = Digraph('Tree', node_attr={'shape': 'ellipse', 'height': '.1'})

    for child in node.children:
        graph.edge(str(node.value), str(child.value))
        render_tree(child, graph)

    return graph


def main():
    """主应用函数，用于显示Streamlit界面和处理用户输入。"""

    st.title("数据结构：树的可视化")

    # 侧边栏：添加节点
    st.sidebar.header("添加节点")
    parent_value = st.sidebar.text_input("父节点值 (如果是根节点，请留空)", value="")
    child_value = st.sidebar.text_input("子节点值", value="")

    # 初始化session_state
    if "nodes" not in st.session_state:
        st.session_state.nodes = {}

    # 当用户点击"添加"按钮时，添加新的节点
    if st.sidebar.button("添加"):
        if child_value:
            child_node = TreeNode(child_value)
            st.session_state.nodes[child_value] = child_node

            if parent_value:
                parent_node = st.session_state.nodes.get(parent_value)
                if parent_node:
                    parent_node.add_child(child_node)
            else:
                st.session_state.nodes["root"] = child_node

    # 渲染并显示树结构
    if "root" in st.session_state.nodes:
        tree_graph = render_tree(st.session_state.nodes["root"])
        st.graphviz_chart(str(tree_graph))
    else:
        st.write("请从侧边栏开始添加节点。")


if __name__ == "__main__":
    main()
