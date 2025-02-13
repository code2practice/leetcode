'''
129. Sum Root to Leaf Numbers
Medium
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
 
Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''
class Solution:
   def sumNumbers(self, root: Optional[TreeNode]) -> int:
       s = [0]
       def util(root, n, s):
           if not root:
               return
           curr = n * 10 + root.val
           if not (root.left or root.right):
               s[0] += curr
           util(root.left, curr, s)
           util(root.right, curr,s)
       util(root, 0, s)
       return s[0]
