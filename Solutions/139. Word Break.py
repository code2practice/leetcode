'''139. Word Break
Medium
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
 
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

# Recursion with Memoization(Accepted):
class Solution:
   def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       words = set(wordDict)
       @cache
       def util(st):
           if not st:
               return True
           for i in range(1, len(st) + 1):
               if st[:i] in words:
                   if util(st[i:]):
                       return True
           return False
       return util(s)

# DP(Accepted)
class Solution:
   def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       words = set(wordDict)
       l = len(s)
       d = [False] * (l + 1)
       d[0] = True
       for i in range(len(s) + 1):
           for j in range(i):
               if d[j] and s[j:i] in words:
                   d[i] = True
       return d[l]

