"""
下面这个有很大问题，有待完善，期待的效果是，实现构造函数的启发，以及理解各个定理的适用条件
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from scipy.misc import derivative
import matplotlib

# 初始化session_state
if 'custom_function' not in st.session_state:
    st.session_state.custom_function = 'x**2'
if 'custom_function_g' not in st.session_state:
    st.session_state.custom_function_g = 'x'

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用 'SimHei' 字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 用户自定义函数输入
st.session_state.custom_function = st.text_input(
    "输入一个以 'x' 为变量的自定义函数 f(x)：", st.session_state.custom_function)

# 选择定理
theorem_choice = st.selectbox("选择一个要可视化的定理：", [
    "有界与最值定理",
    "介值定理",
    "平均值定理",
    "零点定理",
    "费马定理",
    "罗尔定理",
    "拉格朗日中值定理",
    "柯西中值定理",
    "泰勒公式",
    "积分中值定理"
])

if theorem_choice == "柯西中值定理":
    st.session_state.custom_function_g = st.text_input(
        "输入一个以 'x' 为变量的自定义函数 g(x)：", st.session_state.custom_function_g)


# 定义一个用于绘制有界与最值定理的函数
def plot_boundedness(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    plt.plot(x, f)
    plt.title("有界与最值定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.scatter(x[np.argmax(f)], np.max(f), color='r')
    plt.scatter(x[np.argmin(f)], np.min(f), color='g')
    st.pyplot(plt)

# 定义一个用于绘制介值定理的函数
def plot_intermediate_value(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    plt.plot(x, f)
    plt.title("介值定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    c = st.slider("选择c值", float(np.min(f)), float(np.max(f)), 0)
    plt.axhline(y=c, color='r', linestyle='--')
    st.pyplot(plt)

# 定义一个用于绘制平均值定理的函数
def plot_mean_value_theorem(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    plt.plot(x, f)
    plt.title("平均值定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    # Assuming a and b as two points in the domain
    a, b = -5, 5
    f_a, f_b = eval(f_str.replace('x', 'a')), eval(f_str.replace('x', 'b'))
    slope = (f_b - f_a) / (b - a)
    tangent = f_a + slope * (x - a)
    plt.plot(x, tangent, '--', label='Tangent')
    plt.legend()
    st.pyplot(plt)

# 定义一个用于绘制零点定理的函数
def plot_zeros(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    plt.plot(x, f)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("零点定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    st.pyplot(plt)

# 定义一个用于绘制费马定理的函数


def plot_fermat(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    f_prime = [derivative(lambda x: eval(f_str), xi, dx=1e-6) for xi in x]
    zeros = np.where(np.isclose(f_prime, 0, atol=1e-2))[0]
    plt.plot(x, f)
    for zero in zeros:
        plt.scatter(x[zero], f[zero], color='r')
    plt.title("费马定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    st.pyplot(plt)

# 定义一个用于绘制罗尔定理的函数


def plot_rolle(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    f_prime = [derivative(lambda x: eval(f_str), xi, dx=1e-6) for xi in x]
    if f[0] == f[-1]:
        zero = np.where(np.isclose(f_prime, 0, atol=1e-2))[0]
        plt.scatter(x[zero], f[zero], color='r')
    plt.plot(x, f)
    plt.title("罗尔定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    st.pyplot(plt)

# 定义一个用于绘制拉格朗日中值定理的函数


def plot_lagrange(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    slope = (f[-1] - f[0]) / (x[-1] - x[0])
    tangent = f[0] + slope * (x - x[0])
    plt.plot(x, f, label='Function')
    plt.plot(x, tangent, '--', label='Tangent with slope (f(b)-f(a))/(b-a)')
    plt.title("拉格朗日中值定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    st.pyplot(plt)

# 定义一个用于绘制柯西中值定理的函数
def plot_cauchy(f_str):
    # 代码如下
    plot_mean_value_theorem(f_str)

# 定义一个用于绘制泰勒公式的函数
def plot_taylor(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    # Assuming the Taylor expansion around x=0
    from sympy import symbols, diff, lambdify
    x_sym = symbols('x')
    f_sym = eval(f_str.replace('x', 'x_sym'))
    taylor_approx = f_sym.series(x_sym, 0, 4).removeO()
    taylor_func = lambdify(x_sym, taylor_approx, "numpy")
    plt.plot(x, f, label='Original Function')
    plt.plot(x, taylor_func(x), '--', label='Taylor Approximation')
    plt.title("泰勒公式")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    st.pyplot(plt)

# 定义一个用于绘制积分中值定理的函数
def plot_integral_mean_value(f_str):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    from scipy.integrate import quad
    integral_value, _ = quad(lambda x: eval(f_str), -10, 10)
    average_value = integral_value / (20)  # b - a = 20
    plt.plot(x, f)
    plt.axhline(average_value, color='r', linestyle='--')
    plt.title("积分中值定理")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    st.pyplot(plt)

# 定义一个用于绘制柯西中值定理的函数
def plot_cauchy(f_str, g_str="x"):
    x = np.linspace(-10, 10, 400)
    f = eval(f_str)
    g = eval(g_str)
    f_prime = [derivative(lambda x: eval(f_str), xi, dx=1e-6) for xi in x]
    g_prime = [derivative(lambda x: eval(g_str), xi, dx=1e-6) for xi in x]

    # Check conditions of Cauchy's theorem
    if g[0] != g[-1] and all(np.array(g_prime) != 0):
        slope = (f[-1] - f[0]) / (g[-1] - g[0])
        for i in range(len(x)):
            if np.isclose(f_prime[i] / g_prime[i], slope, atol=1e-2):
                c = x[i]
                break
        tangent_f = f[i] + f_prime[i] * (x - c)
        tangent_g = g[i] + g_prime[i] * (x - c)
        plt.plot(x, f, label=f'f(x) = {f_str}')
        plt.plot(x, g, label=f'g(x) = {g_str}', linestyle="--")
        plt.plot(x, tangent_f, ':', label='Tangent to f at c')
        plt.plot(x, tangent_g, ':', label='Tangent to g at c')
        plt.scatter(c, f[i], color='r')
        plt.title("柯西中值定理")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        st.pyplot(plt)
    else:
        st.write("Conditions for Cauchy's theorem not met with the given functions.")


# 主逻辑
if theorem_choice == "有界与最值定理":
    plot_boundedness(st.session_state.custom_function)
elif theorem_choice == "介值定理":
    plot_intermediate_value(st.session_state.custom_function)
elif theorem_choice == "平均值定理":
    plot_mean_value_theorem(st.session_state.custom_function)
elif theorem_choice == "零点定理":
    plot_zeros(st.session_state.custom_function)
elif theorem_choice == "费马定理":
    plot_fermat(st.session_state.custom_function)
elif theorem_choice == "罗尔定理":
    plot_rolle(st.session_state.custom_function)
elif theorem_choice == "拉格朗日中值定理":
    plot_lagrange(st.session_state.custom_function)
elif theorem_choice == "柯西中值定理":
    plot_cauchy(st.session_state.custom_function)
elif theorem_choice == "泰勒公式":
    plot_taylor(st.session_state.custom_function)
elif theorem_choice == "积分中值定理":
    plot_integral_mean_value(st.session_state.custom_function)

