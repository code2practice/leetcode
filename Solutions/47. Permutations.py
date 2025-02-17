'''
47. Permutations II
Medium
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
 
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution:
   def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       def util(nums):
           if not nums:
               return []
           if len(nums) == 1:
               return [[nums[0]]]
           res = []
           temp = util(nums[1:])
           for t in temp:
               res.append([nums[0]] + t)
           i = 1
           while i < len(nums):
               if nums[i] == nums[i-1]:
                   i += 1
                   continue
               nums[i], nums[0] = nums[0], nums[i]
               for t in self.permuteUnique(nums[1:]):
                   res.append([nums[0]] + t)
               nums[i], nums[0] = nums[0], nums[i]
               i += 1
           return res
       nums.sort()
       return util(nums)
