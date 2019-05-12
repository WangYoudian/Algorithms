# 注意的一点是，C语言中，除法向0取整
# 而在Python中，除法是向下取整
# 在中间结果为负数时要分类讨论

def evalRPN(tokens):
    stack = []
    for i in range(0,len(tokens)):
        if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
            stack.append(int(tokens[i]))
        else:
            a = stack.pop()
            b = stack.pop()
            if tokens[i] == '+':
                stack.append(a+b)
            if tokens[i] == '-':
                stack.append(b-a)
            if tokens[i] == '*':
                stack.append(a*b)
            if tokens[i] == '/':
                if a*b < 0:
                    stack.append(-((-b)//a))
                else:
                    stack.append(b//a)
    return stack.pop()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
result = evalRPN(tokens)
print(result)