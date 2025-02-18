'''
215. Kth Largest Element in an Array
Medium
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
# (Important solution)RunTime O(N)
class Solution:
   def findKthLargest(self, nums: List[int], k: int) -> int:
       pivot = random.choice(nums)
       left = [x for x in nums if x > pivot]
       mid = [x for x in nums if x == pivot]
       right = [x for x in nums if x < pivot]
       L, M = len(left), len(mid)
       if L >= k:
           return self.findKthLargest(left, k)
       elif k > L + M:
           return self.findKthLargest(right, k-L-M)
       else:
           return mid[0]
