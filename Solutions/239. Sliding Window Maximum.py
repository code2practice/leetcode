'''
239. Sliding Window Maximum
Hard
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
 
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       q = deque()
       ans = []
       for i, v in enumerate(nums):
           if q and i - k + 1 > q[0]:
               q.popleft() # remove index if out of window left
           while q and nums[q[-1]] <= v:
               q.pop()
           q.append(i)
           if i >= k - 1:
               ans.append(nums[q[0]])
       return ans
