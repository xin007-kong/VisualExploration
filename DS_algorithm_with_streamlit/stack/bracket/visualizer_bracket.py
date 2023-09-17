import streamlit as st
from bracket_checker import check_brackets, is_matched

def display_bracket_check(s):
    stack = []
    for index, char in enumerate(s):
        if char in "([{":
            stack.append(char)
            st.write(f"字符 {char} 压入栈。当前栈状态: {stack}")
        elif char in ")]}":
            if stack and is_matched(stack[-1], char):
                st.write(f"字符 {char} 与栈顶的 {stack[-1]} 匹配。")
                stack.pop()
                st.write(f"栈顶的字符被弹出。当前栈状态: {stack}")
            else:
                st.write(f"字符 {char} 与栈顶的 {stack[-1] if stack else 'None'} 不匹配。")
                break
        st.write("---")

    if not stack:
        st.write("括号匹配正确！")
    else:
        st.write("括号匹配错误！")
