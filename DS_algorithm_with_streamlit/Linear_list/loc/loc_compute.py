import streamlit as st


def compute_location(base, i, l):
    return base + (i - 1) * l


st.title("线性表的顺序表示")

base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)
i = st.slider("选择元素索引 i:", 1, 10, 1)

loc = compute_location(base, i, l)

st.write(f"第{i}个元素的地址为: {loc}")

# Visualizing
st.write("线性表可视化：")
for index in range(1, 11):
    cell = "□"
    if index == i:
        cell = "■"
    st.write(f"{index}: {cell}")
