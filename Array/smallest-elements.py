"""
Problem:
Find Smallest Element in an Array

Algorithm:
1. Traverse the array.
2. Keep track of the smallest value.
3. Update whenever a smaller value is found.

Time Complexity:
O(n)

Edge Cases:
- Negative numbers
- Single element array

Date Solved:
June 2026
"""
def find_smallest(arr):
    if not arr:
        return None  

    smallest = arr[0] 

    for num in arr:
        if num < smallest:
            smallest = num  

    return smallest