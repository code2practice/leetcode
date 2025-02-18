'''
102. Binary Tree Level Order Traversal
Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
'''

# Iterative
class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = []
       if not root:
           return res
       q = deque([root])
       while q:
           s = len(q)
           temp = []
           while s:
               t = q.popleft()
               temp.append(t.val)
               if t.left:
                   q.append(t.left)
               if t.right:
                   q.append(t.right)
               s -= 1
           res.append(temp)
       return res

# Recursive
class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = defaultdict(list)
       def util(root, depth):
           if not root:return
           res[depth].append(root.val)
           util(root.left, depth + 1)
           util(root.right, depth + 1)
       util(root, 0)
       return res.values()
