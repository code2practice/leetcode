'''
515. Find Largest Value in Each Tree Row
Solved
Medium
Topics
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
'''

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            m = -math.inf
            l = len(q)
            for _ in range(l):
                top = q.popleft()
                if top.val > m:
                    m = top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            res.append(m)
        return res
