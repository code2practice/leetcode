'''
272. Closest Binary Search Tree Value II
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
 
Example 1:

Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:
Input: root = [1], target = 0.000000, k = 1
Output: [1]
 
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109
 
Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
'''

class Solution:
   def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
       # Perform in-order depth-first search to traverse the tree.
       def in_order_dfs(node):
           if node is None:
               return
        
           # Recurse on the left child.
           in_order_dfs(node.left)
        
           # Process the current node.
           # If we have fewer than k values, add current node's value.
           if len(closest_values) < k:
               closest_values.append(node.val)
           else:
               # Once we have k values, check if current node is closer to target
               # than the first value in the deque. If not, no need to proceed further.
               if abs(node.val - target) >= abs(closest_values[0] - target):
                   return
            
               # If the current node is closer, pop the first value and append the current value.
               closest_values.popleft()
               closest_values.append(node.val)
        
           # Recurse on the right child.
           in_order_dfs(node.right)
       # This deque will store the closest k values encountered so far.
       closest_values = deque()
    
       # Start the in-order traversal of the tree.
       in_order_dfs(root)
    
       # Return the k closest values as a list.
       return list(closest_values)
