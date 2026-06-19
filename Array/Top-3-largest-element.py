"""
Problem:
Find top 3 Largest Elements in an Array

Algorithm:
1. Traverse the array.
2. Keep track of the top 3 largest values.
3. Update whenever a larger value is found.

Time Complexity:
O(n)

Edge Cases:
- Negative numbers
- Single element array

Date Solved:
June 2026
"""
def find_top_three_elements(arr):
   
    first = second = third = float('-inf')

    for num in arr:
       
        if num == first or num == second or num == third:
            continue

       
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

   
    result = []
    for val in (first, second, third):
        if val != float('-inf'):
            result.append(val)
        else:
            result.append(None) 

    
    print(f"Array: {arr}")
    print(f"1st Largest: {result[0]}")
    print(f"2nd Largest: {'Not present' if result[1] is None else result[1]}")
    print(f"3rd Largest: {'Not present' if result[2] is None else result[2]}")
    print("-" * 30)
    
    return result




find_top_three_elements([10, 4, 3, 50, 23, 90, -10])

find_top_three_elements([5, 5, 5, 4, 4, 3, 5, 4])

find_top_three_elements([-5, -1, -10, -1, -5, -20])

find_top_three_elements([10, 10, 10])

find_top_three_elements([1, 2, 1, 2])