import streamlit as st
import numpy as np
import sympy as sp

st.title("Linear Algebra Toolkit")

# 允许用户输入矩阵
rows = st.number_input("Enter number of rows:", min_value=1, value=2)
cols = st.number_input("Enter number of columns:", min_value=1, value=2)
matrix_data = [[st.number_input(f"Element ({i+1}, {j+1}):") for j in range(cols)] for i in range(rows)]
matrix = sp.Matrix(matrix_data)

# 显示输入的矩阵
st.markdown("**Entered Matrix:**")
st.latex(matrix)

# 选择要执行的操作
operation = st.selectbox("Select an operation:", ["Determinant", "Inverse", "Eigenvalues", "Eigenvectors"])

# 执行选定的操作
if operation == "Determinant":
    if rows == cols:
        st.markdown(f"**Determinant:** {matrix.det()}")
    else:
        st.warning("Determinant can only be computed for square matrices.")

elif operation == "Inverse":
    if matrix.det() != 0:
        st.markdown("**Inverse:**")
        st.latex(matrix.inv())
    else:
        st.warning("Matrix is singular, inverse does not exist.")

elif operation == "Eigenvalues":
    st.markdown("**Eigenvalues:**")
    eigenvalues = matrix.eigenvals()
    st.write(eigenvalues)

elif operation == "Eigenvectors":
    st.markdown("**Eigenvectors:**")
    eigenvectors = matrix.eigenvects()
    st.write(eigenvectors)
