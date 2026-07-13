stack = []
s = ")("

if len(s) % 2 != 0:
    print(False)
else:
    for char in s:
        if char == "(":
            stack.append(char)

        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop() 
            else:
                stack.append(char)

    if len(stack) == 0:
        print(True)
    else:
        print(False)

"""
Problem:
Check if a string of parentheses is valid.

Algorithm:
1. Use a stack to keep track of opening parentheses.
2. For each closing parenthesis, check if it matches the most recent opening parenthesis.
3. If all parentheses are matched and the stack is empty, the string is valid.

Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with unmatched opening or closing parentheses

Date Solved:
13 JULY 2026
"""