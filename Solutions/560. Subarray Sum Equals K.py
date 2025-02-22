'''
560. Subarray Sum Equals K
Medium
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''

'''
This solution also works if there are negative integers in the array. If only positive integers are present, 
sliding window can also work.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        # There is a subarray(empty) with sum 0
        m[0] = 1
        running_sum = 0
        count = 0
        for i, n in enumerate(nums):
            running_sum += n
            count += m[running_sum-k]
            # make sure to add 1 to existing instead of assigning
            # 1. There may be multiple subarrays with same sum
            m[running_sum] += 1
        return count
            
