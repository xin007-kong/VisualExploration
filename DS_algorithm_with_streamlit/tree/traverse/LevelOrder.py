"""
智慧校园导航系统
-----------------
这是一个使用完全二叉树结构表示校园建筑物的导航系统。通过这个系统，我们将学习以下内容：

学习目标：
1. 了解完全二叉树的基本结构。
2. 学习如何使用层次遍历算法（BFS）遍历完全二叉树。
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


def bfs(root, graph):
    visited_order = []
    queue = [root]
    process_log = []

    while queue:
        current = queue.pop(0)
        process_log.append(f"出队: {current.name}")
        visited_order.append(current.name)

        if current.left:
            queue.append(current.left)
            graph.add_edge(current.name, current.left.name)
            process_log.append(f"入队: {current.left.name}")
        if current.right:
            queue.append(current.right)
            graph.add_edge(current.name, current.right.name)
            process_log.append(f"入队: {current.right.name}")
    return visited_order, process_log


def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True,
            node_size=3000, node_color="skyblue", ax=ax)
    return fig


def main():
    st.title("智慧校园导航系统")

    # 创建建筑物
    library = Building("Library")
    gym = Building("Gym")
    cafe = Building("Cafe")
    auditorium = Building("Auditorium")
    lab = Building("Lab")
    dorm = Building("Dorm")
    field = Building("Field")

    # 设置完全二叉树结构
    library.left = gym
    library.right = cafe
    gym.left = auditorium
    gym.right = lab
    cafe.left = dorm
    cafe.right = field

    # 使用BFS进行遍历
    G = nx.Graph()
    visited_order, process_log = bfs(library, G)

    # 使用Streamlit显示结果
    st.write("遍历的顺序:", visited_order)
    st.write("执行过程:")
    for log in process_log:
        st.write(log)
    st.pyplot(visualize_graph(G))


if __name__ == "__main__":
    main()
