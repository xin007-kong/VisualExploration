import streamlit as st
import matplotlib.pyplot as plt

# Simulating memory and pointers
TOTAL_ELEMENTS = 10
# Mock base addresses for each element
elem = list(range(1000, 1000 + TOTAL_ELEMENTS*10, 10))
pointer_index = 0  # Pointer starts at the first element


def visualize_pointer_and_array():
    fig, ax = plt.subplots(figsize=(15, 6))

    # Plot each element of the array
    for i, address in enumerate(elem):
        ax.plot(i, 0, 'o', markersize=15, color='blue' if i ==
                pointer_index else 'grey')
        ax.text(i, 0.5, f"elem[{i}]\nAddr: {address}",
                ha='center', va='center', fontsize=10)

    # Displaying the pointer
    ax.annotate('Pointer', xy=(pointer_index, 0), xytext=(pointer_index, -2),
                arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center', va='center', color='red')

    ax.set_xlim(-1, TOTAL_ELEMENTS)
    ax.set_ylim(-3, 2)
    ax.axis('off')

    st.pyplot(fig)


st.title("数组与指针的可视化")

if st.button("Move Pointer Left"):
    pointer_index = max(0, pointer_index - 1)

if st.button("Move Pointer Right"):
    pointer_index = min(TOTAL_ELEMENTS - 1, pointer_index + 1)

selected_index = st.slider(
    "Or select a specific index:", 0, TOTAL_ELEMENTS - 1, pointer_index)
pointer_index = selected_index

visualize_pointer_and_array()
