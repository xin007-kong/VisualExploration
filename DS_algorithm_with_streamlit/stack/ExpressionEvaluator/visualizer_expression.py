import streamlit as st
from expression_evaluator import operate, evaluate_expression


def display_expression_evaluation(expr):
    OPTR = []
    OPND = []
    i = 0
    while i < len(expr):
        st.write(f"当前字符: {expr[i]}")
        if expr[i].isdigit():
            start = i
            while i < len(expr) and expr[i].isdigit():
                i += 1
            OPND.append(int(expr[start:i]))
            st.write(f"识别到数字: {expr[start:i]}，加入操作数栈")
        else:
            if not OPTR or (expr[i] in "+-" and OPTR[-1] in "+-") or (expr[i] in "*/" and OPTR[-1] in "*/"):
                st.write(
                    f"当前运算符 {expr[i]} 与栈顶运算符 {OPTR[-1] if OPTR else 'None'} 优先级相同或更高，直接入栈。")
            while OPTR and OPTR[-1] in "+-*/" and (expr[i] in "+-" or expr[i] in "*/" and OPTR[-1] in "*/"):
                st.write(
                    f"当前运算符 {expr[i]} 优先级低于栈顶运算符 {OPTR[-1]}，因此先执行栈顶运算符的运算。")
                b = OPND.pop()
                a = OPND.pop()
                op = OPTR.pop()
                OPND.append(operate(a, b, op))
                st.write(
                    f"从操作数栈取出 {a} 和 {b}，从算符栈取出 {op}，执行操作 {a} {op} {b}，结果 {operate(a, b, op)} 加入操作数栈")
            OPTR.append(expr[i])
            st.write(f"加入算符栈: {expr[i]}")
            i += 1
        st.write(f"当前算符栈: {OPTR}")
        st.write(f"当前操作数栈: {OPND}")
        st.write("---")

    while OPTR:
        st.write(f"处理剩余的运算符：")
        b = OPND.pop()
        a = OPND.pop()
        op = OPTR.pop()
        OPND.append(operate(a, b, op))
        st.write(
            f"从操作数栈取出 {a} 和 {b}，从算符栈取出 {op}，执行操作 {a} {op} {b}，结果 {operate(a, b, op)} 加入操作数栈")
        st.write(f"当前算符栈: {OPTR}")
        st.write(f"当前操作数栈: {OPND}")
        st.write("---")

    st.write(f"表达式 {expr} 的结果是: {OPND[0]}")
