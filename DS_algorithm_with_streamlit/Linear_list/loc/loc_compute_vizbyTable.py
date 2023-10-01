import streamlit as st

def compute_location(base, l, size=10):
    return [base + (i - 1) * l for i in range(1, size+1)]

st.title("线性表的顺序表示")

base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)

# Compute locations for 10 elements
locations = compute_location(base, l)

# Display table
st.write("线性表地址可视化：")
table_data = [{"Element": f"a{i+1}", "Location": loc} for i, loc in enumerate(locations)]
st.table(table_data)
