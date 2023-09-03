import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def draw_linked_list(head):
    fig, ax = plt.subplots(figsize=(10, 2))
    current = head
    x = 0.1
    while current:
        # 画节点
        rect = patches.Rectangle((x, 0.1), 0.2, 0.2, linewidth=1, edgecolor='blue', facecolor='blue')
        ax.add_patch(rect)
        # 画箭头
        if current.next:
            arrow = patches.FancyArrowPatch((x + 0.2, 0.2), (x + 0.3, 0.2), connectionstyle="arc3,rad=.5", arrowstyle='->', color="red")
            ax.add_patch(arrow)
        x += 0.3
        current = current.next
    plt.xlim(0, 1)
    plt.ylim(0, 0.5)
    plt.axis('off')
    plt.show()

# 调用draw_linked_list函数
# draw_linked_list(head)
# write your code here
if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    head = ListNode(0, node1)

    draw_linked_list(head)