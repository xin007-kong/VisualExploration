# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.misc import derivative


# def sine(x):
#     return np.sin(x)

# def cosine(x):
#     return np.cos(x)

# def exponential(x):
#     return np.exp(x)

# def logarithm(x):
#     return np.log(x)

# FUNCTIONS = {"Sine": sine, "Cosine": cosine, "Exponential": exponential, "Logarithm": logarithm}


# st.title("Taylor Series Expansion")

# selected_function_label = st.sidebar.selectbox("Select a function", list(FUNCTIONS.keys()))
# selected_function = FUNCTIONS[selected_function_label]


# def taylor_series(func, x, x0, n):
#     result = 0
#     for i in range(n+1):
#         result += derivative(func, x0, n=i) * (x - x0)**i / np.math.factorial(i)
#     return result

# x0 = st.sidebar.number_input("Select the point of expansion (x0):", value=0.0)
# order = st.sidebar.slider("Select the order of expansion:", min_value=1, max_value=10, value=2)


# x = np.linspace(-10, 10, 1000)
# y_original = selected_function(x)
# y_taylor = taylor_series(selected_function, x, x0, order)

# plt.plot(x, y_original, label=f"{selected_function_label} function")
# plt.plot(x, y_taylor, label=f"Taylor series (order {order})")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title(f"{selected_function_label} Function and Its Taylor Series Expansion")
# st.pyplot(plt)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 定义符号变量
x = sp.Symbol('x')
x0_symbol = sp.Symbol('x0')

# 定义函数
def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

def exponential(x):
    return np.exp(x)

def logarithm(x):
    return np.log(x)

FUNCTIONS = {"Sine": sine, "Cosine": cosine, "Exponential": exponential, "Logarithm": logarithm}

# 定义符号化的函数
sine_symbolic = sp.sin(x)
cosine_symbolic = sp.cos(x)
exponential_symbolic = sp.exp(x)
logarithm_symbolic = sp.log(x)

FUNCTIONS_SYMBOLIC = {"Sine": sine_symbolic, "Cosine": cosine_symbolic, "Exponential": exponential_symbolic, "Logarithm": logarithm_symbolic}

# Streamlit 应用标题
st.title("Taylor Series Expansion")

# 用户选择的函数
selected_function_label = st.sidebar.selectbox("Select a function", list(FUNCTIONS.keys()))
selected_function = FUNCTIONS[selected_function_label]
selected_function_symbolic = FUNCTIONS_SYMBOLIC[selected_function_label]

# 用户输入的点和阶数
x0 = st.sidebar.number_input("Select the point of expansion (x0):", value=0.0)
order = st.sidebar.slider("Select the order of expansion:", min_value=1, max_value=10, value=2)

# 计算泰勒展开式
taylor_expansion = sp.series(selected_function_symbolic, x, x0_symbol, order).removeO()

# 显示泰勒展开式
st.markdown(f"**Taylor Series Expansion of {selected_function_label}:**")
st.latex(taylor_expansion)

# 计算函数和其泰勒展开
def taylor_series(func, x_val, x0_val, n):
    result = 0
    for i in range(n+1):
        coef = sp.diff(func, x, i).subs(x, x0_val).evalf()
        result += coef * (x_val - x0_val)**i / np.math.factorial(i)
    return result

x_values = np.linspace(-10, 10, 1000)
y_original = selected_function(x_values)
y_taylor = [taylor_series(selected_function_symbolic, x_val, x0, order) for x_val in x_values]

# 画图
plt.plot(x_values, y_original, label=f"{selected_function_label} function")
plt.plot(x_values, y_taylor, label=f"Taylor series (order {order})")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"{selected_function_label} Function and Its Taylor Series Expansion")
st.pyplot(plt)
