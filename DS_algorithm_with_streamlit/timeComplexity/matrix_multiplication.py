import streamlit as st
import numpy as np

def traditional_matrix_multiply(A, B):
    n = len(A)
    C = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def strassen_matrix_multiply(A, B):
    # Implement Strassen matrix multiplication here
    pass

def main():
    st.title("Matrix Multiplication Teaching Tool")

    n = st.slider("Select matrix size (n)", min_value=2, max_value=10, value=3)

    A = np.random.randint(1, 10, (n, n))
    B = np.random.randint(1, 10, (n, n))

    st.write("Matrix A:")
    st.write(A)
    st.write("Matrix B:")
    st.write(B)

    traditional_result = traditional_matrix_multiply(A, B)
    st.write("Traditional Matrix Multiplication Result:")
    st.write(traditional_result)

    strassen_result = strassen_matrix_multiply(A, B)
    st.write("Strassen Matrix Multiplication Result:")
    st.write(strassen_result)

if __name__ == "__main__":
    main()
