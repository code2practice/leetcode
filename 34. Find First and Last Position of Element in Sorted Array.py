'''
34. Find First and Last Position of Element in Sorted Array
Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''
class Solution:
   def searchRange(self, nums: List[int], target: int) -> List[int]:
       res = [-1,-1]
       if not nums:
           return res
       l, h = 0, len(nums)-1
       while l < h:
           mid = (l + h)//2
           if nums[mid] >= target:
               h = mid
           else:
               l = mid + 1
       if nums[l] != target:
           return res
       res[0] = l
       h = len(nums)
       while l < h:
           mid = (l + h)//2
           if nums[mid] > target:
               h = mid
           else:
               l = mid + 1
       res[1] = l-1
       return res
