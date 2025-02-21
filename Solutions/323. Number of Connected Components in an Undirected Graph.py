'''
323. Number of Connected Components in an Undirected Graph
Medium
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
     0          3
     |          |
     1 --- 2    4
Output: 2
Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1
Note:
 You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

def NumberOfconnectedComponents(self):
       # Mark all the vertices as not visited
       visited = [False for i in range(self.V)]
       # To store the number of connected
       # components
       count = 0
       for v in range(self.V):
           if (visited[v] == False):
               self.DFSUtil(v, visited)
               count += 1
       return count
   def DFSUtil(self, v, visited):
       # Mark the current node as visited
       visited[v] = True
       # Recur for all the vertices
       # adjacent to this vertex
       for i in self.adj[v]:
           if (not visited[i]):
               self.DFSUtil(i, visited)
