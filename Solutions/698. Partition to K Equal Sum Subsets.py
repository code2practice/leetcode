'''
698. Partition to K Equal Sum Subsets
Medium
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
 
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0 or nums_sum < k:
            return False
        subset_sum = nums_sum / k
        ks = [0] * k
        nums.sort(reverse=True)
        def can_partition(j):
            if j == len(nums):
                for i in range(k):
                    if ks[i] != subset_sum:
                        return False
                return True
            for i in range(k):
                if ks[i] + nums[j] <= subset_sum:
                    ks[i] += nums[j]
                    if can_partition(j + 1):
                        return True
                    ks[i] -= nums[j]
            return False
        return can_partition(0)
