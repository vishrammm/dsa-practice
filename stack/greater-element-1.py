nums1  = [4,1,2]
nums2 = [1,3,4,2]

greater = {}
stack = []

for num in nums2:
    while stack and num > stack[-1]:
        n = stack.pop()
        greater[n] = num
    stack.append(num)

ans = []

for num in nums1:
    if num in greater:
        ans.append(greater[num])
    else:
        ans.append(-1)
        
print(ans)
    