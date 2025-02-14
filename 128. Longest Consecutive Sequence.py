'''
128. Longest Consecutive Sequence
Medium
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# With Map
class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
       d = defaultdict(int)
       m = 0
       for n in nums:
           if d[n] != 0:
               continue
           left = d[n-1]
           right = d[n+1]
           res = left + right + 1
           d[n] = res
           m = max(m, res)
           d[n - left] = res
           d[n + right]= res
       return m
      
# With Set
class Solution:
   def longestConsecutive(self, nums):
   nums = set(nums)
   best = 0
   for x in nums:  #We are iterating over the set instead of original list
       if x - 1 not in nums: # Elements in set is always sorted
           y = x + 1
           while y in nums:
               y += 1
           best = max(best, y - x)
   return best 
