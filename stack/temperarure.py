temp = [73,74,75,71,69,72,76,73]
l = len(temp)-1

stack = []

def counts(temp,k):
    h = k
    w = 0
    while k+1 < len(temp) and temp[k+1] < temp[h]:
        k += 1
        w += 1
        
    return w
    
for i in range(l):
    z = 0
    if temp[i+1] > temp[i]:
        z += 1
        stack.append(z)
    else:
        if i == l-1 and temp[l] < temp[i]:
            stack.append(0)
        if i == l-1 and temp[l] > temp[i]:
            stack.append(1)
        k = i
        a = counts(temp,k) + 1
        stack.append(a)
    
print(stack)       
        
