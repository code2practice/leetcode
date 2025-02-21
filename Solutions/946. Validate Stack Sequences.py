'''
946. Validate Stack Sequences
Medium
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
 
Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 
Constraints:
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
'''

# Using Stack
class Solution:
   def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
       s = []
       popped_index = 0
       for v in pushed:
           s.append(v)
           while s and s[-1] == popped[popped_index]:
               s.pop()
               popped_index += 1
       return not s

# Without using stack
'''
Instead of using a stack we're gonna use pushed as the stack.
Everything is, Same as above, the only difference is rather than using a new stack we can use the pushed ARRAY as a stack, using a pointer i. Initially i = 0, that means stack is empty.
'''
class Solution:
   def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
       popped_index = 0
       pushed_index = -1
       for i, v in enumerate(pushed):
           pushed_index += 1
           pushed[pushed_index] = pushed[i]
           while pushed_index >= 0 and popped[popped_index] == pushed[pushed_index]:
               popped_index += 1
               pushed_index -= 1
       return popped_index == len(popped) and pushed_index == -1
