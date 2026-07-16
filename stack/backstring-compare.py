s ="ab#c"
t = "ad#c"
stack = []
stack2 = []
for x in s:
    if stack and x == "#":
        stack.pop()
    else:
        stack.append(x)
        
for y in t:
    if stack2 and y == "#":
        stack2.pop()
    else:
        stack2.append(y)

if stack == stack2:
    print(True)
