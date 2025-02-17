'''
156. Binary Tree Upside Down
Given the root of a binary tree, turn the tree upside down and return the new root.
You can turn a binary tree upside down with the following steps:
The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.
 
Example 1:

Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [1]
Output: [1]
 
Constraints:
The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every right node in the tree has a sibling (a left node that shares the same parent).
Every right node in the tree has no children.
'''
class Solution:
   def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       # Base case: if the root is None or the root doesn't have a left child,
       # the tree cannot be flipped, so return the root as is.
       if root is None or root.left is None:
           return root
       # Recursive case: dive into the left subtree to find the new root after flipping.
       new_root = self.upsideDownBinaryTree(root.left)
       # Once the recursion unwinds, the original root's left child's right child
       # becomes the original root (making the left child the new parent).
       root.left.right = root
       # The left child's left child becomes the original root's right child.
       root.left.left = root.right
       # Erase the original root's left and right children, since they've been reassigned.
       root.left = None
       root.right = None
       # Return the new root of the flipped tree.
       return new_root
