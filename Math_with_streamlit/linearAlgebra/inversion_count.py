# import streamlit as st


# def count_inversions(arr):
#     count = 0
#     inv_pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#                 inv_pairs.append((arr[i], arr[j]))
#                 st.write(f"发现逆序对：({arr[i]}, {arr[j]})")
#                 st.write(f"逆序数数量从{count-1}增加到{count}")
#     return count, inv_pairs


# def main():
#     st.title("逆序数计算器")

#     # 输入数组
#     arr_input = st.text_input("请输入一个整数数组，以逗号分隔：")
#     try:
#         arr = [int(x.strip()) for x in arr_input.split(",") if x.strip()]
#     except ValueError:
#         st.error("请输入有效的整数数组！")
#         return

#     # 计算逆序数
#     inversions, inv_pairs = count_inversions(arr)

#     # 显示结果
#     st.write("输入数组：", arr)
#     st.write("逆序数数量：", inversions)

#     # 可视化逆序对
#     if st.button("显示逆序对"):
#         st.write("逆序对：", inv_pairs)


# if __name__ == "__main__":
#     main()
import time
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'


def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                # plot_array(arr, title=f"交换 {arr[j+1]} 和 {arr[j]}")
                # 改成英文
                plot_array(arr, title=f"Swap {arr[j+1]} and {arr[j]}")
        if not swapped:
            break
    return arr


def plot_array(arr, title=""):
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    st.pyplot(plt)
    plt.close()
    time.sleep(0.5)


def main():
    st.title("逆序数和冒泡排序演示")

    # 输入数组
    arr_input = st.text_input("请输入一个整数数组，以逗号分隔：", "3,2,1,4")
    try:
        arr = [int(x.strip()) for x in arr_input.split(",") if x.strip()]
    except ValueError:
        st.error("请输入有效的整数数组！")
        return

    # 计算逆序数
    inversions = count_inversions(arr)
    st.write("输入数组：", arr)
    st.write("逆序数数量：", inversions)

    # 冒泡排序动画
    if st.button("开始冒泡排序"):
        st.write("冒泡排序过程：")
        bubble_sort(arr.copy())


if __name__ == "__main__":
    main()
