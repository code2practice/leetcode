'''
373. Find K Pairs with Smallest Sums
Medium
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
 
Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 
Constraints:
1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
'''

'''
Note that the approach to increment index by comparing does not work here as
it may miss some cases. Keeping track of visited is the rght way.
'''

class Solution:
   def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
       q = queue.PriorityQueue()
       q.put((a[0] + b[0], 0, 0))
       res = []
       visited = set([(0, 0)])
       for _ in range(k):
           top, i, j = q.get()
           res.append([a[i], b[j]])
           if i + 1 < len(a) and ((i + 1), j) not in visited:
               visited.add(((i + 1), j))
               q.put((b[j] + a[i + 1], i + 1, j))
           if j + 1 < len(b) and (i, (j + 1)) not in visited:
               visited.add((i, (j + 1)))
               q.put((a[i] + b[j + 1], i, j + 1))
       return res
