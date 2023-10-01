# 贝叶斯和全概率公式
# 导入必要的库
import streamlit as st
import matplotlib.pyplot as plt

st.title('全概率与贝叶斯公式教学工具')

# 使用 st.columns 替换 st.beta_columns
left_column, center_column, right_column = st.columns(3)

# 在左边的 column 中设置 B1 和相关的概率滑块
with left_column:
    st.header("原因概率输入")
    p_b1 = st.slider("P(B1) - 第一个原因的概率", 0.0, 1.0, 0.5)
    p_a_given_b1 = st.slider("P(A|B1) - 在第一个原因下结果发生的概率", 0.0, 1.0, 0.5)

# 在中间的 column 中设置 B2 和其它相关的概率滑块
with center_column:
    st.header("原因概率输入")
    p_b2 = 1 - p_b1
    st.write(f"P(B2) = {p_b2:.2f} (自动计算)")
    p_a_given_b2 = st.slider("P(A|B2) - 在第二个原因下结果发生的概率", 0.0, 1.0, 0.5)

# 计算全概率，并在右边的 column 中显示全概率的结果和计算过程
with right_column:
    st.header("全概率结果")
    p_a = p_b1 * p_a_given_b1 + p_b2 * p_a_given_b2
    st.write(f"P(A) = P(B1) × P(A|B1) + P(B2) × P(A|B2)")
    st.write(
        f"P(A) = {p_b1:.2f} × {p_a_given_b1:.2f} + {p_b2:.2f} × {p_a_given_b2:.2f} = {p_a:.4f}")

# 在左边的 column 中设置贝叶斯部分的输入
with left_column:
    st.subheader("贝叶斯公式输入")
    p_a_input = st.slider("P(A) - 已知的结果发生的概率", 0.0, 1.0, p_a)

# 在中间的 column 中显示贝叶斯的计算过程和结果
with center_column:
    st.subheader("贝叶斯公式计算")
    p_b1_result = (p_a_given_b1 * p_b1) / p_a_input
    st.write(f"P(B1|A) = [P(A|B1) × P(B1)] / P(A)")
    st.write(
        f"P(B1|A) = [{p_a_given_b1:.2f} × {p_b1:.2f}] / {p_a_input:.2f} = {p_b1_result:.4f}")

# 在右边的 column 中展示一个柱状图
with right_column:
    st.subheader("图表展示")
    fig, ax = plt.subplots()
    categories = ['P(B1|A)', 'P(B2|A)']
    values = [p_b1_result, 1-p_b1_result]
    ax.bar(categories, values, color=['blue', 'green'])
    ax.set_ylim(0, 1)
    ax.set_ylabel('Probability')
    ax.set_title('Posterior Probabilities')
    st.pyplot(fig)

st.write("使用上面的滑块调整概率值，观察结果如何随着输入值的变化而变化，并理解其中的计算过程。")
