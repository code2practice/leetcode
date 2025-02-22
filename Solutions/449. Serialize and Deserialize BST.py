'''
449. Serialize and Deserialize BST
Medium
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.
 
Example 1:
Input: root = [2,1,3]
Output: [2,1,3]
Example 2:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
'''

class Codec:
    def serialize(self, root):
        vals = []
        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return " ".join(map(str, vals))
    # Naive way to deserialize.
    # Note start and end inedex in helper is important. Code
    # does not work if they are wrong. be very careful.
    def deserialize(self, data):
        if not data:
            return None
        vals = [int(val) for val in data.split(' ')]
        def helper(start, end):
            if start > end or start >= len(vals):
                return None
            if start == end:
                return TreeNode(vals[start])
            root = TreeNode(vals[start])
            ni = start + 1
            while ni <= end and vals[ni] < vals[start]:
                ni += 1
            root.left = helper(start + 1, ni-1)
            root.right = helper(ni, end)
            return root
        return helper(0, len(vals)-1)

# Alternate solution
# look at the build method. Fancy implementation
class Codec:
    def serialize(self, root):
        vals = []
        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return " ".join(map(str, vals))
    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())
        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node
        return build(float("-infinity"), float("infinity"))
