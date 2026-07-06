items = "programming"
seen = set()
duplicates = set()
og = []

for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
        
for i in items:
    if i not in duplicates:
        og.append(i)
wow = og[0]
print(f"The first non repeating char is '{wow}'.")


"""
Problem:
Find the first non-repeating character in a string.

Algorithm:
1. Traverse the string.
2. Keep track of character frequencies.
3. Traverse the string again and return the first character with a frequency of 1.

Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with all repeating characters

Date Solved:
03JULY 2026
"""