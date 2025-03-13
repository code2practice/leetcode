'''
62. Unique Paths
Solved
Medium
Topics
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''

# Using 2D array
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] *n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# Using 1D Array
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] *n
        for i in range(1, m):
            temp = [0] * n
            for j in range(n):
                temp[j] = dp[j] + temp[j-1]
            dp = temp.copy()

        return dp[n-1]

# Code to print the actual path using 'D' and 'R'
def paths(m, n):
    def helper(r, c,m, n):
        if  r > m or c > n:
            return []
        if (r == m and c == n):
            return ['']
        down = helper(r+1, c, m,n)
        right = helper(r, c+1, m, n)
        res = []
        for d in down:
            res.append('D' +d)
        for r in right:
            res.append('R' + r)
        return res
    return helper(0,0, m,n)

p = paths(1,0)
print(len(p))
print(len(set(p)))
print(p)
