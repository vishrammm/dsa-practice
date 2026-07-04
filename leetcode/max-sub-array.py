class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0 
        max_sum = sum(nums)
       
        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum , current_sum)
            
        return max_sum
    
    
"""
Problem:
Find the maximum sum of a contiguous subarray.

Algorithm:
1. Keep track of the current sum and the maximum sum.
2. For each element, update the current sum to be the maximum of the current element and the current sum plus the current element.
3. Update the maximum sum if the current sum is greater.


Time Complexity:
O(n)

Edge Cases:
- Empty array
- Array with all negative numbers

Date Solved:
04 JULY 2026
"""