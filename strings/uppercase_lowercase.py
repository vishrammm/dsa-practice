
s = "chatGPT"
upper = 0
lower = 0
for c in s:
    if c != c.lower():
        upper += 1
    else:
        lower += 1
    
print(upper)
print(lower)

"""
Problem:
Count the number of uppercase and lowercase letters in a string.

Algorithm:
1. Traverse the string.
2. Keep track of uppercase and lowercase letters.
3. Increment respective counters based on the case of each character.

Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with all uppercase letters
- String with all lowercase letters

Date Solved:
03 JULY 2026
"""