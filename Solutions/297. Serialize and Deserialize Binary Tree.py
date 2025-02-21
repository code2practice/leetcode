'''
297. Serialize and Deserialize Binary Tree
Hard
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
 
Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:
Input: root = []
Output: []
'''

class Codec:
   def __init__(self):
       self.splitter = ','
       self.null = 'null'
   def serialize(self, root):
       res = []
       if not root:
           return ''
       q = deque([root])
       while q:
           top = q.popleft()
           if top:
               res.append(str(top.val))
               q.append(top.left)
               q.append(top.right)
           else:
               res.append(self.null)
       return self.splitter.join(res)

    def deserialize(self, data):
       if not data:
           return None
       s_data = data.split(self.splitter)
       if not s_data:
           return None
       root = TreeNode(s_data[0])
       q = deque([root])
       i = 1
       while i < len(s_data) and q:
           top = q.popleft()
           if s_data[i] != self.null:
               left = TreeNode(s_data[i])
               top.left = left
               q.append(left)
           i += 1
           if s_data[i] != self.null:
               right = TreeNode(s_data[i])
               top.right = right
               q.append(right)
           i += 1
       return root
