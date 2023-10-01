import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Simulating a simplified memory management system
TOTAL_BLOCKS = 100
memory = [0] * TOTAL_BLOCKS  # 0 means free, 1 means occupied

def allocate_memory(blocks):
    start_index = -1
    consecutive_free_blocks = 0
    
    for i, block in enumerate(memory):
        if block == 0:
            if start_index == -1:
                start_index = i
            consecutive_free_blocks += 1
            if consecutive_free_blocks == blocks:
                for j in range(start_index, start_index + blocks):
                    memory[j] = 1
                return True
        else:
            start_index = -1
            consecutive_free_blocks = 0
            
    return False

def free_memory(start, blocks):
    for i in range(start, start + blocks):
        if i < TOTAL_BLOCKS:
            memory[i] = 0

def visualize_memory():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow([memory], cmap="RdBu_r", aspect="auto")
    ax.set_title("Memory Blocks")
    ax.set_yticks([])
    ax.set_xlabel("Block Index")
    ax.set_xticks(range(0, TOTAL_BLOCKS, 10))
    st.pyplot(fig)

st.title("动态存储分配模拟")

action = st.selectbox("选择操作:", ["分配", "释放"])
if action == "分配":
    blocks = st.slider("选择要分配的块数量:", 1, 20, 5)
    if st.button("分配内存"):
        if allocate_memory(blocks):
            st.success(f"成功分配 {blocks} 块!")
        else:
            st.error("不足够的连续内存块可供分配!")
elif action == "释放":
    start = st.slider("选择释放内存的起始块:", 0, TOTAL_BLOCKS - 1, 0)
    blocks = st.slider("选择要释放的块数量:", 1, 20, 5)
    if st.button("释放内存"):
        free_memory(start, blocks)
        st.success(f"从 {start} 开始的 {blocks} 块已被释放!")

visualize_memory()
