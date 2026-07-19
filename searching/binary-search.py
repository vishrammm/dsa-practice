a = list(map(int, input("Enter the sorted array elements separated by space: ").split()))
x = int(input("Enter the element to search for: "))

def binary(a, x):
    left = 0
    right = len(a) - 1
    while(left <= right):
        mid = (left + right) // 2
        if a[mid] == x:
            print(f"Element found at index {mid}")
            return
        if a[mid] < x:
            left = mid +1
            
        else:
            right = mid - 1
            
binary(a, x)
"""
Problem:
Binary Search in a Sorted Array

Algorithm:
1. Initialize left and right pointers.
2. Calculate the middle index.
3. Compare the middle element with the target.
4. Adjust pointers based on the comparison.
5. Repeat until the element is found or the search space is exhausted.

Time Complexity:
O(log n)

Edge Cases:
- Negative numbers
- Single element array

Date Solved:
July 2026
"""