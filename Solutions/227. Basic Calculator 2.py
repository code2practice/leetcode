'''
227. Basic Calculator II
Medium
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''

class Solution:
   def calculate(self, s):   
       def calc(it):
           def update(op, v):
               if op == "+": stack.append(v)
               if op == "-": stack.append(-v)
               if op == "*": stack.append(stack.pop() * v)
               if op == "/": stack.append(int(stack.pop() / v))
      
           num, stack, sign = 0, [], "+"
          
           while it < len(s):
               if s[it].isdigit():
                   num = num * 10 + int(s[it])
               elif s[it] in "+-*/":
                   update(sign, num)
                   num, sign = 0, s[it]
               elif s[it] == "(":
                   num, j = calc(it + 1)
                   it = j - 1
               elif s[it] == ")":
                   update(sign, num)
                   return sum(stack), it + 1
               it += 1
           update(sign, num)
           return sum(stack)
       return calc(0)
