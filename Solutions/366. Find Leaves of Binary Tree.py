'''
366. Find Leaves of Binary Tree
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 
Example 1:

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:
Input: root = [1]
Output: [[1]]
'''

class Solution:
   def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
       d = defaultdict(list)
       def dfs(u):
           if u == None:
               return 0
           leftLevel = dfs(u.left)
           rightLevel = dfs(u.right)
           currentLevel = (
               max(leftLevel, rightLevel) + 1
           )  # calculate level of current node
           d[currentLevel].append(u.val)
           return currentLevel
       dfs(root)
       return list(d.values())
