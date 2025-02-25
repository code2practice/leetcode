'''
261. Graph Valid Tree
Medium
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
'''

# BFS
from collections import deque, defaultdict
class Solution:
    def validTree(self, n, edges):
        graph = defaultdict(set)
        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].add(end)
            graph[end].add(start)
        visited = [False] * n
        q = deque([0])
        while q:
            top = q.popleft()
            if visited[top]:
                return False
            visited[top] = True
            for n in graph[top]:
                q.append(n)
                graph[n].remove(top)
        return all(visited)

# DFS
class Solution:
    def validTree(self, n, edges):
        def dfs(root, graph, visited, parent):
         visited[root] = 1
         for nbr in graph.get(root, []):
           if nbr == parent:
             continue
           elif visited[nbr] != 0:
             return False
           if not dfs(nbr, graph, visited, root):
             return False
         visited[root] = 2
         self.nodeVisited += 1
         return True
    visited = [0 for _ in range(n)]
    graph = {}
    self.nodeVisited = 0
    for edge in edges:
        start, end = edge[0], edge[1]
        graph[start] = graph.get(start, []) + [end]
        graph[end] = graph.get(end, []) + [start]
    if dfs(0, graph, visited, -1) and self.nodeVisited == n:
        return True
    else:
        return False

# Union Find
class Solution:
    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
       # Helper function to find the root of a node 'x'.
       # Uses path compression to flatten the structure for faster future lookups.
       def find_root(node):
           if parent[node] != node:
               parent[node] = find_root(parent[node])  # Path compression
           return parent[node]
    
       # Initialize the parent list where each node is initially its own parent.
       parent = list(range(num_nodes))
    
       # Iterate over all the edges in the graph.
       for node_1, node_2 in edges:
           # Find the root of the two nodes.
           root_1 = find_root(node_1)
           root_2 = find_root(node_2)
        
           # If the roots are the same, it means we encountered a cycle.
           if root_1 == root_2:
               return False
        
           # Union the sets - attach the root of one component to the other.
           parent[root_1] = root_2
        
           # Each time we connect two components, reduce the total number of components by one.
           num_nodes -= 1
    
       # A tree should have exactly one more node than it has edges.
       # After union operations, we should have exactly one component left.
       return num_nodes == 1
