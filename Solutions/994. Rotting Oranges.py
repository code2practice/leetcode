'''
994. Rotting Oranges
Medium
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
 
Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = deque()
        fresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = -1
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0
        count = 0
        while q:
            for _ in range(len(q)):
                top = q.popleft()
                for d in dirs:
                    new_i, new_j = top[0] + d[0], top[1] + d[1]
                    if (
                        new_i < 0
                        or new_i >= r
                        or new_j < 0
                        or new_j >= c
                        or grid[new_i][new_j] == -1
                        or grid[new_i][new_j] != 1
                    ):
                        continue
                    q.append((new_i, new_j))
                    grid[new_i][new_j] = -1
                    fresh -= 1
            count += 1
        if fresh:
            return -1
        return count - 1
