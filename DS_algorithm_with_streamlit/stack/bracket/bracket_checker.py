def is_matched(opening, closing):
    return (opening, closing) in [('(', ')'), ('[', ']'), ('{', '}')]

def check_brackets(s):
    stack = []
    for char in s:
        if char in "([{}":
            stack.append(char)
        elif char in ")]}":
            if not stack or not is_matched(stack.pop(), char):
                return False
    return not stack # 意思是如果栈为空，返回True，否则返回False
