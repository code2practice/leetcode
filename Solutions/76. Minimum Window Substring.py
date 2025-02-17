'''
76. Minimum Window Substring
Hard
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
 
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
   def minWindow(self, s: str, t: str) -> str:
       if t == "":
           return ""
       counter_t = Counter(t)
       left = 0
       length_t = len(t)
       minLength = float("inf")
       start = 0
       for right in range(len(s)):
           if s[right] not in counter_t:
               continue
           if counter_t[s[right]] > 0:
               length_t -= 1
           counter_t[s[right]] -= 1
           while length_t == 0:
               if right - left + 1 < minLength:
                   minLength = right - left + 1
                   start = left
               if s[left] in counter_t:
                   counter_t[s[left]] += 1
                   if counter_t[s[left]] > 0:
                       length_t += 1
               left += 1
       return s[start : start + minLength] if minLength != float("inf") else ""
