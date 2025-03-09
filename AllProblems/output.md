# [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii)

[Meta Variants](https://github.com/CodingWithMinmer/CodingWithMinmer/tree/main/1004_max_consecutive_ones_3)
## Description

<!-- description:start -->

<p>Given a binary array <code>nums</code> and an integer <code>k</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array if you can flip at most</em> <code>k</code> <code>0</code>&#39;s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> [1,1,1,0,0,<u><strong>1</strong>,1,1,1,1,<strong>1</strong></u>]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> [0,0,<u>1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1</u>,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        m = 0
        for right in range(len(nums)):
            count += nums[right]
            if right - left + 1 - count <= k:
                m = max(m, right - left + 1)
            else:
                while right - left + 1 - count > k:
                    count -= nums[left]
                    left += 1
        return m
```
```
1017. Convert to Base -2
Medium
Given an integer n, return a binary string representing its representation in base -2.
Note that the returned string should not have leading zeros unless the string is "0".
 
Example 1:
Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:
Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:
Input: n = 4
Output: "100"
Explantion: (-2)2 = 4
 
Constraints:
0 <= n <= 109
```

```python
class Solution:
   def baseNeg2(self, N: int) -> str:
       ans = ""
       while N != 0:
           N, r = divmod(N, -2)
           if r < 0:
               N, r = N + 1, 1
           ans = str(r) + ans
       return max(ans, "0")
```

# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/images/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

```python
# Iterative
class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = []
       if not root:
           return res
       q = deque([root])
       while q:
           s = len(q)
           temp = []
           while s:
               t = q.popleft()
               temp.append(t.val)
               if t.left:
                   q.append(t.left)
               if t.right:
                   q.append(t.right)
               s -= 1
           res.append(temp)
       return res
```

```python
# Recursive
class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = defaultdict(list)
       def util(root, depth):
           if not root:return
           res[depth].append(root.val)
           util(root.left, depth + 1)
           util(root.right, depth + 1)
       util(root, 0)
       return res.values()
```
# [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling)


## Description

<!-- description:start -->

<p>A company is planning to interview <code>2n</code> people. Given the array <code>costs</code> where <code>costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]</code>,&nbsp;the cost of flying the <code>i<sup>th</sup></code> person to city <code>a</code> is <code>aCost<sub>i</sub></code>, and the cost of flying the <code>i<sup>th</sup></code> person to city <code>b</code> is <code>bCost<sub>i</sub></code>.</p>

<p>Return <em>the minimum cost to fly every person to a city</em> such that exactly <code>n</code> people arrive in each city.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> costs = [[10,20],[30,200],[400,50],[30,20]]
<strong>Output:</strong> 110
<strong>Explanation: </strong>
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
<strong>Output:</strong> 1859
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
<strong>Output:</strong> 3086
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 * n == costs.length</code></li>
	<li><code>2 &lt;= costs.length &lt;= 100</code></li>
	<li><code>costs.length</code> is even.</li>
	<li><code>1 &lt;= aCost<sub>i</sub>, bCost<sub>i</sub> &lt;= 1000</code></li>
</ul>

### Solution
The problem is to send n persons to city A 
and n persons to city B with minimum cost.

The idea is to send each person to city A.
costs = [[10,20],[30,200],[400,50],[30,20]]

So, totalCost = 10 + 30 + 400 + 30 = 470

Now, we need to send n persons to city B.
Which persons do we need to send city B?

Here, we need to minimize the cost.
We have already paid money to go to city A.
So, Send the persons to city B who get more refund
so that our cost will be minimized.

So, maintain refunds of each person
refund[i] = cost[i][1] - cost[i][0]

So, refunds of each person
    refund = [10, 170, -350, -10]

Here, refund +ve means we need to pay
             -ve means we will get refund.

So, sort the refund array.

refund = [-350, -10, 10, 170]

Now, get refund for N persons,
totalCost += 470 + -350 + -10 = 110

So, minimum cost is 110


IF YOU HAVE ANY DOUBTS, FEEL FREE TO ASK.
IF YOU UNDERSTAND, DON'T FORGET TO UPVOTE.

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        cost = 0
        for i in range(len(costs) // 2):
            cost += costs[i][1]
        for i in range(len(costs) // 2, len(costs)):
            cost += costs[i][0]
        return cost
```
## 103. Binary Tree Zigzag Level Order Traversal

### Question:
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

```
For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
```

### Iterative
```python
class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       if not root:
           return []
       count = 0
       q = deque([root])
       res = []
       while q:
           count += 1
           temp = []
           for _ in range(len(q)):
               top = q.popleft()
               temp.append(top.val)
               if top.left:
                   q.append(top.left)
               if top.right:
                   q.append(top.right)
           if count %2 == 1:
               res.append(temp)
           else:
               res.append(temp[::-1])
       return res
```
### Recursive
```python
class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       res = defaultdict(deque)
       def util(root, depth):
           if not root:return
           if depth %2 == 1:
               res[depth].appendleft(root.val)
           else:
               res[depth].append(root.val)
           util(root.left, depth + 1)
           util(root.right, depth + 1)
       util(root, 0)
       return res.values()
```
```
1041. Robot Bounded In Circle
Medium
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:
"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
 
Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.
Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.
 
Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
```

```python
class Solution(object):
   def isRobotBounded(self, instructions):
       dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
       x, y = 0, 0
       i = 0
       for instruction in instructions:
           if instruction == "G":
               x, y = x + dirs[i][0], y + dirs[i][1]
           elif instruction == "L":
               i = (i + 1) % 4
           else:
               i = (i + 3) % 4
       return (x == 0 and y == 0) or i != 0
```
# [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain)


## Description

<!-- description:start -->

<p>You are given an array of <code>words</code> where each word consists of lowercase English letters.</p>

<p><code>word<sub>A</sub></code> is a <strong>predecessor</strong> of <code>word<sub>B</sub></code> if and only if we can insert <strong>exactly one</strong> letter anywhere in <code>word<sub>A</sub></code> <strong>without changing the order of the other characters</strong> to make it equal to <code>word<sub>B</sub></code>.</p>

<ul>
	<li>For example, <code>&quot;abc&quot;</code> is a <strong>predecessor</strong> of <code>&quot;ab<u>a</u>c&quot;</code>, while <code>&quot;cba&quot;</code> is not a <strong>predecessor</strong> of <code>&quot;bcad&quot;</code>.</li>
</ul>

<p>A <strong>word chain</strong><em> </em>is a sequence of words <code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code> with <code>k &gt;= 1</code>, where <code>word<sub>1</sub></code> is a <strong>predecessor</strong> of <code>word<sub>2</sub></code>, <code>word<sub>2</sub></code> is a <strong>predecessor</strong> of <code>word<sub>3</sub></code>, and so on. A single word is trivially a <strong>word chain</strong> with <code>k == 1</code>.</p>

<p>Return <em>the <strong>length</strong> of the <strong>longest possible word chain</strong> with words chosen from the given list of </em><code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]
<strong>Output:</strong> 4
<strong>Explanation</strong>: One of the longest word chains is [&quot;a&quot;,&quot;<u>b</u>a&quot;,&quot;b<u>d</u>a&quot;,&quot;bd<u>c</u>a&quot;].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;xbc&quot;,&quot;pcxbcf&quot;,&quot;xb&quot;,&quot;cxbc&quot;,&quot;pcxbc&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> All the words can be put in a word chain [&quot;xb&quot;, &quot;xb<u>c</u>&quot;, &quot;<u>c</u>xbc&quot;, &quot;<u>p</u>cxbc&quot;, &quot;pcxbc<u>f</u>&quot;].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abcd&quot;,&quot;dbqca&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The trivial word chain [&quot;abcd&quot;] is one of the longest word chains.
[&quot;abcd&quot;,&quot;dbqca&quot;] is not a valid word chain because the ordering of the letters is changed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of lowercase English letters.</li>
</ul>

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    res = max(res, dp[word])

        return res
```
# [1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors)


## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>, the number of nodes in a directed graph where the nodes are labeled from <code>0</code> to <code>n - 1</code>. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.</p>

<p>You are given two arrays <code>redEdges</code> and <code>blueEdges</code> where:</p>

<ul>
	<li><code>redEdges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is a directed red edge from node <code>a<sub>i</sub></code> to node <code>b<sub>i</sub></code> in the graph, and</li>
	<li><code>blueEdges[j] = [u<sub>j</sub>, v<sub>j</sub>]</code> indicates that there is a directed blue edge from node <code>u<sub>j</sub></code> to node <code>v<sub>j</sub></code> in the graph.</li>
</ul>

<p>Return an array <code>answer</code> of length <code>n</code>, where each <code>answer[x]</code> is the length of the shortest path from node <code>0</code> to node <code>x</code> such that the edge colors alternate along the path, or <code>-1</code> if such a path does not exist.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
<strong>Output:</strong> [0,1,-1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
<strong>Output:</strong> [0,1,-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= redEdges.length,&nbsp;blueEdges.length &lt;= 400</code></li>
	<li><code>redEdges[i].length == blueEdges[j].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub>, u<sub>j</sub>, v<sub>j</sub> &lt; n</code></li>
</ul>

```python
from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(
        self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(lambda: defaultdict(set))
        red, blue = 0, 1
        for st, end in red_edges:
            graph[st][red].add(end)
        for st, end in blue_edges:
            graph[st][blue].add(end)
        res = [math.inf] * n
        q = deque([(0, red), (0, blue)])
        level = 0
        while q:
            for i in range(len(q)):
                node, color = q.popleft()
                opp_color = not color
                res[node] = min(level, res[node])
                for child in list(graph[node][opp_color]):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
            level += 1
        return [r if r != math.inf else -1 for r in res]
```
## 116. Populating Next Right Pointers in Each Node

### Question:
Given a binary tree

```C
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Note:
* You may only use constant extra space.
* Recursive approach is fine, implicit stack space does not count as extra space for this problem.
* You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

```
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```


### Using BFS
```python
class Solution:
   def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       if not root:
           return
       q = deque([root])
       while q:
           s = len(q)
           for i in range(s):
               top = q.popleft()
               if i < s -1:
                   top.next = q[0]
               if top.left:
                   q.append(top.left)
               if top.right:
                   q.append(top.right)
       return root
```
### using Recursion
```python
class Solution:
   def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       if not root:
           return
       if root.left:
           root.left.next = root.right
       if root.right:
           root.right.next = root.next.left if root.next else None
       self.connect(root.left)
       self.connect(root.right)
       return root
```

### (Important)BFS - Space-Optimized Approach O(1) space
We first populate the next pointers of child nodes of current level. This makes it possible to traverse the next level without using a queue. 
To populate next pointers of child, the exact same logic as above is used
We simply traverse to root's left child and repeat the process - traverse current level, fill next pointers of child 
nodes and then again update root = root -> left. So, we are basically performing standard BFS traversal in O(1) space by 
using next pointers to our advantage
The process continues till we reach the last level of tree

```python
class Solution:
   def connect(self, root):
       head = root
       while root:
           cur, root = root, root.left
           while cur:
               if cur.left:
                   cur.left.next = cur.right
                   if cur.next: cur.right.next = cur.next.left
               else: break
               cur = cur.next 
       return head
```
# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman)

[中文文档](/solution/0000-0099/0012.Integer%20to%20Roman/README.md)

## Description

<!-- description:start -->

<p>Seven different symbols represent Roman numerals with the following values:</p>

<table>
	<thead>
		<tr>
			<th>Symbol</th>
			<th>Value</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>I</td>
			<td>1</td>
		</tr>
		<tr>
			<td>V</td>
			<td>5</td>
		</tr>
		<tr>
			<td>X</td>
			<td>10</td>
		</tr>
		<tr>
			<td>L</td>
			<td>50</td>
		</tr>
		<tr>
			<td>C</td>
			<td>100</td>
		</tr>
		<tr>
			<td>D</td>
			<td>500</td>
		</tr>
		<tr>
			<td>M</td>
			<td>1000</td>
		</tr>
	</tbody>
</table>

<p>Roman numerals are formed by appending&nbsp;the conversions of&nbsp;decimal place values&nbsp;from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:</p>

<ul>
	<li>If the value does not start with 4 or&nbsp;9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.</li>
	<li>If the value starts with 4 or 9 use the&nbsp;<strong>subtractive form</strong>&nbsp;representing&nbsp;one symbol subtracted from the following symbol, for example,&nbsp;4 is 1 (<code>I</code>) less than 5 (<code>V</code>): <code>IV</code>&nbsp;and 9 is 1 (<code>I</code>) less than 10 (<code>X</code>): <code>IX</code>.&nbsp;Only the following subtractive forms are used: 4 (<code>IV</code>), 9 (<code>IX</code>),&nbsp;40 (<code>XL</code>), 90 (<code>XC</code>), 400 (<code>CD</code>) and 900 (<code>CM</code>).</li>
	<li>Only powers of 10 (<code>I</code>, <code>X</code>, <code>C</code>, <code>M</code>) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5&nbsp;(<code>V</code>), 50 (<code>L</code>), or 500 (<code>D</code>) multiple times. If you need to append a symbol&nbsp;4 times&nbsp;use the <strong>subtractive form</strong>.</li>
</ul>

<p>Given an integer, convert it to a Roman numeral.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 3749</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;MMMDCCXLIX&quot;</span></p>

<p><strong>Explanation:</strong></p>

<pre>
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 58</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;LVIII&quot;</span></p>

<p><strong>Explanation:</strong></p>

<pre>
50 = L
 8 = VIII
</pre>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 1994</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;MCMXCIV&quot;</span></p>

<p><strong>Explanation:</strong></p>

<pre>
1000 = M
 900 = CM
  90 = XC
   4 = IV
</pre>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>

```python
class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        res = ""
        for i, v in enumerate(values):
            res += (num // v) * numerals[i]
            num %= v
        return res
```
# [127. Word Ladder](https://leetcode.com/problems/word-ladder)


## Description

<!-- description:start -->

<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -&gt; s<sub>1</sub> -&gt; s<sub>2</sub> -&gt; ... -&gt; s<sub>k</sub></code> such that:</p>

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every <code>s<sub>i</sub></code> for <code>1 &lt;= i &lt;= k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
	<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>the <strong>number of words</strong> in the <strong>shortest transformation sequence</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or </em><code>0</code><em> if no such sequence exists.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> One shortest transformation sequence is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; cog&quot;, which is 5 words long.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The endWord &quot;cog&quot; is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 10</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord != endWord</code></li>
	<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
</ul>

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def areWordsAdjacent(word1, word2):
            if len(word1) != len(word2):
                return False
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if count == 1:
                        return False
                    count += 1
            return True

        adj = defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if areWordsAdjacent(wordList[i], wordList[j]):
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])
        q = deque([beginWord])
        visited = set()
        count = 0
        while q:
            s = len(q)
            count += 1
            while s > 0:
                top = q.popleft()
                if top == endWord:
                    return count
                visited.add(top)
                for n in adj[top]:
                    if n not in visited:
                        q.append(n)
                s -= 1
        return 0
```

### Code to print the ladder
```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def areWordsAdjacent(word1, word2):
            if len(word1) != len(word2):
                return False
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if count == 1:
                        return False
                    count += 1
            return True

        adj = defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if areWordsAdjacent(wordList[i], wordList[j]):
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])
        q = deque([(beginWord, [beginWord])])
        visited = set()
        count = 0
        while q:
            s = len(q)
            count += 1
            while s > 0:
                top, path = q.popleft()
                if top == endWord:
                    print(path)
                    return count
                visited.add(top)
                for n in adj[top]:
                    if n not in visited:
                        q.append((n, path + [n]))
                s -= 1
        return 0
```
# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)


## Description

<!-- description:start -->

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
### With Map

```python
class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
       d = defaultdict(int)
       m = 0
       for n in nums:
           if d[n] != 0:
               continue
           left = d[n-1]
           right = d[n+1]
           res = left + right + 1
           d[n] = res
           m = max(m, res)
           d[n - left] = res
           d[n + right]= res
       return m
```
### With Set
``` python     
class Solution:
   def longestConsecutive(self, nums):
   nums = set(nums)
   best = 0
   for x in nums:  #We are iterating over the set instead of original list
       if x - 1 not in nums: # Elements in set is always sorted
           y = x + 1
           while y in nums:
               y += 1
           best = max(best, y - x)
   return best 
```
# [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers)


## Description

<!-- description:start -->

<p>You are given the <code>root</code> of a binary tree containing digits from <code>0</code> to <code>9</code> only.</p>

<p>Each root-to-leaf path in the tree represents a number.</p>

<ul>
	<li>For example, the root-to-leaf path <code>1 -&gt; 2 -&gt; 3</code> represents the number <code>123</code>.</li>
</ul>

<p>Return <em>the total sum of all root-to-leaf numbers</em>. Test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>A <strong>leaf</strong> node is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0129.Sum%20Root%20to%20Leaf%20Numbers/images/num1tree.jpg" style="width: 212px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 25
<strong>Explanation:</strong>
The root-to-leaf path <code>1-&gt;2</code> represents the number <code>12</code>.
The root-to-leaf path <code>1-&gt;3</code> represents the number <code>13</code>.
Therefore, sum = 12 + 13 = <code>25</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0129.Sum%20Root%20to%20Leaf%20Numbers/images/num2tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,9,0,5,1]
<strong>Output:</strong> 1026
<strong>Explanation:</strong>
The root-to-leaf path <code>4-&gt;9-&gt;5</code> represents the number 495.
The root-to-leaf path <code>4-&gt;9-&gt;1</code> represents the number 491.
The root-to-leaf path <code>4-&gt;0</code> represents the number 40.
Therefore, sum = 495 + 491 + 40 = <code>1026</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>The depth of the tree will not exceed <code>10</code>.</li>
</ul>

```python
class Solution:
   def sumNumbers(self, root: Optional[TreeNode]) -> int:
       s = [0]
       def util(root, n, s):
           if not root:
               return
           curr = n * 10 + root.val
           if not (root.left or root.right):
               s[0] += curr
           util(root.left, curr, s)
           util(root.right, curr,s)
       util(root, 0, s)
       return s[0]
```
# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


```python
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
```
Time  Complexity: O(N * (2 ^ N))  
Space Complexity: O(N * (2 ^ N))
```
1312. Minimum Insertion Steps to Make a String Palindrome
Hard
Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.
 
Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
```

### Approach
```
Reverse the input string to get a new string reversed_s.
Initialize a 2D array dp of size (n+1)x(n+1) with 0s, where n is the length of the input string s.
Iterate through all pairs of indices (i,j) of the array dp, where 1<=i,j<=n.
If the characters at indices i-1 in string s and j-1 in reversed_s are equal, set dp[i][j] = dp[i-1][j-1] + 1.
Otherwise, set dp[i][j] to the maximum of dp[i-1][j] and dp[i][j-1].
The length of the LCS between s and reversed_s is dp[n][n].
The minimum number of insertions required to make s a palindrome is n - dp[n][n]
Complexity
Time complexity:
O(n^2), where n is the length of the input string s. This is because we are filling up a 2D array of size (n+1)x(n+1) using dynamic programming approach.
Space complexity:
O(n^2), where n is the length of the input string s. This is because we are using a 2D array of size (n+1)x(n+1) to store the LCS of substrings.
```

```python
class Solution(object):
   def minInsertions(self, s):
       # reverse the input string
       reversed_s = s[::-1]
       # get the length of the input string
       n = len(s)
       # create a 2D array to store the LCS of substrings
       dp = [[0 for j in range(n+1)] for i in range(n+1)]
      
       # fill up the dp array using dynamic programming approach
       for i in range(1, n+1):
           for j in range(1, n+1):
               if s[i-1] == reversed_s[j-1]:
                   # if characters match, add 1 to LCS
                   dp[i][j] = dp[i-1][j-1] + 1
               else:
                   # otherwise, take maximum LCS of two substrings
                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
       # return the minimum number of insertions required to make s a palindrome
       # this is the difference between the length of s and the length of its LCS
       return n - dp[n][n]
```
# [133. Clone Graph](https://leetcode.com/problems/clone-graph)

[中文文档](/solution/0100-0199/0133.Clone%20Graph/README.md)

## Description

<!-- description:start -->

<p>Given a reference of a node in a <strong><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a></strong> undirected graph.</p>

<p>Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> (clone) of the graph.</p>

<p>Each node in the graph contains a value (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>

<pre>
class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}
</pre>

<p>&nbsp;</p>

<p><strong>Test case format:</strong></p>

<p>For simplicity, each node&#39;s value is the same as the node&#39;s index (1-indexed). For example, the first node with <code>val == 1</code>, the second node with <code>val == 2</code>, and so on. The graph is represented in the test case using an adjacency list.</p>

<p><b>An adjacency list</b> is a collection of unordered <b>lists</b> used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.</p>

<p>The given node will always be the first node with <code>val = 1</code>. You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0133.Clone%20Graph/images/133_clone_graph_question.png" style="width: 454px; height: 500px;" />
<pre>
<strong>Input:</strong> adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>Output:</strong> [[2,4],[1,3],[2,4],[1,3]]
<strong>Explanation:</strong> There are 4 nodes in the graph.
1st node (val = 1)&#39;s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)&#39;s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)&#39;s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)&#39;s neighbors are 1st node (val = 1) and 3rd node (val = 3).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0133.Clone%20Graph/images/graph.png" style="width: 163px; height: 148px;" />
<pre>
<strong>Input:</strong> adjList = [[]]
<strong>Output:</strong> [[]]
<strong>Explanation:</strong> Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> adjList = []
<strong>Output:</strong> []
<strong>Explanation:</strong> This an empty graph, it does not have any nodes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the graph is in the range <code>[0, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
	<li><code>Node.val</code> is unique for each node.</li>
	<li>There are no repeated edges and no self-loops in the graph.</li>
	<li>The Graph is connected and all nodes can be visited starting from the given node.</li>
</ul>

### BFS
```python
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       if not node:
           return node
       q = deque([node])
       clones = {node.val: Node(node.val)}
       while q:
           top = q.popleft()
           for n in top.neighbors:
               if n.val not in clones:
                   clones[n.val] = Node(n.val)
                   q.append(n)
               clones[top.val].neighbors.append(clones[n.val])          
       return clones[node.val]
```


### DFS
```python
from typing import Optional
class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       def dfs(node, m):
           if not node:
               return
           if node.val in m:
               return m[node.val]
           new_node = Node(node.val)
           m[node.val] = new_node
           for n in node.neighbors:
               new_node.neighbors.append(dfs(n, m))
           return new_node
       return dfs(node, {})
```

# [1368. Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid)


## Description

<!-- description:start -->

<p>Given an <code>m x n</code> grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of <code>grid[i][j]</code> can be:</p>

<ul>
	<li><code>1</code> which means go to the cell to the right. (i.e go from <code>grid[i][j]</code> to <code>grid[i][j + 1]</code>)</li>
	<li><code>2</code> which means go to the cell to the left. (i.e go from <code>grid[i][j]</code> to <code>grid[i][j - 1]</code>)</li>
	<li><code>3</code> which means go to the lower cell. (i.e go from <code>grid[i][j]</code> to <code>grid[i + 1][j]</code>)</li>
	<li><code>4</code> which means go to the upper cell. (i.e go from <code>grid[i][j]</code> to <code>grid[i - 1][j]</code>)</li>
</ul>

<p>Notice that there could be some signs on the cells of the grid that point outside the grid.</p>

<p>You will initially start at the upper left cell <code>(0, 0)</code>. A valid path in the grid is a path that starts from the upper left cell <code>(0, 0)</code> and ends at the bottom-right cell <code>(m - 1, n - 1)</code> following the signs on the grid. The valid path does not have to be the shortest.</p>

<p>You can modify the sign on a cell with <code>cost = 1</code>. You can modify the sign on a cell <strong>one time only</strong>.</p>

<p>Return <em>the minimum cost to make the grid have at least one valid path</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1368.Minimum%20Cost%20to%20Make%20at%20Least%20One%20Valid%20Path%20in%20a%20Grid/images/grid1.png" style="width: 400px; height: 390px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --&gt; (0, 1) --&gt; (0, 2) --&gt; (0, 3) change the arrow to down with cost = 1 --&gt; (1, 3) --&gt; (1, 2) --&gt; (1, 1) --&gt; (1, 0) change the arrow to down with cost = 1 --&gt; (2, 0) --&gt; (2, 1) --&gt; (2, 2) --&gt; (2, 3) change the arrow to down with cost = 1 --&gt; (3, 3)
The total cost = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1368.Minimum%20Cost%20to%20Make%20at%20Least%20One%20Valid%20Path%20in%20a%20Grid/images/grid2.png" style="width: 350px; height: 341px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,3],[3,2,2],[1,1,4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You can follow the path from (0, 0) to (2, 2).
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1368.Minimum%20Cost%20to%20Make%20at%20Least%20One%20Valid%20Path%20in%20a%20Grid/images/grid3.png" style="width: 200px; height: 192px;" />
<pre>
<strong>Input:</strong> grid = [[1,2],[4,3]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 4</code></li>
</ul>

```python
class Solution:
   def minCost(self, grid: List[List[int]]) -> int:
       m, n = len(grid), len(grid[0])
       dirs = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
       q = deque([(0, 0, 0)])
       vis = set()
       while q:
           i, j, d = q.popleft()
           if (i, j) in vis:
               continue
           vis.add((i, j))
           if i == m - 1 and j == n - 1:
               return d
           for k in range(1, 5):
               x, y = i + dirs[k][0], j + dirs[k][1]
               if 0 <= x < m and 0 <= y < n:
                   # Add to deque based on cost.
                   # The code also works if we append the new row and new column to the end of the
                   # queue instead of adding it to the front or back based in the cost,
                   # but the runtime is faster if we use this logic.
                   if grid[i][j] == k:
                       q.appendleft((x, y, d))
                   else:
                       q.append((x, y, d + 1))
       return -1
```
# [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer)

[中文文档](/solution/0100-0199/0138.Copy%20List%20with%20Random%20Pointer/README.md)

## Description

<!-- description:start -->

<p>A linked list of length <code>n</code> is given such that each node contains an additional random pointer, which could point to any node in the list, or <code>null</code>.</p>

<p>Construct a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> of the list. The deep copy should consist of exactly <code>n</code> <strong>brand new</strong> nodes, where each new node has its value set to the value of its corresponding original node. Both the <code>next</code> and <code>random</code> pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. <strong>None of the pointers in the new list should point to nodes in the original list</strong>.</p>

<p>For example, if there are two nodes <code>X</code> and <code>Y</code> in the original list, where <code>X.random --&gt; Y</code>, then for the corresponding two nodes <code>x</code> and <code>y</code> in the copied list, <code>x.random --&gt; y</code>.</p>

<p>Return <em>the head of the copied linked list</em>.</p>

<p>The linked list is represented in the input/output as a list of <code>n</code> nodes. Each node is represented as a pair of <code>[val, random_index]</code> where:</p>

<ul>
	<li><code>val</code>: an integer representing <code>Node.val</code></li>
	<li><code>random_index</code>: the index of the node (range from <code>0</code> to <code>n-1</code>) that the <code>random</code> pointer points to, or <code>null</code> if it does not point to any node.</li>
</ul>

<p>Your code will <strong>only</strong> be given the <code>head</code> of the original linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0138.Copy%20List%20with%20Random%20Pointer/images/e1.png" style="width: 700px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>Output:</strong> [[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0138.Copy%20List%20with%20Random%20Pointer/images/e2.png" style="width: 700px; height: 114px;" />
<pre>
<strong>Input:</strong> head = [[1,1],[2,1]]
<strong>Output:</strong> [[1,1],[2,1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0138.Copy%20List%20with%20Random%20Pointer/images/e3.png" style="width: 700px; height: 122px;" /></strong></p>

<pre>
<strong>Input:</strong> head = [[3,null],[3,0],[3,null]]
<strong>Output:</strong> [[3,null],[3,0],[3,null]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>Node.random</code> is <code>null</code> or is pointing to some node in the linked list.</li>
</ul>


### With Extra space

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        m = {}
        temp = head
        while temp:
            m[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        m[None] = None
        while temp:
            m[temp].random = m[temp.random]
            m[temp].next = m[temp.next]
            temp = temp.next
        return m[head]
```


### Without Extra space

```python
class Solution:
   def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       if not head:
           return head
       currhead = head
       # Set the next of original list to the node of the new list
       # Set the next of the node of the new list to the next of
       # same node in original list
       while currhead:
           node = Node(currhead.val)
           node.next = currhead.next
           currhead.next = node
           currhead = node.next
      
       # Copy the random pointers in the new list from the
       # random pointers in the original list
       currhead = head
       while currhead:
           if currhead.random:
               currhead.next.random = currhead.random.next
           currhead = currhead.next.next
       ohead = head
       chead = ccopy = ohead.next
      
       # Reset the next pointers in the original list
       while ccopy.next:
           ohead.next = ohead.next.next
           ohead = ohead.next
           ccopy.next = ohead.next
           ccopy = ccopy.next
       return chead   
```

# [139. Word Break](https://leetcode.com/problems/word-break)


## Description

<!-- description:start -->

<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;,&quot;code&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because &quot;leetcode&quot; can be segmented as &quot;leet code&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;,&quot;pen&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because &quot;applepenapple&quot; can be segmented as &quot;apple pen apple&quot;.
Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;,&quot;dog&quot;,&quot;sand&quot;,&quot;and&quot;,&quot;cat&quot;]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>


### Recursion with Memoization(Accepted):
```python
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
```


### DP(Accepted)
```python
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
```


# [143. Reorder List](https://leetcode.com/problems/reorder-list)

[中文文档](/solution/0100-0199/0143.Reorder%20List/README.md)

## Description

<!-- description:start -->

<p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>
L<sub>0</sub> &rarr; L<sub>1</sub> &rarr; &hellip; &rarr; L<sub>n - 1</sub> &rarr; L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>
L<sub>0</sub> &rarr; L<sub>n</sub> &rarr; L<sub>1</sub> &rarr; L<sub>n - 1</sub> &rarr; L<sub>2</sub> &rarr; L<sub>n - 2</sub> &rarr; &hellip;
</pre>

<p>You may not modify the values in the list&#39;s nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0143.Reorder%20List/images/reorder1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0143.Reorder%20List/images/reorder2-linked-list.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>

```python
class Solution:
    def reorderList(self, head):
        # step 1: find middle
        if not head:
            return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
```
# [146. LRU Cache](https://leetcode.com/problems/lru-cache)


## Description

<!-- description:start -->

<p>Design a data structure that follows the constraints of a <strong><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a></strong>.</p>

<p>Implement the <code>LRUCache</code> class:</p>

<ul>
	<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with <strong>positive</strong> size <code>capacity</code>.</li>
	<li><code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, <strong>evict</strong> the least recently used key.</li>
</ul>

<p>The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>Explanation</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>

```python
class Node:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.next = None
        self.prev = None


class Dll:
    def __init__(self):
        # dummy head and tail to avoid checking multiple
        # null conditions.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    @staticmethod
    def remove(node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

    def add(self, node):
        print(type(self.head))
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

class LRUCache:
    def __init__(self, capacity: int):
        self.kv = {}
        self.c = capacity
        self.dll = Dll()
    
    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        Dll.remove(node)
        self.dll.add(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            Dll.remove(self.kv[key])
        node = Node(key, value)
        self.kv[key] = node
        self.dll.add(node)
        if len(self.kv) > self.c:
            p = self.dll.tail.prev
            Dll.remove(p)
            self.kv.pop(p.k)
```

# [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line)

[中文文档](/solution/0100-0199/0149.Max%20Points%20on%20a%20Line/README.md)

## Description

<!-- description:start -->

<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <em>the maximum number of points that lie on the same straight line</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0149.Max%20Points%20on%20a%20Line/images/plane1.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0149.Max%20Points%20on%20a%20Line/images/plane2.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 300</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>All the <code>points</code> are <strong>unique</strong>.</li>
</ul>


```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return inf
            return (y1 - y2) / (x1 - x2)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i + 1 :]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1

```
# [15. 3Sum](https://leetcode.com/problems/3sum)


## Description

<!-- description:start -->

<p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

```python
class Solution:
   def threeSum(self, nums):
       nums.sort()
       result = []
       for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
           if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
               continue
           mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
           right = len(nums) - 1
           while mid < right:
               curr_sum = nums[left] + nums[mid] + nums[right]
               if curr_sum < 0:
                   mid += 1
               elif curr_sum > 0:
                   right -= 1
               else:
                   result.append([nums[left], nums[mid], nums[right]])
                   while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                       mid += 1
                   while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                       right -= 1
                   mid += 1
                   right -= 1
       return result
```



### Time Complexity
The time complexity of the given code is O(n^2). This is because there is a nested loop where the outer loop runs for n times (reduced by 2 to avoid unnecessary 
last iterations due to triplets), and within this loop, there are two pointers that are moving independently towards each other, which in total will lead to n iterations 
in the worst case. There are no nested loops inside the while loop, so the inner operations are constant time notwithstanding the while conditions which are also O(n). 
Multiplying these together gives us n * n = n^2, hence O(n^2).
### Space Complexity
The space complexity of the code is O(log n) if we don't take the output space into consideration, which would be O(n). The space complexity arises due to the space used 
by the sorting algorithm, which is typically O(log n) for the commonly used algorithms like QuickSort or MergeSort in many standard programming libraries.
# [155. Min Stack](https://leetcode.com/problems/min-stack)

[中文文档](/solution/0100-0199/0155.Min%20Stack/README.md)

## Description

<!-- description:start -->

<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>

<ul>
	<li><code>MinStack()</code> initializes the stack object.</li>
	<li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
	<li><code>void pop()</code> removes the element on the top of the stack.</li>
	<li><code>int top()</code> gets the top element of the stack.</li>
	<li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p>You must implement a solution with <code>O(1)</code> time complexity for each function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>


```python
class MinStack:
    def __init__(self):
        self.vals = []
        self.min = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if not self.min or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.min.pop()
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min[-1]
```

# [156. Binary Tree Upside Down 🔒](https://leetcode.com/problems/binary-tree-upside-down)

[中文文档](/solution/0100-0199/0156.Binary%20Tree%20Upside%20Down/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, turn the tree upside down and return <em>the new root</em>.</p>

<p>You can turn a binary tree upside down with the following steps:</p>

<ol>
	<li>The original left child becomes the new root.</li>
	<li>The original root becomes the new right child.</li>
	<li>The original right child becomes the new left child.</li>
</ol>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0156.Binary%20Tree%20Upside%20Down/images/main.jpg" style="width: 600px; height: 95px;" />
<p>The mentioned steps are done level by level. It is <strong>guaranteed</strong> that every right node has a sibling (a left node with the same parent) and has no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0156.Binary%20Tree%20Upside%20Down/images/updown.jpg" style="width: 800px; height: 161px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> [4,5,2,null,null,3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[0, 10]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10</code></li>
	<li>Every right node in the tree has a sibling (a left node that shares the same parent).</li>
	<li>Every right node in the tree has no children.</li>
</ul>

```python
class Solution:
   def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       # Base case: if the root is None or the root doesn't have a left child,
       # the tree cannot be flipped, so return the root as is.
       if root is None or root.left is None:
           return root
       # Recursive case: dive into the left subtree to find the new root after flipping.
       new_root = self.upsideDownBinaryTree(root.left)
       # Once the recursion unwinds, the original root's left child's right child
       # becomes the original root (making the left child the new parent).
       root.left.right = root
       # The left child's left child becomes the original root's right child.
       root.left.left = root.right
       # Erase the original root's left and right children, since they've been reassigned.
       root.left = None
       root.right = None
       # Return the new root of the flipped tree.
       return new_root
```

```
1570. Dot Product of Two Sparse Vectors
Given two sparse vectors, compute their dot product.
Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
Follow up: What if only one of the vectors is sparse?
 
Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 
Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
```

```python
class SparseVector:
   def __init__(self, nums: List[int]):
       self.d = {i: v for i, v in enumerate(nums) if v}
   # Return the dotProduct of two sparse vectors
   def dotProduct(self, vec: "SparseVector") -> int:
       a, b = self.d, vec.d
       # Swapping is not necessary. But it is done to improve time
       # complexity because look ups will be fewer if we process
       # the smaller array.
       if len(b) < len(a):
           a, b = b, a
       return sum(v * b.get(i, 0) for i, v in a.items())
```
# [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder)

[中文文档](/solution/1500-1599/1598.Crawler%20Log%20Folder/README.md)

## Description

<!-- description:start -->

<p>The Leetcode file system keeps a log each time some user performs a <em>change folder</em> operation.</p>

<p>The operations are described below:</p>

<ul>
	<li><code>&quot;../&quot;</code> : Move to the parent folder of the current folder. (If you are already in the main folder, <strong>remain in the same folder</strong>).</li>
	<li><code>&quot;./&quot;</code> : Remain in the same folder.</li>
	<li><code>&quot;x/&quot;</code> : Move to the child folder named <code>x</code> (This folder is <strong>guaranteed to always exist</strong>).</li>
</ul>

<p>You are given a list of strings <code>logs</code> where <code>logs[i]</code> is the operation performed by the user at the <code>i<sup>th</sup></code> step.</p>

<p>The file system starts in the main folder, then the operations in <code>logs</code> are performed.</p>

<p>Return <em>the minimum number of operations needed to go back to the main folder after the change folder operations.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1598.Crawler%20Log%20Folder/images/sample_11_1957.png" style="width: 775px; height: 151px;" /></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;../&quot;,&quot;d21/&quot;,&quot;./&quot;]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Use this change folder operation &quot;../&quot; 2 times and go back to the main folder.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1598.Crawler%20Log%20Folder/images/sample_22_1957.png" style="width: 600px; height: 270px;" /></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;./&quot;,&quot;d3/&quot;,&quot;../&quot;,&quot;d31/&quot;]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;../&quot;,&quot;../&quot;,&quot;../&quot;]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code></li>
	<li><code>2 &lt;= logs[i].length &lt;= 10</code></li>
	<li><code>logs[i]</code> contains lowercase English letters, digits, <code>&#39;.&#39;</code>, and <code>&#39;/&#39;</code>.</li>
	<li><code>logs[i]</code> follows the format described in the statement.</li>
	<li>Folder names consist of lowercase English letters and digits.</li>
</ul>

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = ["main"]
        for op in logs:
            if op == "../":
                if st and st[-1] == "main":
                    continue
                else:
                    st.pop()
            elif op == "./":
                continue
            else:
                st.append(op)
        return len(st) - 1
```
# [1644. Lowest Common Ancestor of a Binary Tree II 🔒](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii)

[中文文档](/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the lowest common ancestor (LCA) of two given nodes, </em><code>p</code><em> and </em><code>q</code>. If either node <code>p</code> or <code>q</code> <strong>does not exist</strong> in the tree, return <code>null</code>. All values of the nodes in the tree are <strong>unique</strong>.</p>

<p>According to the <strong><a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a></strong>: &quot;The lowest common ancestor of two nodes <code>p</code> and <code>q</code> in a binary tree <code>T</code> is the lowest node that has both <code>p</code> and <code>q</code> as <strong>descendants</strong> (where we allow <b>a node to be a descendant of itself</b>)&quot;. A <strong>descendant</strong> of a node <code>x</code> is a node <code>y</code> that is on the path from node <code>x</code> to some leaf node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II/images/binarytree.png" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The LCA of nodes 5 and 1 is 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II/images/binarytree.png" /></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II/images/binarytree.png" /></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
<strong>Output:</strong> null
<strong>Explanation:</strong> Node 10 does not exist in the tree, so return null.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>&nbsp;Can you find the LCA traversing the tree, without checking nodes existence?

### Solution
```
This problem is similar to problem #236, with the difference that node p and node q are not always in the binary tree.
First do depth first search on the binary tree to find the nodes p and q. If either node does not exist, return null.
If both p and q are in the binary tree, then do depth first search again to find the lowest common ancestor.
Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
DFS. If both nodes are in the tree, refer to problem 236-Lowest-Common-Ancestor-of-a-Binary-Tree.
During DFS, if the root is equal to p or q, it cannot immediately return the root like in problem 236-Lowest-Common-Ancestor-of-a-Binary-Tree because we cannot determine if the other node is in the tree. Therefore, our solution is to adopt post-order traversal to ensure that each node is visited. The logic is then the same as when both nodes are in the tree. Additionally, when we encounter p or q during the search, we keep a count. Finally, if the count equals 2, it means that both nodes have been found and we can return the answer.
Algorithm for followup
The solution uses a Depth-First Search (DFS) traversal to go through each node in the binary tree and check for the presence of nodes p and q. To do this, we define a helper function dfs within the lowestCommonAncestor method.
Here is a breakdown of how the dfs function works:
The function takes three arguments: root, p, and q, where root is the current node of the tree that we are exploring.
It begins with a base case that checks if the root is None, meaning we have reached the end of a path without finding a node. If this is the case, it returns False.
Left Recursion: Recursively call dfs for the left child of the current node (root.left).
Right Recursion: Recursively call dfs for the right child of the current node (root.right).
These recursive calls will do a post-order traversal of the tree. After these calls, we have three pieces of information:
l: Whether node p or q has been found in the left subtree.
r: Whether node p or q has been found in the right subtree.
The value of the current node.
Using this information, we can detect the LCA:
If l and r are both True, it implies that p is found in one subtree and q in the other, making the current node their LCA, so we set ans to root.
If one of l or r is True and the current node's value matches p or q, the current node is the LCA - this happens when one is a descendant of the other.
After the visit to each node, we return a boolean to indicate if either p or q has been found in the current subtree or if the current node is p or q. This boolean is the OR of:
l (result from the left subtree),
r (result from the right subtree), and
a check whether the current root matches either p or q.
Finally, lowestCommonAncestor initializes a variable ans to None, which is used to store the LCA. We declare ans as nonlocal inside dfs so that it can be modified within the nested function. The dfs function is then called with the original root, p, and q. The ans is returned as the final result of the lowestCommonAncestor method. If p and q are both present in the tree, ans will be their lowest common ancestor; if either is not present, ans will remain None.
This approach efficiently utilizes the single pass post-order DFS traversal to not just search for p and q but also to identify the LCA without any additional storage or multiple passes through the tree.
```

```python
class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       # This variable will hold the lowest common ancestor once it is found.
       self.ancestor = None
       def dfs(current_node):
           """
           Perform a depth-first search to find the lowest common ancestor.
        
           Args:
           current_node (TreeNode): The current node being visited.
        
           Returns:
           bool: True if the current node is ancestor or is a subtree containing p or q.
           """
           if current_node is None:
               return False
        
           # Search left subtree for p or q
           left = dfs(current_node.left)
        
           # Search right subtree for p or q
           right = dfs(current_node.right)
        
           # Check if current node is either p or q
           mid = current_node == p or current_node == q
        
           # If any two of the three flags left, right, mid are True, current_node is an ancestor
           if mid + left + right >= 2:
               self.ancestor = current_node
        
           # Return True if the current node is p, q, or if p or q is in the subtree rooted at current_node
           return mid or left or right
       # Call dfs to initiate the depth-first search
       dfs(root)
    
       return self.ancestor
```
# [1650. Lowest Common Ancestor of a Binary Tree III 🔒](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii)

[中文文档](/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III/README.md)

## Description

<!-- description:start -->

<p>Given two nodes of a&nbsp;binary tree <code>p</code> and <code>q</code>, return <em>their&nbsp;lowest common ancestor (LCA)</em>.</p>

<p>Each node will have a reference to its parent node. The definition for <code>Node</code> is below:</p>

<pre>
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
</pre>

<p>According to the <strong><a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a></strong>: &quot;The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow <b>a node to be a descendant of itself</b>).&quot;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III/images/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The LCA of nodes 5 and 1 is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III/images/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2], p = 1, q = 2
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> exist in the tree.</li>
</ul>

```python
class Solution:
   def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
       a, b = p, q
       while a != b:
           a = a.parent if a.parent else q
           b = b.parent if b.parent else p
       return a
############
# ref: https://iamageek.medium.com/leetcode-1650-lowest-common-ancestor-of-a-binary-tree-iii-6d008b93376c
def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
   ancestors = set()
   while a is not None:
       ancestors.add(a)
       a = a.parent
   while b is not None:
       if b in ancestors:
           return b
       b = b.parent
# or another one
def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
   pointerA, pointerB = a, b
   while pointerA != pointerB:
       pointerA = pointerA.parent if pointerA else b
       pointerB = pointerB.parent if pointerA else a
   return pointerA
```
# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)


## Description

<!-- description:start -->

<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0017.Letter%20Combinations%20of%20a%20Phone%20Number/images/1200px-telephone-keypad2svg.png" style="width: 300px; height: 243px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;,&quot;ae&quot;,&quot;af&quot;,&quot;bd&quot;,&quot;be&quot;,&quot;bf&quot;,&quot;cd&quot;,&quot;ce&quot;,&quot;cf&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;&quot;
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;2&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>[&#39;2&#39;, &#39;9&#39;]</code>.</li>
</ul>


```python
class Solution:
   def letterCombinations(self, digits: str) -> List[str]:
       d = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
       def dfs(digits, curr, ans, index):
           if index > len(digits):
               return
           if index == len(digits):
               ans.append(curr)
               return
           for c in d[digits[index]]:
               dfs(digits, curr + c, ans, index + 1)
       if not digits:
           return []
       ans = []
       dfs(digits, '', ans, 0)
       return ans
```
# [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator)

[中文文档](/solution/0100-0199/0173.Binary%20Search%20Tree%20Iterator/README.md)

## Description

<!-- description:start -->

<p>Implement the <code>BSTIterator</code> class that represents an iterator over the <strong><a href="https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)" target="_blank">in-order traversal</a></strong> of a binary search tree (BST):</p>

<ul>
	<li><code>BSTIterator(TreeNode root)</code> Initializes an object of the <code>BSTIterator</code> class. The <code>root</code> of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there exists a number in the traversal to the right of the pointer, otherwise returns <code>false</code>.</li>
	<li><code>int next()</code> Moves the pointer to the right, then returns the number at the pointer.</li>
</ul>

<p>Notice that by initializing the pointer to a non-existent smallest number, the first call to <code>next()</code> will return the smallest element in the BST.</p>

<p>You may assume that <code>next()</code> calls will always be valid. That is, there will be at least a next number in the in-order traversal when <code>next()</code> is called.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0173.Binary%20Search%20Tree%20Iterator/images/bst-tree.png" style="width: 189px; height: 178px;" />
<pre>
<strong>Input</strong>
[&quot;BSTIterator&quot;, &quot;next&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
<strong>Output</strong>
[null, 3, 7, true, 9, true, 15, true, 20, false]

<strong>Explanation</strong>
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next(); // return 3
bSTIterator.next(); // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 20
bSTIterator.hasNext(); // return False

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made to <code>hasNext</code>, and <code>next</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Could you implement <code>next()</code> and <code>hasNext()</code> to run in average <code>O(1)</code> time and use&nbsp;<code>O(h)</code> memory, where <code>h</code> is the height of the tree?</li>
</ul>

### My Solution(Satisfies next() in O(n))

```python
class BSTIterator:
   def __init__(self, root: Optional[TreeNode]):
       self.s = []
       while root:
           self.s.append(root)
           root = root.left
   def next(self) -> int:
       if not self.hasNext():
           return -1
       top = self.s.pop()
       root = top.right
       while root:
           self.s.append(root)
           root = root.left
       return top.val
   def hasNext(self) -> bool:
       return self.s != []
```


The average time complexity of next() function is O(1) indeed in your case. As the next function can be called n times at most,   
and the number of right nodes in self.pushAll(tmpNode.right) function is maximal n in a tree which has n nodes, so the amortized   
time complexity is O(1).  
# [1797. Design Authentication Manager](https://leetcode.com/problems/design-authentication-manager)


## Description

<!-- description:start -->

<p>There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire <code>timeToLive</code> seconds after the <code>currentTime</code>. If the token is renewed, the expiry time will be <b>extended</b> to expire <code>timeToLive</code> seconds after the (potentially different) <code>currentTime</code>.</p>

<p>Implement the <code>AuthenticationManager</code> class:</p>

<ul>
	<li><code>AuthenticationManager(int timeToLive)</code> constructs the <code>AuthenticationManager</code> and sets the <code>timeToLive</code>.</li>
	<li><code>generate(string tokenId, int currentTime)</code> generates a new token with the given <code>tokenId</code> at the given <code>currentTime</code> in seconds.</li>
	<li><code>renew(string tokenId, int currentTime)</code> renews the <strong>unexpired</strong> token with the given <code>tokenId</code> at the given <code>currentTime</code> in seconds. If there are no unexpired tokens with the given <code>tokenId</code>, the request is ignored, and nothing happens.</li>
	<li><code>countUnexpiredTokens(int currentTime)</code> returns the number of <strong>unexpired</strong> tokens at the given currentTime.</li>
</ul>

<p>Note that if a token expires at time <code>t</code>, and another action happens on time <code>t</code> (<code>renew</code> or <code>countUnexpiredTokens</code>), the expiration takes place <strong>before</strong> the other actions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1700-1799/1797.Design%20Authentication%20Manager/images/copy-of-pc68_q2.png" style="width: 500px; height: 287px;" />
<pre>
<strong>Input</strong>
[&quot;AuthenticationManager&quot;, &quot;<code>renew</code>&quot;, &quot;generate&quot;, &quot;<code>countUnexpiredTokens</code>&quot;, &quot;generate&quot;, &quot;<code>renew</code>&quot;, &quot;<code>renew</code>&quot;, &quot;<code>countUnexpiredTokens</code>&quot;]
[[5], [&quot;aaa&quot;, 1], [&quot;aaa&quot;, 2], [6], [&quot;bbb&quot;, 7], [&quot;aaa&quot;, 8], [&quot;bbb&quot;, 10], [15]]
<strong>Output</strong>
[null, null, null, 1, null, null, null, 0]

<strong>Explanation</strong>
AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with <code>timeToLive</code> = 5 seconds.
authenticationManager.<code>renew</code>(&quot;aaa&quot;, 1); // No token exists with tokenId &quot;aaa&quot; at time 1, so nothing happens.
authenticationManager.generate(&quot;aaa&quot;, 2); // Generates a new token with tokenId &quot;aaa&quot; at time 2.
authenticationManager.<code>countUnexpiredTokens</code>(6); // The token with tokenId &quot;aaa&quot; is the only unexpired one at time 6, so return 1.
authenticationManager.generate(&quot;bbb&quot;, 7); // Generates a new token with tokenId &quot;bbb&quot; at time 7.
authenticationManager.<code>renew</code>(&quot;aaa&quot;, 8); // The token with tokenId &quot;aaa&quot; expired at time 7, and 8 &gt;= 7, so at time 8 the <code>renew</code> request is ignored, and nothing happens.
authenticationManager.<code>renew</code>(&quot;bbb&quot;, 10); // The token with tokenId &quot;bbb&quot; is unexpired at time 10, so the <code>renew</code> request is fulfilled and now the token will expire at time 15.
authenticationManager.<code>countUnexpiredTokens</code>(15); // The token with tokenId &quot;bbb&quot; expires at time 15, and the token with tokenId &quot;aaa&quot; expired at time 7, so currently no token is unexpired, so return 0.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= timeToLive &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= currentTime &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= tokenId.length &lt;= 5</code></li>
	<li><code>tokenId</code> consists only of lowercase letters.</li>
	<li>All calls to <code>generate</code> will contain unique values of <code>tokenId</code>.</li>
	<li>The values of <code>currentTime</code> across all the function calls will be <strong>strictly increasing</strong>.</li>
	<li>At most <code>2000</code> calls will be made to all functions combined.</li>
</ul>


```python
class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.token = {}
        self.time = timeToLive  # store timeToLive and create dictionary

    def generate(self, tokenId, currentTime):
        self.token[tokenId] = currentTime  # store tokenId with currentTime

    def renew(self, tokenId, currentTime):
        limit = (
            currentTime - self.time
        )  # calculate limit time to filter unexpired tokens
        if (
            tokenId in self.token and self.token[tokenId] > limit
        ):  # filter tokens and renew its time
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime):
        # print('----')
        limit = (
            currentTime - self.time
        )  # calculate limit time to filter unexpired tokens
        count = 0
        popkeys = []
        for id, timetolive in self.token.items():
            if timetolive > limit:  # count unexpired tokens
                count += 1
            else:
                popkeys.append(id)
        if popkeys:
            for k in popkeys:
                self.token.pop(k)
        return ccount
```

### Python O(1) solution: Doubly Linked List + Dict. Beat 99.7%

#### Intuition
Borrow the idea from LRU cache. Maintain a dict and a doubly linked list(dll) to store the existing tokens.

Approach
generate: add the node to the dict and to the dll.
renew: remove the current node and append it to the tail of dll
countUnexpiredTokens: check the head of the dll and remove those expired. Return the size of dll
Complexity
Time complexity:

generate: O(1)
renew: O(1)
countUnexpiredTokens: amortized O(1)
Space complexity:

O(n)

```python
class ListNode:
    def __init__(self, token, currentTime):
        self.token = token
        self.insertTime = currentTime
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.size = 0
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # add to the tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def print(self):
        node = self.head.next
        while node.token != -1:
            print(node.token, " ->", end="")
            node = node.next
        print()


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.dll = DLL()
        self.cache = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        node = ListNode(tokenId, currentTime)
        self.dll.add(node)
        self.cache[tokenId] = node

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.cache:
            return

        node = self.cache[tokenId]

        if node.insertTime + self.timeToLive <= currentTime:
            # expired
            self.dll.remove(node)
            del self.cache[tokenId]
        else:
            self.dll.remove(node)
            node.insertTime = currentTime
            self.dll.add(node)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        node = self.dll.head.next
        while (
            node.insertTime != -1 and node.insertTime + self.timeToLive <= currentTime
        ):
            self.dll.remove(node)
            del self.cache[node.token]
            node = self.dll.head.next
        return self.dll.size
```
# [18. 4Sum](https://leetcode.com/problems/4sum)


## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of <code>n</code> integers, return <em>an array of all the <strong>unique</strong> quadruplets</em> <code>[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>

<ul>
	<li><code>0 &lt;= a, b, c, d&nbsp;&lt; n</code></li>
	<li><code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code> are <strong>distinct</strong>.</li>
	<li><code>nums[a] + nums[b] + nums[c] + nums[d] == target</code></li>
</ul>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], target = 8
<strong>Output:</strong> [[2,2,2,2]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

```python
class Solution:
   def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       nums.sort()
       n = len(nums)
       ans = set()
       for i in range(n):
           for j in range(i+1, n):
               l, r = j + 1, n - 1
               remain = target - nums[i] - nums[j]
               while l < r:
                   if nums[l] + nums[r] == remain:
                       ans.add((nums[i], nums[j], nums[l], nums[r]))
                       l += 1
                       r -= 1
                   elif nums[l] + nums[r] > remain:
                       r -= 1
                   else:
                       l += 1
       return ans
```





### (Important)Follow-up question: Calculate K-Sum?
```python
class Solution:  # 1084 ms, faster than 37.26%
   def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       def dfs(l, r, k, target, path, out):  # [l, r] inclusive
           if k == 2:
               while l < r:
                   if nums[l] + nums[r] == target:
                       out.append(path + [nums[l], nums[r]])
                       while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                       l, r = l + 1, r - 1
                   elif nums[l] + nums[r] > target:
                       r -= 1  # Decrease sum
                   else:
                       l += 1  # Increase sum
               return
           while l < r:
               dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
               while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
               l += 1
       def kSum(k):  # k >= 2
           ans = []
           nums.sort()
           dfs(0, len(nums)-1, k, target, [], ans)
           return ans
       return kSum(4)
```
# [189. Rotate Array](https://leetcode.com/problems/rotate-array)

[中文文档](/solution/0100-0199/0189.Rotate%20Array/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Try to come up with as many solutions as you can. There are at least <strong>three</strong> different ways to solve this problem.</li>
	<li>Could you do it in-place with <code>O(1)</code> extra space?</li>
</ul>


```python
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        if k == 0:
            return
        n = len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)
```
# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

### Question:
Given a linked list, remove the n-th node from the end of list and return its head.

```
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

```
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0019.Remove%20Nth%20Node%20From%20End%20of%20List/images/remove_ex1.jpg" style="width: 542px; height: 222px;" />

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
```
#### Check if list size is less than n

```python

def RemoveFromEnd(head, n):
    fast = head
    i = 0
    while i < n:
        if fast:
            fast = fast.next
        else:
            print(f"List size less than {n}")
            return head
        i += 1
    slow = head
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
    slow.next = slow.next.next
    return head
```
# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)

[中文文档](/solution/0100-0199/0199.Binary%20Tree%20Right%20Side%20View/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, imagine yourself standing on the <strong>right side</strong> of it, return <em>the values of the nodes you can see ordered from top to bottom</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,null,5,null,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0199.Binary%20Tree%20Right%20Side%20View/images/tmpd5jn43fs-1.png" style="width: 400px; height: 207px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,4,null,null,null,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,4,5]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0199.Binary%20Tree%20Right%20Side%20View/images/tmpkpe40xeh-1.png" style="width: 400px; height: 214px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,null,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3]</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = []</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            s = len(q)
            ans.append(q[0].val)
            while s:
                top = q.popleft()
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
                s -= 1
        return ans
```

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def util(root, depth):
            if not root:
                return
            if len(ans) == depth:
                ans.append(root.val)
            util(root.right, depth + 1)
            util(root.left, depth + 1)

        util(root, 0)
        return ans
```
## 17. Letter Combinations of a Phone Number

### Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

```
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(digits, curr, ans, index):
            if index > len(digits):
                return
            if index == len(digits):
                ans.append(curr)
                return
            for c in d[digits[index]]:
                dfs(digits, curr + c, ans, index + 1)

        if not digits:
            return []
        ans = []
        dfs(digits, "", ans, 0)
        return ans
```

# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)


## Description

<!-- description:start -->

<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()[]{}&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([])&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

Traverse the bracket string $s$. When encountering a left bracket, push the current left bracket into the stack; when encountering a right bracket, pop the top element of the stack (if the stack is empty, directly return `false`), and judge whether it matches. If it does not match, directly return `false`.

Alternatively, when encountering a left bracket, you can push the corresponding right bracket into the stack; when encountering a right bracket, pop the top element of the stack (if the stack is empty, directly return `false`), and judge whether they are equal. If they do not match, directly return `false`.

> The difference between the two methods is only the timing of bracket conversion, one is when pushing into the stack, and the other is when popping out of the stack.

At the end of the traversal, if the stack is empty, it means the bracket string is valid, return `true`; otherwise, return `false`.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the bracket string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {'()', '[]', '{}'}
        for c in s:
            if c in '({[':
                stk.append(c)
            elif not stk or stk.pop() + c not in d:
                return False
        return not stk
```


# [200. Number of Islands](https://leetcode.com/problems/number-of-islands)


## Description

<!-- description:start -->

<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
```

# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)

[中文文档](/solution/0000-0099/0021.Merge%20Two%20Sorted%20Lists/README.md)

## Description

<!-- description:start -->

<p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0021.Merge%20Two%20Sorted%20Lists/images/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

First, we judge whether the linked lists $l_1$ and $l_2$ are empty. If one of them is empty, we return the other linked list. Otherwise, we compare the head nodes of $l_1$ and $l_2$:

-   If the value of the head node of $l_1$ is less than or equal to the value of the head node of $l_2$, we recursively call the function $mergeTwoLists(l_1.next, l_2)$, and connect the head node of $l_1$ with the returned linked list head node, and return the head node of $l_1$.
-   Otherwise, we recursively call the function $mergeTwoLists(l_1, l_2.next)$, and connect the head node of $l_2$ with the returned linked list head node, and return the head node of $l_2$.

The time complexity is $O(m + n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the lengths of the two linked lists respectively.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```
# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii)

[中文文档](/solution/0200-0299/0210.Course%20Schedule%20II/README.md)

## Description

<!-- description:start -->

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <em>the ordering of courses you should take to finish all courses</em>. If there are many valid answers, return <strong>any</strong> of them. If it is impossible to finish all courses, return <strong>an empty array</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>Output:</strong> [0,2,1,3]
<strong>Explanation:</strong> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 1, prerequisites = []
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are <strong>distinct</strong>.</li>
</ul>


```python
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        d_count = defaultdict(int)
        dep = defaultdict(list)
        for p in pre:
            dep[p[1]].append(p[0])
            d_count[p[0]] += 1
        q = deque()
        res = []
        for i in range(numCourses):
            if not d_count[i]:
                q.append(i)
        while q:
            top = q.popleft()
            res.append(top)
            for t in dep[top]:
                d_count[t] -= 1
                if not d_count[t]:
                    q.append(t)
        return res if max(d_count.values()) == 0 else []
```
# [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure)

[中文文档](/solution/0200-0299/0211.Design%20Add%20and%20Search%20Words%20Data%20Structure/README.md)

## Description

<!-- description:start -->

<p>Design a data structure that supports adding new words and finding if a string matches any previously added string.</p>

<p>Implement the <code>WordDictionary</code> class:</p>

<ul>
	<li><code>WordDictionary()</code>&nbsp;Initializes the object.</li>
	<li><code>void addWord(word)</code> Adds <code>word</code> to the data structure, it can be matched later.</li>
	<li><code>bool search(word)</code>&nbsp;Returns <code>true</code> if there is any string in the data structure that matches <code>word</code>&nbsp;or <code>false</code> otherwise. <code>word</code> may contain dots <code>&#39;.&#39;</code> where dots can be matched with any letter.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<pre>
<strong>Input</strong>
[&quot;WordDictionary&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;]
[[],[&quot;bad&quot;],[&quot;dad&quot;],[&quot;mad&quot;],[&quot;pad&quot;],[&quot;bad&quot;],[&quot;.ad&quot;],[&quot;b..&quot;]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord(&quot;bad&quot;);
wordDictionary.addWord(&quot;dad&quot;);
wordDictionary.addWord(&quot;mad&quot;);
wordDictionary.search(&quot;pad&quot;); // return False
wordDictionary.search(&quot;bad&quot;); // return True
wordDictionary.search(&quot;.ad&quot;); // return True
wordDictionary.search(&quot;b..&quot;); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 25</code></li>
	<li><code>word</code> in <code>addWord</code> consists of lowercase English letters.</li>
	<li><code>word</code> in <code>search</code> consist of <code>&#39;.&#39;</code> or lowercase English letters.</li>
	<li>There will be at most <code>2</code> dots in <code>word</code> for <code>search</code> queries.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>addWord</code> and <code>search</code>.</li>
</ul>

```python
class Tnode:
    def __init__(self):
        self.child = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.head = Tnode()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.child:
                node.child[c] = Tnode()
            node = node.child[c]
        node.word = True

    def search(self, word: str) -> bool:
        def searchutil(head, i):
            if i == len(word):
                return head.word
            if word[i] == ".":
                for ch in head.child.values():
                    if searchutil(ch, i + 1):
                        return True
            if word[i] in head.child:
                return searchutil(head.child[word[i]], i + 1)
            return False

        return searchutil(self.head, 0)

```
# [213. House Robber II](https://leetcode.com/problems/house-robber-ii)

[中文文档](/solution/0200-0299/0213.House%20Robber%20II/README.md)

## Description

<!-- description:start -->

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


```python
class Solution:
   def rob(self, nums: List[int]) -> int:
       def robutil(nums: List[int]) -> int:
           if len(nums) < 2:
               return nums[len(nums) - 1]
           d = [0] * len(nums)
           d[0] = nums[0]
           d[1] = max(d[0], nums[1])
           i = 2
           while i < len(nums):
               d[i] = max(d[i-2] + nums[i], d[i-1])
               i += 1
           return d[i-1]
       if len(nums) < 2:
           return nums[len(nums)-1]
       return max(robutil(nums[0:-1]), robutil(nums[1:]))
```


# [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii)

[中文文档](/solution/0200-0299/0216.Combination%20Sum%20III/README.md)

## Description

<!-- description:start -->

<p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that the following conditions are true:</p>

<ul>
	<li>Only numbers <code>1</code> through <code>9</code> are used.</li>
	<li>Each number is used <strong>at most once</strong>.</li>
</ul>

<p>Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 &gt; 1, there are no valid combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, 10)]

        def util(index, path, sum):
            if sum == 0 and len(path) == k:
                res.append(path)
                return
            if index >= len(nums):
                return
            util(index + 1, path + [nums[index]], sum - nums[index])
            util(index + 1, path, sum)

        util(0, [], n)
        return res
```
# [2174. Remove All Ones With Row and Column Flips II 🔒](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii)

[中文文档](/solution/2100-2199/2174.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips%20II/README.md)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> <strong>binary</strong> matrix <code>grid</code>.</p>

<p>In one operation, you can choose any <code>i</code> and <code>j</code> that meet the following conditions:</p>

<ul>
	<li><code>0 &lt;= i &lt; m</code></li>
	<li><code>0 &lt;= j &lt; n</code></li>
	<li><code>grid[i][j] == 1</code></li>
</ul>

<p>and change the values of <strong>all</strong> cells in row <code>i</code> and column <code>j</code> to zero.</p>

<p>Return <em>the <strong>minimum</strong> number of operations needed to remove all </em><code>1</code><em>&#39;s from </em><code>grid</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2174.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips%20II/images/image-20220213162716-1.png" style="width: 709px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,1,1],[0,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
In the first operation, change all cell values of row 1 and column 1 to zero.
In the second operation, change all cell values of row 0 and column 0 to zero.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2174.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips%20II/images/image-20220213162737-2.png" style="width: 734px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,0],[1,0,1],[0,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
In the first operation, change all cell values of row 1 and column 0 to zero.
In the second operation, change all cell values of row 2 and column 1 to zero.
Note that we cannot perform an operation using row 1 and column 1 because grid[1][1] != 1.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2174.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips%20II/images/image-20220213162752-3.png" style="width: 156px; height: 150px;" />
<pre>
<strong>Input:</strong> grid = [[0,0],[0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
There are no 1&#39;s to remove so return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 15</code></li>
	<li><code>1 &lt;= m * n &lt;= 15</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

```python
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        state = sum(1 << (i * n + j) for i in range(m) for j in range(n) if grid[i][j])
        q = deque([state])
        vis = {state}
        ans = 0
        while q:
            for _ in range(len(q)):
                state = q.popleft()
                if state == 0:
                    return ans
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 0:
                            continue
                        nxt = state
                        for r in range(m):
                            nxt &= ~(1 << (r * n + j))
                        for c in range(n):
                            nxt &= ~(1 << (i * n + c))
                        if nxt not in vis:
                            vis.add(nxt)
                            q.append(nxt)
            ans += 1
        return -1
```
## 22. Generate Parentheses

### Question:
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

### Solution:
The idea is to add ')' only after valid '('
We use two integer variables left & right to see how many '(' & ')' are in the current string
If left < n then we can add '(' to the current string
If right < left then we can add ')' to the current string

#### Using Recusrion
``` python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")

        res = []
        dfs(0, 0, "")
        return res
```
#### Using Stack
``` python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        if n < 1:
            return res
        s.append(("(", 1, 0))
        while s:
            curr, left, right = s.pop()
            if len(curr) == 2 * n:
                res.append(curr)
                continue
            if left < n:
                s.append((curr + "(", left + 1, right))
            if right < left:
                s.append((curr + ")", left, right + 1))
        return res
```
# [224. Basic Calculator](https://leetcode.com/problems/basic-calculator)

Solution to 227 covers all the cases for this problem to.
## Description

<!-- description:start -->

<p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return <em>the result of the evaluation</em>.</p>

<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1 + 1&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; 2-1 + 2 &quot;
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(1+(4+5+2)-3)+(6+8)&quot;
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of digits, <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, and <code>&#39; &#39;</code>.</li>
	<li><code>s</code> represents a valid expression.</li>
	<li><code>&#39;+&#39;</code> is <strong>not</strong> used as a unary operation (i.e., <code>&quot;+1&quot;</code> and <code>&quot;+(2 + 3)&quot;</code> is invalid).</li>
	<li><code>&#39;-&#39;</code> could be used as a unary operation (i.e., <code>&quot;-1&quot;</code> and <code>&quot;-(2 + 3)&quot;</code> is valid).</li>
	<li>There will be no two consecutive operators in the input.</li>
	<li>Every number and running calculation will fit in a signed 32-bit integer.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We use a stack $stk$ to save the current calculation result and operator, a variable $sign$ to save the current sign, and a variable $ans$ to save the final calculation result.

Next, we traverse each character of the string $s$:

-   If the current character is a number, we use a loop to read the following consecutive numbers, and then add or subtract it to $ans$ according to the current sign.
-   If the current character is `'+'`, we change the variable $sign$ to positive.
-   If the current character is `'-'`, we change the variable $sign$ to negative.
-   If the current character is `'('`, we push the current $ans$ and $sign$ into the stack, and reset them to empty and 1, and start to calculate the new $ans$ and $sign$.
-   If the current character is `')'`, we pop the top two elements of the stack, one is the operator, and the other is the number calculated before the bracket. We multiply the current number by the operator, and add the previous number to get the new $ans$.

After traversing the string $s$, we return $ans$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        ans, sign = 0, 1
        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                x = 0
                j = i
                while j < n and s[j].isdigit():
                    x = x * 10 + int(s[j])
                    j += 1
                ans += sign * x
                i = j - 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans = stk.pop() * ans + stk.pop()
            i += 1
        return ans
```
# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

[中文文档](/solution/0000-0099/0023.Merge%20k%20Sorted%20Lists/README.md)

## Description

<!-- description:start -->

<p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
</ul>


### Using Merge Sort
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge2list(l1.next, l2)
                return l1
            else:
                l2.next = merge2list(l1, l2.next)
                return l2

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l = len(lists) // 2
        first = self.mergeKLists(lists[:l])
        second = self.mergeKLists(lists[l:])
        return merge2list(first, second)
```


### Using Priority Queue
```python
import queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        curr = res = ListNode(0)
        q = queue.PriorityQueue()
        for index, l in enumerate(lists):
            if not l:
                continue
            q.put((l.val, index, l))
        while q.qsize():
            v, index, node = q.get()
            curr.next = node
            curr = curr.next
            if node.next:
                q.put((node.next.val, index, node.next))
        return res.next
```


### Time complexity:
Heap Operations: Each insertion and extraction from the heap takes O(logk), where k is the number of lists.  
Total Nodes Processed: Across all lists, there are N nodes in total.  
Overall Complexity: Since each node is pushed and popped once, the total time complexity is O(Nlogk).  
### Space complexity:
The heap stores at most k elements at any time, giving O(k) space for the heap.  
Other auxiliary space used is O(1) (excluding the output list).  
Total Space Complexity: O(k).  
## 24. Swap Nodes in Pairs

### Question:
Given a linked list, swap every two adjacent nodes and return its head.

```
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

Note:

* Your algorithm should use only constant extra space.
* You may not modify the values in the list's nodes, only nodes itself may be changed.

``` python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            adj = cur.next
            if prev:
                prev.next = adj
            cur.next = adj.next
            adj.next = cur
            prev, cur = cur, cur.next
        return ans or head
```
## 25. Reverse Nodes in k-Group

### Question:
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

```
Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
```

Note:
* Only constant extra memory is allowed.
* You may not alter the values in the list's nodes, only nodes itself may be changed.

``` python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
	# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev
```
# [254. Factor Combinations 🔒](https://leetcode.com/problems/factor-combinations)


## Description

<!-- description:start -->

<p>Numbers can be regarded as the product of their factors.</p>

<ul>
	<li>For example, <code>8 = 2 x 2 x 2 = 2 x 4</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>all possible combinations of its factors</em>. You may return the answer in <strong>any order</strong>.</p>

<p><strong>Note</strong> that the factors should be in the range <code>[2, n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> [[2,6],[3,4],[2,2,3]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 37
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>7</sup></code></li>
</ul>

Iterate from 2 to n. If the current number i is divisible by n, it means that i is a factor of n. Store it in a onePath list, and then recursively call n/i.  
At next recursion, do not traverse from 2. It traverses from i to n/i, and the condition for stopping is when n is equal to 1, if there is a factor in onePath at this time, store this combination in the result.  

```python
class Solution:
   def getFactors(self, n: int) -> List[List[int]]:
       # Helper function to perform depth-first search
       def depth_first_search(target, start_factor):
           # If temp_factors has elements, then add a combination to the answer
           if temp_factors:
               answer.append(temp_factors + [target])
           # Initialize a factor to start from
           factor = start_factor
           # Check for factors only up to the square root of the target
           while factor * factor <= target:
               # If factor is a valid factor of target
               if target % factor == 0:
                   # Append the factor to the temporary list for possible answer
                   temp_factors.append(factor)
                   # Recurse with the reduced number (integer division)
                   depth_first_search(target // factor, factor)
                   # Pop the last factor to backtrack
                   temp_factors.pop()
               # Increment the factor
               factor += 1
       # A list to keep a temporary set of factors for a combination
       temp_factors = []
       # The final list of lists to be returned
       answer = []
       # Initiate depth-first search with the full target and the smallest factor
       depth_first_search(n, 2)
       return answer
```

```
2560. House Robber IV
Medium

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2
```

### Explanation
```
Binary search the minimum capability of the robber to steal at least k houses.


we can initial the binary search range as left = min(A) and right = max(A).

Assume the capability is mid, we iterate the houses A, and greedily take the houses as many as possible, if mid > A[i] and we didn't take A[i-1].

Then we check if we have take k houses, If take >= k, we have big enough capability, right = mid.
If take < k, we don't have big enough capability, left = mid + 1.

Finally we return the binary search result.

Complexity
Time O(nlogm),
where m is the range of A[i]
Space O(1)
```

```python
class Solution:
   def minCapability(self, A: List[int], k: int) -> int:
       l, r = min(A), max(A)
       while l < r:
           m = (l + r) // 2
           lastTaken = False
           count = 0
           for a in A:
               if lastTaken:
                   lastTaken = False
                   continue
               if a <= m:
                   count += 1
                   lastTaken = True
           if count >= k:
               r = m
           else:
               l = m + 1
       return l
```
# [2707. Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string)


## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>s</code> and a dictionary of words <code>dictionary</code>. You have to break <code>s</code> into one or more <strong>non-overlapping</strong> substrings such that each substring is present in <code>dictionary</code>. There may be some <strong>extra characters</strong> in <code>s</code> which are not present in any of the substrings.</p>

<p>Return <em>the <strong>minimum</strong> number of extra characters left over if you break up </em><code>s</code><em> optimally.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetscode&quot;, dictionary = [&quot;leet&quot;,&quot;code&quot;,&quot;leetcode&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can break s in two substrings: &quot;leet&quot; from index 0 to 3 and &quot;code&quot; from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;sayhelloworld&quot;, dictionary = [&quot;hello&quot;,&quot;world&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can break s in two substrings: &quot;hello&quot; from index 3 to 7 and &quot;world&quot; from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 50</code></li>
	<li><code>dictionary[i]</code>&nbsp;and <code>s</code> consists of only lowercase English letters</li>
	<li><code>dictionary</code> contains distinct words</li>
</ul>

<!-- description:end -->

## Solutions

### My Solution(Recursion with Memoization, Accepted)
```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)

        @cache
        def util(st):
            if len(st) == 0:
                return 0
            res = []
            for i in range(1, len(st) + 1):
                if st[:i] in d:
                    res.append(util(st[i:]))
                else:
                    res.append(i + util(st[i:]))
            return min(res)

        return util(s)
```
### Dynamic Programming
The idea here is to use the Dynamic Programming array dp to store the minimum number of extra characters needed when the string is broken up optimally up to index i.
Initialization: Create an array dp of length |s| + 1, initialized with a large value (larger than the maximum possible extra characters). Set dp[0] = 0.


Main Algorithm:


Iterate through the string from 1 to |s|.
For each i, set dp[i] = dp[i-1] + 1 as a worst-case scenario.
Update dp[i] based on substrings of s ending at i that are in the dictionary. Use dp[i - len(substring)] for this.
Time Complexity: O(n2)O(n^2)O(n2) — We iterate through the string and for each character, we consider all substrings ending at that character.
Space Complexity: O(n)— For the DP array.


```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = [float("inf")] * (len(s) + 1)
        d[0] = 0
        dic = set(dictionary)
        for i in range(1, len(s) + 1):
            d[i] = d[i - 1] + 1
            for j in range(0, i):
                if s[j:i] in dic:
                    d[i] = min(d[j], d[i])
        return d[len(s)]

```
# [272. Closest Binary Search Tree Value II 🔒](https://leetcode.com/problems/closest-binary-search-tree-value-ii)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree, a <code>target</code> value, and an integer <code>k</code>, return <em>the </em><code>k</code><em> values in the BST that are closest to the</em> <code>target</code>. You may return the answer in <strong>any order</strong>.</p>

<p>You are <strong>guaranteed</strong> to have only one unique set of <code>k</code> values in the BST that are closest to the <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0272.Closest%20Binary%20Search%20Tree%20Value%20II/images/closest1-1-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,2,5,1,3], target = 3.714286, k = 2
<strong>Output:</strong> [4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1], target = 0.000000, k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Assume that the BST is balanced. Could you solve it in less than <code>O(n)</code> runtime (where <code>n = total nodes</code>)?</p>

```python
class Solution:
   def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
       # Perform in-order depth-first search to traverse the tree.
       def in_order_dfs(node):
           if node is None:
               return
        
           # Recurse on the left child.
           in_order_dfs(node.left)
        
           # Process the current node.
           # If we have fewer than k values, add current node's value.
           if len(closest_values) < k:
               closest_values.append(node.val)
           else:
               # Once we have k values, check if current node is closer to target
               # than the first value in the deque. If not, no need to proceed further.
               if abs(node.val - target) >= abs(closest_values[0] - target):
                   return
            
               # If the current node is closer, pop the first value and append the current value.
               closest_values.popleft()
               closest_values.append(node.val)
        
           # Recurse on the right child.
           in_order_dfs(node.right)
       # This deque will store the closest k values encountered so far.
       closest_values = deque()
    
       # Start the in-order traversal of the tree.
       in_order_dfs(root)
    
       # Return the k closest values as a list.
       return list(closest_values)
```


# [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words)

[中文文档](/solution/0200-0299/0273.Integer%20to%20English%20Words/README.md)

## Description

<!-- description:start -->

<p>Convert a non-negative integer <code>num</code> to its English words representation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 123
<strong>Output:</strong> &quot;One Hundred Twenty Three&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 12345
<strong>Output:</strong> &quot;Twelve Thousand Three Hundred Forty Five&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 1234567
<strong>Output:</strong> &quot;One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

```python
class Solution:
   def __init__(self):
       # initialize arrays
       self.ones = [
           "",
           " One",
           " Two",
           " Three",
           " Four",
           " Five",
           " Six",
           " Seven",
           " Eight",
           " Nine",
           " Ten",
           " Eleven",
           " Twelve",
           " Thirteen",
           " Fourteen",
           " Fifteen",
           " Sixteen",
           " Seventeen",
           " Eighteen",
           " Nineteen",
       ]
       self.tens = [
           "",
           " Ten",
           " Twenty",
           " Thirty",
           " Forty",
           " Fifty",
           " Sixty",
           " Seventy",
           " Eighty",
           " Ninety",
       ]
       self.thousands = ["", " Thousand", " Million", " Billion"]
   def helper(self, n: int) -> str:
       if n < 20:
           return self.ones[n]
       elif n < 100:
           return self.tens[n // 10] + self.helper(n % 10)
       elif n < 1000:
           return self.helper(n // 100) + " Hundred" + self.helper(n % 100)
       else:
           for i in range(3, 0, -1):
               if n >= 1000**i:
                   return (
                       self.helper(n // (1000**i))
                       + self.thousands[i]
                       + self.helper(n % (1000**i))
                   )
       return ""
   def numberToWords(self, num: int) -> str:
       # edge case
       if num == 0:
           return "Zero"
       return self.helper(num).lstrip()
```
# [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream)


## Description

<!-- description:start -->

<p>The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.</p>

<ul>
	<li>For example, for <code>arr = [2,3,4]</code>, the median is <code>3</code>.</li>
	<li>For example, for <code>arr = [2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p>Implement the MedianFinder class:</p>

<ul>
	<li><code>MedianFinder()</code> initializes the <code>MedianFinder</code> object.</li>
	<li><code>void addNum(int num)</code> adds the integer <code>num</code> from the data stream to the data structure.</li>
	<li><code>double findMedian()</code> returns the median of all elements so far. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MedianFinder&quot;, &quot;addNum&quot;, &quot;addNum&quot;, &quot;findMedian&quot;, &quot;addNum&quot;, &quot;findMedian&quot;]
[[], [1], [2], [], [3], []]
<strong>Output</strong>
[null, null, null, 1.5, null, 2.0]

<strong>Explanation</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>5</sup> &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li>There will be at least one element in the data structure before calling <code>findMedian</code>.</li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls will be made to <code>addNum</code> and <code>findMedian</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>If all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution?</li>
	<li>If <code>99%</code> of all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution?</li>
</ul>


### Solution

The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on n's parity.  
This way we only need to peek the two heaps' top number to calculate median.  
Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):  
(1) length of (small, large) == (k, k)  
(2) length of (small, large) == (k, k + 1)  
After adding the number, total (n + 1) numbers, they will become:  
(1) length of (small, large) == (k, k + 1)  
(2) length of (small, large) == (k + 1, k + 1)  
Here we take the first scenario for example, we know the large will gain one more item and small will remain the same size, but we cannot just push the item into large. What we should do is we push the new number into small and pop the maximum item from small then push it into large (all the pop and push here are heappop and heappush). By doing this kind of operations for the two scenarios we can keep our invariant.  
Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided us a function "heappushpop" which saves some time by combine two into one. The document says:  
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().  
Alltogether, the add operation is O(logn), The findMedian operation is O(1).  
Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".  

```python
from heapq import *
class MedianFinder:
    def __init__(self):
        self.maxheap = []  # the maxheaper half of the list, max heap (invert min-heap)
        self.minheap = []  # the minheapr half of the list, min heap

    def addNum(self, num):
        if len(self.maxheap) == len(self.minheap):
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
        else:
            heappush(self.maxheap, -heappushpop(self.minheap, num))

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return float(self.minheap[0] - self.maxheap[0]) / 2.0
        else:
            return float(self.minheap[0])
```
# [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)


## Description

<!-- description:start -->

<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p><strong>Clarification:</strong> The input/output format is the same as <a href="https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A" target="_blank">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0297.Serialize%20and%20Deserialize%20Binary%20Tree/images/serdeser.jpg" style="width: 442px; height: 324px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,null,4,5]
<strong>Output:</strong> [1,2,3,null,null,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

```python
class Codec:
   def __init__(self):
       self.splitter = ','
       self.null = 'null'
   def serialize(self, root):
       res = []
       if not root:
           return ''
       q = deque([root])
       while q:
           top = q.popleft()
           if top:
               res.append(str(top.val))
               q.append(top.left)
               q.append(top.right)
           else:
               res.append(self.null)
       return self.splitter.join(res)

    def deserialize(self, data):
       if not data:
           return None
       s_data = data.split(self.splitter)
       if not s_data:
           return None
       root = TreeNode(s_data[0])
       q = deque([root])
       i = 1
       while i < len(s_data) and q:
           top = q.popleft()
           if s_data[i] != self.null:
               left = TreeNode(s_data[i])
               top.left = left
               q.append(left)
           i += 1
           if s_data[i] != self.null:
               right = TreeNode(s_data[i])
               top.right = right
               q.append(right)
           i += 1
       return root
```

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charMap = {}
        left = 0
        for right, char in enumerate(s):
            if char not in charMap or charMap[char] < left:
               maxLength = max(maxLength, right - left + 1)
            else:
               left = charMap[char] + 1
            charMap[char] = right
        return maxLength
```
# [31. Next Permutation](https://leetcode.com/problems/next-permutation)


## Description

<!-- description:start -->

<p>A <strong>permutation</strong> of an array of integers is an arrangement of its members into a sequence or linear order.</p>

<ul>
	<li>For example, for <code>arr = [1,2,3]</code>, the following are all the permutations of <code>arr</code>: <code>[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]</code>.</li>
</ul>

<p>The <strong>next permutation</strong> of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the <strong>next permutation</strong> of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).</p>

<ul>
	<li>For example, the next permutation of <code>arr = [1,2,3]</code> is <code>[1,3,2]</code>.</li>
	<li>Similarly, the next permutation of <code>arr = [2,3,1]</code> is <code>[3,1,2]</code>.</li>
	<li>While the next permutation of <code>arr = [3,2,1]</code> is <code>[1,2,3]</code> because <code>[3,2,1]</code> does not have a lexicographical larger rearrangement.</li>
</ul>

<p>Given an array of integers <code>nums</code>, <em>find the next permutation of</em> <code>nums</code>.</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a></strong> and use only constant extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,5]
<strong>Output:</strong> [1,5,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


### Solution

According to Wikipedia, a man named Narayana Pandita presented the following simple algorithm to solve this problem in the 14th century.  
Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.  
Find the largest index l > k such that nums[k] < nums[l].  
Swap nums[k] and nums[l].  
Reverse the sub-array nums[k + 1:].  


```python
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:  # nums are in descending order
            nums.reverse()
            return
        k = i - 1  # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

```
# [311. Sparse Matrix Multiplication 🔒](https://leetcode.com/problems/sparse-matrix-multiplication)


## Description

<!-- description:start -->

<p>Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> <code>mat1</code> of size <code>m x k</code> and <code>mat2</code> of size <code>k x n</code>, return the result of <code>mat1 x mat2</code>. You may assume that multiplication is always possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0311.Sparse%20Matrix%20Multiplication/images/mult-grid.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> [[7,0,0],[-7,0,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat1 = [[0]], mat2 = [[0]]
<strong>Output:</strong> [[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat1.length</code></li>
	<li><code>k == mat1[i].length == mat2.length</code></li>
	<li><code>n == mat2[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>-100 &lt;= mat1[i][j], mat2[i][j] &lt;= 100</code></li>
</ul>

### Solution 1: Direct Multiplication
We can directly calculate each element in the result matrix according to the definition of matrix multiplication.  
The time complexity isO(m*n*k), and the space complexity is O(m*n). Where and are the number of rows of matrix and the number of columns of matrix respectively, and is the number of columns of matrix or the number of rows of matrix .  

```python
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2)
        l = len(mat2[0])
        ans = [[0] * l for _ in range(m)]
        for i in range(m):
         for j in range(l):
           for k in range(n):
             ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans 

```
### Solution 2: Preprocessing with hashmaps

```python
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
       def f(mat: List[List[int]]) -> List[List[int]]:
           g = [[] for _ in range(len(mat))]
           for i, row in enumerate(mat):
               for j, x in enumerate(row):
                   if x:
                       g[i].append((j, x))
           return g
       g1 = f(mat1)
       g2 = f(mat2)
       m, n = len(mat1), len(mat2[0])
       ans = [[0] * n for _ in range(m)]
       for i in range(m):
           for k, x in g1[i]:
               for j, y in g2[k]:
                   ans[i][j] += x * y
       return ans
```
# [323. Number of Connected Components in an Undirected Graph 🔒](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph)


## Description

<!-- description:start -->

<p>You have a graph of <code>n</code> nodes. You are given an integer <code>n</code> and an array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.</p>

<p>Return <em>the number of connected components in the graph</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0323.Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph/images/conn1-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[3,4]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0323.Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph/images/conn2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>

```python
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
```

# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)


## Description

<!-- description:start -->

<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values).</p>

<p>Prior to being passed to your function, <code>nums</code> is <strong>possibly rotated</strong> at an unknown pivot index <code>k</code> (<code>1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,5,6,7]</code> might be rotated at pivot index <code>3</code> and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the possible rotation and an integer <code>target</code>, return <em>the index of </em><code>target</code><em> if it is in </em><code>nums</code><em>, or </em><code>-1</code><em> if it is not in </em><code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is an ascending array that is possibly rotated.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```

# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)


## Description

<!-- description:start -->

<p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

```python
class Solution:
   def searchRange(self, nums: List[int], target: int) -> List[int]:
       res = [-1,-1]
       if not nums:
           return res
       l, h = 0, len(nums)-1
       while l < h:
           mid = (l + h)//2
           if nums[mid] >= target:
               h = mid
           else:
               l = mid + 1
       if nums[l] != target:
           return res
       res[0] = l
       h = len(nums)
       while l < h:
           mid = (l + h)//2
           if nums[mid] > target:
               h = mid
           else:
               l = mid + 1
       res[1] = l-1
       return res
```

# [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator)


## Description

<!-- description:start -->

<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.</p>

<p>Implement the <code>NestedIterator</code> class:</p>

<ul>
	<li><code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> Initializes the iterator with the nested list <code>nestedList</code>.</li>
	<li><code>int next()</code> Returns the next integer in the nested list.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there are still some integers in the nested list and <code>false</code> otherwise.</li>
</ul>

<p>Your code will be tested with the following pseudocode:</p>

<pre>
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
</pre>

<p>If <code>res</code> matches the expected flattened list, then your code will be judged as correct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> [1,1,2,1,1]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> [1,4,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 500</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.</li>
</ul>

### Solution where you flatten the entire nested list in the constructor(Inefficient)
```python
def flatten(nested):
   res = []
   for e in nested:
       if e.isInteger():
           res.append(e.getInteger())
       else:
           res.extend(flatten(e.getList()))
   return res
class NestedIterator:
   def __init__(self, nestedList: [NestedInteger]):
       self.nums = flatten(nestedList)
       self.index = 0
   def next(self) -> int:
       if self.hasNext():
           self.index += 1
           return self.nums[self.index -1]
  
   def hasNext(self) -> bool:
        return self.index < len(self.nums)
```


### Solution where you keep flatenning the list when needed(when next is called)
More efficient solution
```python
class NestedIterator(object):
   def __init__(self, nestedList):
       # Stores the list in reverse order
       self.stack = nestedList[::-1]
      
   def next(self):
       return self.stack.pop().getInteger()
      
   def hasNext(self):
       while self.stack:
           top = self.stack[-1]
           if top.isInteger():
               return True
           self.stack = self.stack[:-1] + top.getList()[::-1]
       return False
```

# [343. Integer Break](https://leetcode.com/problems/integer-break)


## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        return dp[-1]
```

# [346. Moving Average from Data Stream 🔒](https://leetcode.com/problems/moving-average-from-data-stream)

[中文文档](/solution/0300-0399/0346.Moving%20Average%20from%20Data%20Stream/README.md)

## Description

<!-- description:start -->

<p>Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.</p>

<p>Implement the&nbsp;<code>MovingAverage</code> class:</p>

<ul>
	<li><code>MovingAverage(int size)</code> Initializes&nbsp;the object with the size of the window <code>size</code>.</li>
	<li><code>double next(int val)</code> Returns the moving average of the last <code>size</code> values of the stream.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MovingAverage&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;]
[[3], [1], [10], [3], [5]]
<strong>Output</strong>
[null, 1.0, 5.5, 4.66667, 6.0]

<strong>Explanation</strong>
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= size &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= val &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>next</code>.</li>
</ul>

```python
​​class MovingAverage:
   def __init__(self, size: int):
       self.arr = [0] * size
       self.s = 0
       self.cnt = 0


   def next(self, val: int) -> float:
       idx = self.cnt % len(self.arr)  # circular array
       self.s += val - self.arr[idx]
       self.arr[idx] = val
       self.cnt += 1
       return self.s / min(self.cnt, len(self.arr))
```
```
35. Search Insert Position
Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
```

```python
class Solution:
   def searchInsert(self, nums: List[int], target: int) -> int:
       left, right = 0, len(nums)
       while left < right:
           mid = (left + right) // 2
           if nums[mid] < target:
               left = mid + 1
           else:
               right = mid
       return left
```
# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku)


## Description

<!-- description:start -->

<p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>

<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
	<li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0036.Valid%20Sudoku/images/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" />
<pre>
<strong>Input:</strong> board = 
[[&quot;5&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;]
,[&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;]
,[&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;]
,[&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;]
,[&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = 
[[&quot;8&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;]
,[&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;]
,[&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;]
,[&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;]
,[&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8&#39;s in the top left 3x3 sub-box, it is invalid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>&#39;.&#39;</code>.</li>
</ul>

```python
class Solution:
    def isValidSudoku(self, board):
        return (
            self.is_row_valid(board)
            and self.is_col_valid(board)
            and self.is_square_valid(board)
        )

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)
```
# [360. Sort Transformed Array 🔒](https://leetcode.com/problems/sort-transformed-array)

[中文文档](/solution/0300-0399/0360.Sort%20Transformed%20Array/README.md)

## Description

<!-- description:start -->

<p>Given a <strong>sorted</strong> integer array <code>nums</code> and three integers <code>a</code>, <code>b</code> and <code>c</code>, apply a quadratic function of the form <code>f(x) = ax<sup>2</sup> + bx + c</code> to each element <code>nums[i]</code> in the array, and return <em>the array in a sorted order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-4,-2,2,4], a = 1, b = 3, c = 5
<strong>Output:</strong> [3,9,15,33]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-4,-2,2,4], a = -1, b = 3, c = 5
<strong>Output:</strong> [-23,-5,1,7]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>-100 &lt;= nums[i], a, b, c &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>ascending</strong> order.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it in <code>O(n)</code> time?</p>


```python
class Solution:
   def sort_transformed_array(
       self, nums: List[int], a: int, b: int, c: int
   ) -> List[int]:
       # Function to calculate the transformed value based on input x
       def quadratic(x):
           return a * x ** 2 + b * x + c
       # length of the input nums list
       n = len(nums)
    
       # Initialize pointers:
       # 'left' to start of array, 'right' to end of array
       # 'index' to either start or end based on sign of a
       left, right = 0, n - 1
       index = 0 if a < 0 else n - 1
    
       # Initialize the result array with zeros
       result = [0] * n
    
       # Iterate through the array until left exceeds right
       while left <= right:
           # Calculate the transformed values for both ends
           left_val = quadratic(nums[left])
           right_val = quadratic(nums[right])
        
           # If 'a' is negative, parabola opens downward.
           # Smaller values are closer to the ends of the array.
           if a < 0:
               if left_val <= right_val:
                   result[index] = left_val
                   left += 1
               else:
                   result[index] = right_val
                   right -= 1
               index += 1
           else:
               # If 'a' is non-negative, parabola opens upward.
               # Larger values are closer to the ends of the array.
               if left_val >= right_val:
                   result[index] = left_val
                   left += 1
               else:
                   result[index] = right_val
                   right -= 1
               index -= 1
    
       # Return the sorted transformed array
       return result
```
# [361. Bomb Enemy 🔒](https://leetcode.com/problems/bomb-enemy)


## Description

<!-- description:start -->

<p>Given an <code>m x n</code> matrix <code>grid</code> where each cell is either a wall <code>&#39;W&#39;</code>, an enemy <code>&#39;E&#39;</code> or empty <code>&#39;0&#39;</code>, return <em>the maximum enemies you can kill using one bomb</em>. You can only place the bomb in an empty cell.</p>

<p>The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0361.Bomb%20Enemy/images/bomb1-grid.jpg" style="width: 600px; height: 187px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;0&quot;,&quot;E&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;E&quot;,&quot;0&quot;,&quot;W&quot;,&quot;E&quot;],[&quot;0&quot;,&quot;E&quot;,&quot;0&quot;,&quot;0&quot;]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0361.Bomb%20Enemy/images/bomb2-grid.jpg" style="width: 500px; height: 194px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;W&quot;,&quot;W&quot;,&quot;W&quot;],[&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;E&quot;,&quot;E&quot;,&quot;E&quot;]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;W&#39;</code>, <code>&#39;E&#39;</code>, or <code>&#39;0&#39;</code>.</li>
</ul>

```python
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize a grid to keep track of the kill count
        kill_count = [[0] * cols for _ in range(rows)]
        # Traverse the grid row-wise from left to right and right to left
        for i in range(rows):
            row_hits = 0  # Counter for enemies in the current row
            # Left to right traversal
            for j in range(cols):
                if grid[i][j] == "W":  # Reset counter when a wall is found
                    row_hits = 0
                elif grid[i][j] == "E":  # Increment counter if an enemy is found
                    row_hits += 1
                kill_count[i][j] += row_hits  # Accumulate hits for the current cell

            # Right to left traversal
            row_hits = 0  # Reset counter for the reverse traversal
            for j in range(cols - 1, -1, -1):
                if grid[i][j] == "W":
                    row_hits = 0
                elif grid[i][j] == "E":
                    row_hits += 1
                kill_count[i][j] += row_hits  # Accumulate hits for the current cell

        # Traverse the grid column-wise from top to bottom and bottom to top
        for j in range(cols):
            col_hits = 0  # Counter for enemies in the current column
            # Top to bottom traversal
            for i in range(rows):
                if grid[i][j] == "W":  # Reset counter when a wall is found
                    col_hits = 0
                elif grid[i][j] == "E":  # Increment counter if an enemy is found
                    col_hits += 1
                kill_count[i][j] += col_hits  # Accumulate hits for the current cell

            # Bottom to top traversal
            col_hits = 0  # Reset counter for the reverse traversal
            for i in range(rows - 1, -1, -1):
                if grid[i][j] == "W":
                    col_hits = 0
                elif grid[i][j] == "E":
                    col_hits += 1
                kill_count[i][j] += col_hits  # Accumulate hits for the current cell
        # Calculate the max kills possible by placing a bomb in an empty cell ('0')
        max_kills = max(
            [
                kill_count[i][j]
                for i in range(rows)
                for j in range(cols)
                if grid[i][j] == "0"
            ],
            default=0,  # Fallback value to use if no '0' cells are found
        )
        return max_kills  # Return the maximum number of kills
```
# [364. Nested List Weight Sum II 🔒](https://leetcode.com/problems/nested-list-weight-sum-ii)

[中文文档](/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/README.md)

## Description

<!-- description:start -->

<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>The <strong>depth</strong> of an integer is the number of lists that it is inside of. For example, the nested list <code>[1,[2,2],[[3],2],1]</code> has each integer&#39;s value set to its <strong>depth</strong>. Let <code>maxDepth</code> be the <strong>maximum depth</strong> of any integer.</p>

<p>The <strong>weight</strong> of an integer is <code>maxDepth - (the depth of the integer) + 1</code>.</p>

<p>Return <em>the sum of each integer in </em><code>nestedList</code><em> multiplied by its <strong>weight</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/images/nestedlistweightsumiiex1.png" style="width: 426px; height: 181px;" />
<pre>
<strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Four 1&#39;s with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/images/nestedlistweightsumiiex2.png" style="width: 349px; height: 192px;" />
<pre>
<strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 50</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-100, 100]</code>.</li>
	<li>The maximum <strong>depth</strong> of any integer is less than or equal to <code>50</code>.</li>
	<li>There are no empty lists.</li>
</ul>

### 1, two passes
Straightforward solution is 2 passes  
1st pass to depth first  
then calculate  

```python
class Solution:
   def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
       def max_depth(nestedList):
           depth = 1
           for item in nestedList:
               if item.isInteger():
                   continue
               depth = max(depth, max_depth(item.getList()) + 1)
           return depth
       def dfs(nestedList, max_depth):
           depth_sum = 0
           for item in nestedList:
               if item.isInteger():
                   depth_sum += item.getInteger() * max_depth
               else:
                   depth_sum += dfs(item.getList(), max_depth - 1)
           return depth_sum
       depth = max_depth(nestedList)
       return dfs(nestedList, depth)
```
 - 2, one passes  
The solution uses an iterative approach to traverse the nested list level by level, starting from the outermost level (level 1) and moving inward. It keeps track of two sums:  
unweighted: The cumulative sum of all integers encountered so far, regardless of their depth.  
weighted: The weighted sum, which is recalculated at each level to reflect the increasing weight of previously encountered integers as the traversal goes deeper.  
Initialization: If the input list is empty, the function immediately returns 0. This check is technically redundant due to Python’s treatment of empty lists as falsy values, which would naturally terminate the loop.  


Iterative Traversal: The solution iteratively traverses the nested list. At each iteration, it processes one level of the list.  


Accumulating unweighted Sum: For each element a in the current level (nestedList), if a is an integer, its value is added to unweighted. This sum accumulates values from all levels processed so far but does not account for their depth.  


Preparing for Next Level: If a is not an integer but another nested list, the elements of this list are added to next_level, preparing them for processing in the next iteration.  


Updating weighted Sum: After processing each level, weighted is increased by unweighted. This step is crucial because it effectively adds the unweighted sum repeatedly, once for each level of depth, thereby inversely weighting the depth. Deeper integers have already contributed to unweighted in earlier iterations, so they are counted multiple times in weighted, reflecting their deeper level.  


Moving to the Next Level: The list to be processed in the next iteration is updated to next_level, moving the traversal one level deeper into the nested list structure.  


Returning the Result: Once all levels have been processed and there are no more elements to traverse, the weighted sum represents the inverse depth sum of the original nested list, and it is returned as the result.  


Example  
Consider the nested list [[1,1],2,[1,1]]. The inverse depth sum is calculated as follows:  
At the outermost level, the sum of integers is 2 (only the integer 2 is at this level). This value is added to weighted. So weighted=2 and unweighted=2  
At the next level, the sum of integers is 4 (from the four 1s in the nested lists). This sum is added to unweighted making it 6 (once for this level and once from the previous level’s unweighted sum 2).  
The final weighted sum is weighted + unweighted, i.e. 2 + 6 = 8, which is the inverse depth sum of the nested list.  
This approach efficiently calculates the inverse depth sum without needing to explicitly track the depth of each integer, leveraging the iterative re-accumulation of unweighted sums to achieve the correct weighting.  

```python
class Solution_onePass: # iterative
   def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
       if not nestedList:
       # can remove this check, an empty list in Python is considered "falsy"
       # and the loop will exit when it reaches the end of the list
           return 0
       # weighted is like previous round result
       unweighted = weighted = 0
       while nestedList:
           next_level = []
           for a in nestedList:
               if a.isInteger():
                   unweighted += a.getInteger()
               else:
                   next_level.extend(a.getList())
           weighted += unweighted
           nestedList = next_level
       return weighted
```



# [366. Find Leaves of Binary Tree 🔒](https://leetcode.com/problems/find-leaves-of-binary-tree)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, collect a tree&#39;s nodes as if you were doing this:</p>

<ul>
	<li>Collect all the leaf nodes.</li>
	<li>Remove all the leaf&nbsp;nodes.</li>
	<li>Repeat until the tree is empty.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0366.Find%20Leaves%20of%20Binary%20Tree/images/remleaves-tree.jpg" style="width: 500px; height: 215px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

```python
class Solution:
   def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
       d = defaultdict(list)
       def dfs(u):
           if u == None:
               return 0
           leftLevel = dfs(u.left)
           rightLevel = dfs(u.right)
           currentLevel = (
               max(leftLevel, rightLevel) + 1
           )  # calculate level of current node
           d[currentLevel].append(u.val)
           return currentLevel
       dfs(root)
       return list(d.values())
```

# [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)


## Description

<!-- description:start -->

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> sorted in <strong>non-decreasing&nbsp;order</strong> and an integer <code>k</code>.</p>

<p>Define a pair <code>(u, v)</code> which consists of one element from the first array and one element from the second array.</p>

<p>Return <em>the</em> <code>k</code> <em>pairs</em> <code>(u<sub>1</sub>, v<sub>1</sub>), (u<sub>2</sub>, v<sub>2</sub>), ..., (u<sub>k</sub>, v<sub>k</sub>)</code> <em>with the smallest sums</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,7,11], nums2 = [2,4,6], k = 3
<strong>Output:</strong> [[1,2],[1,4],[1,6]]
<strong>Explanation:</strong> The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,1,2], nums2 = [1,2,3], k = 2
<strong>Output:</strong> [[1,1],[1,1]]
<strong>Explanation:</strong> The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums1</code> and <code>nums2</code> both are sorted in <strong>non-decreasing order</strong>.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>k &lt;=&nbsp;nums1.length *&nbsp;nums2.length</code></li>
</ul>


### Solution
Note that the approach to increment index by comparing does not work here as  
it may miss some cases. Keeping track of visited is the rght way.

```python
class Solution:
   def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
       q = queue.PriorityQueue()
       q.put((a[0] + b[0], 0, 0))
       res = []
       visited = set([(0, 0)])
       for _ in range(k):
           top, i, j = q.get()
           res.append([a[i], b[j]])
           if i + 1 < len(a) and ((i + 1), j) not in visited:
               visited.add(((i + 1), j))
               q.put((b[j] + a[i + 1], i + 1, j))
           if j + 1 < len(b) and (i, (j + 1)) not in visited:
               visited.add((i, (j + 1)))
               q.put((a[i] + b[j + 1], i, j + 1))
       return res
```
# [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1)


## Description

<!-- description:start -->

<p>Implement the <code>RandomizedSet</code> class:</p>

<ul>
	<li><code>RandomizedSet()</code> Initializes the <code>RandomizedSet</code> object.</li>
	<li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if the item was not present, <code>false</code> otherwise.</li>
	<li><code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if the item was present, <code>false</code> otherwise.</li>
	<li><code>int getRandom()</code> Returns a random element from the current set of elements (it&#39;s guaranteed that at least one element exists when this method is called). Each element must have the <b>same probability</b> of being returned.</li>
</ul>

<p>You must implement the functions of the class such that each function works in&nbsp;<strong>average</strong>&nbsp;<code>O(1)</code>&nbsp;time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RandomizedSet&quot;, &quot;insert&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;]
[[], [1], [2], [2], [], [1], [2], []]
<strong>Output</strong>
[null, true, false, true, 2, true, false, 2]

<strong>Explanation</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>2 *&nbsp;</code><code>10<sup>5</sup></code> calls will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li>
	<li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li>
</ul>

```python
import random
class RandomizedSet:
   def __init__(self):
       self.arr = []
       self.m = {}
       self.index = -1
      
   def insert(self, val: int) -> bool:
       if val in self.m:
           return False
       self.arr.append(val)
       self.index += 1
       self.m[val] = self.index
       return True
   def remove(self, val: int) -> bool:
       if not val in self.m:
           return False
       val_index = self.m[val]
       self.arr[val_index] = self.arr[-1]
       self.m[self.arr[val_index]] = val_index
       self.arr.pop()
       self.m.pop(val)
       self.index -= 1
       return True
      
   def getRandom(self) -> int:
       return self.arr[random.randint(0, self.index)]
```


# [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed)


## Description

<!-- description:start -->

<p><code>RandomizedCollection</code> is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.</p>

<p>Implement the <code>RandomizedCollection</code> class:</p>

<ul>
	<li><code>RandomizedCollection()</code> Initializes the empty <code>RandomizedCollection</code> object.</li>
	<li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the multiset, even if the item is already present. Returns <code>true</code> if the item is not present, <code>false</code> otherwise.</li>
	<li><code>bool remove(int val)</code> Removes an item <code>val</code> from the multiset if present. Returns <code>true</code> if the item is present, <code>false</code> otherwise. Note that if <code>val</code> has multiple occurrences in the multiset, we only remove one of them.</li>
	<li><code>int getRandom()</code> Returns a random element from the current multiset of elements. The probability of each element being returned is <strong>linearly related</strong> to the number of the same values the multiset contains.</li>
</ul>

<p>You must implement the functions of the class such that each function works on <strong>average</strong> <code>O(1)</code> time complexity.</p>

<p><strong>Note:</strong> The test cases are generated such that <code>getRandom</code> will only be called if there is <strong>at least one</strong> item in the <code>RandomizedCollection</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RandomizedCollection&quot;, &quot;insert&quot;, &quot;insert&quot;, &quot;insert&quot;, &quot;getRandom&quot;, &quot;remove&quot;, &quot;getRandom&quot;]
[[], [1], [1], [2], [], [1], []]
<strong>Output</strong>
[null, true, false, true, 2, true, 1]

<strong>Explanation</strong>
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return true since the collection does not contain 1.
                                  // Inserts 1 into the collection.
randomizedCollection.insert(1);   // return false since the collection contains 1.
                                  // Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2);   // return true since the collection does not contain 2.
                                  // Inserts 2 into the collection. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should:
                                  // - return 1 with probability 2/3, or
                                  // - return 2 with probability 1/3.
randomizedCollection.remove(1);   // return true since the collection contains 1.
                                  // Removes 1 from the collection. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li>
	<li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li>
</ul>


```python
import random


class RandomizedCollection(object):

    def __init__(self):
        self.vals = []
        self.idxs = collections.defaultdict(set)
        self.index = -1

    def insert(self, val):
        self.index += 1
        self.vals.append(val)
        self.idxs[val].add(self.index)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if val not in self.idxs:
            return False
        # pay attention here. pop() works on set. but it does not
        # remove the last element. Instead it removes a random element
        # from the set
        out, ins = self.idxs[val].pop(), self.vals[-1]
        self.vals[out] = ins
        self.idxs[ins].add(out)
        self.idxs[ins].discard(self.index)
        self.index -= 1
        self.vals.pop()
        if not self.idxs[val]:
            self.idxs.pop(val)
        return True

    def getRandom(self):
        return random.choice(self.vals)
```

# [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array)

[中文文档](/solution/0300-0399/0384.Shuffle%20an%20Array/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, design an algorithm to randomly shuffle the array. All permutations of the array should be <strong>equally likely</strong> as a result of the shuffling.</p>

<p>Implement the <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
	<li><code>int[] reset()</code> Resets the array to its original configuration and returns it.</li>
	<li><code>int[] shuffle()</code> Returns a random shuffling of the array.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Solution&quot;, &quot;shuffle&quot;, &quot;reset&quot;, &quot;shuffle&quot;]
[[[1, 2, 3]], [], [], []]
<strong>Output</strong>
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

<strong>Explanation</strong>
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li>All the elements of <code>nums</code> are <strong>unique</strong>.</li>
	<li>At most <code>10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>reset</code> and <code>shuffle</code>.</li>
</ul>


```python
class Solution:


   def __init__(self, nums: List[int]):
       self.nums = nums
       self.orig = list(nums)


   def reset(self) -> List[int]:
       return self.orig


   def shuffle(self) -> List[int]:
       for i in range(len(self.nums) - 1, -1, -1):
           r = random.randint(0, i)
           self.nums[r], self.nums[i] = self.nums[i], self.nums[r]
       return self.nums
```
# [39. Combination Sum](https://leetcode.com/problems/combination-sum)


## Description

<!-- description:start -->

<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the <span data-keyword="frequency-array">frequency</span> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return candidates
        result = []
        def helper(index, current, target):
            if target == 0:
                result.append(current.copy())
                return
            if target < 0 or index >= len(candidates):
                return
            helper(index, current + [candidates[index]], target - candidates[index])
            helper(index + 1, current, target)
        helper(0, [], target)
        return result
```

### Time Complexity
The time complexity of the given code primarily depends on the number of potential combinations that can be 
formed with the given candidates array that sum up to the target. Considering the array has a length n and the 
recursion involves iterating over candidates and including/excluding them, we get a recursion tree with a depth 
that could potentially go up to target/min(candidates), if we keep using the smallest element. This leads to 
an exponential number of possibilities. Thus, the time complexity of the algorithm is O(2^n) in the worst case, 
when the recursion tree is fully developed. However, since we often return early when s < candidates[i], this 
is an upper bound.

### Space Complexity
The space complexity of the algorithm is also important to consider. It is mainly used by recursion stack space and the 
space to store combinations. The maximum depth of the recursion could be target/min(candidates) which would at most be 
O(target) if 1 is in the candidates. However, the space required for the list t, which is used to store the current 
combination, is also dependent on the target and could at most have target elements when 1 is in the candidates. The 
space for ans depends on the number of combinations found. Since it's hard to give an exact number without knowing the 
specifics of candidates and target, we consider it for the upper bound space complexity. Thus, as the list ans grows with 
each combination found, in the worst case, it could store a combination for every possible subset of candidates, leading 
to a space complexity of O(2^n * target), where 2^n is the number of combinations and target is the maximum size of any
combination.
However, if we look at the auxiliary space excluding the space taken by the output (which is the space ans takes), 
then the space complexity is O(target) due to the depth of the recursive call stack and the temporary list t.
# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)


## Description

<!-- description:start -->

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>

### Approach 1: Merge and Sort
Create a new array with a size equal to the total number of elements in both input arrays.
Insert elements from both input arrays into the new array.
Sort the new array.
Find and return the median of the sorted array.
Time Complexity
In the worst case TC is O((n + m) * log(n + m)).
Space Complexity
O(n + m), where ‘n’ and ‘m’ are the sizes of the arrays.

### Approach 2: Two-Pointer Method
Initialize two pointers, i and j, both initially set to 0.
Move the pointer that corresponds to the smaller value forward at each step.
Continue moving the pointers until you have processed half of the total number of elements.
Calculate and return the median based on the values pointed to by i and j.
Time Complexity
O(n + m), where ‘n’ & ‘m’ are the sizes of the two arrays.
Space Complexity
O(1).
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        m1 = m2 = 0
        # Find median.
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0
```

### Approach 3: Binary Search
Use binary search to partition the smaller of the two input arrays into two parts.
Find the partition of the larger array such that the sum of elements on the left side of the partition in both arrays is half of the total elements.
Check if this partition is valid by verifying if the largest number on the left side is smaller than the smallest number on the right side.
If the partition is valid, calculate and return the median.
Time Complexity
O(logm/logn)
Space Complexity
O(1)
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        left = (n1 + n2 + 1) // 2  # Calculate the left partition size
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2  # Calculate mid index for nums1
            mid2 = left - mid1  # Calculate mid index for nums2

            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")

            # Determine values of l1, l2, r1, and r2
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1

        return 0  # If the code reaches here, the input arrays were not sorted.
```
# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

[中文文档](/solution/0000-0099/0040.Combination%20Sum%20II/README.md)

## Description

<!-- description:start -->

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return candidates
        result = []
        candidates.sort()
        def helper(index, current, target):
            if target == 0:
                result.append(current.copy())
                return
            if target < 0 or index >= len(candidates):
                return
            helper(index + 1, current + [candidates[index]], target - candidates[index])
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            helper(index + 1, current, target)
        helper(0, [], target)
        return result
```

# [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)


## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <code>true</code> <em>if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

```python
# Using the 0/1 Knapsack concept.
# Pay attention the inner loop is decreasing in order to avoid repetition.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for n in nums:
            sum += n
        if sum % 2 == 1:
            return False
        half = sum // 2
        d = [False] * (half + 1)
        d[0] = True
        for i in range(len(nums)):
            for j in range(half, nums[i] - 1, -1):
                d[j] = d[j - nums[i]] | d[j]
        return d[half]
```


# [430. Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list)


## Description

<!-- description:start -->

<p>You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional <strong>child pointer</strong>. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a <strong>multilevel data structure</strong> as shown in the example below.</p>

<p>Given the <code>head</code> of the first level of the list, <strong>flatten</strong> the list so that all the nodes appear in a single-level, doubly linked list. Let <code>curr</code> be a node with a child list. The nodes in the child list should appear <strong>after</strong> <code>curr</code> and <strong>before</strong> <code>curr.next</code> in the flattened list.</p>

<p>Return <em>the </em><code>head</code><em> of the flattened list. The nodes in the list must have <strong>all</strong> of their child pointers set to </em><code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List/images/flatten11.jpg" style="width: 700px; height: 339px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
<strong>Output:</strong> [1,2,3,7,8,11,12,9,10,4,5,6]
<strong>Explanation:</strong> The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List/images/flatten12.jpg" style="width: 1000px; height: 69px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List/images/flatten2.1jpg" style="width: 200px; height: 200px;" />
<pre>
<strong>Input:</strong> head = [1,2,null,3]
<strong>Output:</strong> [1,3,2]
<strong>Explanation:</strong> The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List/images/list.jpg" style="width: 300px; height: 87px;" />
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
<strong>Explanation:</strong> There could be empty list in the input.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of Nodes will not exceed <code>1000</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>How the multilevel linked list is represented in test cases:</strong></p>

<p>We use the multilevel linked list from <strong>Example 1</strong> above:</p>

<pre>
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL</pre>

<p>The serialization of each level is as follows:</p>

<pre>
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
</pre>

<p>To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:</p>

<pre>
[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
</pre>

<p>Merging the serialization of each level and removing trailing nulls we obtain:</p>

<pre>
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
</pre>

### Naive Solution(By me):

```python
class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue
            child_head = self.flatten(curr.child)
            curr.child = None
            if not curr.next:
                curr.next = child_head
                child_head.prev = curr
                return head
            curr_next = curr.next
            curr.next = child_head
            child_head.prev = curr
            curr = child_head
            while curr.next:
                curr = curr.next
            curr.next = curr_next
            curr_next.prev = curr
            curr = curr_next
        return head
```


### Nice Solution:
```python
class Solution:
   def flatten(self, head):
       if not head: return head
       stack, order = [head], []
       while stack:
           last = stack.pop()
           order.append(last)
           if last.next:
               stack.append(last.next)
           if last.child:
               stack.append(last.child)
      
       for i in range(len(order) - 1):
           order[i+1].prev = order[i]
           order[i].next = order[i+1]
           order[i].child = None
          
       return order[0]
```

# [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure)


## Description

<!-- description:start -->

<p>Design a data structure to store the strings&#39; count with the ability to return the strings with minimum and maximum counts.</p>

<p>Implement the <code>AllOne</code> class:</p>

<ul>
	<li><code>AllOne()</code> Initializes the object of the data structure.</li>
	<li><code>inc(String key)</code> Increments the count of the string <code>key</code> by <code>1</code>. If <code>key</code> does not exist in the data structure, insert it with count <code>1</code>.</li>
	<li><code>dec(String key)</code> Decrements the count of the string <code>key</code> by <code>1</code>. If the count of <code>key</code> is <code>0</code> after the decrement, remove it from the data structure. It is guaranteed that <code>key</code> exists in the data structure before the decrement.</li>
	<li><code>getMaxKey()</code> Returns one of the keys with the maximal count. If no element exists, return an empty string <code>&quot;&quot;</code>.</li>
	<li><code>getMinKey()</code> Returns one of the keys with the minimum count. If no element exists, return an empty string <code>&quot;&quot;</code>.</li>
</ul>

<p><strong>Note</strong> that each function must run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;AllOne&quot;, &quot;inc&quot;, &quot;inc&quot;, &quot;getMaxKey&quot;, &quot;getMinKey&quot;, &quot;inc&quot;, &quot;getMaxKey&quot;, &quot;getMinKey&quot;]
[[], [&quot;hello&quot;], [&quot;hello&quot;], [], [], [&quot;leet&quot;], [], []]
<strong>Output</strong>
[null, null, null, &quot;hello&quot;, &quot;hello&quot;, null, &quot;hello&quot;, &quot;leet&quot;]

<strong>Explanation</strong>
AllOne allOne = new AllOne();
allOne.inc(&quot;hello&quot;);
allOne.inc(&quot;hello&quot;);
allOne.getMaxKey(); // return &quot;hello&quot;
allOne.getMinKey(); // return &quot;hello&quot;
allOne.inc(&quot;leet&quot;);
allOne.getMaxKey(); // return &quot;hello&quot;
allOne.getMinKey(); // return &quot;leet&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= key.length &lt;= 10</code></li>
	<li><code>key</code> consists of lowercase English letters.</li>
	<li>It is guaranteed that for each call to <code>dec</code>, <code>key</code> is existing in the data structure.</li>
	<li>At most <code>5 * 10<sup>4</sup></code>&nbsp;calls will be made to <code>inc</code>, <code>dec</code>, <code>getMaxKey</code>, and <code>getMinKey</code>.</li>
</ul>


```python
# DLL Node definition
class Node(object):
    def __init__(self):
        self.keys = set()
        self.prev = self.next = None

# Doubly Linked List class.
# Note to add sentinel head and tail to avoid adding null checks for append
# and delete operations.
class Dll(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def append(self, node, prev):
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        node.prev = prev
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Implementation of O(1) data structure
class AllOne:
    def __init__(self):
        self.freq_map = {}
        self.key_map = defaultdict(int)
        self.dll = Dll()
    
    def _remove_key_from_node(self, cf, key):
        if cf == 0:
            return
        node = self.freq_map[cf]
        node.keys.remove(key)
        # if this is the only key in this Node, remove node
        if not len(node.keys):
            self.dll.remove(node)
            self.freq_map.pop(cf)
    
    def inc(self, key: str) -> None:
        cf = self.key_map[key]
        nf = cf + 1
        self.key_map[key] = nf
        if nf not in self.freq_map:
            self.freq_map[nf] = Node()
            prev = self.freq_map[cf] if cf > 0 else self.dll.head
            self.dll.append(self.freq_map[nf], prev)
        self.freq_map[nf].keys.add(key)
        self._remove_key_from_node(cf, key)
    
    def dec(self, key: str) -> None:
        self.key_map[key] -= 1
        nf, cf = self.key_map[key], self.key_map[key] + 1
        if nf == 0:
            self.key_map.pop(key)
        else:
            if nf not in self.freq_map:
                self.freq_map[nf] = Node()
                self.dll.append(self.freq_map[nf], self.freq_map[cf].prev)
            self.freq_map[nf].keys.add(key)
        self._remove_key_from_node(cf, key)
    def getMaxKey(self) -> str:
        keys = self.dll.tail.prev.keys
        if keys:
            return next(iter(keys))
        return ""
    def getMinKey(self) -> str:
        keys = self.dll.head.next.keys
        if keys:
            return next(iter(keys))
        return ""
```
# [46. Permutations](https://leetcode.com/problems/permutations)


## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of distinct integers, return all the possible <span data-keyword="permutation-array">permutations</span>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>


```python
class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]:
       def util(nums):
           if not nums:
               return []
           if len(nums) == 1:
               return [[nums[0]]]
           res = []
           for i in range(len(nums)):
               nums[0], nums[i] = nums[i], nums[0]
               for t in self.permute(nums[1:]):
                   res.append([nums[0]] + t)
           return res
       return util(nums)

```

# [460. LFU Cache](https://leetcode.com/problems/lfu-cache)

[中文文档](/solution/0400-0499/0460.LFU%20Cache/README.md)

## Description

<!-- description:start -->

<p>Design and implement a data structure for a <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache.</p>

<p>Implement the <code>LFUCache</code> class:</p>

<ul>
	<li><code>LFUCache(int capacity)</code> Initializes the object with the <code>capacity</code> of the data structure.</li>
	<li><code>int get(int key)</code> Gets the value of the <code>key</code> if the <code>key</code> exists in the cache. Otherwise, returns <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if present, or inserts the <code>key</code> if not already present. When the cache reaches its <code>capacity</code>, it should invalidate and remove the <strong>least frequently used</strong> key before inserting a new item. For this problem, when there is a <strong>tie</strong> (i.e., two or more keys with the same frequency), the <strong>least recently used</strong> <code>key</code> would be invalidated.</li>
</ul>

<p>To determine the least frequently used key, a <strong>use counter</strong> is maintained for each key in the cache. The key with the smallest <strong>use counter</strong> is the least frequently used key.</p>

<p>When a key is first inserted into the cache, its <strong>use counter</strong> is set to <code>1</code> (due to the <code>put</code> operation). The <strong>use counter</strong> for a key in the cache is incremented either a <code>get</code> or <code>put</code> operation is called on it.</p>

<p>The functions&nbsp;<code data-stringify-type="code">get</code>&nbsp;and&nbsp;<code data-stringify-type="code">put</code>&nbsp;must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LFUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

<strong>Explanation</strong>
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
&nbsp;                // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code>&nbsp;calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>

<p>&nbsp;</p>
<span style="display: none;">&nbsp;</span>

### Solution
What is my data structure?
1. A Doubly linked Node
class Node:
	+ key: int
	+ value: int
	+ freq: int
	+ prev: Node
	+ next: Node
2. A Doubly Linked List
Note: This part could be replaced by OrderedDict, I implemented it by hand for clarity
class DLinkedList:
	- sentinel: Node
	+ size: int
	+ append(node: Node) -> None
	+ pop(node: Node) -> Node
3. Our LFUCache
class LFUCache:
	- node: dict[key: int, node: Node]
	- freq: dict[freq: int, lst: DlinkedList]
	- minfreq: int
	+ get(key: int) -> int
	+ put(key: int, value: int) -> None
Visualization
<img alt="" src="https://github.com/code2practice/leetcode/blob/main/Solutions/lfu_image.png" />

Explanation \
Each key is mapping to the corresponding node (self._node), where we can retrieve the node in O(1) time.  \
Each frequency freq is mapped to a Doubly Linked List (self._freq), where all nodes in the DLinkedList have the same frequency, freq. Moreover, each node will be always inserted in the head (indicating most recently used).  
A minimum frequency self._minfreq is maintained to keep track of the minimum frequency of across all nodes in this cache, such that the DLinkedList with the min frequency can always be retrieved in O(1) time.  
Here is how the algorithm works  
get(key)  
query the node by calling self._node[key]  
find the frequency by checking node.freq, assigned as f, and query the DLinkedList that this node is in, through calling self._freq[f]  
pop this node  
update node's frequence, append the node to the new DLinkedList with frequency f+1  
if the DLinkedList is empty and self._minfreq == f, update self._minfreq to f+1.  
return node.val  
put(key, value)  
If key is already in cache, do the same thing as get(key), and update node.val as value  
Otherwise:  
if the cache is full, pop the least frequenly used element (*)  
add new node to self._node  
add new node to self._freq[1]  
reset self._minfreq to 1  
(*) The least frequently used element is the tail element in the DLinkedList with frequency self._minfreq  

```python
import collections


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    """An implementation of doubly linked list.

    Two APIs provided:

    append(node): append the node to the head of the linked list.
    pop(node=None): remove the referenced node.
                    If None is given, remove the one from tail, which is the least recently used.

    Both operation, apparently, are in O(1) complexity.
    """

    def __init__(self):
        self._sentinel = Node(None, None)  # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int

        Three things to maintain:

        1. a dict, named as `self._node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.

        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`

        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
           two rules:

           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.

           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)

        """
        self._size = 0
        self._capacity = capacity

        self._node = dict()  # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0

    def _update(self, node):
        """
        This is a helper function that used in the following two cases:

            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.

        The common point of these two cases is that:

            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed ->
               thus the place of this node will change

        The logic of this function is:

            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`

        All of the above opeartions took O(1) time.
        """
        freq = node.freq

        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1

        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key):
        """
        Through checking self._node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.

        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.

        Otherwise, the following logic will be performed

        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1

        (*) How to pop the least frequently used item? Two facts:

        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)

        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...

        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity == 0:
            return

        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1
```
# [47. Permutations II](https://leetcode.com/problems/permutations-ii)


## Description

<!-- description:start -->

<p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def util(nums):
            if not nums:
                return []
            if len(nums) == 1:
                return [[nums[0]]]
            res = []
            i = 0
            while i < len(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                nums[i], nums[0] = nums[0], nums[i]
                for t in self.permuteUnique(nums[1:]):
                    res.append([nums[0]] + t)
                nums[i], nums[0] = nums[0], nums[i]
                i += 1
            return res

        nums.sort()
        return util(nums)
```

# [470. Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7)

[中文文档](/solution/0400-0499/0470.Implement%20Rand10%28%29%20Using%20Rand7%28%29/README.md)

## Description

<!-- description:start -->

<p>Given the <strong>API</strong> <code>rand7()</code> that generates a uniform random integer in the range <code>[1, 7]</code>, write a function <code>rand10()</code> that generates a uniform random integer in the range <code>[1, 10]</code>. You can only call the API <code>rand7()</code>, and you shouldn&#39;t call any other API. Please <strong>do not</strong> use a language&#39;s built-in random API.</p>

<p>Each test case will have one <strong>internal</strong> argument <code>n</code>, the number of times that your implemented function <code>rand10()</code> will be called while testing. Note that this is <strong>not an argument</strong> passed to <code>rand10()</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> [2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [2,8]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> [3,8,10]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>What is the <a href="https://en.wikipedia.org/wiki/Expected_value" target="_blank">expected value</a> for the number of calls to <code>rand7()</code> function?</li>
	<li>Could you minimize the number of calls to <code>rand7()</code>?</li>
</ul>




```python
class Solution:
   def rand10(self):
       curr = 40
       while curr >= 40:
           curr = (rand7() - 1) * 7 + rand7() - 1
       return curr % 10 + 1
```

### Generalised solution for creating randM() using randN()

```python
class Solution:
   def randM(self, N, M):
       """
       :rtype: int
       """
       # acceptable is the desired range which can generate required integer directly
       curr = acceptable = N * N - (N * N) % M
       # if current no is not in the acceptable range, discard it and repeat the process again
       while curr >= acceptable:
           curr = (randN() - 1) * N + randN() - 1
       return curr % M + 1
```
# [489. Robot Room Cleaner 🔒](https://leetcode.com/problems/robot-room-cleaner)

[中文文档](/solution/0400-0499/0489.Robot%20Room%20Cleaner/README.md)

## Description

<!-- description:start -->

<p>You are controlling a robot that is located somewhere in a room. The room is modeled as an <code>m x n</code> binary grid where <code>0</code> represents a wall and <code>1</code> represents an empty slot.</p>

<p>The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API <code>Robot</code>.</p>

<p>You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is <code>90</code> degrees.</p>

<p>When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.</p>

<p>Design an algorithm to clean the entire room using the following APIs:</p>

<pre>
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
</pre>

<p><strong>Note</strong> that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.</p>

<p>&nbsp;</p>

<p><strong>Custom testing:</strong></p>

<p>The input is only given to initialize the room and the robot&#39;s position internally. You must solve this problem &quot;blindfolded&quot;. In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot&#39;s position.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0489.Robot%20Room%20Cleaner/images/lc-grid.jpg" style="width: 500px; height: 314px;" />
<pre>
<strong>Input:</strong> room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
<strong>Output:</strong> Robot cleaned all rooms.
<strong>Explanation:</strong> All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> room = [[1]], row = 0, col = 0
<strong>Output:</strong> Robot cleaned all rooms.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == room.length</code></li>
	<li><code>n == room[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>room[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= row &lt;&nbsp;m</code></li>
	<li><code>0 &lt;= col &lt; n</code></li>
	<li><code>room[row][col] == 1</code></li>
	<li>All the empty cells can be visited from the starting position.</li>
</ul>

```python
class Solution:
   def cleanRoom(self, robot):
       """
       :type robot: Robot
       :rtype: None
       """


       def dfs(i, j, d):
           vis.add((i, j))
           robot.clean()
           for k in range(4):
               nd = (d + k) % 4
               x, y = i + dirs[nd], j + dirs[nd + 1]
               if (x, y) not in vis and robot.move():
                   dfs(x, y, nd)
                   robot.turnRight()
                   robot.turnRight()
                   robot.move()
                   robot.turnRight()
                   robot.turnRight()
               robot.turnRight()


       dirs = (-1, 0, 1, 0, -1)
       vis = set()
       dfs(0, 0, 0)
```

### Time and Space Complexity
The time complexity of the above code is O(4^(N-M)), where N is the total number of cells in the room and M is the number of obstacles. This is because the algorithm has to visit each non-obstacle cell once and at each cell, it makes up to 4 decisions – move in 4 possible directions. The recursion may go up to 4 branches at each level but would not revisit cells that are already visited, summarized by visited set vis.  
The space complexity of the DFS is O(N) for the recursive call stack as well as the space to hold the set of visited cells (in the worst case where there are no obstacles and we can move to every cell). However, in a densely packed room with obstructions, the number of visited states will be less than N.
# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>

```python
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
```

### Using DP
```python
class Solution:
    def longestPalindrome(self, s):
        longest_palindrom = ""
        dp = [[False] * len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        # filling the dp table
        for i in range(len(s) - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:  # if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True
                    # if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence
                        if len(longest_palindrom) < len(s[i : j + 1]):
                            longest_palindrom = s[i : j + 1]

        return longest_palindrom
```
# [50. Pow(x, n)](https://leetcode.com/problems/powx-n)

[中文文档](/solution/0000-0099/0050.Pow%28x%2C%20n%29/README.md)

## Description

<!-- description:start -->

<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2.10000, n = 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
	<li><code>n</code> is an integer.</li>
	<li>Either <code>x</code> is not zero or <code>n &gt; 0</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>

# Recursive(Extra space for stack)
```python
class Solution:
   def myPow(self, x: float, n: int) -> float:
       if n == 0:
           return 1
       half = self.myPow(x, int(n/2))
       power = half * half
       if n % 2 == 1:
           power =  power * x if n > 0 else float(power/x)
       return power
```


# Iterative(No extra space)
```python
class Solution:
   def myPow(self, x, n):
       if n < 0:
           x = 1 / x
           n = -n
       pow = 1
       while n:
           if n & 1:
               pow *= x
           x *= x
           n >>= 1
       return pow
```

# [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>an array of the largest value in each row</em> of the tree <strong>(0-indexed)</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0515.Find%20Largest%20Value%20in%20Each%20Tree%20Row/images/largest_e1.jpg" style="width: 300px; height: 172px;" />
<pre>
<strong>Input:</strong> root = [1,3,2,5,3,null,9]
<strong>Output:</strong> [1,3,9]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> [1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->
```python
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            curr_level_size = len(queue)
            max_val = float('-inf')
            
            for _ in range(curr_level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            
            result.append(max_val)
        
        return result
```

# [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, find <em>the longest palindromic <strong>subsequence</strong>&#39;s length in</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbab&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bbbb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bb&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

### Solution 1: Top down DP
Let dp(l, r) denote the length of the longest palindromic subsequence of s[l..r].  
There are 2 options:  
If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2  
Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).  
Then dp(0, n-1) is our result.  

Complexity  
Time: O(N^2), where N <= 1000 is length of string s.  
Space: O(N^2)  
```python
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
```

### Solution 2: Bottom up DP
Let dp[l][r] denote the length of the longest palindromic subsequence of s[l..r].  
There are 2 options:  
If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2  
Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).  
Then dp[0][n-1] is our result.  
```python
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
```

# [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum)


## Description

<!-- description:start -->

<p>Given an integer array nums and an integer k, return <code>true</code> <em>if </em><code>nums</code><em> has a <strong>good subarray</strong> or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>good subarray</strong> is a subarray where:</p>

<ul>
	<li>its length is <strong>at least two</strong>, and</li>
	<li>the sum of the elements of the subarray is a multiple of <code>k</code>.</li>
</ul>

<p><strong>Note</strong> that:</p>

<ul>
	<li>A <strong>subarray</strong> is a contiguous part of the array.</li>
	<li>An integer <code>x</code> is a multiple of <code>k</code> if there exists an integer <code>n</code> such that <code>x = n * k</code>. <code>0</code> is <strong>always</strong> a multiple of <code>k</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [23,<u>2,4</u>,6,7], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<u>23,2,6,4,7</u>], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [23,2,6,4,7], k = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

### Solution 1: Prefix Sum + Hash Table

According to the problem description, if there exist two positions $i$ and $j$ ($j < i$) where the remainders of the prefix sums modulo $k$ are the same, then the sum of the subarray $\textit{nums}[j+1..i]$ is a multiple of $k$.

Therefore, we can use a hash table to store the first occurrence of each remainder of the prefix sum modulo $k$. Initially, we store a key-value pair $(0, -1)$ in the hash table, indicating that the remainder $0$ of the prefix sum $0$ appears at position $-1$.

As we iterate through the array, we calculate the current prefix sum's remainder modulo $k$. If the current prefix sum's remainder modulo $k$ has not appeared in the hash table, we store the current prefix sum's remainder modulo $k$ and its corresponding position in the hash table. Otherwise, if the current prefix sum's remainder modulo $k$ has already appeared in the hash table at position $j$, then we have found a subarray $\textit{nums}[j+1..i]$ that meets the conditions, and thus return $\textit{True}$.

After completing the iteration, if no subarray meeting the conditions is found, we return $\textit{False}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkSubarraySum(self, nums, k):
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False
```
# [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement)


## Description

<!-- description:start -->

<p>Suppose you have <code>n</code> integers labeled <code>1</code> through <code>n</code>. A permutation of those <code>n</code> integers <code>perm</code> (<strong>1-indexed</strong>) is considered a <strong>beautiful arrangement</strong> if for every <code>i</code> (<code>1 &lt;= i &lt;= n</code>), <strong>either</strong> of the following is true:</p>

<ul>
	<li><code>perm[i]</code> is divisible by <code>i</code>.</li>
	<li><code>i</code> is divisible by <code>perm[i]</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the <strong>number</strong> of the <strong>beautiful arrangements</strong> that you can construct</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<b>Explanation:</b> 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
</ul>

### Solution
It took a while for me to understand this question. In the end all they were asking for was to find a permutation of n numbers that satisfy one of these conditions. EIther the number at index + 1 is divisible by the index + 1 or index + 1 is divisible by the number. Also a much better example would have been to show what happens with 3 numbers.  
I'll just put one example of where this fails because it seems like a better example.  
[1,3,2] - This fails because 3 is not divisible by index + 1 (2) and also index + 1 (2) is not divisible by 3.  
Generate the array of numbers that will be used to create permutations of 1 to n (n inclusive) ex: 3 will become [1,2,3]  
Iterate through all elements in the list and compare it to i which is initialized at 1 to avoid the while index + 1 thing.  
If the number is divisible by i or i is divisible by the number, remove the number from nums and continue generating the permutation.  
If a full permutation is generated (i == n+1, aka went past the index) then we have one solution. Add that to the result.  
Note that we are using tuple because list cannot be used as a cache key.
```python
class Solution:
    def countArrangement(self, n: int) -> int:

        @cache
        def dfs(nums: tuple, i):
            if i == n + 1:
                return 1
            count = 0
            for j, num in enumerate(nums):
                if not (num % i and i % num):
                    count += dfs(tuple(nums[:j] + nums[j + 1 :]), i + 1)
            return count

        return dfs(tuple([i for i in range(1, n + 1)]), 1)
```
# [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight)


## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of positive integers <code>w</code> where <code>w[i]</code> describes the <strong>weight</strong> of the <code>i<sup>th</sup></code> index.</p>

<p>You need to implement the function <code>pickIndex()</code>, which <strong>randomly</strong> picks an index in the range <code>[0, w.length - 1]</code> (<strong>inclusive</strong>) and returns it. The <strong>probability</strong> of picking an index <code>i</code> is <code>w[i] / sum(w)</code>.</p>

<ul>
	<li>For example, if <code>w = [1, 3]</code>, the probability of picking index <code>0</code> is <code>1 / (1 + 3) = 0.25</code> (i.e., <code>25%</code>), and the probability of picking index <code>1</code> is <code>3 / (1 + 3) = 0.75</code> (i.e., <code>75%</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Solution&quot;,&quot;pickIndex&quot;]
[[[1]],[]]
<strong>Output</strong>
[null,0]

<strong>Explanation</strong>
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Solution&quot;,&quot;pickIndex&quot;,&quot;pickIndex&quot;,&quot;pickIndex&quot;,&quot;pickIndex&quot;,&quot;pickIndex&quot;]
[[[1,3]],[],[],[],[],[]]
<strong>Output</strong>
[null,1,1,1,1,0]

<strong>Explanation</strong>
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= w.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= w[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>pickIndex</code> will be called at most <code>10<sup>4</sup></code> times.</li>
</ul>

### Solution
Use accumulated freq array to get idx.\
 w[] = {2,5,3,4} => wsum[] = {2,7,10,14}\
 then get random val random.nextInt(14)+1, idx is in range [1,14]\
idx in [1,2] return 0\
idx in [3,7] return 1\
idx in [8,10] return 2\
idx in [11,14] return 3\
then become LeetCode 35. Search Insert Position\
Time: O(n) to init, O(logn) for one pick\
Space: O(n)

```python
import random

class Solution:
    def __init__(self, w: List[int]):
        self.w_sum = []
        self.w = w
        self.w_sum.append(self.w[0])
        for i in range(1, len(self.w)):
            self.w_sum.append(self.w_sum[i - 1] + self.w[i])

    def pickIndex(self) -> int:
        rand = random.randint(1, self.w_sum[-1])
        left = 0
        right = len(self.w)
        while left < right:
            mid = (left + right) // 2
            if self.w_sum[mid] == rand:
                return mid
            elif self.w_sum[mid] > rand:
                right = mid
            else:
                left = mid + 1
        return left
```
# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

[中文文档](/solution/0000-0099/0053.Maximum%20Subarray/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>


# O(N) with O(N) space complexity
```python
class Solution:
   def maxSubArray(self, nums: List[int]) -> int:
       d = list(nums)
       for i in range(1, len(nums)):
           d[i] = max(nums[i] + d[i-1], nums[i])
       return max(d)
```

# O(N) with constant space complexity(Kadane’s algorithm)
```python
class Solution:
   def maxSubArray(self, nums: List[int]) -> int:
       m = currmax = nums[0]
       for i in range(1, len(nums)):
           currmax = max(nums[i] + currmax, nums[i])
           m = max(m, currmax)
       return m
```

  
# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals)


## Description

<!-- description:start -->

<p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


```python
class Solution:
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       # Sort the interval list based on the start times of intervals
       intervals.sort()
       # Initialize the merged_intervals list with the first interval
       merged_intervals = [intervals[0]]
       # Iterate over the intervals, starting from the second interval
       for start, end in intervals[1:]:
           # Check if the current interval does not overlap with the last interval in merged_intervals
           if merged_intervals[-1][1] < start:
               # If it does not overlap, add the current interval to merged_intervals
               merged_intervals.append([start, end])
           else:
               # If it does overlap, merge the current interval with the last one by
               # updating the end time of the last interval to the maximum end time seen so far
               merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
       # Return the merged intervals
       return merged_intervals

```

'''
### Time Complexity
The given code has two main operations:  
Sorting the intervals list.  
Iterating through the sorted list and merging overlapping intervals.  
For a list of n intervals:  
The sort operation typically has a complexity of O(n log n), since Python uses TimSort (a hybrid sorting algorithm derived from merge sort and   
insertion sort) for sorting lists.  
The iteration over the list has a complexity of O(n), because we go through the intervals only once.  
Hence, the total time complexity is the sum of these two operations, which is O(n log n) + O(n). Since O(n log n) is the higher order term,   
it dominates the total time complexity, which simplifies to O(n log n).  
# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)


## Description

<!-- description:start -->

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Prefix Sum

We define a hash table `cnt` to store the number of times the prefix sum of the array `nums` appears. Initially, we set the value of `cnt[0]` to `1`, indicating that the prefix sum `0` appears once.

We traverse the array `nums`, calculate the prefix sum `s`, then add the value of `cnt[s - k]` to the answer, and increase the value of `cnt[s]` by `1`.

After the traversal, we return the answer.

The time complexity is `O(n)`, and the space complexity is `O(n)`. Where `n` is the length of the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        # There is a subarray(empty) with sum 0
        m[0] = 1
        running_sum = 0
        count = 0
        for i, n in enumerate(nums):
            running_sum += n
            count += m[running_sum-k]
            # make sure to add 1 to existing instead of assigning
            # 1. There may be multiple subarrays with same sum
            m[running_sum] += 1
        return count
```
# [57. Insert Interval](https://leetcode.com/problems/insert-interval)


## Description

<!-- description:start -->

<p>You are given an array of non-overlapping intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represent the start and the end of the <code>i<sup>th</sup></code> interval and <code>intervals</code> is sorted in ascending order by <code>start<sub>i</sub></code>. You are also given an interval <code>newInterval = [start, end]</code> that represents the start and end of another interval.</p>

<p>Insert <code>newInterval</code> into <code>intervals</code> such that <code>intervals</code> is still sorted in ascending order by <code>start<sub>i</sub></code> and <code>intervals</code> still does not have any overlapping intervals (merge overlapping intervals if necessary).</p>

<p>Return <code>intervals</code><em> after the insertion</em>.</p>

<p><strong>Note</strong> that you don&#39;t need to modify <code>intervals</code> in-place. You can make a new array and return it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals</code> is sorted by <code>start<sub>i</sub></code> in <strong>ascending</strong> order.</li>
	<li><code>newInterval.length == 2</code></li>
	<li><code>0 &lt;= start &lt;= end &lt;= 10<sup>5</sup></code></li>
</ul>

```python
class Solution:
   def insert(
       self, intervals: List[List[int]], newInterval: List[int]
   ) -> List[List[int]]:
       i = 0
       left = []
       right = []
       while i < len(intervals):
           if intervals[i][1] < newInterval[0]:
               left.append(intervals[i])
           elif intervals[i][0] > newInterval[1]:
               right.append(intervals[i])
           else:
               newInterval = [
                   min(intervals[i][0], newInterval[0]),
                   max(intervals[i][1], newInterval[1]),
               ]
           i += 1
       return left + [newInterval] + right
```


# [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers)

[中文文档](/solution/0600-0699/0605.Can%20Place%20Flowers/README.md)

## Description

<!-- description:start -->

<p>You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in <strong>adjacent</strong> plots.</p>

<p>Given an integer array <code>flowerbed</code> containing <code>0</code>&#39;s and <code>1</code>&#39;s, where <code>0</code> means empty and <code>1</code> means not empty, and an integer <code>n</code>, return <code>true</code>&nbsp;<em>if</em> <code>n</code> <em>new flowers can be planted in the</em> <code>flowerbed</code> <em>without violating the no-adjacent-flowers rule and</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 1
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 2
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>flowerbed[i]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There are no two adjacent flowers in <code>flowerbed</code>.</li>
	<li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>


```python
class Solution:
   def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       if n == 0:
           return True
       for i in range(len(flowerbed)):
           if flowerbed[i] != 0:
               continue
           if (i == 0 or flowerbed[i - 1] == 0) and (
               i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
           ):
               flowerbed[i] = 1
               n -= 1
               if n == 0:
                   return True
       return False

```
# [61. Rotate List](https://leetcode.com/problems/rotate-list)

[中文文档](/solution/0000-0099/0061.Rotate%20List/README.md)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0061.Rotate%20List/images/rotate1.jpg" style="width: 450px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0061.Rotate%20List/images/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


```python
class Solution:
   def rotateRight(self, head: ListNode, k: int) -> ListNode:
      
       if not head:
           return None
      
       lastElement = head
       length = 1
       # get the length of the list and the last node in the list
       while lastElement.next:
           lastElement = lastElement.next
           length += 1
       # If k is equal to the length of the list then k == 0
       # ElIf k is greater than the length of the list then k = k % length
       k = k % length
          
       # Set the last node to point to head node
       # The list is now a circular linked list with last node pointing to first node
       lastElement.next = head
      
       # Traverse the list to get to the node just before the ( length - k )th node.
       # Example: In 1->2->3->4->5, and k = 2
       #          we need to get to the Node(3)
       tempNode = head
       for _ in range( length - k - 1 ):
           tempNode = tempNode.next
      
       # Get the next node from the tempNode and then set the tempNode.next as None
       # Example: In 1->2->3->4->5, and k = 2
       #          tempNode = Node(3)
       #          answer = Node(3).next => Node(4)
       #          Node(3).next = None ( cut the linked list from here )
       answer = tempNode.next
       tempNode.next = None
      
       return answer

```

# [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number)


## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

### Solution:
Let n be number of our numbers. Then bruteforce solution is O(n^3). Another approach is to sort numbers and for each pair a_i and a_j, where i<j we need to find the biggest index k, such that a_k < a_i + a_j. It can be done with binary search with overall complexity O(n^2 * log n).
There is even better solution, using two pointers approach. Let us choose first index i. Then we need to find number of pairs (left, right) where left < right < i and a_{left} + a_{right} > a_i. Let us start with left = 1 and right = i-1. Then we can use Two Pointers approach to find number of desired pairs inO(n) for fixed i. Note, that it is very similar to all 2Sum or 3Sum problems.
Complexity
Time complexity is O(n^2), space complexity is O(1).
```python
class Solution:
    def triangleNumber(self, nums):
        nums, count, n = sorted(nums), 0, len(nums)
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
```
```
632. Smallest Range Covering Elements from K Lists
Hard
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
 
Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 
Constraints:
nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
Firstly we merge k groups to one group, each number recoard it's group, eg:
[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
after merged we got：
 [(0, 1), (4, 0), (5, 2), (9, 1), (10, 0), (12, 1), (15, 0), (18, 2), (20, 1), (22, 2), (24, 0), (26, 0), (30, 2)]
and see only group, it's
 [1, 0, 2, 1, 0, 1, 0, 2, 1, 2, 0, 0, 2]
we can slide window by group when current groups satifies condition and recoard min range.
[1 0 2] 2 1 0 1 0 2 1 2 0 0 2    [0, 5]
1 [0 2 1] 1 0 1 0 2 1 2 0 0 2    [0, 5]
1 0 [2 1 0] 0 1 0 2 1 2 0 0 2    [0, 5]
1 0 [2 1 0 1] 1 0 2 1 2 0 0 2    [0, 5]
1 0 [2 1 0 1 0] 0 2 1 2 0 0 2    [0, 5]
1 0 2 1 0 [1 0 2] 2 1 2 0 0 2    [0, 5]
1 0 2 1 0 1 [0 2 1] 1 2 0 0 2    [0, 5]
1 0 2 1 0 1 [0 2 1 2] 2 0 0 2    [0, 5]
1 0 2 1 0 1 0 2 [1 2 0] 0 0 2    [20, 24]
1 0 2 1 0 1 0 2 [1 2 0 0] 0 2    [20, 24]
1 0 2 1 0 1 0 2 [1 2 0 0 2] 2    [20, 24]
```

```python
class Solution:
   def smallestRange(self, nums: List[List[int]]) -> List[int]:
       temp = []
       for i, num in enumerate(nums):
           for n in num:
               temp.append((n, i))
       temp.sort()
       left = 0
       right = 0
       d = defaultdict(int)
       r = []
       need = len(nums)
       while right < len(temp):
           if d[temp[right][1]] == 0:
               need -= 1   
           d[temp[right][1]] += 1
           if need == 0:
               while d[temp[left][1]] > 1:
                   d[temp[left][1]] -= 1
                   left += 1
               if not r:
                   r = [temp[left][0], temp[right][0]]
               elif temp[right][0] - temp[left][0] < r[1] -r[0]:
                   r = [temp[left][0], temp[right][0]]
           right += 1
       return r
```
# [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers)


## Description

<!-- description:start -->

<p>Given a non-negative integer <code>c</code>, decide whether there&#39;re two integers <code>a</code> and <code>b</code> such that <code>a<sup>2</sup> + b<sup>2</sup> = c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> c = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 * 1 + 2 * 2 = 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> c = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            cur = left * left + right * right
            if cur == c:
                return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False
```

# [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions)


## Description

<!-- description:start -->

<p>On a <strong>single-threaded</strong> CPU, we execute a program containing <code>n</code> functions. Each function has a unique ID between <code>0</code> and <code>n-1</code>.</p>

<p>Function calls are <strong>stored in a <a href="https://en.wikipedia.org/wiki/Call_stack">call stack</a></strong>: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is <strong>the current function being executed</strong>. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.</p>

<p>You are given a list <code>logs</code>, where <code>logs[i]</code> represents the <code>i<sup>th</sup></code> log message formatted as a string <code>&quot;{function_id}:{&quot;start&quot; | &quot;end&quot;}:{timestamp}&quot;</code>. For example, <code>&quot;0:start:3&quot;</code> means a function call with function ID <code>0</code> <strong>started at the beginning</strong> of timestamp <code>3</code>, and <code>&quot;1:end:2&quot;</code> means a function call with function ID <code>1</code> <strong>ended at the end</strong> of timestamp <code>2</code>. Note that a function can be called <b>multiple times, possibly recursively</b>.</p>

<p>A function&#39;s <strong>exclusive time</strong> is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for <code>2</code> time units and another call executing for <code>1</code> time unit, the <strong>exclusive time</strong> is <code>2 + 1 = 3</code>.</p>

<p>Return <em>the <strong>exclusive time</strong> of each function in an array, where the value at the </em><code>i<sup>th</sup></code><em> index represents the exclusive time for the function with ID </em><code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0636.Exclusive%20Time%20of%20Functions/images/diag1b.png" style="width: 550px; height: 239px;" />
<pre>
<strong>Input:</strong> n = 2, logs = [&quot;0:start:0&quot;,&quot;1:start:2&quot;,&quot;1:end:5&quot;,&quot;0:end:6&quot;]
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, logs = [&quot;0:start:0&quot;,&quot;0:start:2&quot;,&quot;0:end:5&quot;,&quot;0:start:6&quot;,&quot;0:end:6&quot;,&quot;0:end:7&quot;]
<strong>Output:</strong> [8]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2, logs = [&quot;0:start:0&quot;,&quot;0:start:2&quot;,&quot;0:end:5&quot;,&quot;1:start:6&quot;,&quot;1:end:6&quot;,&quot;0:end:7&quot;]
<strong>Output:</strong> [7,1]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= logs.length &lt;= 500</code></li>
	<li><code>0 &lt;= function_id &lt; n</code></li>
	<li><code>0 &lt;= timestamp &lt;= 10<sup>9</sup></code></li>
	<li>No two start events will happen at the same timestamp.</li>
	<li>No two end events will happen at the same timestamp.</li>
	<li>Each function has an <code>&quot;end&quot;</code> log for each <code>&quot;start&quot;</code> log.</li>
</ul>

### Solutions

#### Solution 1
```python
class Solution:
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = []
        prev_time = 0
        for log in logs:
            fn, typ, time = log.split(":")
            fn, time = int(fn), int(time)
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans
```


#### Solution 2
```python
class Solution:
    def exclusiveTime(self, N, logs):
        stack = []
        result = [0] * N
        
        def normalizeProcessTime(processTime):
            return processTime.split(':') 
        
        for processTime in logs:
            processId, eventType, time = normalizeProcessTime(processTime)
            
            if eventType == "start":
                stack.append([processId, time])
            
            elif eventType == "end":
                processId, startTime = stack.pop()
                timeSpent = int(time) - int(startTime) + 1 # Add 1 cause 0 is included
                result[int(processId)] += timeSpent
                
                # Decrement time for next process in the stack
                if len(stack) != 0:
                    nextProcessId, timeSpentByNextProcess = stack[-1] #
                    result[int(nextProcessId)] -= timeSpent
                    
        return result
```
# [642. Design Search Autocomplete System 🔒](https://leetcode.com/problems/design-search-autocomplete-system)


## Description

<!-- description:start -->

<p>Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character <code>&#39;#&#39;</code>).</p>

<p>You are given a string array <code>sentences</code> and an integer array <code>times</code> both of length <code>n</code> where <code>sentences[i]</code> is a previously typed sentence and <code>times[i]</code> is the corresponding number of times the sentence was typed. For each input character except <code>&#39;#&#39;</code>, return the top <code>3</code> historical hot sentences that have the same prefix as the part of the sentence already typed.</p>

<p>Here are the specific rules:</p>

<ul>
	<li>The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.</li>
	<li>The returned top <code>3</code> hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).</li>
	<li>If less than <code>3</code> hot sentences exist, return as many as you can.</li>
	<li>When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.</li>
</ul>

<p>Implement the <code>AutocompleteSystem</code> class:</p>

<ul>
	<li><code>AutocompleteSystem(String[] sentences, int[] times)</code> Initializes the object with the <code>sentences</code> and <code>times</code> arrays.</li>
	<li><code>List&lt;String&gt; input(char c)</code> This indicates that the user typed the character <code>c</code>.
	<ul>
		<li>Returns an empty array <code>[]</code> if <code>c == &#39;#&#39;</code> and stores the inputted sentence in the system.</li>
		<li>Returns the top <code>3</code> historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than <code>3</code> matches, return them all.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;AutocompleteSystem&quot;, &quot;input&quot;, &quot;input&quot;, &quot;input&quot;, &quot;input&quot;]
[[[&quot;i love you&quot;, &quot;island&quot;, &quot;iroman&quot;, &quot;i love leetcode&quot;], [5, 3, 2, 2]], [&quot;i&quot;], [&quot; &quot;], [&quot;a&quot;], [&quot;#&quot;]]
<strong>Output</strong>
[null, [&quot;i love you&quot;, &quot;island&quot;, &quot;i love leetcode&quot;], [&quot;i love you&quot;, &quot;i love leetcode&quot;], [], []]

<strong>Explanation</strong>
AutocompleteSystem obj = new AutocompleteSystem([&quot;i love you&quot;, &quot;island&quot;, &quot;iroman&quot;, &quot;i love leetcode&quot;], [5, 3, 2, 2]);
obj.input(&quot;i&quot;); // return [&quot;i love you&quot;, &quot;island&quot;, &quot;i love leetcode&quot;]. There are four sentences that have prefix &quot;i&quot;. Among them, &quot;ironman&quot; and &quot;i love leetcode&quot; have same hot degree. Since &#39; &#39; has ASCII code 32 and &#39;r&#39; has ASCII code 114, &quot;i love leetcode&quot; should be in front of &quot;ironman&quot;. Also we only need to output top 3 hot sentences, so &quot;ironman&quot; will be ignored.
obj.input(&quot; &quot;); // return [&quot;i love you&quot;, &quot;i love leetcode&quot;]. There are only two sentences that have prefix &quot;i &quot;.
obj.input(&quot;a&quot;); // return []. There are no sentences that have prefix &quot;i a&quot;.
obj.input(&quot;#&quot;); // return []. The user finished the input, the sentence &quot;i a&quot; should be saved as a historical sentence in system. And the following input will be counted as a new search.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == sentences.length</code></li>
	<li><code>n == times.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= sentences[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= times[i] &lt;= 50</code></li>
	<li><code>c</code> is a lowercase English letter, a hash <code>&#39;#&#39;</code>, or space <code>&#39; &#39;</code>.</li>
	<li>Each tested sentence will be a sequence of characters <code>c</code> that end with the character <code>&#39;#&#39;</code>.</li>
	<li>Each tested sentence will have a length in the range <code>[1, 200]</code>.</li>
	<li>The words in each input sentence are separated by single spaces.</li>
	<li>At most <code>5000</code> calls will be made to <code>input</code>.</li>
</ul>

```python
class Node:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.word = ''
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, frequency):
        # Inserts a word into the trie along with its frequency
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.value += frequency
        node.word = word
    
    def search(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        for sentence, frequency in zip(sentences, times):
            self.trie.insert(sentence, frequency)
        self.typed_characters = []  # Keeps track of characters typed by the user
      
    def input(self, character):
        def dfs(node):
            if node is None:
                return
            if node.value:
                results.append((node.value, node.word))
            for next_node in node.children.values():
                dfs(next_node)
        if character == '#':
            current_sentence = ''.join(self.typed_characters)
            self.trie.insert(current_sentence, 1)  # Increment the frequency of the word
            self.typed_characters = []
            return []
        self.typed_characters.append(character)
        current_prefix = ''.join(self.typed_characters)
        node = self.trie.search(current_prefix)
        if node is None:
            return []
        results = []
        dfs(node)
        results.sort(key=lambda x: (-x[0], x[1]))
        return [entry[1] for entry in results[:3]]
```

      
# The AutocompleteSystem class can be instantiated and used as follows: 
```
sentences= ["i love you", "island", "iroman", "i love leetcode"]  
times = [5, 3, 2, 2]  
obj = AutocompleteSystem(sentences, times)
# suggestions = autocomplete_system.input(character)
print(obj.input("i")); #// return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
print(obj.input(" ")); #// return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a")); #// return []. There are no sentences that have prefix "i a".
print(obj.input("#"));
```
# [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the number of <strong>palindromic substrings</strong> in it</em>.</p>

<p>A string is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three palindromic strings: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaa&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> Six palindromic strings: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Note: count is not inittialzed to 0 but to length of string
        # to account for single character palindromes.
        count = len(s)
        def util(s, i):
            c = 0
            start = i-1
            end = i +1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                c += 1
                start -=1
                end += 1
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                c += 1
                start -=1
                end += 1
            return c
        for i in range(len(s)):
            count += util(s, i)
        return count
```

# [65. Valid Number](https://leetcode.com/problems/valid-number)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return whether <code>s</code> is a <strong>valid number</strong>.<br />
<br />
For example, all the following are valid numbers: <code>&quot;2&quot;, &quot;0089&quot;, &quot;-0.1&quot;, &quot;+3.14&quot;, &quot;4.&quot;, &quot;-.9&quot;, &quot;2e10&quot;, &quot;-90E3&quot;, &quot;3e+7&quot;, &quot;+6e-1&quot;, &quot;53.5e93&quot;, &quot;-123.456e789&quot;</code>, while the following are not valid numbers: <code>&quot;abc&quot;, &quot;1a&quot;, &quot;1e&quot;, &quot;e3&quot;, &quot;99e2.5&quot;, &quot;--6&quot;, &quot;-+3&quot;, &quot;95a54e53&quot;</code>.</p>

<p>Formally, a&nbsp;<strong>valid number</strong> is defined using one of the following definitions:</p>

<ol>
	<li>An <strong>integer number</strong> followed by an <strong>optional exponent</strong>.</li>
	<li>A <strong>decimal number</strong> followed by an <strong>optional exponent</strong>.</li>
</ol>

<p>An <strong>integer number</strong> is defined with an <strong>optional sign</strong> <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code> followed by <strong>digits</strong>.</p>

<p>A <strong>decimal number</strong> is defined with an <strong>optional sign</strong> <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code> followed by one of the following definitions:</p>

<ol>
	<li><strong>Digits</strong> followed by a <strong>dot</strong> <code>&#39;.&#39;</code>.</li>
	<li><strong>Digits</strong> followed by a <strong>dot</strong> <code>&#39;.&#39;</code> followed by <strong>digits</strong>.</li>
	<li>A <strong>dot</strong> <code>&#39;.&#39;</code> followed by <strong>digits</strong>.</li>
</ol>

<p>An <strong>exponent</strong> is defined with an <strong>exponent notation</strong> <code>&#39;e&#39;</code> or <code>&#39;E&#39;</code> followed by an <strong>integer number</strong>.</p>

<p>The <strong>digits</strong> are defined as one or more digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;e&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;.&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of only English letters (both uppercase and lowercase), digits (<code>0-9</code>), plus <code>&#39;+&#39;</code>, minus <code>&#39;-&#39;</code>, or dot <code>&#39;.&#39;</code>.</li>
</ul>

```python
class Solution(object):
   def isNumber(self, s):
       s = s.strip()
       met_dot = met_e = met_digit = False
       for i, char in enumerate(s):
           if char in ['+', '-']:
               if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                   return False
           elif char == '.':
               if met_dot or met_e: return False
               met_dot = True
           elif char == 'e' or char== 'E':
               if met_e or not met_digit:
                   return False
               met_e, met_digit = True, False
           elif char.isdigit():
               met_digit = True
           else:
               return False
       return met_digit
```


# [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree and an integer <code>k</code>, return <code>true</code> <em>if there exist two elements in the BST such that their sum is equal to</em> <code>k</code>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0653.Two%20Sum%20IV%20-%20Input%20is%20a%20BST/images/sum_tree_1.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0653.Two%20Sum%20IV%20-%20Input%20is%20a%20BST/images/sum_tree_2.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>root</code> is guaranteed to be a <strong>valid</strong> binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


### Solution 1
Time: O(N), where N is the number of nodes in the BST.  
Space: O(N), it's the space for seen HashSet in the worst case.  

```python
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, seen):
            if root == None:
                return False
            complement = k - root.val
            if complement in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        return dfs(root, set())
```


### Solution 2

Time: O(N), where N is the number of nodes in the BST.  
Space: O(H), where H is the height of the BST. The size of stack is up to O(H).  
```python
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left
        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right
        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val
        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val
        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)
        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
```

# [655. Print Binary Tree](https://leetcode.com/problems/print-binary-tree)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, construct a <strong>0-indexed</strong> <code>m x n</code> string matrix <code>res</code> that represents a <strong>formatted layout</strong> of the tree. The formatted layout matrix should be constructed using the following rules:</p>

<ul>
	<li>The <strong>height</strong> of the tree is <code>height</code>&nbsp;and the number of rows <code>m</code> should be equal to <code>height + 1</code>.</li>
	<li>The number of columns <code>n</code> should be equal to <code>2<sup>height+1</sup> - 1</code>.</li>
	<li>Place the <strong>root node</strong> in the <strong>middle</strong> of the <strong>top row</strong> (more formally, at location <code>res[0][(n-1)/2]</code>).</li>
	<li>For each node that has been placed in the matrix at position <code>res[r][c]</code>, place its <strong>left child</strong> at <code>res[r+1][c-2<sup>height-r-1</sup>]</code> and its <strong>right child</strong> at <code>res[r+1][c+2<sup>height-r-1</sup>]</code>.</li>
	<li>Continue this process until all the nodes in the tree have been placed.</li>
	<li>Any empty cells should contain the empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>Return <em>the constructed matrix </em><code>res</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0655.Print%20Binary%20Tree/images/print1-tree.jpg" style="width: 141px; height: 181px;" />
<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 
[[&quot;&quot;,&quot;1&quot;,&quot;&quot;],
&nbsp;[&quot;2&quot;,&quot;&quot;,&quot;&quot;]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0655.Print%20Binary%20Tree/images/print2-tree.jpg" style="width: 207px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> 
[[&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;1&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;],
&nbsp;[&quot;&quot;,&quot;2&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;3&quot;,&quot;&quot;],
&nbsp;[&quot;&quot;,&quot;&quot;,&quot;4&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2<sup>10</sup>]</code>.</li>
	<li><code>-99 &lt;= Node.val &lt;= 99</code></li>
	<li>The depth of the tree will be in the range <code>[1, 10]</code>.</li>
</ul>

```python
class Solution(object):
    def printTree(self, root):
        def get_height(node):
            return (
                0
                if not node
                else 1 + max(get_height(node.left), get_height(node.right))
            )
        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1, left, mid - 1)
            update_output(node.right, row + 1, mid + 1, right)
        height = get_height(root)
        width = 2**height - 1
        self.output = [[""] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output

```
# [671. Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree)

[中文文档](/solution/0600-0699/0671.Second%20Minimum%20Node%20In%20a%20Binary%20Tree/README.md)

## Description

<!-- description:start -->

<p>Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-node. If the node has two sub-nodes, then this node&#39;s value is the smaller value among its two sub-nodes. More formally, the property&nbsp;<code>root.val = min(root.left.val, root.right.val)</code>&nbsp;always holds.</p>

<p>Given such a binary tree, you need to output the <b>second minimum</b> value in the set made of all the nodes&#39; value in the whole tree.</p>

<p>If no such second minimum value exists, output -1 instead.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0671.Second%20Minimum%20Node%20In%20a%20Binary%20Tree/images/smbt1.jpg" style="width: 431px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [2,2,5,null,null,5,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The smallest value is 2, the second smallest value is 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0671.Second%20Minimum%20Node%20In%20a%20Binary%20Tree/images/smbt2.jpg" style="width: 321px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,2,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The smallest value is 2, but there isn&#39;t any second smallest value.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 25]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>root.val == min(root.left.val, root.right.val)</code>&nbsp;for each internal node of the tree.</li>
</ul>

```python
class Solution:
   def findSecondMinimumValue(self, root):
       self.ans = float("inf")
       min1 = root.val


       def dfs(node):
           if node:
               if min1 < node.val < self.ans:
                   self.ans = node.val
               elif node.val == min1:
                   dfs(node.left)
                   dfs(node.right)


       dfs(root)
       return self.ans if self.ans < float("inf") else -1

```
# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string)


## Description

<!-- description:start -->

<p>Given a string <code>s</code> containing only three types of characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> and <code>&#39;*&#39;</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
	<li>Any left parenthesis <code>&#39;(&#39;</code> must have a corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li>Any right parenthesis <code>&#39;)&#39;</code> must have a corresponding left parenthesis <code>&#39;(&#39;</code>.</li>
	<li>Left parenthesis <code>&#39;(&#39;</code> must go before the corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li><code>&#39;*&#39;</code> could be treated as a single right parenthesis <code>&#39;)&#39;</code> or a single left parenthesis <code>&#39;(&#39;</code> or an empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>

### O(n) time and O(n) space
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                open.append(i)
            elif c == '*':
                star.append(i)
            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open:
            if not star:
                return False
            if open.pop() > star.pop():
                return False
        return True
```


### O(n) time and O(1) space
Key variables:

cmax: This keeps track of the maximum possible number of unmatched opening parentheses that could result if all '*' characters were interpreted as '('.

cmin: This keeps track of the minimum possible number of unmatched opening parentheses that could result if all '*' characters were interpreted as ')', or as empty strings in the worst case.

Steps:

Iterate over the string:

If the character is '(', it increases both cmax and cmin because it is definitely an unmatched opening parenthesis.

If the character is ')', it decreases both cmax and cmin because it is definitely an unmatched closing parenthesis.

If the character is '*', it increases cmax (because '' could be interpreted as an opening parenthesis) and decreases cmin (because '' could also be interpreted as a closing parenthesis or an empty string).

Check conditions:

If cmax becomes negative at any point, that means there are more closing parentheses than can be matched, so the string cannot be valid, and it returns False.

Ensure that cmin doesn't go negative, because negative cmin means that too many closing parentheses are required, and this could be resolved by interpreting '*' as empty. Hence, cmin is capped at 0.

Final Check:

At the end of the loop, if cmin == 0, it means there is a valid configuration where the parentheses are properly balanced (with possible '*' interpreted correctly). If cmin is not zero, it means that there are unmatched opening parentheses that couldn't be closed.


```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmax = 0
        cmin = 0
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1
                cmin -= 1
            if cmax < 0:
                return False
            # cmin cannot be negative, if it goes negative, we can
            # consider the * to be empty string instead of )
            cmin = max(cmin, 0)
        return cmin == 0
```

# [68. Text Justification](https://leetcode.com/problems/text-justification)


## Description

<!-- description:start -->

<p>Given an array of strings <code>words</code> and a width <code>maxWidth</code>, format the text such that each line has exactly <code>maxWidth</code> characters and is fully (left and right) justified.</p>

<p>You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces <code>&#39; &#39;</code> when necessary so that each line has exactly <code>maxWidth</code> characters.</p>

<p>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.</p>

<p>For the last line of text, it should be left-justified, and no extra space is inserted between words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>A word is defined as a character sequence consisting of non-space characters only.</li>
	<li>Each word&#39;s length is guaranteed to be greater than <code>0</code> and not exceed <code>maxWidth</code>.</li>
	<li>The input array <code>words</code> contains at least one word.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;, &quot;of&quot;, &quot;text&quot;, &quot;justification.&quot;], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &nbsp;&quot;This &nbsp; &nbsp;is &nbsp; &nbsp;an&quot;,
&nbsp; &nbsp;&quot;example &nbsp;of text&quot;,
&nbsp; &nbsp;&quot;justification. &nbsp;&quot;
]</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;What&quot;,&quot;must&quot;,&quot;be&quot;,&quot;acknowledgment&quot;,&quot;shall&quot;,&quot;be&quot;], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &quot;What &nbsp; must &nbsp; be&quot;,
&nbsp; &quot;acknowledgment &nbsp;&quot;,
&nbsp; &quot;shall be &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]
<strong>Explanation:</strong> Note that the last line is &quot;shall be    &quot; instead of &quot;shall     be&quot;, because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;Science&quot;,&quot;is&quot;,&quot;what&quot;,&quot;we&quot;,&quot;understand&quot;,&quot;well&quot;,&quot;enough&quot;,&quot;to&quot;,&quot;explain&quot;,&quot;to&quot;,&quot;a&quot;,&quot;computer.&quot;,&quot;Art&quot;,&quot;is&quot;,&quot;everything&quot;,&quot;else&quot;,&quot;we&quot;,&quot;do&quot;], maxWidth = 20
<strong>Output:</strong>
[
&nbsp; &quot;Science &nbsp;is &nbsp;what we&quot;,
  &quot;understand &nbsp; &nbsp; &nbsp;well&quot;,
&nbsp; &quot;enough to explain to&quot;,
&nbsp; &quot;a &nbsp;computer. &nbsp;Art is&quot;,
&nbsp; &quot;everything &nbsp;else &nbsp;we&quot;,
&nbsp; &quot;do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 300</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>words[i]</code> consists of only English letters and symbols.</li>
	<li><code>1 &lt;= maxWidth &lt;= 100</code></li>
	<li><code>words[i].length &lt;= maxWidth</code></li>
</ul>

```python
class Solution:
   def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
       res, cur_words, cur_len = [], [], 0
       for word in words:
           if cur_len + len(word) + len(cur_words) > maxWidth:
               total_spaces = maxWidth - cur_len
               gaps = len(cur_words) - 1
               if gaps == 0:
                   res.append(cur_words[0] + ' ' * total_spaces)
               else:
                   space_per_gap = total_spaces // gaps
                   extra_spaces = total_spaces % gaps
                   line = ''
                   for i, w in enumerate(cur_words):
                       line += w
                       if i < gaps:
                           line += ' ' * space_per_gap
                           if i < extra_spaces:
                               line += ' '
                   res.append(line)
               cur_words, cur_len = [], 0
           cur_words.append(word)
           cur_len += len(word)
       last_line = ' '.join(cur_words)
       remaining_spaces = maxWidth - len(last_line)
       res.append(last_line + ' ' * remaining_spaces)
       return res
```
# [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)


## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if it is possible to divide this array into <code>k</code> non-empty subsets whose sums are all equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,2,3,5,2,1], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 16</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>The frequency of each element is in the range <code>[1, 4]</code>.</li>
</ul>

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0 or nums_sum < k:
            return False
        subset_sum = nums_sum / k
        ks = [0] * k
        nums.sort(reverse=True)
        def can_partition(j):
            if j == len(nums):
                for i in range(k):
                    if ks[i] != subset_sum:
                        return False
                return True
            for i in range(k):
                if ks[i] + nums[j] <= subset_sum:
                    ks[i] += nums[j]
                    if can_partition(j + 1):
                        return True
                    ks[i] -= nums[j]
            return False
        return can_partition(0)
```

# [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)


## Description

<!-- description:start -->

<p>You are given the <code>root</code> node of a binary search tree (BST) and a <code>value</code> to insert into the tree. Return <em>the root node of the BST after the insertion</em>. It is <strong>guaranteed</strong> that the new value does not exist in the original BST.</p>

<p><strong>Notice</strong>&nbsp;that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0701.Insert%20into%20a%20Binary%20Search%20Tree/images/insertbst.jpg" style="width: 752px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
<strong>Explanation:</strong> Another accepted tree is:
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0701.Insert%20into%20a%20Binary%20Search%20Tree/images/bst.jpg" style="width: 352px; height: 301px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [40,20,60,10,30,50,70], val = 25
<strong>Output:</strong> [40,20,60,10,30,50,70,null,null,25]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in&nbsp;the tree will be in the range <code>[0,&nbsp;10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>8</sup> &lt;= Node.val &lt;= 10<sup>8</sup></code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>-10<sup>8</sup> &lt;= val &lt;= 10<sup>8</sup></code></li>
	<li>It&#39;s <strong>guaranteed</strong> that <code>val</code> does not exist in the original BST.</li>
</ul>

### Recursive
```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
```


### Iterative
```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if curr.val > val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root
```

# [706. Design HashMap](https://leetcode.com/problems/design-hashmap)

[中文文档](/solution/0700-0799/0706.Design%20HashMap/README.md)

## Description

<!-- description:start -->

<p>Design a HashMap without using any built-in hash table libraries.</p>

<p>Implement the <code>MyHashMap</code> class:</p>

<ul>
	<li><code>MyHashMap()</code> initializes the object with an empty map.</li>
	<li><code>void put(int key, int value)</code> inserts a <code>(key, value)</code> pair into the HashMap. If the <code>key</code> already exists in the map, update the corresponding <code>value</code>.</li>
	<li><code>int get(int key)</code> returns the <code>value</code> to which the specified <code>key</code> is mapped, or <code>-1</code> if this map contains no mapping for the <code>key</code>.</li>
	<li><code>void remove(key)</code> removes the <code>key</code> and its corresponding <code>value</code> if the map contains the mapping for the <code>key</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyHashMap&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;remove&quot;, &quot;get&quot;]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, 1, -1, null, 1, null, -1]

<strong>Explanation</strong>
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key, value &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>put</code>, <code>get</code>, and <code>remove</code>.</li>
</ul>


```python
# using just arrays, direct access table
# using linked list for chaining

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None]*self.m
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```
# [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k)


## Description

<!-- description:start -->

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than </em><code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,5,2,6], k = 100
<strong>Output:</strong> 8
<strong>Explanation:</strong> The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], k = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>


```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, prod, count = 0, 1, 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count
```

# [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee)


## Description

<!-- description:start -->

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>fee</code> representing a transaction fee.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</li>
	<li>The transaction fee is only charged once for each stock purchase and sale.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,2,8,4,9], fee = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,7,5,10,3], fee = 3
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt; 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= fee &lt; 5 * 10<sup>4</sup></code></li>
</ul>

### With Extra Space
```python
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        buy = [-inf] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(sell[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] - fee + prices[i], sell[i - 1])
        return sell[n - 1] if sell[n - 1] > 0 else 0
```
### Without Extra Space
```python
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1, n):
            temp = buy
            buy = max(sell - prices[i], buy)
            sell = max(temp + prices[i] - fee, sell)
        return sell if sell > 0 else 0
```
# [716. Max Stack 🔒](https://leetcode.com/problems/max-stack)

## Description

<!-- description:start -->

<p>Design a max stack data structure that supports the stack operations and supports finding the stack&#39;s maximum element.</p>

<p>Implement the <code>MaxStack</code> class:</p>

<ul>
	<li><code>MaxStack()</code> Initializes the stack object.</li>
	<li><code>void push(int x)</code> Pushes element <code>x</code> onto the stack.</li>
	<li><code>int pop()</code> Removes the element on top of the stack and returns it.</li>
	<li><code>int top()</code> Gets the element on the top of the stack without removing it.</li>
	<li><code>int peekMax()</code> Retrieves the maximum element in the stack without removing it.</li>
	<li><code>int popMax()</code> Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the <strong>top-most</strong> one.</li>
</ul>

<p>You must come up with a solution that supports <code>O(1)</code> for each <code>top</code> call and <code>O(logn)</code> for each other call.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MaxStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;top&quot;, &quot;popMax&quot;, &quot;top&quot;, &quot;peekMax&quot;, &quot;pop&quot;, &quot;top&quot;]
[[], [5], [1], [5], [], [], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, 5, 5, 1, 5, 1, 5]

<strong>Explanation</strong>
MaxStack stk = new MaxStack();
stk.push(5);   // [<strong><u>5</u></strong>] the top of the stack and the maximum number is 5.
stk.push(1);   // [<u>5</u>, <strong>1</strong>] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, <strong><u>5</u></strong>] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, <strong><u>5</u></strong>] the stack did not change.
stk.popMax();  // return 5, [<u>5</u>, <strong>1</strong>] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [<u>5</u>, <strong>1</strong>] the stack did not change.
stk.peekMax(); // return 5, [<u>5</u>, <strong>1</strong>] the stack did not change.
stk.pop();     // return 1, [<strong><u>5</u></strong>] the top of the stack and the max element is now 5.
stk.top();     // return 5, [<strong><u>5</u></strong>] the stack did not change.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>7</sup> &lt;= x &lt;= 10<sup>7</sup></code></li>
	<li>At most <code>10<sup>5</sup></code>&nbsp;calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, <code>peekMax</code>, and <code>popMax</code>.</li>
	<li>There will be <strong>at least one element</strong> in the stack when <code>pop</code>, <code>top</code>, <code>peekMax</code>, or <code>popMax</code> is called.</li>
</ul>


### Solutions
A stack supports push, pop, and top already, so only the last two operations need to be implemented. Use two stacks.  
One stack works as the normal stack,  
and the other stack which is called the maximum stack stores the maximum element so far.  
Both stacks are initialized in the constructor. The other three functions should be modified as well.  
The push() function. Push the element into the normal stack, and for the maximum stack, if the maximum stack is empty, then simply push the element into the maximum stack, otherwise push the maximum element between the current element and the element at the top of the maximum stack.


The pop() function. Simply pop both the normal stack and the maximum stack, and return the element popped from the normal stack.  


The top() function. Simply return the top element of the normal stack.  


The peekMax() function. Simply return the top element of the maximum stack. The reason why this works is that, each time the push function is called, the element pushed into the maximum stack is guaranteed to be the maximum element so far, so at any time, the top element of the maximum stack is the maximum element among all the elements pushed.  


The popMax() function. This is a highly complex function that requires careful handling. Since the maximum element may not always be at the top of the normal stack, it may be necessary to first pop some elements from the normal stack in order to locate it. The top element of the normal stack is considered the maximum only if it is identical to the top element of the maximum stack. Once the maximum element has been popped, any other elements that were previously removed from the normal stack must be re-added. To accomplish this, a new stack is used to store all the popped elements until the maximum element is identified. Once the maximum element has been popped and retrieved, each element in the new stack must be pushed back onto the normal stack, to ensure that both the normal stack and the maximum stack contain the correct values.
```python
class MaxStack(object):
   def __init__(self):
       """
       initialize your data structure here.
       """
       self.stack = []
       self.max_stack = []
   def push(self, x):
       """
       :type x: int
       :rtype: void
       """
       self.stack.append(x)
       self.max_stack.append(max(x, self.max_stack[-1]) if self.max_stack else x)
   def pop(self):
       """
       :rtype: int
       """
       if len(self.stack) != 0:
           self.max_stack.pop()
           return self.stack.pop()
   def top(self):
       """
       :rtype: int
       """
       return self.stack[-1] if self.stack else None
   def peekMax(self):
       """
       :rtype: int
       """
       if self.max_stack:
           return self.max_stack[-1]
   def popMax(self):
       """
       :rtype: int
       """
       val = self.peekMax()
       buff = []
       while self.top() != val:
           # re-use pop(), ops on both max_stack and stack
           buff.append(self.pop())
       self.pop()
       while buff:
           # re-use push(), no need to save buffer for max-stack
           self.push(buff.pop())
       return val
       
# Your MaxStack object will be instantiated and called as such:
stk  = MaxStack()
stk.push(5)
stk.push(1)
stk.push(5)
print(stk.top())
print(stk.popMax())
print(stk.top())
print(stk.peekMax())
print(stk.pop())
print(stk.top())
```


# Better Solution using DLL and sortedlist
```python
from sortedcontainers import SortedList
from typing import Optional
class Node:
    def __init__(self, val: int = 0):
       self.val = val  # Value of the node
       self.prev: Optional["Node"] = None  # Link to the previous node
       self.next: Optional["Node"] = None  # Link to the next node
class DoubleLinkedList:
    def __init__(self):
       self.head = Node()  # Sentinel head node of the double linked list
       self.tail = Node()  # Sentinel tail node of the double linked list
       self.head.next = self.tail  # Connect head to tail
       self.tail.prev = self.head  # Connect tail to head
    def append(self, val: int) -> Node:
       """
       Append a new node with value val at the end of the list
       """
       # Create new node
       node = Node(val)
       # Link it with the last element
       node.next = self.tail
       node.prev = self.tail.prev
       # Link the last element with the new node
       self.tail.prev.next = node
       self.tail.prev = node
       return node
    @staticmethod
    def remove_node(node: Node) -> None:
       """
       Remove a node from the list
       """
       # Re-link the previous and next nodes to each other
       node.prev.next = node.next
       node.next.prev = node.prev
    def pop(self) -> Node:
       """
       Pop the last element from the list
       """
       # Use the remove_node static method to remove the last element
       node = self.tail.prev
       self.remove_node(node)
       return node
    def peek(self) -> int:
       """
       Peek the last element's value from the list
       :return: Value of last node
       """
       return self.tail.prev.val
class MaxStack:
    def __init__(self):
       self.stack = DoubleLinkedList()  # The main stack as a double linked list
       self.sorted_nodes = SortedList(
           key=lambda x: x.val
       )  # Sorted keys to track max values efficiently
    def push(self, x: int) -> None:
       """
       Push an element onto the stack
       :param x: Value to push onto the stack
       :return: None
       """
       # Append value to stack and add the node to sorted list for max retrieval
       node = self.stack.append(x)
       self.sorted_nodes.add(node)
    def pop(self) -> int:
       """
       Pop the top element from the stack
       :return: Value of removed element
       """
       # Pop from stack and remove corresponding node from sorted list
       node = self.stack.pop()
       self.sorted_nodes.remove(node)
       return node.val
    def top(self) -> int:
       """
       Get the top element of the stack
       :return: Value of top element
       """
       return self.stack.peek()
    def peekMax(self) -> int:
       """
       Retrieve the maximum value in the stack
       :return: Maximum value
       """
       # Last element of sorted_nodes has the max value
       return self.sorted_nodes[-1].val
    def popMax(self) -> int:
       """
       Pop the maximum value from the stack
       :return: Maximum value that was removed
       """
       # Remove last element from sorted list to get max value
       node = self.sorted_nodes.pop()
       # Use the remove_node static method to detach the node from the stack
       DoubleLinkedList.remove_node(node)
       return node.val

stk  = MaxStack()
stk.push(5)
stk.push(1)
stk.push(5)
print(stk.top())
print(stk.popMax())
print(stk.top())
print(stk.peekMax())
print(stk.pop())
print(stk.top())       
```

# [72. Edit Distance](https://leetcode.com/problems/edit-distance)


## Description

<!-- description:start -->

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->


### Thought process:
Given two strings, we're tasked with finding the minimum number of transformations we need to make to arrive with equivalent strings. From the get-go, there doesn't seem to be any way around trying all possibilities, and in this, possibilities refers to inserting, deleting, or replacing a character. Recursion is usually a good choice for trying all possilbilities.
Whenever we write recursive functions, we'll need some way to terminate, or else we'll end up overflowing the stack via infinite recursion. With strings, the natural state to keep track of is the index. We'll need two indexes, one for word1 and one for word2. Now we just need to handle our base cases, and recursive cases.  
 What happens when we're done with either word? Some thought will tell you that the minimum number of transformations is simply to insert the rest of the other word. This is our base case. What about when we're not done with either string? We'll either match the currently indexed characters in both strings, or mismatch. In the first case, we don't incur any penalty, and we can continue to compare the rest of the strings by recursing on the rest of both strings. In the case of a mismatch, we either insert, delete, or replace. To recap:  
base case: word1 = "" or word2 = "" => return length of other string  
recursive case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]  
recursive case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing  

### Brute Force Solution(TLE)
```python
class Solution:
   @cache
   def minDistance(self, word1, word2):
       """Naive recursive solution"""
       if not word1 and not word2:
           return 0
       if not word1:
           return len(word2)
       if not word2:
           return len(word1)
       if word1[0] == word2[0]:
           return self.minDistance(word1[1:], word2[1:])
       insert =  self.minDistance(word1, word2[1:])
       delete =  self.minDistance(word1[1:], word2)
       replace = self.minDistance(word1[1:], word2[1:])
       return 1 + min(insert, replace, delete)
```


### DP Solution(Accepted)
We can also use a 2D array to do essentially the same thing as the dictionary of cached values. When we do this, we build up  from smaller subproblems to bigger 
subproblems (bottom-up). In this case, since we are no longer "recurring" in the traditional sense, we initialize our 2D table with base constraints. 
The first row and column of the table has known values since if one string is empty, we simply add the length of the non-empty string since that is the 
minimum number of edits necessary to arrive at equivalent strings. For both the memoized and dynamic programming , the runtime is O(mn) and the space complexity 
is O(mn) where m and n are the lengths of word1 and word2, respectively.

```python
class Solution:
   def minDistance(self, word1, word2):
       """Dynamic programming solution"""
       m = len(word1)
       n = len(word2)
       table = [[0] * (n + 1) for _ in range(m + 1)]
       for i in range(m + 1):
           table[i][0] = i
       for j in range(n + 1):
           table[0][j] = j
       for i in range(1, m + 1):
           for j in range(1, n + 1):
               if word1[i - 1] == word2[j - 1]:
                   table[i][j] = table[i - 1][j - 1]
               else:
                   table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
       return table[-1][-1]
```
# [721. Accounts Merge](https://leetcode.com/problems/accounts-merge)


## Description

<!-- description:start -->

<p>Given a list of <code>accounts</code> where each element <code>accounts[i]</code> is a list of strings, where the first element <code>accounts[i][0]</code> is a name, and the rest of the elements are <strong>emails</strong> representing emails of the account.</p>

<p>Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.</p>

<p>After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails <strong>in sorted order</strong>. The accounts themselves can be returned in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john_newyork@mail.com&quot;],[&quot;John&quot;,&quot;johnsmith@mail.com&quot;,&quot;john00@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
<strong>Output:</strong> [[&quot;John&quot;,&quot;john00@mail.com&quot;,&quot;john_newyork@mail.com&quot;,&quot;johnsmith@mail.com&quot;],[&quot;Mary&quot;,&quot;mary@mail.com&quot;],[&quot;John&quot;,&quot;johnnybravo@mail.com&quot;]]
<strong>Explanation:</strong>
The first and second John&#39;s are the same person as they have the common email &quot;johnsmith@mail.com&quot;.
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [[&#39;Mary&#39;, &#39;mary@mail.com&#39;], [&#39;John&#39;, &#39;johnnybravo@mail.com&#39;], 
[&#39;John&#39;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;]] would still be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> accounts = [[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe3@m.co&quot;,&quot;Gabe1@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;,&quot;Kevin0@m.co&quot;],[&quot;Ethan&quot;,&quot;Ethan5@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan0@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo3@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo0@m.co&quot;],[&quot;Fern&quot;,&quot;Fern5@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern0@m.co&quot;]]
<strong>Output:</strong> [[&quot;Ethan&quot;,&quot;Ethan0@m.co&quot;,&quot;Ethan4@m.co&quot;,&quot;Ethan5@m.co&quot;],[&quot;Gabe&quot;,&quot;Gabe0@m.co&quot;,&quot;Gabe1@m.co&quot;,&quot;Gabe3@m.co&quot;],[&quot;Hanzo&quot;,&quot;Hanzo0@m.co&quot;,&quot;Hanzo1@m.co&quot;,&quot;Hanzo3@m.co&quot;],[&quot;Kevin&quot;,&quot;Kevin0@m.co&quot;,&quot;Kevin3@m.co&quot;,&quot;Kevin5@m.co&quot;],[&quot;Fern&quot;,&quot;Fern0@m.co&quot;,&quot;Fern1@m.co&quot;,&quot;Fern5@m.co&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= accounts.length &lt;= 1000</code></li>
	<li><code>2 &lt;= accounts[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= accounts[i][j].length &lt;= 30</code></li>
	<li><code>accounts[i][0]</code> consists of English letters.</li>
	<li><code>accounts[i][j] (for j &gt; 0)</code> is a valid email.</li>
</ul>

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(set)
        for i, ac in enumerate(accounts):
            for a in ac:
                d[a].add(i)
        visited_accounts = set()
        def dfs(i, emails):
            if i in visited_accounts:
                return
            visited_accounts.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in d[email]:
                    dfs(neighbor, emails)
        res = []
        for i, account in enumerate(accounts):
            if i in visited_accounts:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
```

# [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn)


## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. You want to maximize the number of points you get by performing the following operation any number of times:</p>

<ul>
	<li>Pick any <code>nums[i]</code> and delete it to earn <code>nums[i]</code> points. Afterwards, you must delete <b>every</b> element equal to <code>nums[i] - 1</code> and <strong>every</strong> element equal to <code>nums[i] + 1</code>.</li>
</ul>

<p>Return <em>the <strong>maximum number of points</strong> you can earn by applying the above operation some number of times</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,3,3,3,4]
<strong>Output:</strong> 9
<strong>Explanation:</strong> You can perform the following operations:
- Delete a 3 to earn 3 points. All 2&#39;s and 4&#39;s are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


### Solution:
Observations:
The order of nums does not matter.  
Once we decide that we want a num, we can add all the occurrences of num into the total.  
We first transform the nums array into a points array that sums up the total number of points for that particular value. A value of x will be assigned to index x in points.  
nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)  
 points: [0, 0, 4, 9, 4] <- This is the gold in each house!  
The condition that we cannot pick adjacent values is similar to the House Robber question that we cannot rob adjacent houses. Simply pass points into the rob function for a quick win 🌝!

```python
class Solution(object):
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr
    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)
```

# [742. Closest Leaf in a Binary Tree 🔒](https://leetcode.com/problems/closest-leaf-in-a-binary-tree)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree where every node has <strong>a unique value</strong> and a target integer <code>k</code>, return <em>the value of the <strong>nearest leaf node</strong> to the target </em><code>k</code><em> in the tree</em>.</p>

<p><strong>Nearest to a leaf</strong> means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest1-tree.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [1,3,2], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> Either 2 or 3 is the nearest leaf node to the target of 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest2-tree.jpg" style="width: 64px; height: 65px;" />
<pre>
<strong>Input:</strong> root = [1], k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The nearest leaf node is the root node itself.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest3-tree.jpg" style="width: 464px; height: 384px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,null,null,null,5,null,6], k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
	<li>All the values of the tree are <strong>unique</strong>.</li>
	<li>There exist some node in the tree where <code>Node.val == k</code>.</li>
</ul>

```python
class Solution:
   def findClosestLeaf(self, root: TreeNode, k: int) -> int:
       def dfs(root, p):
           if root:
               g[root].append(p)
               g[p].append(root)
               dfs(root.left, root)
               dfs(root.right, root)


       g = defaultdict(list)
       dfs(root, None)
       q = deque([node for node in g if node and node.val == k])
       seen = set()
       while q:
           node = q.popleft()
           seen.add(node)
           if node:
               if node.left is None and node.right is None:
                   return node.val
               for next in g[node]:
                   if next not in seen:
                       q.append(next)
```
# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)


## Description

<!-- description:start -->

<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
<strong>Explanation:</strong> The minimum window substring &quot;BANC&quot; includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;aa&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>

```python
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
```

```
763. Partition Labels
Medium
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.
 
Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:
Input: s = "eccbbbbdec"
Output: [10]
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
```

### Solution
```
Figure out the rightmost index first and use it to denote the start of the next section.
Reset the left pointer at the start of each new section.
Store the difference of right and left pointers + 1 as in the result for each section.
```

```python
class Solution:
   def partitionLabels(self, s: str) -> List[int]:
       d = {}
       for i in range(len(s)):
           d[s[i]] = i
       m = 0
       prev = -1
       res = []
       for i in range(len(s)):
           m = max(m, d[s[i]])
           if m == i:
               res.append(m - prev)
               prev = m
       return res
```

# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)

[中文文档](/solution/0000-0099/0008.String%20to%20Integer%20%28atoi%29/README.md)

## Description

<!-- description:start -->

<p>Implement the <code>myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer.</p>

<p>The algorithm for <code>myAtoi(string s)</code> is as follows:</p>

<ol>
	<li><strong>Whitespace</strong>: Ignore any leading whitespace (<code>&quot; &quot;</code>).</li>
	<li><strong>Signedness</strong>: Determine the sign by checking if the next character is <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code>, assuming positivity if neither present.</li>
	<li><strong>Conversion</strong>: Read the integer by skipping leading zeros&nbsp;until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.</li>
	<li><strong>Rounding</strong>: If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then round the integer to remain in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be rounded to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be rounded to <code>2<sup>31</sup> - 1</code>.</li>
</ol>

<p>Return the integer as the final result.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;42&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
The underlined characters are what is read in and the caret is the current reader position.
Step 1: &quot;42&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;42&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>42</u>&quot; (&quot;42&quot; is read in)
           ^
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot; -042&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;<u>   </u>-042&quot; (leading whitespace is read and ignored)
            ^
Step 2: &quot;   <u>-</u>042&quot; (&#39;-&#39; is read, so the result should be negative)
             ^
Step 3: &quot;   -<u>042</u>&quot; (&quot;042&quot; is read in, leading zeros ignored in the result)
               ^
</pre>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1337c0d3&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1337</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;1337c0d3&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;1337c0d3&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>1337</u>c0d3&quot; (&quot;1337&quot; is read in; reading stops because the next character is a non-digit)
             ^
</pre>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0-1&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;0-1&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;0-1&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>0</u>-1&quot; (&quot;0&quot; is read in; reading stops because the next character is a non-digit)
          ^
</pre>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;words and 987&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Reading stops at the first non-digit character &#39;w&#39;.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), digits (<code>0-9</code>), <code>&#39; &#39;</code>, <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, and <code>&#39;.&#39;</code>.</li>
</ul>

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        neg = s[0] == "-"
        pos = s[0] == "+"
        i = 1 if neg or pos else 0
        while i < len(s) and s[i] == "0":
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num *= 10
            num += int(s[i])
            i += 1
        if neg and num >= pow(2, 31):
            return -pow(2, 31)
        if num > pow(2, 31) - 1:
            num = pow(2, 31) - 1
        if neg:
            return -num
        return num
```
# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)

[中文文档](/solution/0000-0099/0081.Search%20in%20Rotated%20Sorted%20Array%20II/README.md)

## Description

<!-- description:start -->

<p>There is an integer array <code>nums</code> sorted in non-decreasing order (not necessarily with <strong>distinct</strong> values).</p>

<p>Before being passed to your function, <code>nums</code> is <strong>rotated</strong> at an unknown pivot index <code>k</code> (<code>0 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,4,4,5,6,6,7]</code> might be rotated at pivot index <code>5</code> and become <code>[4,5,6,6,7,0,1,2,4,4]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the rotation and an integer <code>target</code>, return <code>true</code><em> if </em><code>target</code><em> is in </em><code>nums</code><em>, or </em><code>false</code><em> if it is not in </em><code>nums</code><em>.</em></p>

<p>You must decrease the overall operation steps as much as possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 0
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 3
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is guaranteed to be rotated at some pivot.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> This problem is similar to&nbsp;<a href="/problems/search-in-rotated-sorted-array/description/" target="_blank">Search in Rotated Sorted Array</a>, but&nbsp;<code>nums</code> may contain <strong>duplicates</strong>. Would this affect the runtime complexity? How and why?</p>


```python
class Solution:
   def search(self, nums: List[int], target: int) -> int:
       low = 0
       high = len(nums) -1
       while low < high:
           mid = (low + high)//2
           if nums[mid] == target:
               return True
           while low < mid and nums[low] == nums[mid]:
               low += 1
           if nums[low] <= nums[mid]:
               if nums[low] <= target and target < nums[mid]:
                   high = mid -1
               else:
                   low = mid + 1
           else:
               if nums[mid] < target and target <= nums[high]:
                   low = mid + 1
               else:
                   high = mid -1
       return nums[low] == target
```

# [833. Find And Replace in String](https://leetcode.com/problems/find-and-replace-in-string)


## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>s</code> that you must perform <code>k</code> replacement operations on. The replacement operations are given as three <strong>0-indexed</strong> parallel arrays, <code>indices</code>, <code>sources</code>, and <code>targets</code>, all of length <code>k</code>.</p>

<p>To complete the <code>i<sup>th</sup></code> replacement operation:</p>

<ol>
	<li>Check if the <strong>substring</strong> <code>sources[i]</code> occurs at index <code>indices[i]</code> in the <strong>original string</strong> <code>s</code>.</li>
	<li>If it does not occur, <strong>do nothing</strong>.</li>
	<li>Otherwise if it does occur, <strong>replace</strong> that substring with <code>targets[i]</code>.</li>
</ol>

<p>For example, if <code>s = &quot;<u>ab</u>cd&quot;</code>, <code>indices[i] = 0</code>, <code>sources[i] = &quot;ab&quot;</code>, and <code>targets[i] = &quot;eee&quot;</code>, then the result of this replacement will be <code>&quot;<u>eee</u>cd&quot;</code>.</p>

<p>All replacement operations must occur <strong>simultaneously</strong>, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will <strong>not overlap</strong>.</p>

<ul>
	<li>For example, a testcase with <code>s = &quot;abc&quot;</code>, <code>indices = [0, 1]</code>, and <code>sources = [&quot;ab&quot;,&quot;bc&quot;]</code> will not be generated because the <code>&quot;ab&quot;</code> and <code>&quot;bc&quot;</code> replacements overlap.</li>
</ul>

<p>Return <em>the <strong>resulting string</strong> after performing all replacement operations on </em><code>s</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0833.Find%20And%20Replace%20in%20String/images/833-ex1.png" style="width: 411px; height: 251px;" />
<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, indices = [0, 2], sources = [&quot;a&quot;, &quot;cd&quot;], targets = [&quot;eee&quot;, &quot;ffff&quot;]
<strong>Output:</strong> &quot;eeebffff&quot;
<strong>Explanation:</strong>
&quot;a&quot; occurs at index 0 in s, so we replace it with &quot;eee&quot;.
&quot;cd&quot; occurs at index 2 in s, so we replace it with &quot;ffff&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0833.Find%20And%20Replace%20in%20String/images/833-ex2-1.png" style="width: 411px; height: 251px;" />
<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, indices = [0, 2], sources = [&quot;ab&quot;,&quot;ec&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>Output:</strong> &quot;eeecd&quot;
<strong>Explanation:</strong>
&quot;ab&quot; occurs at index 0 in s, so we replace it with &quot;eee&quot;.
&quot;ec&quot; does not occur at index 2 in s, so we do nothing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>k == indices.length == sources.length == targets.length</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= indexes[i] &lt; s.length</code></li>
	<li><code>1 &lt;= sources[i].length, targets[i].length &lt;= 50</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>sources[i]</code> and <code>targets[i]</code> consist of only lowercase English letters.</li>
</ul>

```python
class Solution:
    def findReplaceString(self, S, indices, sources, targets):
        modified = list(S)
        for index, source, target in zip(indices, sources, targets):
            if not S[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index + 1, len(source) + index):
                    modified[i] = ""
        return "".join(modified)

```
```
886. Possible Bipartition
Medium
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.
 
Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
 
Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= ai < bi <= n
All the pairs of dislikes are unique.
```

```python
class Solution:
   def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
      
       # Constant defined for color drawing to person
       BLUE, GREEN = 1, -1
       # -------------------------------------
       # Update dislike relationship, either a dislikes b, or b dislikes a       
       dislike = defaultdict(list)
       for a, b in dislikes:
           dislike[a].append(b)
           dislike[b].append(a)
      
       # Color map of each person
       color_of = dict()
       for person in range(1, N+1):
          
           # If this person has been draw, just skip
           if person in color_of: continue
          
           # Without the loss of generality, start drawing from BLUE       
           # (It can be GREEN if you like)
           color_of[person] = BLUE
           bfs_queue = deque([(person, BLUE)])
           while bfs_queue:
               cur, color = bfs_queue.popleft()
               for enemy in dislike[cur]:
                   if enemy not in color_of:
                       # Draw enemy with opposite color
                       color_of[enemy] = -1*color
                       bfs_queue.append( (enemy, color_of[enemy]) )
                   elif color_of[enemy] == color:
                       # If enemy and me have same color, woops, it is impossible to being bipartite
                       return False
                  
       return True
```
# [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack)


## Description

<!-- description:start -->

<p>Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.</p>

<p>Implement the <code>FreqStack</code> class:</p>

<ul>
	<li><code>FreqStack()</code> constructs an empty frequency stack.</li>
	<li><code>void push(int val)</code> pushes an integer <code>val</code> onto the top of the stack.</li>
	<li><code>int pop()</code> removes and returns the most frequent element in the stack.
	<ul>
		<li>If there is a tie for the most frequent element, the element closest to the stack&#39;s top is removed and returned.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;FreqStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, null, null, null, 5, 7, 5, 4]

<strong>Explanation</strong>
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= val &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>2 * 10<sup>4</sup></code> calls will be made to <code>push</code> and <code>pop</code>.</li>
	<li>It is guaranteed that there will be at least one element in the stack before calling <code>pop</code>.</li>
</ul>

### Solution with PQ:
```python
import queue
class FreqStack:
   def __init__(self):
       self.counter = Counter()
       self.index = 0
       self.q = queue.PriorityQueue()
   def push(self, x):
       self.counter[x] += 1
       self.q.put((-self.counter[x], -self.index, x))
       self.index += 1
   def pop(self):
       freq, index, x = self.q.get()
       self.counter[x] -= 1
       return x
```


### More Optimized solution:
```python
class FreqStack:
   def __init__(self):
       self.counter = Counter()
       self.freq_map = defaultdict(list)
       self.max_freq = 0
   def push(self, x):
       self.counter[x] += 1
       self.max_freq = max(self.max_freq, self.counter[x])
       self.freq_map[self.counter[x]].append(x)
   def pop(self):
       x = self.freq_map[self.max_freq].pop()
       self.counter[x] -= 1
       if not self.freq_map[self.max_freq]:
           self.max_freq -= 1
       return x
```

```
921. Minimum Add to Make Parentheses Valid
Medium
A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
 
Example 1:
Input: s = "())"
Output: 1
Example 2:
Input: s = "((("
Output: 3
 
Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
```

```python
class Solution:
   def minAddToMakeValid(self, s: str) -> int:
       open = 0
       close = 0
       for c in s:
           if c == "(":
               open += 1
           else:
               if open > 0:
                   open -= 1
               else:
                   close += 1
       return open + close
```

# [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name)


## Description

<!-- description:start -->

<p>Your friend is typing his <code>name</code> into a keyboard. Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code> characters of the keyboard. Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;alex&quot;, typed = &quot;aaleex&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>&#39;a&#39; and &#39;e&#39; in &#39;alex&#39; were long pressed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>&#39;e&#39; must have been pressed twice, but it was not in the typed output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length, typed.length &lt;= 1000</code></li>
	<li><code>name</code> and <code>typed</code> consist of only lowercase English letters.</li>
</ul>

```python
class Solution:   
   def isLongPressedName(self, name, typed):
       i = 0
       for j in range(len(typed)):
           if i < len(name) and name[i] == typed[j]:
               i += 1
           elif j == 0 or typed[j] != typed[j - 1]:
               return False
       return i == len(name)
```

# [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences)


## Description

<!-- description:start -->

<p>Given two integer arrays <code>pushed</code> and <code>popped</code> each with distinct values, return <code>true</code><em> if this could have been the result of a sequence of push and pop operations on an initially empty stack, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -&gt; 4,
push(5),
pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> 1 cannot be popped before 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pushed.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i] &lt;= 1000</code></li>
	<li>All the elements of <code>pushed</code> are <strong>unique</strong>.</li>
	<li><code>popped.length == pushed.length</code></li>
	<li><code>popped</code> is a permutation of <code>pushed</code>.</li>
</ul>


### Using Stack
```python
class Solution:
   def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
       s = []
       popped_index = 0
       for v in pushed:
           s.append(v)
           while s and s[-1] == popped[popped_index]:
               s.pop()
               popped_index += 1
       return not s
```


### Without using stack
Instead of using a stack we're gonna use pushed as the stack.  
Everything is, Same as above, the only difference is rather than using a new stack we can use the pushed ARRAY as a stack, using a pointer i. Initially i = 0, that means stack is empty.
```python
class Solution:
   def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
       popped_index = 0
       pushed_index = -1
       for i, v in enumerate(pushed):
           pushed_index += 1
           pushed[pushed_index] = pushed[i]
           while pushed_index >= 0 and popped[popped_index] == pushed[pushed_index]:
               popped_index += 1
               pushed_index -= 1
       return popped_index == len(popped) and pushed_index == -1
```

# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin)

## Description


<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane and an integer <code>k</code>, return the <code>k</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>The distance between two points on the <strong>X-Y</strong> plane is the Euclidean distance (i.e., <code>&radic;(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></code>).</p>

<p>You may return the answer in <strong>any order</strong>. The answer is <strong>guaranteed</strong> to be <strong>unique</strong> (except for the order that it is in).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0973.K%20Closest%20Points%20to%20Origin/images/closestplane1.jpg" style="width: 400px; height: 400px;" />
<pre>
<strong>Input:</strong> points = [[1,3],[-2,2]], k = 1
<strong>Output:</strong> [[-2,2]]
<strong>Explanation:</strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:</strong> [[3,3],[-2,4]]
<strong>Explanation:</strong> The answer [[-2,4],[3,3]] would also be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= points.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>

```python
from queue import PriorityQueue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = PriorityQueue()
        ans = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            q.put((-dist, p))
            if q.qsize() > k:
                q.get()
        while q.qsize():
            ans.append(q.get()[1])
        return ans
```
### Using quick select
Randomized QuickSelect
This solution is a modifed version of Quick-sort meant to be used when we need to find k(or kth) smallest(or largest) elements (based on some comparator) but not in any particular order. Most of the partition logic used in this algorithm remains the same as in quicksort but we just modify the recursive part of quicksort to suit our use case.

Each time, we choose a pivot and partition the array around that pivot using a comparator. In this case, we will choose a randomized pivot (the choice of pivot majorly affects the performace of algorithm and we need to try to choose a pivot that partitions the range roughly equally for best result. Without any knowledge of the way that elements occur in array, it's best to choose randomized pivot each time to avoid worst case) and for comparator, we will use the squared euclidean distance.

Initially we start with whole range of array [L, R] = [0, size(P)-1]. After each partition, the partition function will return the pivot index (denoted as p below) which is basically the element which separates all the elements <= than it to left side and all elements > than it to the right side (not in particular order). We have:

If p < k, then we now have p elements which are closest to origin (although they aren't sorted in any particular order) but we still need some more elements to get k points in total. Thus, we iterate again and partition the array from indices [p+1, R] till we find k elements (by getting pivot at kth index)
If p > k, then we now have more than k elements with us that are closest to origin. But we are sure that any element to the right of p wont be ever in our answer. So we iterate again and partition just the range [L, p-1] till we find k elements
If p == k, we now have exactly k elements with us which are closest to origin. Thus, we return the 1st k elements of array

Time Complexity : O(N), at each partition, we are eliminating one end and re-partitioning the other end till we get pivot at kth index. On average, the partitions roughly eliminate half of remaining elements each time thus leading to N + N/2 + N/4 + ... + 1 = O(2N) iterations. However, in the worst case, there's still a chance (although very low) that we choose the worst pivot at each partition and this leads to N + N-1 + N-2 + ... + 1 = N2 total iterations leading to time complexity of O(N2)
Space Complexity : O(1), only constant extra space is being used

```python
class Solution:
   def kClosest(self, P, k):
       euclidean = lambda p: p[0] ** 2 + p[1] ** 2
       def partition(L, R):
           random = randint(L, R)  # choosing random pivot
           P[R], P[random] = P[random], P[R]  # and swapping it to the end
           i, pivotDist = L, euclidean(P[R])
           for j in range(L, R):
               if euclidean(P[j]) < pivotDist:
                   P[i], P[j] = P[j], P[i]
                   i += 1
           P[i], P[R] = P[R], P[i]
           return i
       L, R, p = 0, len(P) - 1, len(P)
       while p != k:
           p = partition(L, R)
           if p < k:
               L = p + 1
           else:
               R = p - 1
       return P[:k]
```
# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

[中文文档](/solution/0000-0099/0098.Validate%20Binary%20Search%20Tree/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left <span data-keyword="subtree">subtree</span> of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0098.Validate%20Binary%20Search%20Tree/images/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0098.Validate%20Binary%20Search%20Tree/images/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node&#39;s value is 5 but its right child&#39;s value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return helper(root.left, min, root.val) and helper(
                root.right, root.val, max
            )

        return helper(root, float("-inf"), float("inf"))
```

# [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store)


## Description

<!-- description:start -->

<p>Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key&#39;s value at a certain timestamp.</p>

<p>Implement the <code>TimeMap</code> class:</p>

<ul>
	<li><code>TimeMap()</code> Initializes the object of the data structure.</li>
	<li><code>void set(String key, String value, int timestamp)</code> Stores the key <code>key</code> with the value <code>value</code> at the given time <code>timestamp</code>.</li>
	<li><code>String get(String key, int timestamp)</code> Returns a value such that <code>set</code> was called previously, with <code>timestamp_prev &lt;= timestamp</code>. If there are multiple such values, it returns the value associated with the largest <code>timestamp_prev</code>. If there are no values, it returns <code>&quot;&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;TimeMap&quot;, &quot;set&quot;, &quot;get&quot;, &quot;get&quot;, &quot;set&quot;, &quot;get&quot;, &quot;get&quot;]
[[], [&quot;foo&quot;, &quot;bar&quot;, 1], [&quot;foo&quot;, 1], [&quot;foo&quot;, 3], [&quot;foo&quot;, &quot;bar2&quot;, 4], [&quot;foo&quot;, 4], [&quot;foo&quot;, 5]]
<strong>Output</strong>
[null, null, &quot;bar&quot;, &quot;bar&quot;, null, &quot;bar2&quot;, &quot;bar2&quot;]

<strong>Explanation</strong>
TimeMap timeMap = new TimeMap();
timeMap.set(&quot;foo&quot;, &quot;bar&quot;, 1);  // store the key &quot;foo&quot; and value &quot;bar&quot; along with timestamp = 1.
timeMap.get(&quot;foo&quot;, 1);         // return &quot;bar&quot;
timeMap.get(&quot;foo&quot;, 3);         // return &quot;bar&quot;, since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is &quot;bar&quot;.
timeMap.set(&quot;foo&quot;, &quot;bar2&quot;, 4); // store the key &quot;foo&quot; and value &quot;bar2&quot; along with timestamp = 4.
timeMap.get(&quot;foo&quot;, 4);         // return &quot;bar2&quot;
timeMap.get(&quot;foo&quot;, 5);         // return &quot;bar2&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= key.length, value.length &lt;= 100</code></li>
	<li><code>key</code> and <code>value</code> consist of lowercase English letters and digits.</li>
	<li><code>1 &lt;= timestamp &lt;= 10<sup>7</sup></code></li>
	<li>All the timestamps <code>timestamp</code> of <code>set</code> are strictly increasing.</li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>set</code> and <code>get</code>.</li>
</ul>

### Solution for linear search to get()
Time complexity is O(N)
```python
class TimeMap:
   def __init__(self):
       self.d = collections.defaultdict(list)
       self.ts = {}
   def set(self, key: str, value: str, timestamp: int) -> None:
       self.d[key].append(timestamp)
       self.ts[timestamp] = value
   def get(self, key: str, timestamp: int) -> str:
       if key not in self.d:
           return ''
       t = self.d[key]
       for i in range(len(t)-1,-1,-1):
           if t[i] <= timestamp:
               return self.ts[t[i]]
       return ''
```
### Solution for binary search to get()
Time complexity is O(logN)
```python
class TimeMap(object):
   def __init__(self):
       self.dic = collections.defaultdict(list)
   def set(self, key, value, timestamp):
       self.dic[key].append([timestamp, value])
   def get(self, key, timestamp):
       arr = self.dic[key]
       left = 0
       right = len(arr)
       while left < right:
           mid = (left + right) // 2
           if arr[mid][0] > timestamp:
               right = mid
           else:
               left = mid + 1
       return "" if left == 0 else arr[left - 1][1]
```
# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges)


## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> <code>grid</code> where each cell can have one of three values:</p>

<ul>
	<li><code>0</code> representing an empty cell,</li>
	<li><code>1</code> representing a fresh orange, or</li>
	<li><code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>

<p>Return <em>the minimum number of minutes that must elapse until no cell has a fresh orange</em>. If <em>this is impossible, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0994.Rotting%20Oranges/images/oranges.png" style="width: 650px; height: 137px;" />
<pre>
<strong>Input:</strong> grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>grid[i][j]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>

```python
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
```
