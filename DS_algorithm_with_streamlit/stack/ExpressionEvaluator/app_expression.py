import streamlit as st
from visualizer_expression import display_expression_evaluation

st.title('表达式求值工具')

expr = st.text_input('请输入一个算术表达式:')
if st.button('求值'):
    display_expression_evaluation(expr)
