import streamlit as st
import datetime
import pandas as pd

# 创建模拟的DataFrame


def create_mock_dataframe():
    data = {
        "formula": [
            r"\sin(x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots",
            r"\cos(x) \approx 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots",
            r"e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots"
            r"ln(1+x)\approx x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\dots",
            r"tan(x) \approx x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \dots",
            r"\frac{1}{1-x} \approx 1 + x + x^2 + x^3 + \dots",
            r"\frac{1}{1+x} \approx 1 - x + x^2 - x^3 + \dots",
            
        ],
        "last_seen": [datetime.datetime.now() - datetime.timedelta(days=i) for i in range(3)],
        "mastery_level": [5, 7, 6]
    }

    df = pd.DataFrame(data)
    return df


df = create_mock_dataframe()


def main():
    st.title("数学公式间隔重复学习")

    # 选择一个公式来评估掌握程度
    formulas = df["formula"].tolist()
    selected_formula = st.selectbox("选择一个公式:", formulas)
    if selected_formula:
        formula_data = df[df["formula"] == selected_formula].iloc[0]
        # 使用markdown展示latex格式
        st.markdown(f"选定的公式: $${formula_data['formula']}$$")
        st.write(f"上次查看时间: {formula_data['last_seen']}")
        st.write(f"目前的掌握程度: {formula_data['mastery_level']}")

        new_mastery = st.slider(
            "评估你的掌握程度 (0完全不会 - 10完全掌握):", 0, 10, int(formula_data['mastery_level']))
        if st.button("更新掌握程度"):
            df.loc[df["formula"] == selected_formula,
                   "mastery_level"] = new_mastery
            df.loc[df["formula"] == selected_formula,
                   "last_seen"] = datetime.datetime.now()
            st.success(f"公式的掌握程度已更新!")


if __name__ == "__main__":
    main()
