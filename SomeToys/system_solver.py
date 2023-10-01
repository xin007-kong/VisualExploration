import streamlit as st
import numpy as np
from scipy.linalg import null_space

st.title("线性齐次方程组的基础解系计算器")

# 用户选择方程数量和未知数数量
num_equations = st.selectbox("选择方程的数量：", list(range(1, 6)))
num_variables = st.selectbox("选择未知数的数量：", list(range(1, 6)))

# 根据选择的数量为用户提供输入框
matrix_data = []
for i in range(num_equations):
    row_data = []
    for j in range(num_variables):
        coeff = st.number_input(f"输入方程 {i+1} 的未知数 {j+1} 的系数：", value=0.0)
        row_data.append(coeff)
    matrix_data.append(row_data)

# 计算基础解系
if st.button("计算基础解系"):
    try:
        matrix = np.array(matrix_data)
        basis = null_space(matrix)
        st.write("基础解系：")
        for col in basis.T:
            st.write(col)
    except Exception as e:
        st.write("错误：", str(e))
