import streamlit as st
from visualizer_bracket import display_bracket_check

st.title('括号检验工具')

input_string = st.text_input('请输入包含括号的字符串:')
if st.button('检验'):
    display_bracket_check(input_string)
