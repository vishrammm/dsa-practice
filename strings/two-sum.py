def two_sum(num, target):
    
    if len(num) < 2:
        return [] 
        
    seen = {}
    for i in range(len(num)):
        current_num = num[i]
        needed_num = target - current_num
        
        if needed_num in seen:
            return [seen[needed_num], i]
            
        seen[current_num] = i
        
    return [] 

print(two_sum([-3, 4, 3, 9], 6))  # Output: [0, 3]

print(two_sum([], 9))             # Output: []


"""
Problem:
Find two numbers in an array that add up to a specific target.

Algorithm:
1. Traverse the array.
2. Keep track of the numbers we have seen so far.
3. For each number, calculate the complement needed to reach the target.
4. If the complement is in our seen set, we have found our pair.
5. Otherwise, add the current number to the seen set.


Time Complexity:
O(n)

Edge Cases:
- Empty array
- Array with only one element
- Array with no valid pair

Date Solved:
11 JULY 2026
"""