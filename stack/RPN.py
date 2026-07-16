import operator
x = ["2","1","+","3","*"]
y = len(x)

stack = []

def oper(o):
    num1 = int(stack[-1])  
    num2 = int(stack[-2])  
    stack.pop()            
    stack.pop()          
    stack.append(o(num2, num1))
    
    
for i in range(y):
    if stack and x[i] == "+":
        oper(operator.add)
    elif stack and x[i] == "*":
        oper(operator.mul)
    elif stack and x[i] == "/":
        oper(operator.floordiv)
    elif stack and x[i] == "-":
        oper(operator.sub)
    else:
        stack.append(x[i])
    
print(stack)   