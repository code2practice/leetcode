'''
364. Nested List Weight Sum II
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.
The weight of an integer is maxDepth - (the depth of the integer) + 1.
Return the sum of each integer in nestedList multiplied by its weight.
 
Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
 
Constraints:
1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
'''

'''
 - 1, two passes
Straightforward solution is 2 passes
1st pass to depth first
then calculate
 - 2, one passes
And moreover, below is another way of solving it via only 1-pass.
Explanation of the Approach
The solution uses an iterative approach to traverse the nested list level by level, starting from the outermost level (level 1) and moving inward. It keeps track of two sums:
unweighted: The cumulative sum of all integers encountered so far, regardless of their depth.
weighted: The weighted sum, which is recalculated at each level to reflect the increasing weight of previously encountered integers as the traversal goes deeper.
Initialization: If the input list is empty, the function immediately returns 0. This check is technically redundant due to Python’s treatment of empty lists as falsy values, which would naturally terminate the loop.


Iterative Traversal: The solution iteratively traverses the nested list. At each iteration, it processes one level of the list.


Accumulating unweighted Sum: For each element a in the current level (nestedList), if a is an integer, its value is added to unweighted. This sum accumulates values from all levels processed so far but does not account for their depth.


Preparing for Next Level: If a is not an integer but another nested list, the elements of this list are added to next_level, preparing them for processing in the next iteration.


Updating weighted Sum: After processing each level, weighted is increased by unweighted. This step is crucial because it effectively adds the unweighted sum repeatedly, once for each level of depth, thereby inversely weighting the depth. Deeper integers have already contributed to unweighted in earlier iterations, so they are counted multiple times in weighted, reflecting their deeper level.


Moving to the Next Level: The list to be processed in the next iteration is updated to next_level, moving the traversal one level deeper into the nested list structure.


Returning the Result: Once all levels have been processed and there are no more elements to traverse, the weighted sum represents the inverse depth sum of the original nested list, and it is returned as the result.


Example
Consider the nested list [[1,1],2,[1,1]]. The inverse depth sum is calculated as follows:
At the outermost level, the sum of integers is 2 (only the integer 2 is at this level). This value is added to weighted. So weighted=2 and unweighted=2
At the next level, the sum of integers is 4 (from the four 1s in the nested lists). This sum is added to unweighted making it 6 (once for this level and once from the previous level’s unweighted sum 2).
The final weighted sum is weighted + unweighted, i.e. 2 + 6 = 8, which is the inverse depth sum of the nested list.
This approach efficiently calculates the inverse depth sum without needing to explicitly track the depth of each integer, leveraging the iterative re-accumulation of unweighted sums to achieve the correct weighting.
'''

class Solution:
   def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
       def max_depth(nestedList):
           depth = 1
           for item in nestedList:
               if item.isInteger():
                   continue
               depth = max(depth, max_depth(item.getList()) + 1)
           return depth
       def dfs(nestedList, max_depth):
           depth_sum = 0
           for item in nestedList:
               if item.isInteger():
                   depth_sum += item.getInteger() * max_depth
               else:
                   depth_sum += dfs(item.getList(), max_depth - 1)
           return depth_sum
       depth = max_depth(nestedList)
       return dfs(nestedList, depth)
############

class Solution_onePass: # iterative
   def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
       if not nestedList:
       # can remove this check, an empty list in Python is considered "falsy"
       # and the loop will exit when it reaches the end of the list
           return 0
       # weighted is like previous round result
       unweighted = weighted = 0
       while nestedList:
           next_level = []
           for a in nestedList:
               if a.isInteger():
                   unweighted += a.getInteger()
               else:
                   next_level.extend(a.getList())
           weighted += unweighted
           nestedList = next_level
       return weighted
