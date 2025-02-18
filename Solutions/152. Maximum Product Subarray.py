'''
152. Maximum Product Subarray
Medium
Given an integer array nums, find a
subarray
that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
 
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
   def maxProduct(self, nums: List[int]) -> int:
       ma = nums[0]
       mi = nums[0]
       res = nums[0]
       for i in range(1, len(nums)):
           num = nums[i]
           if num < 0:
               ma, mi = mi, ma
           ma = max(num * ma, num)
           mi = min(num * mi, num)
           res = max(ma, res)
       return res
