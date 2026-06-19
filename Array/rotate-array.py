"""
Problem:
Rotate an Array to the Right by One Position

Algorithm:
1. Store the last element of the array.
2. Shift all elements to the right by one position. 
3. Place the stored last element at the beginning.


Time Complexity:
O(n)

Edge Cases:
- Negative numbers
- Single element array

Date Solved:
June 2026
"""



a = []
n = len(a) - 2

while True:
	if len(a) == 1 or len(a) == 0:
		print(a)
		break
	else:
		for i in range(n, 0, -1):
			temp = a[i+1]
			a[i+1] = a[i]
			a[i] = temp
		break

if len(a) != 1 and len(a) != 0:
	temp = a[0]
	a[0] = a[1]
	a[1] = temp
	print(a)