def decimal_to_base(n,base):
    digits = "0123456789ABCDEF"
    stack = []
    while n > 0:
        remainder = n % base # 意思是取余数
        stack.append(digits[remainder]) # 将余数添加到栈中
        n = n // base
    return stack # 返回栈