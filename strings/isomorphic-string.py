s = "egg"
w = "add"

def is_isomorphic(s, w):
    if len(s) != len(w):
        return False

    forward = {}
    backward = {}

    for i in range(len(s)):
        if s[i] in forward:
            if forward[s[i]] != w[i]:
                return False
        else:
            if w[i] in backward:
                return False

            forward[s[i]] = w[i]
            backward[w[i]] = s[i]

    return True
print(is_isomorphic(s, w))

"""
Problem:
Determine if two strings are isomorphic.

Algorithm:
1. Check if the lengths of the two strings are equal. If not, they cannot be isomorphic.
2. Create a mapping of characters from the first string to the second string.

Time Complexity:
O(n)

Edge Cases:
- Empty strings

Date Solved:
12 JULY 2026
"""

    
        
    