'''
432. All O`one Data Structure
Hard
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
Implement the AllOne class:
AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
 
Example 1:
Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]
Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 
Constraints:
1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''

# DLL Node definition
class Node(object):
    def __init__(self):
        self.keys = set()
        self.prev = self.next = None

# Doubly Linked List class.
# Note to add sentinel head and tail to avoid adding null checks for append
# and delete operations.
class Dll(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def append(self, node, prev):
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        node.prev = prev
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Implementation of O(1) data structure
class AllOne:
    def __init__(self):
        self.freq_map = {}
        self.key_map = defaultdict(int)
        self.dll = Dll()
    
    def _remove_key_from_node(self, cf, key):
        if cf == 0:
            return
        node = self.freq_map[cf]
        node.keys.remove(key)
        # if this is the only key in this Node, remove node
        if not len(node.keys):
            self.dll.remove(node)
            self.freq_map.pop(cf)
    
    def inc(self, key: str) -> None:
        cf = self.key_map[key]
        nf = cf + 1
        self.key_map[key] = nf
        if nf not in self.freq_map:
            self.freq_map[nf] = Node()
            prev = self.freq_map[cf] if cf > 0 else self.dll.head
            self.dll.append(self.freq_map[nf], prev)
        self.freq_map[nf].keys.add(key)
        self._remove_key_from_node(cf, key)
    
    def dec(self, key: str) -> None:
        self.key_map[key] -= 1
        nf, cf = self.key_map[key], self.key_map[key] + 1
        if nf == 0:
            self.key_map.pop(key)
        else:
            if nf not in self.freq_map:
                self.freq_map[nf] = Node()
                self.dll.append(self.freq_map[nf], self.freq_map[cf].prev)
            self.freq_map[nf].keys.add(key)
        self._remove_key_from_node(cf, key)
    def getMaxKey(self) -> str:
        keys = self.dll.tail.prev.keys
        if keys:
            return next(iter(keys))
        return ""
    def getMinKey(self) -> str:
        keys = self.dll.head.next.keys
        if keys:
            return next(iter(keys))
        return ""
