import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


if "root" not in st.session_state:
  st.session_state.root = None


def visualize_tree(root):

  fig, ax = plt.subplots()

  tree = nx.DiGraph()
  queue = [root]

  while queue:
    curr_node = queue.pop(0)
    if curr_node.left:
      tree.add_edge(curr_node, curr_node.left)
      queue.append(curr_node.left)
    if curr_node.right:
      tree.add_edge(curr_node, curr_node.right)
      queue.append(curr_node.right)

  pos = nx.planar_layout(tree)
  nx.draw(tree, pos=pos, ax=ax)
  st.pyplot(fig)


# 输入新节点值
new_node_val = st.text_input("输入要添加的节点值:")

# 选择作为左子节点还是右子节点
position = st.radio("选择位置", ["左子节点", "右子节点"])

if st.button("添加节点"):
  if not st.session_state.root:
    st.session_state.root = TreeNode(new_node_val)
  else:
    new_node = TreeNode(new_node_val)
    if position == "左子节点":
      st.session_state.root.left = new_node
    else:
      st.session_state.root.right = new_node
  st.experimental_rerun()

# 输入要删除的节点值
del_node_val = st.text_input("输入要删除的节点值:")

if st.button("删除节点"):
  # 遍历树查找并删除节点
  ...

  st.experimental_rerun()

if st.button("显示树"):
  if st.session_state.root:
    visualize_tree(st.session_state.root)
