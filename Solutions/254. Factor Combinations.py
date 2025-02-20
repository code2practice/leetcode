'''
254. Factor Combinations
Numbers can be regarded as the product of their factors.
For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.
Note that the factors should be in the range [2, n - 1].
 
Example 1:
Input: n = 1
Output: []
Example 2:
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:
Input: n = 37
Output: []
 
Constraints:
1 <= n <= 107
'''

'''
Iterate from 2 to n. If the current number i is divisible by n, it means that i is a factor of n. Store it in a onePath list, and then recursively call n/i.
At next recursion, do not traverse from 2. It traverses from i to n/i, and the condition for stopping is when n is equal to 1, if there is a factor in onePath at this time, store this combination in the result.
Pitfall
Need to avoid case: n=32, and only 32 in this list, add check if (onePath.size() > 1)
'''

class Solution:
   def getFactors(self, n: int) -> List[List[int]]:
       # Helper function to perform depth-first search
       def depth_first_search(target, start_factor):
           # If temp_factors has elements, then add a combination to the answer
           if temp_factors:
               answer.append(temp_factors + [target])
           # Initialize a factor to start from
           factor = start_factor
           # Check for factors only up to the square root of the target
           while factor * factor <= target:
               # If factor is a valid factor of target
               if target % factor == 0:
                   # Append the factor to the temporary list for possible answer
                   temp_factors.append(factor)
                   # Recurse with the reduced number (integer division)
                   depth_first_search(target // factor, factor)
                   # Pop the last factor to backtrack
                   temp_factors.pop()
               # Increment the factor
               factor += 1
       # A list to keep a temporary set of factors for a combination
       temp_factors = []
       # The final list of lists to be returned
       answer = []
       # Initiate depth-first search with the full target and the smallest factor
       depth_first_search(n, 2)
       return answer
