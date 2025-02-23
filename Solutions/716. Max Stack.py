'''
716. Max Stack
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
Implement the MaxStack class:
MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.
 
Example 1:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]
Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
 
Constraints:
-107 <= x <= 107
At most 105 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
'''

'''
Solutions
A stack supports push, pop, and top already, so only the last two operations need to be implemented. Use two stacks.
One stack works as the normal stack,
and the other stack which is called the maximum stack stores the maximum element so far.
Both stacks are initialized in the constructor. The other three functions should be modified as well.
The push() function. Push the element into the normal stack, and for the maximum stack, if the maximum stack is empty, then simply push the element into the maximum stack, otherwise push the maximum element between the current element and the element at the top of the maximum stack.


The pop() function. Simply pop both the normal stack and the maximum stack, and return the element popped from the normal stack.


The top() function. Simply return the top element of the normal stack.


The peekMax() function. Simply return the top element of the maximum stack. The reason why this works is that, each time the push function is called, the element pushed into the maximum stack is guaranteed to be the maximum element so far, so at any time, the top element of the maximum stack is the maximum element among all the elements pushed.


The popMax() function. This is a highly complex function that requires careful handling. Since the maximum element may not always be at the top of the normal stack, it may be necessary to first pop some elements from the normal stack in order to locate it. The top element of the normal stack is considered the maximum only if it is identical to the top element of the maximum stack. Once the maximum element has been popped, any other elements that were previously removed from the normal stack must be re-added. To accomplish this, a new stack is used to store all the popped elements until the maximum element is identified. Once the maximum element has been popped and retrieved, each element in the new stack must be pushed back onto the normal stack, to ensure that both the normal stack and the maximum stack contain the correct values.
'''

class MaxStack(object):
   def __init__(self):
       """
       initialize your data structure here.
       """
       self.stack = []
       self.max_stack = []
   def push(self, x):
       """
       :type x: int
       :rtype: void
       """
       self.stack.append(x)
       self.max_stack.append(max(x, self.max_stack[-1]) if self.max_stack else x)
   def pop(self):
       """
       :rtype: int
       """
       if len(self.stack) != 0:
           self.max_stack.pop(-1)
           return self.stack.pop(-1)
   def top(self):
       """
       :rtype: int
       """
       return self.stack[-1] if self.stack else None
   def peekMax(self):
       """
       :rtype: int
       """
       if len(self.max_stack) != 0:
           return self.max_stack[-1]
   def popMax(self):
       """
       :rtype: int
       """
       val = self.peekMax()
       buff = []
       while self.top() != val:
           # re-use pop(), ops on both max_stack and stack
           buff.append(self.pop())
       self.pop()
       while len(buff) != 0:
           # re-use push(), no need to save buffer for max-stack
           self.push(buff.pop(-1))
       return val

# Better Solution using DLL and sortdlist
from sortedcontainers import SortedList
from typing import Optional
class Node:
    def __init__(self, val: int = 0):
       self.val = val  # Value of the node
       self.prev: Optional["Node"] = None  # Link to the previous node
       self.next: Optional["Node"] = None  # Link to the next node
class DoubleLinkedList:
    def __init__(self):
       self.head = Node()  # Sentinel head node of the double linked list
       self.tail = Node()  # Sentinel tail node of the double linked list
       self.head.next = self.tail  # Connect head to tail
       self.tail.prev = self.head  # Connect tail to head
    def append(self, val: int) -> Node:
       """
       Append a new node with value val at the end of the list
       """
       # Create new node
       node = Node(val)
       # Link it with the last element
       node.next = self.tail
       node.prev = self.tail.prev
       # Link the last element with the new node
       self.tail.prev.next = node
       self.tail.prev = node
       return node
    @staticmethod
    def remove_node(node: Node) -> None:
       """
       Remove a node from the list
       """
       # Re-link the previous and next nodes to each other
       node.prev.next = node.next
       node.next.prev = node.prev
    def pop(self) -> Node:
       """
       Pop the last element from the list
       """
       # Use the remove_node static method to remove the last element
       return self.remove_node(self.tail.prev)
    def peek(self) -> int:
       """
       Peek the last element's value from the list
       :return: Value of last node
       """
       return self.tail.prev.val
class MaxStack:
    def __init__(self):
       self.stack = DoubleLinkedList()  # The main stack as a double linked list
       self.sorted_nodes = SortedList(
           key=lambda x: x.val
       )  # Sorted keys to track max values efficiently
    def push(self, x: int) -> None:
       """
       Push an element onto the stack
       :param x: Value to push onto the stack
       :return: None
       """
       # Append value to stack and add the node to sorted list for max retrieval
       node = self.stack.append(x)
       self.sorted_nodes.add(node)
    def pop(self) -> int:
       """
       Pop the top element from the stack
       :return: Value of removed element
       """
       # Pop from stack and remove corresponding node from sorted list
       node = self.stack.pop()
       self.sorted_nodes.remove(node)
       return node.val
    def top(self) -> int:
       """
       Get the top element of the stack
       :return: Value of top element
       """
       return self.stack.peek()
    def peekMax(self) -> int:
       """
       Retrieve the maximum value in the stack
       :return: Maximum value
       """
       # Last element of sorted_nodes has the max value
       return self.sorted_nodes[-1].val
    def popMax(self) -> int:
       """
       Pop the maximum value from the stack
       :return: Maximum value that was removed
       """
       # Remove last element from sorted list to get max value
       node = self.sorted_nodes.pop()
       # Use the remove_node static method to detach the node from the stack
       DoubleLinkedList.remove_node(node)
       return node.val
