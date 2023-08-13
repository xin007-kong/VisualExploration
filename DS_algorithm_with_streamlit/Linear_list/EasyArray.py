import streamlit as st

# 定义链表节点


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 定义链表


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            value = self.head.value
            self.head = None
            return value
        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def insert(self, position, value):
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current:
                current = current.next
        if current:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if position == 0 and self.head:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current:
                current = current.next
        if current and current.next:
            current.next = current.next.next

    def update(self, position, value):
        current = self.head
        for _ in range(position):
            if current:
                current = current.next
        if current:
            current.value = value

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return ' -> '.join(values)


# 初始化链表（只有在会话状态中不存在时）
if 'linked_list' not in st.session_state:
    st.session_state.linked_list = LinkedList()

# 用户输入元素
element = st.text_input("请输入要操作的元素")
position = st.number_input("请输入元素的位置（如果适用）", min_value=0, format="%d")

# 添加元素
if st.button("添加元素"):
    st.session_state.linked_list.append(element)
    st.write('当前链表:', st.session_state.linked_list.display())

# 删除最后一个元素
if st.button("删除最后一个元素"):
    st.session_state.linked_list.pop()
    st.write('当前链表:', st.session_state.linked_list.display())

# 在指定位置插入元素
if st.button("在指定位置插入元素"):
    st.session_state.linked_list.insert(position, element)
    st.write('当前链表:', st.session_state.linked_list.display())

# 删除指定位置的元素
if st.button("删除指定位置的元素"):
    st.session_state.linked_list.delete(position)
    st.write('当前链表:', st.session_state.linked_list.display())

# 更新指定位置的元素
if st.button("更新指定位置的元素"):
    st.session_state.linked_list.update(position, element)
    st.write('当前链表:', st.session_state.linked_list.display())

# 显示链表
st.write('当前链表:', st.session_state.linked_list.display())
