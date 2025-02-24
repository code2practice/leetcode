'''
1541. Minimum Insertions to Balance a Parentheses String
Medium
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.
 
Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 
Constraints:
1 <= s.length <= 105
s consists of '(' and ')' only.
'''
# Using Stack
class Solution:
    def minInsertions(self, s: str) -> int:
        openNeeded = closeNeeded = 0
        st = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                st.append(i)
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    if st:
                        st.pop()
                    else:
                        openNeeded += 1
                    i += 2
                else:
                    if st:
                        st.pop()
                    else:
                        openNeeded += 1
                    closeNeeded += 1
                    i += 1
        return openNeeded + closeNeeded + len(st) * 2

# Without Stack
class Solution:
    def minInsertions(self, s: str) -> int:
        opencount = 0
        openneeded = closeneeded = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                opencount += 1
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    if opencount > 0:
                        opencount -= 1
                    else:
                        openneeded += 1
                    i += 2
                else:
                    if opencount > 0:
                        opencount -= 1
                        closeneeded += 1
                    else:
                        openneeded += 1
                        closeneeded += 1
                    i += 1
        return openneeded + closeneeded + opencount * 2

  
