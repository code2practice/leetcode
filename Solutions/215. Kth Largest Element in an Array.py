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

'''
1. First, we need to choose so-calledpivotand partition element ofnumsinto 3 parts: elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: less and more or equal)
2. Next step is to see how many elements we have in each group: ifk <= L, whereLis size ofleft, than we can be sure that we need to look into the left part. Ifk > L + M, whereMis size ofmidgroup, than we can be sure, that we need to look into the right part. Finally, if none of these two condition holds, we need to look in themidpart, but because all elements there are equal, we can immedietly returnmid[0].

Complexity: time complexity isO(n)in average, because on each time we reduce searching range approximately2times. This is not strict proof, for more details you can do some googling. Space complexity isO(n)as well.
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
