'''
678. Valid Parenthesis String
Medium
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "(*)"
Output: true
Example 3:
Input: s = "(*))"
Output: true
'''

# O(n) time and O(n) space
class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                open.append(i)
            elif c == '*':
                star.append(i)
            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open:
            if not star:
                return False
            if open.pop() > star.pop():
                return False
        return True

# O(n) time and O(1) space
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmax = 0
        cmin = 0
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1
                cmin -= 1
            if cmax < 0:
                return False
            # cmin cannot be negative, if it goes negative, we can
            # consider the * to be empty string instead of )
            cmin = max(cmin, 0)
        return cmin == 0
