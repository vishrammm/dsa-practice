
s = "banana"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print(f" '{ch}' is the first non repeating char ")
        break

"""
Problem:
Find the first non-repeating character in a string.

Algorithm:
1. Traverse the string.
2. Keep track of the frequency of each character.
3. Traverse the string again and find the first character with a frequency of 1.

Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with all uppercase letters
- String with all lowercase letters

Date Solved:
07 JULY 2026
"""