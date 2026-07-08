s = "programming"

# Step 1: Manually count how many times each character appears
char_counts = {}
for char in s:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Step 2: Look through the string and find the ones that appeared only once
output = []
for char in s:
    if char_counts[char] == 1:
        output.append(char)

print(output)
# Output: ['p', 'o', 'a', 'i', 'n']