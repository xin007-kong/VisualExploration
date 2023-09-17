import streamlit as st
from visualizer import display_conversion

st.title("基数转换器")

decimal_num = st.number_input("输入一个十进制数", value=0, step=1)
base = st.selectbox("选择一个基数", [2, 8, 16])

if st.button('开始转换'):
    display_conversion(decimal_num, base)