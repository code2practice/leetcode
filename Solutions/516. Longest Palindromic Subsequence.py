'''
516. Longest Palindromic Subsequence
Medium
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
 
Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 
Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

'''
Solution 1: Top down DP
Let dp(l, r) denote the length of the longest palindromic subsequence of s[l..r].
There are 2 options:
If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
Then dp(0, n-1) is our result.

Complexity
Time: O(N^2), where N <= 1000 is length of string s.
Space: O(N^2)
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(l, r):
            if l > r: return 0  # Return 0 since it's empty string
            if l == r: return 1  # Return 1 since it has 1 character
            if s[l] == s[r]:
                return dp(l+1, r-1) + 2
            return max(dp(l, r-1), dp(l+1, r))
        
        return dp(0, n-1)

'''
 Solution 2: Bottom up DP
Let dp[l][r] denote the length of the longest palindromic subsequence of s[l..r].
There are 2 options:
If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
Then dp[0][n-1] is our result.
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
