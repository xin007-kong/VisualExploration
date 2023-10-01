import streamlit as st
import matplotlib.pyplot as plt

# 全局状态变量
state = st.session_state
if "array" not in state:
    state.array = None
    state.index = 0
    state.value = 0
    state.action = None
    state.step = 0
    state.message = ""


def plot_array():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(len(state.array)), state.array, color='skyblue')
    ax.set_ylim(0, max(state.array + [10]))
    ax.set_title("sequence list")
    st.pyplot(fig)


st.title("顺序表操作演示")

# 允许用户初始化数组
if not state.array:
    array_input = st.text_input("初始化你的数组（用 '@' 分隔每个值）：")
    if st.button("创建数组"):
        try:
            state.array = [int(x.strip()) for x in array_input.split('@') if x]
            state.message = "数组初始化成功！"
        except ValueError:
            st.error("请确保输入的是用'@'分隔的有效整数。")
else:
    # 用户输入
    state.action = st.selectbox("选择操作：", ["插入", "删除"])
    state.index = st.slider("选择位置（从0开始计数）：", 0, len(
        state.array)-1, state.index if state.index else 0)
    if state.action == "插入":
        state.value = st.slider(
            "选择要插入的值：", 1, 10, state.value if state.value else 1)

    # 逐步操作
    if st.button("执行步骤"):
        if state.action == "插入":
            if state.step < len(state.array) - state.index:
                state.array[-state.step-1] = state.array[-state.step-2]
                state.message = f"元素从位置{-state.step-2}移动到位置{-state.step-1}。"
            elif state.step == len(state.array) - state.index:
                state.array[state.index] = state.value
                state.message = f"在位置{state.index}插入了值{state.value}。"
                state.step = -1  # 重置为下一次操作
            state.step += 1
        elif state.action == "删除":
            if state.step < len(state.array) - state.index - 1:
                state.array[state.index +
                            state.step] = state.array[state.index + state.step + 1]
                state.message = f"元素从位置{state.index + state.step + 1}移动到位置{state.index + state.step}。"
            elif state.step == len(state.array) - state.index - 1:
                state.array[-1] = 0
                state.message = f"删除了位置{state.index}的元素。"
                state.step = -1  # 重置为下一次操作
            state.step += 1

    plot_array()
    st.write(state.message)
