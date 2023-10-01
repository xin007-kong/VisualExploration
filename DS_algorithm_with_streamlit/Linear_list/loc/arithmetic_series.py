import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def plot_arithmetic_series(base, l, size=10):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Generating the arithmetic series
    i_values = list(range(1, size+1))
    locations = [base + (i - 1) * l for i in i_values]

    ax.plot(i_values, locations, marker='o', linestyle='-')

    for i, loc in zip(i_values, locations):
        ax.text(i, loc + 0.5*l, f"{loc}", ha='center', fontsize=10)

    ax.set_xlabel("Element Index (i)")
    ax.set_ylabel("Location (LOC(a_i))")
    ax.set_title("Linear Table Address as an Arithmetic Series")
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    st.pyplot(fig)


st.title("线性表的顺序表示：等差数列")

base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)
size = st.slider("选择线性表元素个数:", 1, 20, 10)

# Visualize
plot_arithmetic_series(base, l, size)
