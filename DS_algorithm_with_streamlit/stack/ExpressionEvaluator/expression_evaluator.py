def operate(a, b, op):
    """执行基本的四则运算。
    
    参数:
    - a: 第一个操作数
    - b: 第二个操作数
    - op: 运算符，可以是 '+', '-', '*', '/'
    
    返回:
    - 运算的结果
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def evaluate_expression(expr):
    """评估一个简单的算术表达式。
    
    这个函数使用两个栈来评估一个只包含整数和四则运算符的算术表达式。
    它不支持括号或其他复杂的运算符。
    
    参数:
    - expr: 要评估的算术表达式，例如 "3+5*2"
    
    返回:
    - 表达式的计算结果
    """

    # OPTR栈用于存储运算符
    OPTR = []
    # OPND栈用于存储操作数
    OPND = []

    i = 0
    while i < len(expr):
        # 如果当前字符是数字
        if expr[i].isdigit():
            # 记录数字的开始位置
            start = i
            # 继续遍历，直到找到数字的结束位置
            while i < len(expr) and expr[i].isdigit():
                i += 1
            # 将完整的数字加入到操作数栈
            OPND.append(int(expr[start:i]))
    else:
        # 当前字符是运算符
        # 在执行运算之前，检查运算符的优先级
        
        # 以下循环确保在将新的运算符压入OPTR栈之前，先处理栈顶的高优先级运算符
        while OPTR and OPTR[-1] in "+-*/" and (expr[i] in "+-" or expr[i] in "*/" and OPTR[-1] in "*/"):
            # 例子1: expr = "3+5*2", 当i=3时，expr[i]是'*'，OPTR[-1]是'+'，因为'*'的优先级高于'+'，所以不执行循环内的代码，直接将'*'压入OPTR栈
            
            # 例子2: expr = "3*5+2", 当i=3时，expr[i]是'+'，OPTR[-1]是'*'，因为'*'的优先级高于'+'，所以执行循环内的代码，先处理乘法
            
            # 例子3: expr = "3*5*2", 当i=3时，expr[i]是'*'，OPTR[-1]也是'*'，因为两者优先级相同，所以执行循环内的代码，先处理左边的乘法
            
            # 从操作数栈中取出两个操作数
            b = OPND.pop()
            a = OPND.pop()
            # 从运算符栈中取出一个运算符
            op = OPTR.pop()
            # 执行运算并将结果加入到操作数栈
            OPND.append(operate(a, b, op))
        # 将当前运算符加入到运算符栈
        OPTR.append(expr[i])
        i += 1


    # 如果运算符栈中还有运算符，继续执行运算
    while OPTR:
        b = OPND.pop()
        a = OPND.pop()
        op = OPTR.pop()
        OPND.append(operate(a, b, op))

    # 返回操作数栈的顶部，即表达式的计算结果
    return OPND[0]
