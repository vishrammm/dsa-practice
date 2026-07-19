temperatures = [73,74,75]
n = len(temperatures)
ans = [0] * n
stack = []  
        
for i, t in enumerate(temperatures):
    while stack and t > temperatures[stack[-1]]:
        x = stack.pop()
        ans[x] = i - x
        
    stack.append(i)
            
print(ans)    
