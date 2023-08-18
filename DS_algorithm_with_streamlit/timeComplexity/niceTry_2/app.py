# # import streamlit as st
# # import numpy as np
# # import subprocess

# # # 创建输入界面
# # st.title('矩阵计算器')
# # rows = st.number_input('输入行数', min_value=2, value=2)
# # cols = st.number_input('输入列数', min_value=2, value=2)

# # # 动态创建矩阵输入
# # matrix = np.zeros((rows, cols))
# # for i in range(rows):
# #     for j in range(cols):
# #         matrix[i, j] = st.number_input(f'输入元素({i+1}, {j+1})')

# # if st.button('计算'):
# #     # 调用C语言程序并传递矩阵
    
# #     result = subprocess.run(["./matrix_calculator", str(rows), str(cols)] + list(map(str, matrix.flatten())), stdout=subprocess.PIPE)
# #     result_matrix = result.stdout.decode('utf-8')
# #     st.write('结果矩阵:', result_matrix)

# import streamlit as st
# import numpy as np
# import subprocess
# import os

# # 编译C程序
# c_source_file = "matrix_calculator.c"
# exe_file = "matrix_calculator.exe"
# # compile_command = ["gcc", c_source_file, "-o", exe_file]
# # 编译C程序，使用C99标准
# compile_command = ["gcc", c_source_file, "-o", exe_file, "-std=c99"]

# compile_process = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# if compile_process.returncode != 0:
#     # 编译失败，将错误信息打印到Streamlit界面
#     st.error("编译C程序失败:\n" + compile_process.stderr.decode('utf-8'))
# else:
#     # 创建输入界面
#     st.title('矩阵计算器')
#     rows = st.number_input('输入行数', min_value=2, value=2)
#     cols = st.number_input('输入列数', min_value=2, value=2)

#     # 动态创建矩阵输入
#     matrix = np.zeros((rows, cols))
#     for i in range(rows):
#         for j in range(cols):
#             matrix[i, j] = st.number_input(f'输入元素({i+1}, {j+1})')

#     if st.button('计算'):
#         # 调用C语言程序并传递矩阵
#         result = subprocess.run([exe_file, str(rows), str(cols)] + list(map(str, matrix.flatten())), stdout=subprocess.PIPE)
#         result_matrix = result.stdout.decode('utf-8')
#         st.write('结果矩阵:', result_matrix)

#     # 可选：删除编译的可执行文件
#     os.remove(exe_file)

import streamlit as st
import numpy as np
import subprocess
import os

# 编译C程序，使用C99标准
c_source_file = "matrix_calculator.c"
exe_file = "matrix_calculator.exe"
compile_command = ["gcc", c_source_file, "-o", exe_file, "-std=c99"]
compile_process = subprocess.run(
    compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if compile_process.returncode != 0:
    # 编译失败，将错误信息打印到Streamlit界面
    st.error("编译C程序失败:\n" + compile_process.stderr.decode('utf-8'))
else:
    # 创建输入界面
    st.title('矩阵加减法计算器')
    rows = st.number_input('输入行数', min_value=2, value=2)
    cols = st.number_input('输入列数', min_value=2, value=2)

    st.write('输入第一个矩阵')
    matrix1 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix1[i, j] = st.number_input(f'矩阵1 元素({i+1}, {j+1})')

    st.write('输入第二个矩阵')
    matrix2 = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix2[i, j] = st.number_input(f'矩阵2 元素({i+1}, {j+1})')

    if st.button('计算'):
        # 调用C语言程序并传递矩阵
        result = subprocess.run([exe_file, str(rows), str(cols)] + list(map(
            str, matrix1.flatten())) + list(map(str, matrix2.flatten())), stdout=subprocess.PIPE)
        result_matrix = result.stdout.decode('utf-8')
        st.write('结果矩阵:\n', result_matrix)

# 可选：删除编译的可执行文件
# os.remove(exe_file)
