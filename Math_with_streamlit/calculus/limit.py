import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 定义符号
n = sp.Symbol('n')

# Streamlit 应用标题
st.title("Sequence Limit Calculator")

# 用户输入的数列公式
sequence_input = st.text_input("Enter the sequence formula in terms of n (e.g., 1/n):", value="1/n")
sequence_expr = sp.sympify(sequence_input, locals={'n': n})

# 计算数列的前N项
N = st.slider("Select the number of terms to display:", min_value=5, max_value=100, value=10)
sequence_values = [sequence_expr.subs(n, i).evalf() for i in range(1, N+1)]

# 显示数列的前N项
st.markdown(f"**The first {N} terms of the sequence are:**")
st.write(sequence_values)

# 计算数列的极限
sequence_limit = sp.limit(sequence_expr, n, sp.oo)
st.markdown(f"**The limit of the sequence is:** {sequence_limit}")

# 画图显示数列
plt.plot(range(1, N+1), sequence_values, marker='o')
plt.xlabel('Term (n)')
plt.ylabel('Value')
plt.title('Sequence Plot')
plt.grid(True)
st.pyplot(plt)
