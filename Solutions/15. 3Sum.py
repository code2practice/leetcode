'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
 
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
   def threeSum(self, nums):
       nums.sort()
       result = []
       for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
           if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
               continue
           mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
           right = len(nums) - 1
           while mid < right:
               curr_sum = nums[left] + nums[mid] + nums[right]
               if curr_sum < 0:
                   mid += 1
               elif curr_sum > 0:
                   right -= 1
               else:
                   result.append([nums[left], nums[mid], nums[right]])
                   while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                       mid += 1
                   while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                       right -= 1
                   mid += 1
                   right -= 1
       return result

'''
Time Complexity
The time complexity of the given code is O(n^2). This is because there is a nested loop where the outer loop runs for n times (reduced by 2 to avoid unnecessary 
last iterations due to triplets), and within this loop, there are two pointers that are moving independently towards each other, which in total will lead to n iterations 
in the worst case. There are no nested loops inside the while loop, so the inner operations are constant time notwithstanding the while conditions which are also O(n). 
Multiplying these together gives us n * n = n^2, hence O(n^2).
Space Complexity
The space complexity of the code is O(log n) if we don't take the output space into consideration, which would be O(n). The space complexity arises due to the space used 
by the sorting algorithm, which is typically O(log n) for the commonly used algorithms like QuickSort or MergeSort in many standard programming libraries.
'''
