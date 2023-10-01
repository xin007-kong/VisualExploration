import streamlit as st
import matplotlib.pyplot as plt
import random

# Simulating a simplified memory management system
TOTAL_BLOCKS = 100
memory = [0] * TOTAL_BLOCKS  # 0 means free, 1 means occupied
pointer = None


def allocate_memory(blocks):
    global pointer
    free_blocks = [index for index, block in enumerate(memory) if block == 0]
    if len(free_blocks) >= blocks:
        start = random.choice(free_blocks)
        end = start + blocks
        if end <= TOTAL_BLOCKS and all([memory[i] == 0 for i in range(start, end)]):
            for i in range(start, end):
                memory[i] = 1
            pointer = start
            return True
    return False


def free_memory():
    global pointer
    if pointer is not None:
        block_start = pointer
        while block_start < TOTAL_BLOCKS and memory[block_start] == 1:
            memory[block_start] = 0
            block_start += 1
        pointer = None


def visualize_memory():
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.imshow([memory], cmap="RdBu_r", aspect="auto")

    # Displaying the pointer if it points to a block
    if pointer is not None:
        ax.text(pointer, 0, "↑", ha='center',
                va='center', color='yellow', fontsize=15)
        ax.text(pointer, -0.5, "ptr", ha='center',
                va='center', color='yellow', fontsize=10)

    ax.set_title("Heap Memory Simulation")
    ax.set_yticks([])
    ax.set_xlabel("Block Index")
    ax.set_xticks(range(0, TOTAL_BLOCKS, 5))
    st.pyplot(fig)


st.title("C语言的malloc与free模拟")

action = st.selectbox("选择操作:", ["malloc", "free"])
if action == "malloc":
    blocks = st.slider("选择要分配的块数量:", 1, 20, 5)
    if st.button("分配内存"):
        if allocate_memory(blocks):
            st.success(f"成功分配 {blocks} 块!")
        else:
            st.error("没有足够的连续空闲块!")
elif action == "free":
    if st.button("释放内存"):
        free_memory()
        st.success(f"内存已被释放!")

visualize_memory()
