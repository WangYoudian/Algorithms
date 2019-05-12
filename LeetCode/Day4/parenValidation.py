from queue import LifoQueue

def isValid(s):
    stack = LifoQueue()
    top = ''
    dic = {')':'(', ']':'[', '}':'{'}
    for paren in s:
        if paren in dic:
            if stack.empty():
                return False
            else:
                top = stack.get()
                if dic[paren] != top:
                    stack.put(top)
                    stack.put(paren)
        else:
            stack.put(paren)
    return stack.empty()

# Python3 code to Check for 
# balanced parentheses in an expression 
open_list = ["[","{","("] 
close_list = ["]","}",")"] 

# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"

# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 

string = "[{}{})(]"
print(string,"-", check(string)) 


print(isValid('([)]'))
print(isValid('{[]}'))