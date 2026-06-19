"""
Problem:
Find if the given array is a palindrome

Algorithm:
1. Use two pointers, one at the start and one at the end of the array.
2. Compare elements at both pointers.
3. If they are equal, move the pointers towards each other.
4. If they are not equal, the array is not a palindrome.
5. Continue until the pointers meet or cross each other.

Time Complexity:
O(n)

Edge Cases:
- Negative numbers
- Single element array
- Empty array

Date Solved:
June 2026
"""
def is_palindrome_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True