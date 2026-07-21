stk = [100,80,60,70,60,75,85]
stack = []
spans = []

for s in stk:
    span = 1
    
    while stack and stack[-1][0] <= s:
        span += stack.pop()[1]
        
    stack.append((s,span))
    spans.append(span)
    
print(spans)
        
        