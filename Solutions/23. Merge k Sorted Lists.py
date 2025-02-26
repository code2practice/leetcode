'''
23. Merge k Sorted Lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:
Input: lists = []
Output: []
Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

'''
For those who curious about why Divide-Conquer method has TC : O(Nlog(N))

Splitting list into two, log(N) times = O(log(N))
Merging split lists into one in ascending order, need to traverse every element = O(N)
In Summary, we merging it log(N) times and in each merging we should traverse N element.
Therefore the Time Complexity is O(Nlog(N)) where n is the number of element.

In this case, the element is a linked list, so I think Time Complexity is O(Mlog(N))
N : number of linked lists
M : number of element of merged linked list
'''
# Using Merge Sort
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge2list(l1.next, l2)
                return l1
            else:
                l2.next = merge2list(l1, l2.next)
                return l2

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l = len(lists) // 2
        first = self.mergeKLists(lists[:l])
        second = self.mergeKLists(lists[l:])
        return merge2list(first, second)

# Using Priority Queue
import queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        curr = res = ListNode(0)
        q = queue.PriorityQueue()
        for index, l in enumerate(lists):
            if not l:
                continue
            q.put((l.val, index, l))
        while q.qsize():
            v, index, node = q.get()
            curr.next = node
            curr = curr.next
            if node.next:
                q.put((node.next.val, index, node.next))
        return res.next
'''
Time complexity:
Heap Operations: Each insertion and extraction from the heap takes O(logk), where k is the number of lists.
Total Nodes Processed: Across all lists, there are N nodes in total.
Overall Complexity: Since each node is pushed and popped once, the total time complexity is O(Nlogk).
Space complexity:
The heap stores at most k elements at any time, giving O(k) space for the heap.
Other auxiliary space used is O(1) (excluding the output list).
Total Space Complexity: O(k).
'''
