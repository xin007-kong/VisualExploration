import streamlit as st
import sys
import pandas as pd
sys.path.append("../")

from stack_class.stack import Stack

# 初始化 Streamlit session state
if 'stack' not in st.session_state:
    st.session_state.stack = Stack()

st.title("学习栈的基本操作")

# 使用 DataFrame 和 Streamlit 的 table 组件来动态显示栈的内容
stack_df = pd.DataFrame(st.session_state.stack.items, columns=["栈内容"])
st.table(stack_df[::-1])  # 反转 DataFrame 以使栈顶在上方

# 输入元素并压入栈
item = st.text_input("输入一个元素并将其压入栈中:")
push_button = st.button("压入元素")
if push_button and item:
    st.session_state.stack.push(item)
    st.success(f"元素 {item} 已被压入栈中。")

# 从栈中弹出元素
if st.button("从栈中弹出元素"):
    popped_item = st.session_state.stack.pop()
    if popped_item:
        st.success(f"元素 {popped_item} 已从栈中弹出。")
    else:
        st.error("栈是空的，无法弹出元素。")

# 显示栈顶元素
st.write("栈顶元素：", st.session_state.stack.peek() if not st.session_state.stack.is_empty() else "栈是空的")

# 显示栈的大小
st.write("栈的大小：", st.session_state.stack.size())

# 提供其他操作选项
if st.button("清空栈"):
    while not st.session_state.stack.is_empty():
        st.session_state.stack.pop()
    st.success("栈已清空。")

# 提供操作说明
st.subheader("操作说明")
st.write("""
- **压入元素**：在输入框中输入一个元素，然后点击“压入元素”按钮。
- **从栈中弹出元素**：点击“从栈中弹出元素”按钮。
- **清空栈**：点击“清空栈”按钮。
""")

# 提供实时的指导和反馈
st.subheader("学习指导")
if st.session_state.stack.is_empty():
    st.write("你的栈是空的。试着添加一些元素进去!")
else:
    st.write("很好! 你可以继续添加更多的元素，或者尝试从栈中弹出元素。")