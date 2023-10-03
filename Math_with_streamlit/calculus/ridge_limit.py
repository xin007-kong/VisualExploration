import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge

st.title("利用Ridge回归理解极限")

# 生成一些样本数据
X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
X = X.reshape(-1, 1)

# 用户输入lambda值
lambda_val = st.slider("选择一个λ (Lambda) 的值:", 0.0, 100.0, 1.0)

# 使用Ridge回归
clf = Ridge(alpha=lambda_val)
clf.fit(X, y)
predicted = clf.predict(X)

# 绘图
fig, ax = plt.subplots()
ax.scatter(X, y, color='blue')
ax.plot(X, predicted, color='red',
        label=f"Ridge Regression (λ = {lambda_val})")
ax.set_title("Ridge Regression with varying λ")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

st.write(f"当λ = {lambda_val}时的系数值: {clf.coef_[0]}")

# 解释极限的概念
st.markdown("""
当你将λ的值增加到一个非常大的数时，回归的系数趋向于0。 
这是由于在Ridge回归中引入的惩罚。在极限的术语中，我们可以说：
""")
st.latex(r"""\lim_{\lambda \rightarrow \infty} """ + r""" \text{系数} = 0""")
st.markdown("""另一方面，当λ非常接近0时，Ridge回归与没有任何正则化的普通线性回归非常相似.""")
