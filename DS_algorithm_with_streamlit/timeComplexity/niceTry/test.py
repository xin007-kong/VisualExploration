import streamlit as st
import numpy as np
import subprocess


def write_matrix_to_file(matrix, filename):
    with open(filename, "w") as file:
        for row in matrix:
            row_str = " ".join(map(str, row))
            file.write(row_str + "\n")


def main():
    st.title("Matrix Multiplication Analysis")

    n_rows = st.slider("Select number of rows",
                       min_value=2, max_value=10, value=3)
    n_cols = st.slider("Select number of columns",
                       min_value=2, max_value=10, value=3)

    st.write("Enter Matrix A:")
    matrix_a = []
    for i in range(n_rows):
        row = st.text_input(
            f"Row A-{i + 1}", value=" ".join(["0"] * n_cols), key=f"input_A_{i}")
        matrix_a.append(list(map(int, row.split())))

    st.write("Enter Matrix B:")
    matrix_b = []
    for i in range(n_cols):
        row = st.text_input(
            f"Row B-{i + 1}", value=" ".join(["0"] * n_rows), key=f"input_B_{i}")
        matrix_b.append(list(map(int, row.split())))

    if st.button("Run Traditional Matrix Multiplication"):
        write_matrix_to_file(matrix_a, "matrix_a.txt")
        write_matrix_to_file(matrix_b, "matrix_b.txt")

        st.write("Running C Program for Traditional Matrix Multiplication...")
        subprocess.run(["gcc", "-o", "traditional_multiply",
                       "traditional_multiply.c"])
        result = subprocess.check_output(["./traditional_multiply"]).decode()

        st.write("Matrix C (Result of Multiplication):")
        st.code(result)


if __name__ == "__main__":
    main()
