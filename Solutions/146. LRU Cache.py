'''
146. LRU Cache
Medium
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
 
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

class dll:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.kv = {}
        self.c = capacity
        # dummy head and tail to avoid checking multiple
        # null conditions.
        self.head = dll(0, 0)
        self.tail = dll(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self._remove(node)
        self._add(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self._remove(self.kv[key])
        node = dll(key, value)
        self.kv[key] = node
        self._add(node)
        if len(self.kv) > self.c:
            p = self.tail.prev
            self._remove(p)
            self.kv.pop(p.k)
