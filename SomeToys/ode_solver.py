# import streamlit as st
# import sympy as sp


# def compute_basis_solutions(equation, func):
#     # 定义微分方程
#     f = sp.Function('f')
#     x = sp.symbols('x')
#     ode = equation.subs(func, f(x))

#     # 求解微分方程
#     sol = sp.dsolve(ode)
#     return sol


# st.title("基础解系计算器")

# # 用户选择微分方程的阶数
# order = st.selectbox("选择微分方程的阶数：", [1, 2, 3, 4])

# # 根据阶数为用户提供输入框
# equation_parts = []
# for i in range(order, -1, -1):
#     if i == 0:
#         part = st.number_input(f"输入 f 的系数：", value=1.0)
#     else:
#         part = st.number_input(f"输入 f^{i} 的系数：", value=0.0)
#     equation_parts.append(part)

# # 构建微分方程
# f = sp.Function('f')
# x = sp.symbols('x')
# equation = sum(coeff * f(x).diff(x, i)
#                for i, coeff in enumerate(equation_parts[::-1]))

# if st.button("计算基础解系"):
#     try:
#         solutions = compute_basis_solutions(equation, f)
#         st.write("基础解系：", solutions)
#     except Exception as e:
#         st.write("错误：", str(e))
import streamlit as st
import sympy as sp


def compute_basis_solutions(equation, func):
    # 定义微分方程
    f = sp.Function('f')
    x = sp.symbols('x')
    ode = equation.subs(func, f(x))

    # 求解微分方程
    sol = sp.dsolve(ode)
    return sol


st.title("基础解系计算器")

# 设置 sympy 参数以确保结果中包含 π
sp.pprint_use_unicode(True)

# 用户选择微分方程的阶数
order = st.selectbox("选择微分方程的阶数：", [1, 2, 3, 4])

# 根据阶数为用户提供输入框
equation_parts = []
for i in range(order, -1, -1):
    if i == 0:
        part = st.number_input(f"输入 f 的系数：", value=1.0)
    else:
        part = st.number_input(f"输入 f^{i} 的系数：", value=0.0)
    equation_parts.append(part)

# 构建微分方程
f = sp.Function('f')
x = sp.symbols('x')
equation = sum(coeff * f(x).diff(x, i)
               for i, coeff in enumerate(equation_parts[::-1]))

if st.button("计算基础解系"):
    try:
        solutions = compute_basis_solutions(equation, f)
        st.write("基础解系：", solutions)
    except Exception as e:
        st.write("错误：", str(e))
