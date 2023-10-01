# import streamlit as st
# import matplotlib.pyplot as plt

# def plot_linear_table(base, l, size=10):
#     fig, ax = plt.subplots(figsize=(10, 8))
#     locations = [base + (i - 1) * l for i in range(1, size+1)]
#     for i, loc in enumerate(locations):
#         rect = plt.Rectangle((0, i), l, 0.8, fc='blue')
#         ax.add_patch(rect)
#         ax.text(0.5*l, i+0.4, f"a{i+1} ({loc})", va='center', ha='center', color='white')
#     ax.set_xlim(0, l)
#     ax.set_ylim(0, size)
#     ax.axis('off')
#     st.pyplot(fig)

# st.title("线性表的顺序表示")

# base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
# l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)

# # Visualize
# plot_linear_table(base, l)


# -----------------------------

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np


# def plot_memory_palace(base, l, size=10):
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Drawing the corridor
#     ax.plot([0, size+1], [0, 0], color="grey", lw=8)

#     # Visualizing data elements as frames
#     locations = [base + (i - 1) * l for i in range(1, size+1)]
#     for i, loc in enumerate(locations):
#         color_intensity = np.clip((loc-base)/1000.0, 0, 1)
#         ax.plot([i+1, i+1], [-0.5, 0.5],
#                 color=plt.cm.Blues(color_intensity), lw=4)
#         ax.text(i+1, 0.6, f"Loc: {loc}", ha='center', fontsize=10, rotation=90)
#         ax.text(i+1, -0.6, f"a{i+1}", ha='center', fontsize=12, color="red")

#     # Setting aesthetics
#     ax.set_xlim(0, size+1)
#     ax.set_ylim(-1, 1)
#     ax.axis("off")

#     st.pyplot(fig)


# st.title("线性表的顺序表示：记忆宫殿")

# base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
# l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)

# # Visualize
# plot_memory_palace(base, l)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def plot_memory_palace(base, l, size=10):
    fig, ax = plt.subplots(figsize=(15, 8))

    # Drawing the corridor
    ax.plot([0, size+1], [0, 0], color="grey", lw=8)

    # Visualizing data elements as frames
    locations = [base + (i - 1) * l for i in range(1, size+1)]
    for i, loc in enumerate(locations):
        color_intensity = np.clip((loc-base)/1000.0, 0, 1)
        ax.plot([i+1, i+1], [-0.5, 0.5],
                color=plt.cm.Blues(color_intensity), lw=4)
        ax.text(i+1, 0.6, f"Loc: {loc}", ha='center', fontsize=10, rotation=90)
        ax.text(i+1, -0.6, f"a{i+1}", ha='center', fontsize=12, color="red")

    # Setting aesthetics
    ax.set_xlim(0, size+1)
    ax.set_ylim(-1, 1)
    ax.axis("off")

    st.pyplot(fig)


st.title("线性表的顺序表示：记忆宫殿")

base = st.number_input("请输入基地址 LOC(a1):", min_value=0, value=100, step=1)
l = st.number_input("请输入元素所占存储单位:", min_value=0, value=10, step=1)
size = st.slider("选择线性表元素个数:", 1, 20, 10)

# Visualize
plot_memory_palace(base, l, size)
