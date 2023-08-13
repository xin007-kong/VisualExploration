import streamlit as st
import time
# st.title("二分查找可视化演示")


def binary_search(arr, target):
    """二分查找算法"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 计算中间位置
        if arr[mid] == target:
            return mid  # 找到目标值，返回其索引
        elif arr[mid] < target:
            left = mid + 1  # 目标值在右半部分，更新左边界
        else:
            right = mid - 1  # 目标值在左半部分，更新右边界
    return -1  # 未找到目标值


def visualize_search_process(arr, target):
    """可视化演示二分查找过程"""
    st.write("数据列表：", arr)
    st.write("查找目标：", target)

    # 二分查找前需要对列表进行排序
    arr.sort()
    st.write("排序后的数据列表：", arr)

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # 可视化展示当前查找范围
        st.write("当前查找范围：", arr[left:right+1])
        # 可视化展示当前中间位置和中间值
        st.write("当前中间位置：", mid)
        st.write("当前中间值：", arr[mid])
        time.sleep(1)  # 延迟一秒以方便演示

        if arr[mid] == target:
            st.write("找到目标值，其索引为：", mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    st.write("未找到目标值")
    return -1


def main():
    # 用streamlit实现可视化界面
    st.title("二分查找可视化演示")
    st.write("请输入待查找的数据列表和目标值")
    # 输入数据列表
    arr_input = st.text_input("输入数据列表（以空格分隔）：")
    arr = arr_input.split()  # 将输入的字符串转化为列表
    arr = [int(x) for x in arr]  # 将列表中的元素都转化为整数
    # 输入目标值
    target_input = st.text_input("输入查找目标：")
    if target_input:
        target = int(target_input)

    if not arr:
        st.warning("请先输入数据列表")
    elif not target_input:
        st.warning("请先输入查找目标")
    else:
        st.write("开始演示二分查找过程")
        visualize_search_process(arr, target)


main()
