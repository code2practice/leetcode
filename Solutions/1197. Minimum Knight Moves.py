'''
1197. Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.
 
Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
Constraints:
-300 <= x, y <= 300
0 <= |x| + |y| <= 300
'''

'''
Solution 1: BFS
This problem can be solved using the BFS shortest path model. The search space for this problem is not large, so we can directly use the naive BFS. The solution below also provides the code for bidirectional BFS for reference.
Bidirectional BFS is a common optimization method for BFS. The main implementation ideas are as follows:
Create two queues, q1 and q2, for “start -> end” and “end -> start” search directions, respectively.
Create two hash maps, m1 and m2, to record the visited nodes and their corresponding expansion times (steps).
During each search, prioritize the queue with fewer elements for search expansion. If a node visited from the other direction is found during the expansion, it means the shortest path has been found.
If one of the queues is empty, it means that the search in the current direction cannot continue, indicating that the start and end points are not connected, and there is no need to continue the search.
'''

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
       q = deque([(0, 0)])
       ans = 0
       vis = {(0, 0)}
       dirs = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
       while q:
           for _ in range(len(q)):
               i, j = q.popleft()
               if (i, j) == (x, y):
                   return ans
               for a, b in dirs:
                   c, d = i + a, j + b
                   if (c, d) not in vis:
                       vis.add((c, d))
                       q.append((c, d))
           ans += 1
       return -1
