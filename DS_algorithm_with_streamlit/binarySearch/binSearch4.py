# from bokeh.plotting import figure, curdoc
# from bokeh.models import ColumnDataSource
# from bokeh.models.widgets import TextInput, Button
# from bokeh.layouts import row, column
# import numpy as np

# # 创建Bokeh图表对象
# plot = figure(x_range=(0, 100), y_range=(-1, 1), plot_height=200)

# # 创建数据源
# source = ColumnDataSource(data=dict(x=[], y=[]))

# # 创建图形元素
# line = plot.line(x='x', y='y', source=source, line_width=3, line_alpha=0.6)

# # 创建文本框和按钮
# arr_input = TextInput(title="数据列表（以空格分隔）：")
# target_input = TextInput(title="查找目标：")
# button = Button(label="开始搜索")

# # 定义二分查找函数


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# # 定义搜索事件回调函数


# def search():
#     # 获取文本框中的输入值
#     arr = np.sort(np.array(arr_input.value.split(), dtype=int))
#     target = int(target_input.value)

#     # 首先清空数据源
#     source.data = dict(x=[], y=[])

#     # 进行二分查找，并更新数据源
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             source.stream(dict(x=[mid, mid], y=[-1, 1]))
#             return
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#         # 更新数据源
#         source.stream(dict(x=[mid, mid], y=[-1, 1]))

#     # 显示未找到目标值的提示
#     source.stream(dict(x=[-1], y=[0]))


# # 将图形元素和控件组合起来，并显示
# layout = column(row(arr_input, target_input, button), plot)
# button.on_click(search)
# curdoc().add_root(layout)
import streamlit as st
import igraph as ig

# 创建一个空的有向图
graph = ig.Graph(directed=True)

# 添加节点和边
graph.add_vertices(5)
graph.add_edges([(0, 1), (1, 2), (2, 3), (3, 4)])

# 创建一个Streamlit应用程序
st.title('交互式链表学习程序')

# 添加一个用于显示图形的容器
graph_container = st.container()

# 在容器中绘制图形
with graph_container:
    st.write(ig.plot(graph, bbox=(300, 300), margin=20))

# 添加一个用于选择节点的滑块
selected_node = st.slider('选择节点', 0, 4)

# 在图形中突出显示所选节点
highlighted = [True if i == selected_node else False for i in range(5)]
graph.vs['color'] = ['red' if h else 'blue' for h in highlighted]

# 更新图形容器中的图形
with graph_container:
    st.write(ig.plot(graph, bbox=(300, 300), margin=20))
