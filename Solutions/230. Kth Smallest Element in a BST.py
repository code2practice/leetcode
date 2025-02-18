'''
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
 
Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
'''

class Solution:
   def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       if not root:
           return 0
       s = []
       while s or root:
           while root :
               s.append(root)
               root = root.left
           top = s.pop()
           k -= 1
           if k == 0:
               return top.val
           root = top.right
