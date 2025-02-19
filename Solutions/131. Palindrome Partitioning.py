'''
131. Palindrome Partitioning
Medium
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]
'''

class Solution:
    @cache
    def ispal(self,st):
        if not st:
            return True
        return st[0] == st[-1] and self.ispal(st[1:-1])
    def partition(self, st: str) -> List[List[str]]:
        @cache
        def helper(s):
            if not st:
                return [[]]
            ans = []
            for i in range(1, len(st)+1):
                curr = st[:i]
                if self.ispal(curr):
                    rem = self.partition(st[i:])
                    for r in rem:
                        ans.append([curr] + r)
            return ans
        return helper(st)

'''
Time  Complexity: O(N * (2 ^ N))
Space Complexity: O(N * (2 ^ N))
'''
