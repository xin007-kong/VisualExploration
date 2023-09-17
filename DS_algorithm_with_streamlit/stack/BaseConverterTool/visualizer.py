import streamlit as st
from converter import decimal_to_base


def display_conversion(decimal_num, base):
    st.write(f"开始将 {decimal_num} 转换为基数 {base} ...")
    stack = []
    temp_num = decimal_num

    while temp_num > 0:
        remainder = temp_num % base
        quotient = temp_num // base

        # 显示这一步的余数
        st.write(f"当前数字: {temp_num}")
        st.write(f"除以 {base} 得到的商: {quotient} 余数: {remainder}")

        # 显示入栈情况
        st.write(f"入栈: {remainder}")
        stack.append(remainder)

        # 显示实际的栈顺序
        st.write(f"栈状态 (从栈顶到栈底): {stack}")

        # 为了直观展示，我们通常从栈底到栈顶显示数字，因此需要逆序显示
        st.write(f"栈状态 (从栈底到栈顶，用于直观展示): {list(reversed(stack))}")

        st.write("---")

        temp_num = quotient

    # 从栈底到栈顶构建数字
    st.write(
        f"{decimal_num} 在基数 {base} 下的表示为: {''.join(map(str, reversed(stack)))}")
