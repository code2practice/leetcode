'''
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s.
 
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s):
        res = ""
        maxLength = 0
        for i in range(len(s)):
            # odd case, like "aba"
            tmp, length = self.helper(s, i, i)
            if length > maxLength:
                res = tmp
                maxLength = length
            # even case, like "abba"
            tmp, length = self.helper(s, i, i + 1)
            if length > maxLength:
                res = tmp
                maxLength = length
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (s[l + 1 : r], r - l)
