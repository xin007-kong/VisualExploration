# import streamlit as st
# import numpy as np
# import subprocess


# def traditional_matrix_multiply(A, B):
#     # Implement traditional matrix multiplication here
#     pass


# # def strassen_matrix_multiply(A, B):
# #     # Implement Strassen matrix multiplication here
# #     pass


# def main():
#     st.title("Matrix Multiplication Analysis")

#     n = st.slider("Select matrix size (n)", min_value=2, max_value=10, value=3)

#     A = np.random.randint(1, 10, (n, n))
#     B = np.random.randint(1, 10, (n, n))

#     st.write("Matrix A:")
#     st.write(A)
#     st.write("Matrix B:")
#     st.write(B)

#     st.write("Running C Programs for Analysis...")
#     subprocess.run(["gcc", "-o", "traditional_multiply",
#                    "traditional_multiply.c"])
#     # subprocess.run(["gcc", "-o", "strassen_multiply", "strassen_multiply.c"])

#     st.write("Traditional Matrix Multiplication Result:")
#     st.code(subprocess.check_output(["./traditional_multiply"]).decode())

#     # st.write("Strassen Matrix Multiplication Result:")
#     # st.code(subprocess.check_output(["./strassen_multiply"]).decode())


# if __name__ == "__main__":
#     main()

# import streamlit as st
# import numpy as np
# import subprocess


# def traditional_matrix_multiply(A, B):
#     # Implement traditional matrix multiplication here
#     pass


# def main():
#     st.title("Matrix Multiplication Analysis")

#     n = st.slider("Select matrix size (n)", min_value=2, max_value=10, value=3)

#     A = np.random.randint(1, 10, (n, n))
#     B = np.random.randint(1, 10, (n, n))

#     st.write("Matrix A:")
#     st.write(A)
#     st.write("Matrix B:")
#     st.write(B)

#     if st.button("Run Traditional Matrix Multiplication"):
#         st.write("Running C Program for Traditional Matrix Multiplication...")
#         subprocess.run(["gcc", "-o", "traditional_multiply",
#                        "traditional_multiply.c"])
#         result = subprocess.check_output(["./traditional_multiply"]).decode()
#         st.code(result)


# if __name__ == "__main__":
#     main()

import streamlit as st
import numpy as np
import subprocess


def traditional_matrix_multiply(A, B):
    # Implement traditional matrix multiplication here
    n = len(A)
    C = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def main():
    st.title("Matrix Multiplication Analysis")

    n = st.slider("Select matrix size (n)", min_value=2, max_value=10, value=3)

    st.write("Enter Matrix A:")
    matrix_a = []
    for i in range(n):
        row = st.text_input(f"Row {i + 1}", value="1 2 3")
        matrix_a.append(list(map(int, row.split())))

    st.write("Enter Matrix B:")
    matrix_b = []
    for i in range(n):
        row = st.text_input(f"Row {i + 1}", value="9 8 7")
        matrix_b.append(list(map(int, row.split())))

    if st.button("Run Traditional Matrix Multiplication"):
        st.write("Running C Program for Traditional Matrix Multiplication...")
        subprocess.run(["gcc", "-o", "traditional_multiply",
                       "traditional_multiply.c"])

        A = np.array(matrix_a)
        B = np.array(matrix_b)
        result = traditional_matrix_multiply(A, B)

        st.write("Matrix C (Result of Multiplication):")
        st.write(result)


if __name__ == "__main__":
    main()
