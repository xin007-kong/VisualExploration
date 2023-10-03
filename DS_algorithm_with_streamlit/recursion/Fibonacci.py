import matplotlib.pyplot as plt

def factorial(n, depth=0):
    if n == 0:
        plt.text(depth, n, 'f(0) = 1')
        return 1
    else:
        value = n * factorial(n-1, depth+1)
        plt.text(depth, n, f'f({n}) = {value}')
        return value

factorial(5)
plt.gca().invert_yaxis()  # 使y轴从大到小显示
plt.show()
