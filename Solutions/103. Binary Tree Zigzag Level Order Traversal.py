'''
103. Binary Tree Zigzag Level Order Traversal
Medium
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

# Iterative
class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       if not root:
           return []
       count = 0
       q = deque([root])
       res = []
       while q:
           count += 1
           temp = []
           for _ in range(len(q)):
               top = q.popleft()
               temp.append(top.val)
               if top.left:
                   q.append(top.left)
               if top.right:
                   q.append(top.right)
           if count %2 == 1:
               res.append(temp)
           else:
               res.append(temp[::-1])
       return res

# Recursive
class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = defaultdict(deque)
       def util(root, depth):
           if not root:return
           if depth %2 == 1:
               res[depth].appendleft(root.val)
           else:
               res[depth].append(root.val)
           util(root.left, depth + 1)
           util(root.right, depth + 1)
       util(root, 0)
       return res.values()
