'''
18. 4Sum
Medium
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
 
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
Complexity:
Time: O(N^3)
Extra Space (Without count output as space): O(sorting)
'''

class Solution:
   def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       nums.sort()
       n = len(nums)
       ans = set()
       for i in range(n):
           for j in range(i+1, n):
               l, r = j + 1, n - 1
               remain = target - nums[i] - nums[j]
               while l < r:
                   if nums[l] + nums[r] == remain:
                       ans.add((nums[i], nums[j], nums[l], nums[r]))
                       l += 1
                       r -= 1
                   elif nums[l] + nums[r] > remain:
                       r -= 1
                   else:
                       l += 1
       return ans

# (Important)Follow-up question: Calculate K-Sum?
class Solution:  # 1084 ms, faster than 37.26%
   def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       def dfs(l, r, k, target, path, out):  # [l, r] inclusive
           if k == 2:
               while l < r:
                   if nums[l] + nums[r] == target:
                       out.append(path + [nums[l], nums[r]])
                       while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                       l, r = l + 1, r - 1
                   elif nums[l] + nums[r] > target:
                       r -= 1  # Decrease sum
                   else:
                       l += 1  # Increase sum
               return
           while l < r:
               dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
               while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
               l += 1
       def kSum(k):  # k >= 2
           ans = []
           nums.sort()
           dfs(0, len(nums)-1, k, target, [], ans)
           return ans
       return kSum(4)
