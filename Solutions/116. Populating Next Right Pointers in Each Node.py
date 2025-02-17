'''
116. Populating Next Right Pointers in Each Node
Medium
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 
Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:
Input: root = []
Output: []
'''

# Using BFS
class Solution:
   def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       if not root:
           return
       q = deque([root])
       while q:
           s = len(q)
           for i in range(s):
               top = q.popleft()
               if i < s -1:
                   top.next = q[0]
               if top.left:
                   q.append(top.left)
               if top.right:
                   q.append(top.right)
       return root

# using Recursion
class Solution:
   def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       if not root:
           return
       if root.left:
           root.left.next = root.right
       if root.right:
           root.right.next = root.next.left if root.next else None
       self.connect(root.left)
       self.connect(root.right)
       return root

'''
(Important)BFS - Space-Optimized Approach O(1) space
We first populate the next pointers of child nodes of current level. This makes it possible to traverse the next level without using a queue. 
To populate next pointers of child, the exact same logic as above is used
We simply traverse to root's left child and repeat the process - traverse current level, fill next pointers of child 
nodes and then again update root = root -> left. So, we are basically performing standard BFS traversal in O(1) space by 
using next pointers to our advantage
The process continues till we reach the last level of tree
'''
class Solution:
   def connect(self, root):
       head = root
       while root:
           cur, root = root, root.left
           while cur:
               if cur.left:
                   cur.left.next = cur.right
                   if cur.next: cur.right.next = cur.next.left
               else: break
               cur = cur.next 
       return head
