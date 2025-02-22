'''
416. Partition Equal Subset Sum
Medium
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
Using the 0/1 Knapsack concept. Pay attention the inner loop is decreasing in order to avoid repetition.
'''

class Solution:
   def canPartition(self, nums: List[int]) -> bool:
       sum = 0
       for n in nums:
           sum += n
       if sum % 2 == 1:
           return False
       half = sum//2
       d = [False] * (half  +1)
       d[0] = True
       for i in range(len(nums)):
           for j in range(half, nums[i]-1, -1):
               d[j] = d[j - nums[i]] | d[j]
       return d[half]
