'''
32. Longest Valid Parentheses
Hard
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:
Input: s = ""
Output: 0
 
Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

Solution:

We can use a stack to find the longest valid parentheses.
We keep storing the indices for the invalid parentheses in the string. Every time we find a valid parentheses substring, we compare the 
length of current index - last invalid index to find the longest
Time Complexity : O(N), for iterating over the string s.
Space Complexity : O(N), for maintaining the stack.
'''
class Solution:
   def longestValidParentheses(self, s: str) -> int:
       st = []
       longest = 0
       for i, c in enumerate(s):
           if c == '(':
               st.append(i)
           else:
               if st and s[st[-1]] == '(':
                   st.pop()
                   if st:
                       longest = max(longest, i - st[-1])
                   else:
                       longest = max(longest, i + 1)
               else:
                   st.append(i)
       return longest
