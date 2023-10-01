# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt


# def plot_integral(func, a, b):
#     x = np.linspace(a-1, b+1, 400)
#     y = func(x)

#     fig, ax = plt.subplots()
#     ax.plot(x, y, 'r', linewidth=2)
#     ax.fill_between(
#         x, y, where=[a <= xi <= b for xi in x], color='skyblue', alpha=0.4)
#     ax.text(0.5 * (a + b), 0, f"Area = {np.trapz(y[(x >= a) & (x <= b)], x[(x >= a) & (x <= b)]):.2f}",
#             horizontalalignment='center', verticalalignment='bottom')
#     ax.axhline(0, color='black', linewidth=0.5)
#     ax.axvline(a, color='green', linestyle='--', linewidth=1)
#     ax.axvline(b, color='blue', linestyle='--', linewidth=1)
#     ax.grid(True, which='both', linestyle='--', linewidth=0.5)
#     return fig


# st.title("不定积分可视化")

# # 选择函数
# func_option = st.selectbox("选择一个函数:", ["x^2", "sin(x)", "cos(x)", "e^x"])
# if func_option == "x^2":
#     def func(x): return x**2
# elif func_option == "sin(x)":
#     func = np.sin
# elif func_option == "cos(x)":
#     func = np.cos
# else:
#     func = np.exp

# # 选择积分的上下限
# a = st.slider("选择下限 a:", -10.0, 10.0, -1.0, 0.1)
# b = st.slider("选择上限 b:", -10.0, 10.0, 1.0, 0.1)

# # 绘制函数和其下的面积
# st.pyplot(plot_integral(func, a, b))
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def plot_integral(func, a, b):
    x = np.linspace(a-1, b+1, 400)
    y = func(x)

    integral_value, _ = quad(func, a, b)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ax.fill_between(
        x, y, where=[a <= xi <= b for xi in x], color='skyblue', alpha=0.4)
    ax.text(0.5 * (a + b), 0, f"Area = {integral_value:.2f}",
            horizontalalignment='center', verticalalignment='bottom')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(a, color='green', linestyle='--', linewidth=1)
    ax.axvline(b, color='blue', linestyle='--', linewidth=1)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    return fig


st.title("不定积分可视化")

# 选择函数
func_option = st.selectbox("选择一个函数:", ["x^2", "sin(x)", "cos(x)", "e^x"])
if func_option == "x^2":
    def func(x): return x**2
elif func_option == "sin(x)":
    func = np.sin
elif func_option == "cos(x)":
    func = np.cos
else:
    func = np.exp

# 选择积分的上下限
a = st.slider("选择下限 a:", -10.0, 10.0, -1.0, 0.1)
b = st.slider("选择上限 b:", -10.0, 10.0, 1.0, 0.1)

# 绘制函数和其下的面积
st.pyplot(plot_integral(func, a, b))
