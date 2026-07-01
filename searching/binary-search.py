a = [2, 5, 8, 11, 15, 19, 24, 30]
x = 20

def binary(a):
    left = 0 
    right = len(a)-1
    while(True):
        mid = (left + right) // 2
        if a[mid] == x:
            print(f"Element found at index {mid}")
            break
        else:
            print("Element not found")
            break
        
        if a[mid] < x:
            left = mid +1
            
        else:
            right = mid - 1
            
binary(a)
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