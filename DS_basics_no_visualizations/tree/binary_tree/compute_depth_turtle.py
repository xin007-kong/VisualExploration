import turtle
"""
下面的例子树是：
         1
        / \
       2   3
      / \
     4   5
    /
   6

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def draw_tree(node, x, y, step):
    if not node:
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(node.value, align="center", font=("Arial", 12, "normal"))
    if node.left:
        turtle.penup()
        turtle.goto(x-step, y-step)
        turtle.pendown()
        turtle.goto(x, y)
        draw_tree(node.left, x-step, y-step, step/2)
    if node.right:
        turtle.penup()
        turtle.goto(x+step, y-step)
        turtle.pendown()
        turtle.goto(x, y)
        draw_tree(node.right, x+step, y-step, step/2)

def max_depth(root, depth=1):
    if not root:
        return 0
    turtle.penup()
    turtle.goto(-400, turtle.ycor()-20)
    turtle.pendown()
    turtle.write("进入max_depth("+str(root.value)+")，当前深度为："+str(depth), align="left", font=("Arial", 12, "normal"))
    left_depth = max_depth(root.left, depth+1)
    turtle.penup()
    turtle.goto(-400, turtle.ycor()-20)
    turtle.pendown()
    turtle.write("max_depth("+str(root.value)+")的左子树递归结束，返回值为："+str(left_depth), align="left", font=("Arial", 12, "normal"))
    right_depth = max_depth(root.right, depth+1)
    turtle.penup()
    turtle.goto(-400, turtle.ycor()-20)
    turtle.pendown()
    turtle.write("max_depth("+str(root.value)+")的右子树递归结束，返回值为："+str(right_depth), align="left", font=("Arial", 12, "normal"))
    result = max(left_depth, right_depth) + 1
    turtle.penup()
    turtle.goto(-400, turtle.ycor()-20)
    turtle.pendown()
    turtle.write("max_depth("+str(root.value)+")结束，返回值为："+str(result), align="left", font=("Arial", 12, "normal"))
    return result

# 示例用法
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

turtle.speed(1)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
draw_tree(root, 0, 200, 100)
turtle.penup()
turtle.goto(-400, -200)
turtle.pendown()
turtle.write("递归过程：", align="left", font=("Arial", 12, "normal"))
turtle.penup()
turtle.goto(-400, turtle.ycor()-20)
turtle.pendown()
max_depth(root)
turtle.done()