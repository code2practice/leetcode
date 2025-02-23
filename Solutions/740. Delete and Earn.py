'''
740. Delete and Earn
Medium
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
 
Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 
Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''

'''
Solution:
Observations:
The order of nums does not matter.
Once we decide that we want a num, we can add all the occurrences of num into the total.
We first transform the nums array into a points array that sums up the total number of points for that particular value. A value of x will be assigned to index x in points.
nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
 points: [0, 0, 4, 9, 4] <- This is the gold in each house!
The condition that we cannot pick adjacent values is similar to the House Robber question that we cannot rob adjacent houses. Simply pass points into the rob function for a quick win 🌝!
'''

class Solution(object):
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr
    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)
