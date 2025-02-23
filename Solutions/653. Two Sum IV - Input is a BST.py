'''
653. Two Sum IV - Input is a BST
Easy
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
 
Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
'''

'''
Complexity
Time: O(N), where N is the number of nodes in the BST.
Space: O(N), it's the space for seen HashSet in the worst case.
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, seen):
            if root == None:
                return False
            complement = k - root.val
            if complement in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        return dfs(root, set())


'''
Time: O(N), where N is the number of nodes in the BST.
Space: O(H), where H is the height of the BST. The size of stack is up to O(H).
'''
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left
        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right
        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val
        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val
        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)
        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
