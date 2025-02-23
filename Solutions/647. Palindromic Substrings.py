'''
647. Palindromic Substrings
Medium
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
 
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Note: count is not inittialzed to 0 but to length of string
        # to account for single character palindromes.
        count = len(s)
        def util(s, i):
            c = 0
            start = i-1
            end = i +1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                c += 1
                start -=1
                end += 1
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                c += 1
                start -=1
                end += 1
            return c
        for i in range(len(s)):
            count += util(s, i)
        return count
