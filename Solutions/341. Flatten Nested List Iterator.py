'''
341. Flatten Nested List Iterator
Medium
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
Implement the NestedIterator class:
NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.
 
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 
Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
'''

# Solution where you flatten the entire nested list in the constructor(Inefficient)
def flatten(nested):
   res = []
   for e in nested:
       if e.isInteger():
           res.append(e.getInteger())
       else:
           res.extend(flatten(e.getList()))
   return res
class NestedIterator:
   def __init__(self, nestedList: [NestedInteger]):
       self.nums = flatten(nestedList)
       self.index = 0
   def next(self) -> int:
       if self.hasNext():
           self.index += 1
           return self.nums[self.index -1]
  
   def hasNext(self) -> bool:
        return self.index < len(self.nums)

# Solution where you keep flatenning the list when needed(when next is called)
# More efficient solution
class NestedIterator(object):
   def __init__(self, nestedList):
       # Stores the list in reverse order
       self.stack = nestedList[::-1]
      
   def next(self):
       return self.stack.pop().getInteger()
      
   def hasNext(self):
       while self.stack:
           top = self.stack[-1]
           if top.isInteger():
               return True
           self.stack = self.stack[:-1] + top.getList()[::-1]
       return False
