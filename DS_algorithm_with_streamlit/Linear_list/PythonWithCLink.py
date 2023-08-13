import ctypes
import streamlit as st

# 加载DLL文件
linked_list = ctypes.CDLL('./linked_list.dll')

# 指定返回类型为字符串
linked_list.get_list.restype = ctypes.c_char_p

# 用户输入元素
element = st.number_input("请输入要添加的元素", step=1, format="%d")

# 添加元素
if st.button("添加元素"):
    linked_list.append(ctypes.c_int(element))

# 删除最后一个元素
if st.button("删除最后一个元素"):
    linked_list.delete_last()

# 获取并显示链表
list_str = linked_list.get_list().decode('utf-8')
st.write("当前链表:", list_str)
