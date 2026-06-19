"""
Problem:
Find Largest Element in an Array

Algorithm:
1. Traverse the array.
2. Keep track of the largest value.
3. Update whenever a larger value is found.

Time Complexity:
O(n)

Edge Cases:
- Negative numbers
- Single element array

Date Solved:
June 2026
"""
def find_largest(arr):
    if not arr:
        return None  

    largest = arr[0] 

    for num in arr:
        if num > largest:
            largest = num  

    return largest