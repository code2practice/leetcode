'''
450. Delete Node in a BST
Medium
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
 
Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:
Input: root = [], key = 0
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 
Follow up: Could you solve it with time complexity O(height of tree)?
It will be easier if we consider some tree and try to understand, what we need to do in different cases.

First we need to find our node in tree, so we just traverse it until root.val == key.
Case 1: node do not have any children, like 1, 8, 11, 14, 6 or 18: then we just delete it and nothing else to do here.
Case 2: node has left children, but do not have right, for example 3 or 20. In this case we can just delete this node and put connection betweeen its parent and its children: for example for 3, we put connection 5->1 and for 20 we put connection 17->18. Note, that the property of BST will be fulfilled, because for parent all left subtree will be less than its value and nothing will change for others nodes.
Case 3: node has right children, but do not have left, for example 13 and 17. This case is almost like case 2: we just can delete node and reconnect its parent with its children.
Case 4: node has both children, like 12, 5, 7, 9 or 15. In this case we can not just delete it. Let us consider node 5. We want to find succesor of this node: the node with next value, to do this we need to go one time to the right and then as left as possible. For node 5 our succesor will be 6: we go 5->7->6. How we can delete node 5 now? We swap nodes 5 and 6 (or just put value 6 to 5) and then we need to deal with new tree, where we need to delete node which I put in square. How to do it? Just understand, that this node do not have left children, so it is either Case 1 or Case 3, which we already can solve.

Complexity: Complexity of finding node is O(h), Cases 1,2,3 is O(1). Complexity of Case 4 is O(h) as well, because we first find succesor and then apply one of the Cases 1,3 only once. So, overall complexity is O(h). Space complexity is O(h) as well, because we use recursion and potentially we can find our node in the bottom of tree.
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > k:
            root.left = self.deleteNode(root.left, k)
        elif root.val < k:
            root.right = self.deleteNode(root.right, k)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        return root
