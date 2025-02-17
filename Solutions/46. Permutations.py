'''
46. Permutations
Medium
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]:
       def util(nums):
           if not nums:
               return []
           if len(nums) == 1:
               return [[nums[0]]]
           res = []
           temp = util(nums[1:])
           for t in temp:
               res.append([nums[0]] + t)
           for i in range(1, len(nums)):
               nums[0], nums[i] = nums[i], nums[0]
               for t in self.permute(nums[1:]):
                   res.append([nums[0]] + t)
           return res
       return util(nums)
