def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:

        # Opening bracket
        if char not in pairs:
            stack.append(char)

        # Closing bracket
        else:

            # No opening bracket to match
            if not stack:
                return False

            # Wrong opening bracket
            if stack[-1] != pairs[char]:
                return False

            # Correct match
            stack.pop()

    return len(stack) == 0


print(is_valid("()"))        # True
print(is_valid("([{}])"))    # True
print(is_valid("([)]"))      # False
print(is_valid("(()"))       # False
print(is_valid(")("))        # False