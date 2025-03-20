---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0002.Add%20Two%20Numbers/README_EN.md
tags:
    - Recursion
    - Linked List
    - Math
---

<!-- problem:start -->

# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

[中文文档](/solution/0000-0099/0002.Add%20Two%20Numbers/README.md)

## Description

<!-- description:start -->

<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0002.Add%20Two%20Numbers/images/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We traverse two linked lists $l_1$ and $l_2$ at the same time, and use the variable $carry$ to indicate whether there is a carry.

Each time we traverse, we take out the current bit of the corresponding linked list, calculate the sum with the carry $carry$, and then update the value of the carry. Then we add the current bit to the answer linked list. If both linked lists are traversed, and the carry is $0$, the traversal ends.

Finally, we return the head node of the answer linked list.

The time complexity is $O(\max (m, n))$, where $m$ and $n$ are the lengths of the two linked lists. We need to traverse the entire position of the two linked lists, and each position only needs $O(1)$ time. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        carry, curr = 0, dummy
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

#### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        int carry = 0;
        ListNode cur = dummy;
        while (l1 != null || l2 != null || carry != 0) {
            int s = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
            carry = s / 10;
            cur.next = new ListNode(s % 10);
            cur = cur.next;
            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }
        return dummy.next;
    }
}
```

#### C++

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        int carry = 0;
        ListNode* cur = dummy;
        while (l1 || l2 || carry) {
            int s = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = s / 10;
            cur->next = new ListNode(s % 10);
            cur = cur->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        return dummy->next;
    }
};
```

#### Go

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	carry := 0
	cur := dummy
	for l1 != nil || l2 != nil || carry != 0 {
		s := carry
		if l1 != nil {
			s += l1.Val
		}
		if l2 != nil {
			s += l2.Val
		}
		carry = s / 10
		cur.Next = &ListNode{s % 10, nil}
		cur = cur.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	return dummy.Next
}
```

#### TypeScript

```ts
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let cur = dummy;
    let sum = 0;
    while (l1 != null || l2 != null || sum !== 0) {
        if (l1 != null) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2 != null) {
            sum += l2.val;
            l2 = l2.next;
        }
        cur.next = new ListNode(sum % 10);
        cur = cur.next;
        sum = Math.floor(sum / 10);
    }
    return dummy.next;
}
```

#### Rust

```rust
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode::new(0)));
        let mut cur = &mut dummy;
        let mut sum = 0;
        while l1.is_some() || l2.is_some() || sum != 0 {
            if let Some(node) = l1 {
                sum += node.val;
                l1 = node.next;
            }
            if let Some(node) = l2 {
                sum += node.val;
                l2 = node.next;
            }
            cur.as_mut().unwrap().next = Some(Box::new(ListNode::new(sum % 10)));
            cur = &mut cur.as_mut().unwrap().next;
            sum /= 10;
        }
        dummy.unwrap().next.take()
    }
}
```

#### JavaScript

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    const dummy = new ListNode();
    let carry = 0;
    let cur = dummy;
    while (l1 || l2 || carry) {
        const s = (l1?.val || 0) + (l2?.val || 0) + carry;
        carry = Math.floor(s / 10);
        cur.next = new ListNode(s % 10);
        cur = cur.next;
        l1 = l1?.next;
        l2 = l2?.next;
    }
    return dummy.next;
};
```

#### C#

```cs
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        int carry = 0;
        ListNode cur = dummy;
        while (l1 != null || l2 != null || carry != 0) {
            int s = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
            carry = s / 10;
            cur.next = new ListNode(s % 10);
            cur = cur.next;
            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }
        return dummy.next;
    }
}
```

#### PHP

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {
    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $dummy = new ListNode(0);
        $current = $dummy;
        $carry = 0;

        while ($l1 !== null || $l2 !== null) {
            $x = $l1 !== null ? $l1->val : 0;
            $y = $l2 !== null ? $l2->val : 0;

            $sum = $x + $y + $carry;
            $carry = (int) ($sum / 10);
            $current->next = new ListNode($sum % 10);
            $current = $current->next;

            if ($l1 !== null) {
                $l1 = $l1->next;
            }

            if ($l2 !== null) {
                $l2 = $l2->next;
            }
        }

        if ($carry > 0) {
            $current->next = new ListNode($carry);
        }

        return $dummy->next;
    }
}
```

#### Swift

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var dummy = ListNode.init()
        var carry = 0
        var l1 = l1
        var l2 = l2
        var cur = dummy
        while l1 != nil || l2 != nil || carry != 0 {
            let s = (l1?.val ?? 0) + (l2?.val ?? 0) + carry
            carry = s / 10
            cur.next = ListNode.init(s % 10)
            cur = cur.next!
            l1 = l1?.next
            l2 = l2?.next
        }
        return dummy.next
    }
}
```

#### Ruby

```rb
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    dummy = ListNode.new()
    carry = 0
    cur = dummy
    while !l1.nil? || !l2.nil? || carry > 0
        s = (l1.nil? ? 0 : l1.val) + (l2.nil? ? 0 : l2.val) + carry
        carry = s / 10
        cur.next = ListNode.new(s % 10)
        cur = cur.next
        l1 = l1.nil? ? l1 : l1.next
        l2 = l2.nil? ? l2 : l2.next
    end
    dummy.next
end
```

#### Nim

```nim
#[
    # Driver code in the solution file
    # Definition for singly-linked list.
    type
    Node[int] = ref object
        value: int
        next: Node[int]

    SinglyLinkedList[T] = object
        head, tail: Node[T]
]#

# More efficient code churning ...
proc addTwoNumbers(l1: var SinglyLinkedList, l2: var SinglyLinkedList): SinglyLinkedList[int] =
  var
    aggregate: SinglyLinkedList
    psum: seq[char]
    temp_la, temp_lb: seq[int]

  while not l1.head.isNil:
    temp_la.add(l1.head.value)
    l1.head = l1.head.next

  while not l2.head.isNil:
    temp_lb.add(l2.head.value)
    l2.head = l2.head.next

  psum = reversed($(reversed(temp_la).join("").parseInt() + reversed(temp_lb).join("").parseInt()))
  for i in psum: aggregate.append(($i).parseInt())

  result = aggregate
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0009.Palindrome%20Number/README_EN.md
tags:
    - Math
---

<!-- problem:start -->

# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number)

[中文文档](/solution/0000-0099/0009.Palindrome%20Number/README.md)

## Description

<!-- description:start -->

<p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Reverse Half of the Number

First, we determine special cases:

-   If $x < 0$, then $x$ is not a palindrome, directly return `false`;
-   If $x > 0$ and the last digit of $x$ is $0$, then $x$ is not a palindrome, directly return `false`;
-   If the last digit of $x$ is not $0$, then $x$ might be a palindrome, continue the following steps.

We reverse the second half of $x$ and compare it with the first half. If they are equal, then $x$ is a palindrome, otherwise, $x$ is not a palindrome.

For example, for $x = 1221$, we can reverse the second half from "21" to "12" and compare it with the first half "12". Since they are equal, we know that $x$ is a palindrome.

Let's see how to reverse the second half.

For the number $1221$, if we perform $1221 \bmod 10$, we will get the last digit $1$. To get the second last digit, we can first remove the last digit from $1221$ by dividing by $10$, $1221 / 10 = 122$, then get the remainder of the previous result divided by $10$, $122 \bmod 10 = 2$, to get the second last digit.

If we continue this process, we will get more reversed digits.

By continuously multiplying the last digit to the variable $y$, we can get the number in reverse order.

In the code implementation, we can repeatedly "take out" the last digit of $x$ and "add" it to the end of $y$, loop until $y \ge x$. If at this time $x = y$, or $x = y / 10$, then $x$ is a palindrome.

The time complexity is $O(\log_{10}(n))$, where $n$ is $x$. For each iteration, we will divide the input by $10$, so the time complexity is $O(\log_{10}(n))$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y // 10)
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0011.Container%20With%20Most%20Water/README_EN.md
tags:
    - Greedy
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water)

[中文文档](/solution/0000-0099/0011.Container%20With%20Most%20Water/README.md)

## Description

<!-- description:start -->

<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0011.Container%20With%20Most%20Water/images/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers $l$ and $r$ to point to the left and right ends of the array, respectively, i.e., $l = 0$ and $r = n - 1$, where $n$ is the length of the array.

Next, we use a variable $\textit{ans}$ to record the maximum capacity of the container, initially set to $0$.

Then, we start a loop. In each iteration, we calculate the current capacity of the container, i.e., $\textit{min}(height[l], height[r]) \times (r - l)$, and compare it with $\textit{ans}$, assigning the larger value to $\textit{ans}$. Then, we compare the values of $height[l]$ and $height[r]$. If $\textit{height}[l] < \textit{height}[r]$, moving the $r$ pointer will not improve the result because the height of the container is determined by the shorter vertical line, so we move the $l$ pointer. Otherwise, we move the $r$ pointer.

After the iteration, we return $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{height}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            t = min(height[l], height[r]) * (r - l)
            ans = max(ans, t)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0013.Roman%20to%20Integer/README_EN.md
tags:
    - Hash Table
    - Math
    - String
---

<!-- problem:start -->

# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer)

[中文文档](/solution/0000-0099/0013.Roman%20to%20Integer/README.md)

## Description

<!-- description:start -->

<p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two ones added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;III&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;LVIII&quot;
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;MCMXCIV&quot;
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s</code> contains only&nbsp;the characters <code>(&#39;I&#39;, &#39;V&#39;, &#39;X&#39;, &#39;L&#39;, &#39;C&#39;, &#39;D&#39;, &#39;M&#39;)</code>.</li>
	<li>It is <strong>guaranteed</strong>&nbsp;that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Simulation

First, we use a hash table $d$ to record the numerical value corresponding to each character. Then, we traverse the string $s$ from left to right. If the numerical value corresponding to the current character is less than the numerical value corresponding to the character on the right, we subtract the numerical value corresponding to the current character. Otherwise, we add the numerical value corresponding to the current character.

The time complexity is $O(n)$, and the space complexity is $O(m)$. Here, $n$ and $m$ are the length of the string $s$ and the size of the character set, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum((-1 if d[a] < d[b] else 1) * d[a] for a, b in pairwise(s)) + d[s[-1]]
```

#### Java

```java
class Solution {
    public int romanToInt(String s) {
        String cs = "IVXLCDM";
        int[] vs = {1, 5, 10, 50, 100, 500, 1000};
        Map<Character, Integer> d = new HashMap<>();
        for (int i = 0; i < vs.length; ++i) {
            d.put(cs.charAt(i), vs[i]);
        }
        int n = s.length();
        int ans = d.get(s.charAt(n - 1));
        for (int i = 0; i < n - 1; ++i) {
            int sign = d.get(s.charAt(i)) < d.get(s.charAt(i + 1)) ? -1 : 1;
            ans += sign * d.get(s.charAt(i));
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> nums{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int ans = nums[s.back()];
        for (int i = 0; i < s.size() - 1; ++i) {
            int sign = nums[s[i]] < nums[s[i + 1]] ? -1 : 1;
            ans += sign * nums[s[i]];
        }
        return ans;
    }
};
```

#### Go

```go
func romanToInt(s string) (ans int) {
	d := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	for i := 0; i < len(s)-1; i++ {
		if d[s[i]] < d[s[i+1]] {
			ans -= d[s[i]]
		} else {
			ans += d[s[i]]
		}
	}
	ans += d[s[len(s)-1]]
	return
}
```

#### TypeScript

```ts
function romanToInt(s: string): number {
    const d: Map<string, number> = new Map([
        ['I', 1],
        ['V', 5],
        ['X', 10],
        ['L', 50],
        ['C', 100],
        ['D', 500],
        ['M', 1000],
    ]);
    let ans: number = d.get(s[s.length - 1])!;
    for (let i = 0; i < s.length - 1; ++i) {
        const sign = d.get(s[i])! < d.get(s[i + 1])! ? -1 : 1;
        ans += sign * d.get(s[i])!;
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let d = vec![
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]
        .into_iter()
        .collect::<std::collections::HashMap<_, _>>();

        let s: Vec<char> = s.chars().collect();
        let mut ans = 0;
        let len = s.len();

        for i in 0..len - 1 {
            if d[&s[i]] < d[&s[i + 1]] {
                ans -= d[&s[i]];
            } else {
                ans += d[&s[i]];
            }
        }

        ans += d[&s[len - 1]];
        ans
    }
}
```

#### JavaScript

```js
const romanToInt = function (s) {
    const d = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
    let ans = d[s[s.length - 1]];
    for (let i = 0; i < s.length - 1; ++i) {
        const sign = d[s[i]] < d[s[i + 1]] ? -1 : 1;
        ans += sign * d[s[i]];
    }
    return ans;
};
```

#### C#

```cs
public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> d = new Dictionary<char, int>();
        d.Add('I', 1);
        d.Add('V', 5);
        d.Add('X', 10);
        d.Add('L', 50);
        d.Add('C', 100);
        d.Add('D', 500);
        d.Add('M', 1000);
        int ans = d[s[s.Length - 1]];
        for (int i = 0; i < s.Length - 1; ++i) {
            int sign = d[s[i]] < d[s[i + 1]] ? -1 : 1;
            ans += sign * d[s[i]];
        }
        return ans;
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $d = [
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
        ];
        $ans = 0;
        $len = strlen($s);

        for ($i = 0; $i < $len - 1; $i++) {
            if ($d[$s[$i]] < $d[$s[$i + 1]]) {
                $ans -= $d[$s[$i]];
            } else {
                $ans += $d[$s[$i]];
            }
        }

        $ans += $d[$s[$len - 1]];
        return $ans;
    }
}
```

#### Ruby

```rb
# @param {String} s
# @return {Integer}
def roman_to_int(s)
  d = {
      'I' => 1, 'V' => 5, 'X' => 10,
      'L' => 50, 'C' => 100,
      'D' => 500, 'M' => 1000
  }
  ans = 0
  len = s.length

  (0...len-1).each do |i|
      if d[s[i]] < d[s[i + 1]]
          ans -= d[s[i]]
      else
          ans += d[s[i]]
      end
  end

  ans += d[s[len - 1]]
  ans
end
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0014.Longest%20Common%20Prefix/README_EN.md
tags:
    - Trie
    - String
---

<!-- problem:start -->

# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

[中文文档](/solution/0000-0099/0014.Longest%20Common%20Prefix/README.md)

## Description

<!-- description:start -->

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Character Comparison

We use the first string $strs[0]$ as a benchmark, and compare whether the $i$-th character of the subsequent strings is the same as the $i$-th character of $strs[0]$. If they are the same, we continue to compare the next character. Otherwise, we return the first $i$ characters of $strs[0]$.

If the traversal ends, it means that the first $i$ characters of all strings are the same, and we return $strs[0]$.

The time complexity is $O(n \times m)$, where $n$ and $m$ are the length of the string array and the minimum length of the strings, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s) <= i or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
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
# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

[中文文档](/solution/0000-0099/0019.Remove%20Nth%20Node%20From%20End%20of%20List/README.md)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0019.Remove%20Nth%20Node%20From%20End%20of%20List/images/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do this in one pass?</p>

### Solution with One pass only
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

### Solution

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
### Time and Space Complexity
```
For those who curious about why Divide-Conquer method has TC : O(Nlog(N))

Splitting list into two, log(N) times = O(log(N))
Merging split lists into one in ascending order, need to traverse every element = O(N)
In Summary, we merging it log(N) times and in each merging we should traverse N element.
Therefore the Time Complexity is O(Nlog(N)) where n is the number of element.

In this case, the element is a linked list, so I think Time Complexity is O(Mlog(N))
N : number of linked lists
M : number of element of merged linked list
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
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0026.Remove%20Duplicates%20from%20Sorted%20Array/README_EN.md
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

[中文文档](/solution/0000-0099/0026.Remove%20Duplicates%20from%20Sorted%20Array/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>. Then return <em>the number of unique elements in </em><code>nums</code>.</p>

<p>Consider the number of unique elements of <code>nums</code> to be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the unique elements in the order they were present in <code>nums</code> initially. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

We use a variable $k$ to record the current length of the processed array. Initially, $k=0$ represents an empty array.

Then we traverse the array from left to right. For each element $x$ we encounter, if $k=0$ or $x \neq nums[k-1]$, we place $x$ in the position of $nums[k]$, and then increment $k$ by $1$. Otherwise, $x$ is the same as $nums[k-1]$, so we skip this element. Continue to traverse until the entire array is traversed.

In this way, when the traversal ends, the first $k$ elements in $nums$ are the answer we are looking for, and $k$ is the length of the answer.

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array.

Supplement:

The original problem requires that the same number appear at most once. We can extend it to keep at most $k$ identical numbers.

-   Since the same number can be kept at most $k$ times, we can directly keep the first $k$ elements of the original array;
-   For the following numbers, the premise of being able to keep them is: the current number $x$ is compared with the last $k$th element of the previously retained numbers. If they are different, keep them, otherwise skip them.

Similar problems:

-   [80. Remove Duplicates from Sorted Array II](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k
```

#### Java

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int x : nums) {
            if (k == 0 || x != nums[k - 1]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int x : nums) {
            if (k == 0 || x != nums[k - 1]) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

#### Go

```go
func removeDuplicates(nums []int) int {
	k := 0
	for _, x := range nums {
		if k == 0 || x != nums[k-1] {
			nums[k] = x
			k++
		}
	}
	return k
}
```

#### TypeScript

```ts
function removeDuplicates(nums: number[]): number {
    let k: number = 0;
    for (const x of nums) {
        if (k === 0 || x !== nums[k - 1]) {
            nums[k++] = x;
        }
    }
    return k;
}
```

#### Rust

```rust
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut k = 0;
        for i in 0..nums.len() {
            if k == 0 || nums[i] != nums[k - 1] {
                nums[k] = nums[i];
                k += 1;
            }
        }
        k as i32
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let k = 0;
    for (const x of nums) {
        if (k === 0 || x !== nums[k - 1]) {
            nums[k++] = x;
        }
    }
    return k;
};
```

#### C#

```cs
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int k = 0;
        foreach (int x in nums) {
            if (k == 0 || x != nums[k - 1]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $k = 0;
        foreach ($nums as $x) {
            if ($k == 0 || $x != $nums[$k - 1]) {
                $nums[$k++] = $x;
            }
        }
        return $k;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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

## Meta variant
VARIANT: What if you had to find the previous permutation?

```python
class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        peak = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                peak = i - 1
                break

        if peak is None:
            nums.reverse()
            return

        next_lower = len(nums) - 1
        while nums[next_lower] >= nums[peak]:
            next_lower -= 1

        nums[peak], nums[next_lower] = nums[next_lower], nums[peak]

        left = peak + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    # Basic cases
    solution = Solution()
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 3, 5]
    nums = [3, 2, 1]
    solution.previousPermutation(nums)
    assert nums == [3, 1, 2]
    nums = [1, 2, 3]
    solution.previousPermutation(nums)
    assert nums == [3, 2, 1]
    nums = [9, 6, 5, 4, 3, 2]
    solution.previousPermutation(nums)
    assert nums == [9, 6, 5, 4, 2, 3]
    nums = [4, 5, 1, 1, 3, 7]
    solution.previousPermutation(nums)
    assert nums == [4, 3, 7, 5, 1, 1]
    nums = [1, 5, 8, 5, 1, 3, 4, 6, 7]
    solution.previousPermutation(nums)
    assert nums == [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]

    # Single digit case
    nums = [5]
    solution.previousPermutation(nums)
    assert nums == [5]

    # Duplicate digits case
    nums = [1, 1, 1]
    solution.previousPermutation(nums)
    assert nums == [1, 1, 1]

    # Already smallest case (loops around)
    nums = [1, 2, 3, 4, 5, 6]
    solution.previousPermutation(nums)
    assert nums == [6, 5, 4, 3, 2, 1]
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

## Meta variant
 What if you had to return the number of unique elements in an integer array?
Note this must be done in K LOG N time complexity (unless the input has all unique integers)

```python
class Solution:
    def countUnique(self, nums: list[int]) -> int:
        # Should run in O(k * log(N)) complexity, where k is # of unique elements
        if len(nums) == 0:
            return 0

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = 0
        count = 0
        while start < len(nums):
            end = upper(nums, nums[start])
            start = end + 1
            count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    # Nonzero Count cases
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    assert solution.countUnique(nums) == 5
    nums = [-3, -2, -1, 0, 1, 2, 3]
    assert solution.countUnique(nums) == 7
    nums = [-3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert solution.countUnique(nums) == 7
    nums = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 6
    nums = [19, 19, 19, 19]
    assert solution.countUnique(nums) == 1
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution.countUnique(nums) == 1
    nums = [9001]
    assert solution.countUnique(nums) == 1
    nums = [5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 4
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.countUnique(nums) == 10

    # Zero Count case
    nums = []
    assert solution.countUnique(nums) == 0
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0043.Multiply%20Strings/README_EN.md
tags:
    - Math
    - String
    - Simulation
---

<!-- problem:start -->

# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings)

[中文文档](/solution/0000-0099/0043.Multiply%20Strings/README.md)

## Description

<!-- description:start -->

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Note:</strong>&nbsp;You must not use any built-in BigInteger library or convert the inputs to integer directly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num1 = "2", num2 = "3"
<strong>Output:</strong> "6"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num1 = "123", num2 = "456"
<strong>Output:</strong> "56088"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1.length, num2.length &lt;= 200</code></li>
	<li><code>num1</code> and <code>num2</code> consist of digits only.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number <code>0</code> itself.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulating Mathematical Multiplication

Assume the lengths of $num1$ and $num2$ are $m$ and $n$ respectively, then the length of their product can be at most $m + n$.

The proof is as follows:

-   If $num1$ and $num2$ both take the minimum value, then their product is ${10}^{m - 1} \times {10}^{n - 1} = {10}^{m + n - 2}$, with a length of $m + n - 1$.
-   If $num1$ and $num2$ both take the maximum value, then their product is $({10}^m - 1) \times ({10}^n - 1) = {10}^{m + n} - {10}^m - {10}^n + 1$, with a length of $m + n$.

Therefore, we can apply for an array of length $m + n$ to store each digit of the product.

From the least significant digit to the most significant digit, we calculate each digit of the product in turn, and finally convert the array into a string.

Note to check whether the most significant digit is $0$, if it is, remove it.

The time complexity is $O(m \times n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the lengths of $num1$ and $num2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                prod_pos = i + j + 1
                res[prod_pos] += int(num1[i]) * int(num2[j])
                res[prod_pos - 1] += res[prod_pos] // 10
                res[prod_pos] = res[prod_pos] % 10
        res = "".join(map(str, res))
        return "0" if not res.lstrip("0") else res.lstrip("0")
```

#### Java

```java
class Solution {
    public String multiply(String num1, String num2) {
        if ("0".equals(num1) || "0".equals(num2)) {
            return "0";
        }
        int m = num1.length(), n = num2.length();
        int[] arr = new int[m + n];
        for (int i = m - 1; i >= 0; --i) {
            int a = num1.charAt(i) - '0';
            for (int j = n - 1; j >= 0; --j) {
                int b = num2.charAt(j) - '0';
                arr[i + j + 1] += a * b;
            }
        }
        for (int i = arr.length - 1; i > 0; --i) {
            arr[i - 1] += arr[i] / 10;
            arr[i] %= 10;
        }
        int i = arr[0] == 0 ? 1 : 0;
        StringBuilder ans = new StringBuilder();
        for (; i < arr.length; ++i) {
            ans.append(arr[i]);
        }
        return ans.toString();
    }
}
```

#### C++

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        int m = num1.size(), n = num2.size();
        vector<int> arr(m + n);
        for (int i = m - 1; i >= 0; --i) {
            int a = num1[i] - '0';
            for (int j = n - 1; j >= 0; --j) {
                int b = num2[j] - '0';
                arr[i + j + 1] += a * b;
            }
        }
        for (int i = arr.size() - 1; i; --i) {
            arr[i - 1] += arr[i] / 10;
            arr[i] %= 10;
        }
        int i = arr[0] ? 0 : 1;
        string ans;
        for (; i < arr.size(); ++i) {
            ans += '0' + arr[i];
        }
        return ans;
    }
};
```

#### Go

```go
func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	m, n := len(num1), len(num2)
	arr := make([]int, m+n)
	for i := m - 1; i >= 0; i-- {
		a := int(num1[i] - '0')
		for j := n - 1; j >= 0; j-- {
			b := int(num2[j] - '0')
			arr[i+j+1] += a * b
		}
	}
	for i := len(arr) - 1; i > 0; i-- {
		arr[i-1] += arr[i] / 10
		arr[i] %= 10
	}
	i := 0
	if arr[0] == 0 {
		i = 1
	}
	ans := []byte{}
	for ; i < len(arr); i++ {
		ans = append(ans, byte('0'+arr[i]))
	}
	return string(ans)
}
```

#### TypeScript

```ts
function multiply(num1: string, num2: string): string {
    if (num1 === '0' || num2 === '0') {
        return '0';
    }
    const m: number = num1.length;
    const n: number = num2.length;
    const arr: number[] = Array(m + n).fill(0);
    for (let i: number = m - 1; i >= 0; i--) {
        const a: number = +num1[i];
        for (let j: number = n - 1; j >= 0; j--) {
            const b: number = +num2[j];
            arr[i + j + 1] += a * b;
        }
    }
    for (let i: number = arr.length - 1; i > 0; i--) {
        arr[i - 1] += Math.floor(arr[i] / 10);
        arr[i] %= 10;
    }
    let i: number = 0;
    while (i < arr.length && arr[i] === 0) {
        i++;
    }
    return arr.slice(i).join('');
}
```

#### Rust

```rust
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return String::from("0");
        }
        let (num1, num2) = (num1.as_bytes(), num2.as_bytes());
        let (n, m) = (num1.len(), num2.len());
        let mut res = vec![];
        for i in 0..n {
            let a = num1[n - i - 1] - b'0';
            let mut sum = 0;
            let mut j = 0;
            while j < m || sum != 0 {
                if i + j == res.len() {
                    res.push(0);
                }
                let b = num2.get(m - j - 1).unwrap_or(&b'0') - b'0';
                sum += a * b + res[i + j];
                res[i + j] = sum % 10;
                sum /= 10;
                j += 1;
            }
        }
        res.into_iter()
            .rev()
            .map(|v| char::from(v + b'0'))
            .collect()
    }
}
```

#### C#

```cs
public class Solution {
    public string Multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        int m = num1.Length;
        int n = num2.Length;
        int[] arr = new int[m + n];

        for (int i = m - 1; i >= 0; i--) {
            int a = num1[i] - '0';
            for (int j = n - 1; j >= 0; j--) {
                int b = num2[j] - '0';
                arr[i + j + 1] += a * b;
            }
        }

        for (int i = arr.Length - 1; i > 0; i--) {
            arr[i - 1] += arr[i] / 10;
            arr[i] %= 10;
        }

        int index = 0;
        while (index < arr.Length && arr[index] == 0) {
            index++;
        }

        StringBuilder ans = new StringBuilder();
        for (; index < arr.Length; index++) {
            ans.Append(arr[index]);
        }

        return ans.ToString();
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param string $num1
     * @param string $num2
     * @return string
     */

    function multiply($num1, $num2) {
        $length1 = strlen($num1);
        $length2 = strlen($num2);
        $product = array_fill(0, $length1 + $length2, 0);

        for ($i = $length1 - 1; $i >= 0; $i--) {
            for ($j = $length2 - 1; $j >= 0; $j--) {
                $digit1 = intval($num1[$i]);
                $digit2 = intval($num2[$j]);

                $temp = $digit1 * $digit2 + $product[$i + $j + 1];
                $product[$i + $j + 1] = $temp % 10;

                $carry = intval($temp / 10);
                $product[$i + $j] += $carry;
            }
        }
        $result = implode('', $product);
        $result = ltrim($result, '0');
        return $result === '' ? '0' : $result;
    }
}
```

#### Kotlin

```kotlin
class Solution {
    fun multiply(num1: String, num2: String): String {
        if (num1 == "0" || num2 == "0") return "0"

        val chars_1 = num1.toCharArray().reversedArray()
        val chars_2 = num2.toCharArray().reversedArray()

        val result = mutableListOf<Int>()

        chars_1.forEachIndexed { i, c1 ->
            val multiplier_1 = c1 - '0'
            var over = 0
            var index = 0

            fun sum(product: Int = 0): Unit {
                while (index >= result.size) {
                    result.add(0)
                }
                val value = product + over + result[index]
                result[index] = value % 10
                over = value / 10
                return
            }

            chars_2.forEachIndexed { j, c2 ->
                index = i + j
                val multiplier_2 = c2 - '0'
                sum(multiplier_1 * multiplier_2)
            }

            while (over > 0) {
                index++
                sum()
            }
        }

        return result.reversed().joinToString("")
    }
}
```

#### JavaScript

```js
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
    if (num1 === '0' || num2 === '0') return '0';

    const result = Array(num1.length + num2.length).fill(0);
    const code_0 = '0'.charCodeAt(0);

    const num1_len = num1.length;
    const num2_len = num2.length;

    for (let i = 0; i < num1_len; ++i) {
        const multiplier_1 = num1.charCodeAt(num1_len - i - 1) - code_0;
        for (let j = 0; j < num2_len; ++j) {
            const multiplier_2 = num2.charCodeAt(num2_len - j - 1) - code_0;
            result[i + j] += multiplier_1 * multiplier_2;
        }
    }

    result.reduce((carry, value, index) => {
        const sum = carry + value;
        result[index] = sum % 10;
        return (sum / 10) | 0;
    }, 0);

    return result
        .slice(0, result.findLastIndex(d => d !== 0) + 1)
        .reverse()
        .join('');
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0049.Group%20Anagrams/README_EN.md
tags:
    - Array
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

[中文文档](/solution/0000-0099/0049.Group%20Anagrams/README.md)

## Description

<!-- description:start -->

<p>Given an array of strings <code>strs</code>, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>&quot;bat&quot;</code>.</li>
	<li>The strings <code>&quot;nat&quot;</code> and <code>&quot;tan&quot;</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>&quot;ate&quot;</code>, <code>&quot;eat&quot;</code>, and <code>&quot;tea&quot;</code> are anagrams as they can be rearranged to form each other.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;&quot;]]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

1. Traverse the string array, sort each string in **character dictionary order** to get a new string.
2. Use the new string as `key` and `[str]` as `value`, and store them in the hash table (`HashMap<String, List<String>>`).
3. When encountering the same `key` during subsequent traversal, add it to the corresponding `value`.

Take `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]` as an example. At the end of the traversal, the state of the hash table is:

| key     | value                   |
| ------- | ----------------------- |
| `"aet"` | `["eat", "tea", "ate"]` |
| `"ant"` | `["tan", "nat"] `       |
| `"abt"` | `["bat"] `              |

Finally, return the `value` list of the hash table.

The time complexity is $O(n\times k\times \log k)$, where $n$ and $k$ are the lengths of the string array and the maximum length of the string, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        return list(d.values())
```


### Solution 2: Counting

We can also change the sorting part in Solution 1 to counting, that is, use the characters in each string $s$ and their occurrence times as `key`, and use the string $s$ as `value` to store in the hash table.

The time complexity is $O(n\times (k + C))$, where $n$ and $k$ are the lengths of the string array and the maximum length of the string, respectively, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(s)
        return list(d.values())
```

#### Counting and using count as key
You have to create the key like this and you can't use counters. Remember Counters cannot be used as a key for dictionary.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for s in strs:
            count = [0] * 256
            for c in s:
                count[ord(c)] += 1
            d[tuple(count)].append(s)
        return list(d.values())
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
        if n < 0:
            return self.myPow(float(1 / x), -n)

        half = self.myPow(x, n // 2)
        power = half * half
        if n % 2 == 1:
            power = power * x
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

## Meta variant
What if you had to merge two interval lists instead of one?
```python
from typing import List

def try_merge(result: List[List[int]], curr_interval: List[int]):
    if not result or curr_interval[0] > result[-1][1]:
        result.append(curr_interval)
    else:
        result[-1][1] = max(curr_interval[1], result[-1][1])

def merge_2_interval_lists_56_variant_python(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][0]:
            curr_interval = A[i]
            i += 1
        else:
            curr_interval = B[j]
            j += 1

        try_merge(result, curr_interval)

    if i < len(A):
        while i < len(A):
            try_merge(result, A[i])
            i += 1
    else:
        while j < len(B):
            try_merge(result, B[j])
            j += 1

    return result

if __name__ == "__main__":
    A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
    B = [[2, 8], [13, 20]]
    expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = []
    B = [[2, 8], [13, 20]]
    expected = [[2, 8], [13, 20]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [10, 15], [20, 25]]
    B = [[5, 10], [15, 20]]
    expected = [[1, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [11, 15], [21, 25]]
    B = [[6, 10], [16, 20]]
    expected = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)
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

## Meta variant
What if you didn't have to implement exponents?
```python
class Solution(object):
    def isNumber(self, s: str):
        seen_digit, seen_dot = [False, False]
        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in {"+", "-"}:
                if i != 0:
                    return False
            elif s[i] == ".":
                if seen_dot:
                    return False
                seen_dot = True
            else:
                return False

        if not seen_digit:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNumber("0089")
    assert solution.isNumber("-0.1")
    assert solution.isNumber("+3.14")
    assert solution.isNumber("4.")
    assert solution.isNumber("-.9")
    assert solution.isNumber("420")
    assert solution.isNumber("+3")
    assert solution.isNumber("-10")
    assert solution.isNumber("2")
    # Exponents not valid anymore
    assert not solution.isNumber("3e+7")
    assert not solution.isNumber("+6e-1")
    assert not solution.isNumber("53.5e93")
    assert not solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("2e10")
    assert not solution.isNumber("-90E3")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")
    assert not solution.isNumber("7..")
    assert not solution.isNumber(".")
    assert not solution.isNumber("3-")
    assert not solution.isNumber("+7e5")
    assert not solution.isNumber("7E5")
    assert not solution.isNumber("7ee")
    assert not solution.isNumber("7e")
    assert not solution.isNumber("8e1.2")
    assert not solution.isNumber("+20e-5")
    assert not solution.isNumber("Abc")
```


---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0066.Plus%20One/README_EN.md
tags:
    - Array
    - Math
---

<!-- problem:start -->

# [66. Plus One](https://leetcode.com/problems/plus-one)

[中文文档](/solution/0000-0099/0066.Plus%20One/README.md)

## Description

<!-- description:start -->

<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>&#39;s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>&#39;s.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We start traversing from the last element of the array, add one to the current element, and then take the modulus by $10$. If the result is not $0$, it means that there is no carry for the current element, and we can directly return the array. Otherwise, the current element is $0$ and needs to be carried over. We continue to traverse the previous element and repeat the above operation. If we still haven't returned after traversing the array, it means that all elements in the array are $0$, and we need to insert a $1$ at the beginning of the array.

The time complexity is $O(n)$, where $n$ is the length of the array. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
```

#### Java

```java
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; --i) {
            ++digits[i];
            digits[i] %= 10;
            if (digits[i] != 0) {
                return digits;
            }
        }
        digits = new int[n + 1];
        digits[0] = 1;
        return digits;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i) {
            ++digits[i];
            digits[i] %= 10;
            if (digits[i] != 0) return digits;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

#### Go

```go
func plusOne(digits []int) []int {
	n := len(digits)
	for i := n - 1; i >= 0; i-- {
		digits[i]++
		digits[i] %= 10
		if digits[i] != 0 {
			return digits
		}
	}
	return append([]int{1}, digits...)
}
```

#### TypeScript

```ts
function plusOne(digits: number[]): number[] {
    const n = digits.length;
    for (let i = n - 1; i >= 0; i--) {
        if (10 > ++digits[i]) {
            return digits;
        }
        digits[i] %= 10;
    }
    return [1, ...digits];
}
```

#### Rust

```rust
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let n = digits.len();
        for i in (0..n).rev() {
            digits[i] += 1;
            if 10 > digits[i] {
                return digits;
            }
            digits[i] %= 10;
        }
        digits.insert(0, 1);
        digits
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    for (let i = digits.length - 1; i >= 0; --i) {
        ++digits[i];
        digits[i] %= 10;
        if (digits[i] != 0) {
            return digits;
        }
    }
    return [1, ...digits];
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0070.Climbing%20Stairs/README_EN.md
tags:
    - Memoization
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs)

[中文文档](/solution/0000-0099/0070.Climbing%20Stairs/README.md)

## Description

<!-- description:start -->

<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

We define $f[i]$ to represent the number of ways to climb to the $i$-th step, then $f[i]$ can be transferred from $f[i - 1]$ and $f[i - 2]$, that is:

$$
f[i] = f[i - 1] + f[i - 2]
$$

The initial conditions are $f[0] = 1$ and $f[1] = 1$, that is, the number of ways to climb to the 0th step is 1, and the number of ways to climb to the 1st step is also 1.

The answer is $f[n]$.

Since $f[i]$ is only related to $f[i - 1]$ and $f[i - 2]$, we can use two variables $a$ and $b$ to maintain the current number of ways, reducing the space complexity to $O(1)$.

The time complexity is $O(n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b
```

#### Java

```java
class Solution {
    public int climbStairs(int n) {
        int a = 0, b = 1;
        for (int i = 0; i < n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int climbStairs(int n) {
        int a = 0, b = 1;
        for (int i = 0; i < n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```

#### Go

```go
func climbStairs(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return b
}
```

#### TypeScript

```ts
function climbStairs(n: number): number {
    let p = 1;
    let q = 1;
    for (let i = 1; i < n; i++) {
        [p, q] = [q, p + q];
    }
    return q;
}
```

#### Rust

```rust
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let (mut p, mut q) = (1, 1);
        for i in 1..n {
            let t = p + q;
            p = q;
            q = t;
        }
        q
    }
}
```

#### JavaScript

```js
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    let a = 0,
        b = 1;
    for (let i = 0; i < n; ++i) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
};
```

#### PHP

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        if ($n <= 2) {
            return $n;
        }
        $dp = [0, 1, 2];
        for ($i = 3; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 2] + $dp[$i - 1];
        }
        return $dp[$n];
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Matrix Quick Power to Accelerate Recursion

We set $Fib(n)$ to represent a $1 \times 2$ matrix $\begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}$, where $F_n$ and $F_{n - 1}$ are the $n$-th and $(n - 1)$-th Fibonacci numbers respectively.

We hope to derive $Fib(n)$ based on $Fib(n-1) = \begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix}$. That is to say, we need a matrix $base$, so that $Fib(n - 1) \times base = Fib(n)$, that is:

$$
\begin{bmatrix}
F_{n - 1} & F_{n - 2}
\end{bmatrix} \times base = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

Since $F_n = F_{n - 1} + F_{n - 2}$, the first column of the matrix $base$ is:

$$
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

The second column is:

$$
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Therefore:

$$
\begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix} \times \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix} = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

We define the initial matrix $res = \begin{bmatrix} 1 & 1 \end{bmatrix}$, then $F_n$ is equal to the first element of the first row of the result matrix of $res$ multiplied by $base^{n - 1}$. We can solve it using matrix quick power.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
import numpy as np


class Solution:
    def climbStairs(self, n: int) -> int:
        res = np.asmatrix([(1, 1)], np.dtype("O"))
        factor = np.asmatrix([(1, 1), (1, 0)], np.dtype("O"))
        n -= 1
        while n:
            if n & 1:
                res *= factor
            factor *= factor
            n >>= 1
        return res[0, 0]
```

#### Java

```java
class Solution {
    private final int[][] a = {{1, 1}, {1, 0}};

    public int climbStairs(int n) {
        return pow(a, n - 1)[0][0];
    }

    private int[][] mul(int[][] a, int[][] b) {
        int m = a.length, n = b[0].length;
        int[][] c = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < a[0].length; ++k) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;
    }

    private int[][] pow(int[][] a, int n) {
        int[][] res = {{1, 1}, {0, 0}};
        while (n > 0) {
            if ((n & 1) == 1) {
                res = mul(res, a);
            }
            n >>= 1;
            a = mul(a, a);
        }
        return res;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<vector<long long>> a = {{1, 1}, {1, 0}};
        return pow(a, n - 1)[0][0];
    }

private:
    vector<vector<long long>> mul(vector<vector<long long>>& a, vector<vector<long long>>& b) {
        int m = a.size(), n = b[0].size();
        vector<vector<long long>> res(m, vector<long long>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < a[0].size(); ++k) {
                    res[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return res;
    }

    vector<vector<long long>> pow(vector<vector<long long>>& a, int n) {
        vector<vector<long long>> res = {{1, 1}, {0, 0}};
        while (n) {
            if (n & 1) {
                res = mul(res, a);
            }
            a = mul(a, a);
            n >>= 1;
        }
        return res;
    }
};
```

#### Go

```go
type matrix [2][2]int

func climbStairs(n int) int {
	a := matrix{{1, 1}, {1, 0}}
	return pow(a, n-1)[0][0]
}

func mul(a, b matrix) (c matrix) {
	m, n := len(a), len(b[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < len(a[0]); k++ {
				c[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return
}

func pow(a matrix, n int) matrix {
	res := matrix{{1, 1}, {0, 0}}
	for n > 0 {
		if n&1 == 1 {
			res = mul(res, a)
		}
		a = mul(a, a)
		n >>= 1
	}
	return res
}
```

#### TypeScript

```ts
function climbStairs(n: number): number {
    const a = [
        [1, 1],
        [1, 0],
    ];
    return pow(a, n - 1)[0][0];
}

function mul(a: number[][], b: number[][]): number[][] {
    const [m, n] = [a.length, b[0].length];
    const c = Array(m)
        .fill(0)
        .map(() => Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            for (let k = 0; k < a[0].length; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}

function pow(a: number[][], n: number): number[][] {
    let res = [
        [1, 1],
        [0, 0],
    ];
    while (n) {
        if (n & 1) {
            res = mul(res, a);
        }
        a = mul(a, a);
        n >>= 1;
    }
    return res;
}
```

#### JavaScript

```js
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    const a = [
        [1, 1],
        [1, 0],
    ];
    return pow(a, n - 1)[0][0];
};

function mul(a, b) {
    const [m, n] = [a.length, b[0].length];
    const c = Array(m)
        .fill(0)
        .map(() => Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            for (let k = 0; k < a[0].length; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}

function pow(a, n) {
    let res = [
        [1, 1],
        [0, 0],
    ];
    while (n) {
        if (n & 1) {
            res = mul(res, a);
        }
        a = mul(a, a);
        n >>= 1;
    }
    return res;
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
# [71. Simplify Path](https://leetcode.com/problems/simplify-path)


## Description

<!-- description:start -->

<p>You are given an <em>absolute</em> path for a Unix-style file system, which always begins with a slash <code>&#39;/&#39;</code>. Your task is to transform this absolute path into its <strong>simplified canonical path</strong>.</p>

<p>The <em>rules</em> of a Unix-style file system are as follows:</p>

<ul>
	<li>A single period <code>&#39;.&#39;</code> represents the current directory.</li>
	<li>A double period <code>&#39;..&#39;</code> represents the previous/parent directory.</li>
	<li>Multiple consecutive slashes such as <code>&#39;//&#39;</code> and <code>&#39;///&#39;</code> are treated as a single slash <code>&#39;/&#39;</code>.</li>
	<li>Any sequence of periods that does <strong>not match</strong> the rules above should be treated as a <strong>valid directory or</strong> <strong>file </strong><strong>name</strong>. For example, <code>&#39;...&#39; </code>and <code>&#39;....&#39;</code> are valid directory or file names.</li>
</ul>

<p>The simplified canonical path should follow these <em>rules</em>:</p>

<ul>
	<li>The path must start with a single slash <code>&#39;/&#39;</code>.</li>
	<li>Directories within the path must be separated by exactly one slash <code>&#39;/&#39;</code>.</li>
	<li>The path must not end with a slash <code>&#39;/&#39;</code>, unless it is the root directory.</li>
	<li>The path must not have any single or double periods (<code>&#39;.&#39;</code> and <code>&#39;..&#39;</code>) used to denote current or parent directories.</li>
</ul>

<p>Return the <strong>simplified canonical path</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home/&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The trailing slash should be removed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home//foo/&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home/foo&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Multiple consecutive slashes are replaced by a single one.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home/user/Documents/../Pictures&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home/user/Pictures&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>A double period <code>&quot;..&quot;</code> refers to the directory up a level (the parent directory).</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/../&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Going one level up from the root directory is not possible.</p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/.../a/../b/c/../d/./&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/.../b/d&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>&quot;...&quot;</code> is a valid name for a directory in this problem.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 3000</code></li>
	<li><code>path</code> consists of English letters, digits, period <code>&#39;.&#39;</code>, slash <code>&#39;/&#39;</code> or <code>&#39;_&#39;</code>.</li>
	<li><code>path</code> is a valid absolute Unix path.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We first split the path into a number of substrings split by `'/'`. Then, we traverse each substring and perform the following operations based on the content of the substring:

-   If the substring is empty or `'.'`, no operation is performed because `'.'` represents the current directory.
-   If the substring is `'..'`, the top element of the stack is popped, because `'..'` represents the parent directory.
-   If the substring is other strings, the substring is pushed into the stack, because the substring represents the subdirectory of the current directory.

Finally, we concatenate all the elements in the stack from the bottom to the top of the stack to form a string, which is the simplified canonical path.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the path.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for s in path.split("/"):
            # if not s is used to check for repeating / in the path
            # split function will return a empty string for multiple /
            # Ex - '/a/b/c//d////e'.split('/') = ['', 'a', 'b', 'c', '', 'd', '', '', '', 'e']
            if not s or s == ".":
                continue
            if s == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        return "/" + "/".join(stk)
```

## Meta variant
 What if you were given a new "cd" parameter to change where you currently were on your filesystem (represented by "cwd")? If "cd" starts with "/" then this has many implications on the code.

 ```python
class Solution:
    def changeDirectory(self, cwd: str, cd: str) -> str:
        if not cd:
            return cwd
        
        if cd[0] == '/':
            cwd = ''
        
        tokens = []
        for token in cwd.split('/'):
            if token:
                tokens.append(token)
        
        for token in cd.split('/'):
            if not token:
                continue
            if token == '.':
                continue
            elif token == '..':
                if tokens:
                    tokens.pop()
            else:
                tokens.append(token)
        
        if not tokens:
            return '/'
        
        return '/' + '/'.join(tokens)

if __name__ == "__main__":
    solution = Solution()
    assert solution.changeDirectory("/a/b/c", "/d/./e") == "/d/e"
    assert solution.changeDirectory("", "/d/./e") == "/d/e"
    assert solution.changeDirectory("/a/b/c", "") == "/a/b/c"
    assert solution.changeDirectory("/a/b", ".//c/../../d/f") == "/a/d/f"
    assert solution.changeDirectory("/", "foo") == "/foo"
    assert solution.changeDirectory("/", "foo/bar/././xyz///") == "/foo/bar/xyz"
    assert solution.changeDirectory("/baz", "/bar") == "/bar"
    assert solution.changeDirectory("/foo/bar", "../../../../..") == "/"
    assert solution.changeDirectory("/x/y", "../p/../q") == "/x/q"
    assert solution.changeDirectory("/x/y", "/p/./q") == "/p/q"
    assert solution.changeDirectory("/facebook/anin", "../abc/def") == "/facebook/abc/def"
    assert solution.changeDirectory("/facebook/instagram", "../../../../.") == "/"
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0075.Sort%20Colors/README_EN.md
tags:
    - Array
    - Two Pointers
    - Sorting
---

<!-- problem:start -->

# [75. Sort Colors](https://leetcode.com/problems/sort-colors)

[中文文档](/solution/0000-0099/0075.Sort%20Colors/README.md)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library&#39;s sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Three Pointers

We define three pointers $i$, $j$, and $k$. Pointer $i$ is used to point to the rightmost boundary of the elements with a value of $0$ in the array, and pointer $j$ is used to point to the leftmost boundary of the elements with a value of $2$ in the array. Initially, $i=-1$, $j=n$. Pointer $k$ is used to point to the current element being traversed, initially $k=0$.

When $k < j$, we perform the following operations:

-   If $nums[k] = 0$, then swap it with $nums[i+1]$, then increment both $i$ and $k$ by $1$;
-   If $nums[k] = 2$, then swap it with $nums[j-1]$, then decrement $j$ by $1$;
-   If $nums[k] = 1$, then increment $k$ by $1$.

After the traversal, the elements in the array are divided into three parts: $[0,i]$, $[i+1,j-1]$ and $[j,n-1]$.

The time complexity is $O(n)$, where $n$ is the length of the array. Only one traversal of the array is needed. The space complexity is $O(1)$.

```

procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
```
<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = -1, len(nums), 0
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif nums[k] == 2:
                j -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                k += 1
```

#### Java

```java
class Solution {
    public void sortColors(int[] nums) {
        int i = -1, j = nums.length, k = 0;
        while (k < j) {
            if (nums[k] == 0) {
                swap(nums, ++i, k++);
            } else if (nums[k] == 2) {
                swap(nums, --j, k);
            } else {
                ++k;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}
```

#### C++

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = -1, j = nums.size(), k = 0;
        while (k < j) {
            if (nums[k] == 0) {
                swap(nums[++i], nums[k++]);
            } else if (nums[k] == 2) {
                swap(nums[--j], nums[k]);
            } else {
                ++k;
            }
        }
    }
};
```

#### Go

```go
func sortColors(nums []int) {
	i, j, k := -1, len(nums), 0
	for k < j {
		if nums[k] == 0 {
			i++
			nums[i], nums[k] = nums[k], nums[i]
			k++
		} else if nums[k] == 2 {
			j--
			nums[j], nums[k] = nums[k], nums[j]
		} else {
			k++
		}
	}
}
```

#### TypeScript

```ts
/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    let i = -1;
    let j = nums.length;
    let k = 0;
    while (k < j) {
        if (nums[k] === 0) {
            ++i;
            [nums[i], nums[k]] = [nums[k], nums[i]];
            ++k;
        } else if (nums[k] === 2) {
            --j;
            [nums[j], nums[k]] = [nums[k], nums[j]];
        } else {
            ++k;
        }
    }
}
```

#### Rust

```rust
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut i = -1;
        let mut j = nums.len();
        let mut k = 0;
        while k < j {
            if nums[k] == 0 {
                i += 1;
                nums.swap(i as usize, k as usize);
                k += 1;
            } else if nums[k] == 2 {
                j -= 1;
                nums.swap(j, k);
            } else {
                k += 1;
            }
        }
    }
}
```

#### C#

```cs
public class Solution {
    public void SortColors(int[] nums) {
        int i = -1, j = nums.Length, k = 0;
        while (k < j) {
            if (nums[k] == 0) {
                swap(nums, ++i, k++);
            } else if (nums[k] == 2) {
                swap(nums, --j, k);
            } else {
                ++k;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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

---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0078.Subsets/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - Backtracking
---

<!-- problem:start -->

# [78. Subsets](https://leetcode.com/problems/subsets)

[中文文档](/solution/0000-0099/0078.Subsets/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS (Backtracking)

We design a function $dfs(i)$, which represents starting the search from the $i$th element of the array for all subsets. The execution logic of the function $dfs(i)$ is as follows:

-   If $i = n$, it means the current search has ended. Add the current subset $t$ to the answer array $ans$, and then return.
-   Otherwise, we can choose not to select the current element and directly execute $dfs(i + 1)$; or we can choose the current element, i.e., add the current element $nums[i]$ to the subset $t$, and then execute $dfs(i + 1)$. Note that we need to remove $nums[i]$ from the subset $t$ after executing $dfs(i + 1)$ (backtracking).

In the main function, we call $dfs(0)$, i.e., start searching all subsets from the first element of the array. Finally, return the answer array $ans$.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array. There are a total of $2^n$ subsets, and each subset takes $O(n)$ time to construct.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def util(index, curr):
            if index >= len(nums):
                res.append(curr)
                return
            util(index + 1, curr)
            util(index + 1, curr + [nums[index]])

        util(0, [])
        return res
```

#### Java

```java
class Solution {
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> t = new ArrayList<>();
    private int[] nums;

    public List<List<Integer>> subsets(int[] nums) {
        this.nums = nums;
        dfs(0);
        return ans;
    }

    private void dfs(int i) {
        if (i == nums.length) {
            ans.add(new ArrayList<>(t));
            return;
        }
        dfs(i + 1);
        t.add(nums[i]);
        dfs(i + 1);
        t.remove(t.size() - 1);
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int)> dfs = [&](int i) -> void {
            if (i == nums.size()) {
                ans.push_back(t);
                return;
            }
            dfs(i + 1);
            t.push_back(nums[i]);
            dfs(i + 1);
            t.pop_back();
        };
        dfs(0);
        return ans;
    }
};
```

#### Go

```go
func subsets(nums []int) (ans [][]int) {
	t := []int{}
	var dfs func(int)
	dfs = func(i int) {
		if i == len(nums) {
			ans = append(ans, append([]int(nil), t...))
			return
		}
		dfs(i + 1)
		t = append(t, nums[i])
		dfs(i + 1)
		t = t[:len(t)-1]
	}
	dfs(0)
	return
}
```

#### TypeScript

```ts
function subsets(nums: number[]): number[][] {
    const ans: number[][] = [];
    const t: number[] = [];
    const dfs = (i: number) => {
        if (i === nums.length) {
            ans.push(t.slice());
            return;
        }
        dfs(i + 1);
        t.push(nums[i]);
        dfs(i + 1);
        t.pop();
    };
    dfs(0);
    return ans;
}
```

#### Rust

```rust
impl Solution {
    fn dfs(i: usize, t: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>, nums: &Vec<i32>) {
        if i == nums.len() {
            ans.push(t.clone());
            return;
        }
        Self::dfs(i + 1, t, ans, nums);
        t.push(nums[i]);
        Self::dfs(i + 1, t, ans, nums);
        t.pop();
    }

    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        Self::dfs(0, &mut Vec::new(), &mut ans, &nums);
        ans
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Enumeration

We can also use the method of binary enumeration to get all subsets.

We can use $2^n$ binary numbers to represent all subsets of $n$ elements. For the current binary number $mask$, if the $i$th bit is $1$, it means that the $i$th element is selected, otherwise it means that the $i$th element is not selected.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array. There are a total of $2^n$ subsets, and each subset takes $O(n)$ time to construct.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for mask in range(1 << len(nums)):
            t = [x for i, x in enumerate(nums) if mask >> i & 1]
            ans.append(t)
        return ans
```

#### Java

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for (int mask = 0; mask < 1 << n; ++mask) {
            List<Integer> t = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                if (((mask >> i) & 1) == 1) {
                    t.add(nums[i]);
                }
            }
            ans.add(t);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        for (int mask = 0; mask < 1 << n; ++mask) {
            vector<int> t;
            for (int i = 0; i < n; ++i) {
                if (mask >> i & 1) {
                    t.emplace_back(nums[i]);
                }
            }
            ans.emplace_back(t);
        }
        return ans;
    }
};
```

#### Go

```go
func subsets(nums []int) (ans [][]int) {
	n := len(nums)
	for mask := 0; mask < 1<<n; mask++ {
		t := []int{}
		for i, x := range nums {
			if mask>>i&1 == 1 {
				t = append(t, x)
			}
		}
		ans = append(ans, t)
	}
	return
}
```

#### TypeScript

```ts
function subsets(nums: number[]): number[][] {
    const n = nums.length;
    const ans: number[][] = [];
    for (let mask = 0; mask < 1 << n; ++mask) {
        const t: number[] = [];
        for (let i = 0; i < n; ++i) {
            if (((mask >> i) & 1) === 1) {
                t.push(nums[i]);
            }
        }
        ans.push(t);
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let mut ans = Vec::new();
        for mask in 0..(1 << n) {
            let mut t = Vec::new();
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    t.push(nums[i]);
                }
            }
            ans.push(t);
        }
        ans
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README_EN.md
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii)

[中文文档](/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears <strong>at most twice</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code>k</code>&nbsp;elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,3]
<strong>Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
<strong>Output:</strong> 7, nums = [0,0,1,1,2,3,3,_,_]
<strong>Explanation:</strong> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

We use a variable $k$ to record the current length of the array that has been processed. Initially, $k=0$, representing an empty array.

Then we traverse the array from left to right. For each element $x$ we traverse, if $k < 2$ or $x \neq nums[k-2]$, we put $x$ in the position of $nums[k]$, and then increment $k$ by $1$. Otherwise, $x$ is the same as $nums[k-2]$, we directly skip this element. Continue to traverse until the entire array is traversed.

In this way, when the traversal ends, the first $k$ elements in $nums$ are the answer we want, and $k$ is the length of the answer.

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array.

Supplement:

The original problem requires that the same number appears at most $2$ times. We can extend it to keep at most $k$ identical numbers.

-   Since the same number can be kept at most $k$ times, we can directly keep the first $k$ elements of the original array;
-   For the later numbers, the premise of being able to keep them is: the current number $x$ compares with the $k$th element from the end of the previously kept numbers. If they are different, keep it, otherwise skip it.

Similar problems:

-   [26. Remove Duplicates from Sorted Array](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0026.Remove%20Duplicates%20from%20Sorted%20Array/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k
```

#### Java

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int x : nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int x : nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

#### Go

```go
func removeDuplicates(nums []int) int {
	k := 0
	for _, x := range nums {
		if k < 2 || x != nums[k-2] {
			nums[k] = x
			k++
		}
	}
	return k
}
```

#### TypeScript

```ts
function removeDuplicates(nums: number[]): number {
    let k = 0;
    for (const x of nums) {
        if (k < 2 || x !== nums[k - 2]) {
            nums[k++] = x;
        }
    }
    return k;
}
```

#### Rust

```rust
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut k = 0;
        for i in 0..nums.len() {
            if k < 2 || nums[i] != nums[k - 2] {
                nums[k] = nums[i];
                k += 1;
            }
        }
        k as i32
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let k = 0;
    for (const x of nums) {
        if (k < 2 || x !== nums[k - 2]) {
            nums[k++] = x;
        }
    }
    return k;
};
```

#### C#

```cs
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int k = 0;
        foreach (int x in nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)

[中文文档](/solution/0000-0099/0088.Merge%20Sorted%20Array/README.md)

## Description

<!-- description:start -->

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in <strong>non-decreasing order</strong>, and two integers <code>m</code> and <code>n</code>, representing the number of elements in <code>nums1</code> and <code>nums2</code> respectively.</p>

<p><strong>Merge</strong> <code>nums1</code> and <code>nums2</code> into a single array sorted in <strong>non-decreasing order</strong>.</p>

<p>The final sorted array should not be returned by the function, but instead be <em>stored inside the array </em><code>nums1</code>. To accommodate this, <code>nums1</code> has a length of <code>m + n</code>, where the first <code>m</code> elements denote the elements that should be merged, and the last <code>n</code> elements are set to <code>0</code> and should be ignored. <code>nums2</code> has a length of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
<strong>Explanation:</strong> The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [1] and [].
The result of the merge is [1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= m + n &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Can you come up with an algorithm that runs in <code>O(m + n)</code> time?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers $i$ and $j$ pointing to the end of two arrays, and a pointer $k$ pointing to the end of the merged array.

Every time we compare the two elements at the end of the two arrays, and move the larger one to the end of the merged array. Then we move the pointer one step forward, and repeat this process until the two pointers reach the start of the arrays.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of two arrays. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0090.Subsets%20II/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - Backtracking
---

<!-- problem:start -->

# [90. Subsets II](https://leetcode.com/problems/subsets-ii)

[中文文档](/solution/0000-0099/0090.Subsets%20II/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span><em> (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + DFS

We can first sort the array $\textit{nums}$ to facilitate deduplication.

Then, we design a function $\textit{dfs}(i)$, which represents the current search for subsets starting from the $i$-th element. The execution logic of the function $\textit{dfs}(i)$ is as follows:

If $i \geq n$, it means all elements have been searched, add the current subset to the answer array, and end the recursion.

If $i < n$, add the $i$-th element to the subset, execute $\textit{dfs}(i + 1)$, then remove the $i$-th element from the subset. Next, we check if the $i$-th element is the same as the next element. If they are the same, skip the element in a loop until we find the first element different from the $i$-th element, then execute $\textit{dfs}(i + 1)$.

Finally, we only need to call $\textit{dfs}(0)$ and return the answer array.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subutil(index, curr):
            if index >= len(nums):
                res.append(curr)
                return
            subutil(index + 1, curr + [nums[index]])
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            subutil(index + 1, curr)

        nums.sort()
        subutil(0, [])
        return res
```

#### Java

```java
class Solution {
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> t = new ArrayList<>();
    private int[] nums;

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        this.nums = nums;
        dfs(0);
        return ans;
    }

    private void dfs(int i) {
        if (i >= nums.length) {
            ans.add(new ArrayList<>(t));
            return;
        }
        t.add(nums[i]);
        dfs(i + 1);
        int x = t.remove(t.size() - 1);
        while (i + 1 < nums.length && nums[i + 1] == x) {
            ++i;
        }
        dfs(i + 1);
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        vector<int> t;
        int n = nums.size();
        auto dfs = [&](this auto&& dfs, int i) {
            if (i >= n) {
                ans.push_back(t);
                return;
            }
            t.push_back(nums[i]);
            dfs(i + 1);
            t.pop_back();
            while (i + 1 < n && nums[i + 1] == nums[i]) {
                ++i;
            }
            dfs(i + 1);
        };
        dfs(0);
        return ans;
    }
};
```

#### Go

```go
func subsetsWithDup(nums []int) (ans [][]int) {
	slices.Sort(nums)
	n := len(nums)
	t := []int{}
	var dfs func(int)
	dfs = func(i int) {
		if i >= n {
			ans = append(ans, slices.Clone(t))
			return
		}
		t = append(t, nums[i])
		dfs(i + 1)
		t = t[:len(t)-1]
		for i+1 < n && nums[i+1] == nums[i] {
			i++
		}
		dfs(i + 1)
	}
	dfs(0)
	return
}
```

#### TypeScript

```ts
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const t: number[] = [];
    const ans: number[][] = [];
    const dfs = (i: number): void => {
        if (i >= n) {
            ans.push([...t]);
            return;
        }
        t.push(nums[i]);
        dfs(i + 1);
        t.pop();
        while (i + 1 < n && nums[i] === nums[i + 1]) {
            i++;
        }
        dfs(i + 1);
    };
    dfs(0);
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let mut ans = Vec::new();
        let mut t = Vec::new();

        fn dfs(i: usize, nums: &Vec<i32>, t: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>) {
            if i >= nums.len() {
                ans.push(t.clone());
                return;
            }
            t.push(nums[i]);
            dfs(i + 1, nums, t, ans);
            t.pop();
            let mut i = i;
            while i + 1 < nums.len() && nums[i + 1] == nums[i] {
                i += 1;
            }
            dfs(i + 1, nums, t, ans);
        }

        dfs(0, &nums, &mut t, &mut ans);
        ans
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const t = [];
    const ans = [];
    const dfs = i => {
        if (i >= n) {
            ans.push([...t]);
            return;
        }
        t.push(nums[i]);
        dfs(i + 1);
        t.pop();
        while (i + 1 < n && nums[i] === nums[i + 1]) {
            i++;
        }
        dfs(i + 1);
    };
    dfs(0);
    return ans;
};
```

#### C#

```cs
public class Solution {
    private IList<IList<int>> ans = new List<IList<int>>();
    private IList<int> t = new List<int>();
    private int[] nums;

    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        Array.Sort(nums);
        this.nums = nums;
        Dfs(0);
        return ans;
    }

    private void Dfs(int i) {
        if (i >= nums.Length) {
            ans.Add(new List<int>(t));
            return;
        }
        t.Add(nums[i]);
        Dfs(i + 1);
        t.RemoveAt(t.Count - 1);
        while (i + 1 < nums.Length && nums[i + 1] == nums[i]) {
            ++i;
        }
        Dfs(i + 1);
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Binary Enumeration

Similar to Solution 1, we first sort the array $\textit{nums}$ to facilitate deduplication.

Next, we enumerate a binary number $\textit{mask}$ in the range $[0, 2^n)$, where the binary representation of $\textit{mask}$ is an $n$-bit bit string. If the $i$-th bit of $\textit{mask}$ is $1$, it means selecting $\textit{nums}[i]$, and $0$ means not selecting $\textit{nums}[i]$. Note that if the $(i - 1)$-th bit of $\textit{mask}$ is $0$ and $\textit{nums}[i] = \textit{nums}[i - 1]$, it means that the $i$-th element is the same as the $(i - 1)$-th element in the current enumeration scheme. To avoid duplication, we skip this case. Otherwise, we add the subset corresponding to $\textit{mask}$ to the answer array.

After the enumeration, we return the answer array.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for mask in range(1 << n):
            ok = True
            t = []
            for i in range(n):
                if mask >> i & 1:
                    if i and (mask >> (i - 1) & 1) == 0 and nums[i] == nums[i - 1]:
                        ok = False
                        break
                    t.append(nums[i])
            if ok:
                ans.append(t)
        return ans
```

#### Java

```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for (int mask = 0; mask < 1 << n; ++mask) {
            List<Integer> t = new ArrayList<>();
            boolean ok = true;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i & 1) == 1) {
                    if (i > 0 && (mask >> (i - 1) & 1) == 0 && nums[i] == nums[i - 1]) {
                        ok = false;
                        break;
                    }
                    t.add(nums[i]);
                }
            }
            if (ok) {
                ans.add(t);
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        ranges::sort(nums);
        int n = nums.size();
        vector<vector<int>> ans;
        for (int mask = 0; mask < 1 << n; ++mask) {
            vector<int> t;
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i & 1) == 1) {
                    if (i > 0 && (mask >> (i - 1) & 1) == 0 && nums[i] == nums[i - 1]) {
                        ok = false;
                        break;
                    }
                    t.push_back(nums[i]);
                }
            }
            if (ok) {
                ans.push_back(t);
            }
        }
        return ans;
    }
};
```

#### Go

```go
func subsetsWithDup(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	for mask := 0; mask < 1<<n; mask++ {
		t := []int{}
		ok := true
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				if i > 0 && mask>>(i-1)&1 == 0 && nums[i] == nums[i-1] {
					ok = false
					break
				}
				t = append(t, nums[i])
			}
		}
		if ok {
			ans = append(ans, t)
		}
	}
	return
}
```

#### TypeScript

```ts
function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const ans: number[][] = [];
    for (let mask = 0; mask < 1 << n; ++mask) {
        const t: number[] = [];
        let ok: boolean = true;
        for (let i = 0; i < n; ++i) {
            if (((mask >> i) & 1) === 1) {
                if (i && ((mask >> (i - 1)) & 1) === 0 && nums[i] === nums[i - 1]) {
                    ok = false;
                    break;
                }
                t.push(nums[i]);
            }
        }
        if (ok) {
            ans.push(t);
        }
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut ans = Vec::new();
        for mask in 0..1 << n {
            let mut t = Vec::new();
            let mut ok = true;
            for i in 0..n {
                if ((mask >> i) & 1) == 1 {
                    if i > 0 && ((mask >> (i - 1)) & 1) == 0 && nums[i] == nums[i - 1] {
                        ok = false;
                        break;
                    }
                    t.push(nums[i]);
                }
            }
            if ok {
                ans.push(t);
            }
        }
        ans
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const ans = [];
    for (let mask = 0; mask < 1 << n; ++mask) {
        const t = [];
        let ok = true;
        for (let i = 0; i < n; ++i) {
            if (((mask >> i) & 1) === 1) {
                if (i && ((mask >> (i - 1)) & 1) === 0 && nums[i] === nums[i - 1]) {
                    ok = false;
                    break;
                }
                t.push(nums[i]);
            }
        }
        if (ok) {
            ans.push(t);
        }
    }
    return ans;
};
```

#### C#

```cs
public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        IList<IList<int>> ans = new List<IList<int>>();
        for (int mask = 0; mask < 1 << n; ++mask) {
            IList<int> t = new List<int>();
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i & 1) == 1) {
                    if (i > 0 && (mask >> (i - 1) & 1) == 0 && nums[i] == nums[i - 1]) {
                        ok = false;
                        break;
                    }
                    t.Add(nums[i]);
                }
            }
            if (ok) {
                ans.Add(t);
            }
        }
        return ans;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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

### Another BFS Solution with less checking for index and length
```python
class Solution:
    def connect(self, root):
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    # Pay attention here we are appending the right before left
                    # which mean we are doing level order from right to left.
                    # this saves us a lot of length and index checking
                    q.append(cur.right)
                    q.append(curr.left)
        return root
```

### Solution 2: Recursion
```python
class Solution:
    def connect(self, root):
        if not root:
            return None

        def helper(root):
            if not root:
                return
            if root.left:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                helper(root.right)
                helper(root.left)

        helper(root)
        return root
```

### Solution3 (Iterative. No extra space)
* We first populate the next pointers of child nodes of current level. This makes it possible to traverse the next level without using a queue. To populate next pointers of child, the exact same logic as above is used
* We simply traverse to root's left child and repeat the process - traverse current level, fill next pointers of child nodes and then again update root = root -> left. So, we are basically performing standard BFS traversal in O(1) space by using next pointers to our advantage
* The process continues till we reach the last level of tree

```python
class Solution:
    def connect(self, root):
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                else:
                    break
                cur = cur.next
        return head
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0121.Best%20Time%20to%20Buy%20and%20Sell%20Stock/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

[中文文档](/solution/0100-0199/0121.Best%20Time%20to%20Buy%20and%20Sell%20Stock/README.md)

## Description

<!-- description:start -->

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate + Maintain the Minimum Value of the Prefix

We can enumerate each element of the array $nums$ as the selling price. Then we need to find a minimum value in front of it as the purchase price to maximize the profit.

Therefore, we use a variable $mi$ to maintain the prefix minimum value of the array $nums$. Then we traverse the array $nums$ and for each element $v$, calculate the difference between it and the minimum value $mi$ in front of it, and update the answer to the maximum of the difference. Then update $mi = min(mi, v)$. Continue to traverse the array $nums$ until the traversal ends.

Finally, return the answer.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mi = 0, inf
        for v in prices:
            ans = max(ans, v - mi)
            mi = min(mi, v)
        return ans
```

## Meta variant
What if you had to return the minimum cost to buy a roundtrip flight?
Note you cannot fly somewhere and back on the same day.

```python
def find_cheapest_tickets(departures, returns):
    min_departure_cost = departures[0]
    min_cost = float('inf')
    
    for i in range(1, len(departures)):
        min_cost = min(min_cost, min_departure_cost + returns[i])

        if departures[i] < min_departure_cost:
            min_departure_cost = departures[i]
    
    return min_cost

if __name__ == "__main__":
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0122.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/README_EN.md
tags:
    - Greedy
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)

[中文文档](/solution/0100-0199/0122.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/README.md)

## Description

<!-- description:start -->

<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>On each day, you may decide to buy and/or sell the stock. You can only hold <strong>at most one</strong> share of the stock at any time. However, you can buy it then immediately sell it on the <strong>same day</strong>.</p>

<p>Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy Algorithm

Starting from the second day, if the stock price is higher than the previous day, buy on the previous day and sell on the current day to make a profit. If the stock price is lower than the previous day, do not buy or sell. In other words, buy and sell on all rising trading days, and do not trade on all falling trading days. The final profit will be the maximum.

The time complexity is $O(n)$, where $n$ is the length of the `prices` array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMinimum, profit = float("inf"), 0
        for price in prices:
            if price < currentMinimum:
                currentMinimum = price
            else:
                profit += price - currentMinimum
                currentMinimum = price
        return profit
```

#### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        for (int i = 1; i < prices.length; ++i) {
            ans += Math.max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        for (int i = 1; i < prices.size(); ++i) ans += max(0, prices[i] - prices[i - 1]);
        return ans;
    }
};
```

#### Go

```go
func maxProfit(prices []int) (ans int) {
	for i, v := range prices[1:] {
		t := v - prices[i]
		if t > 0 {
			ans += t
		}
	}
	return
}
```

#### TypeScript

```ts
function maxProfit(prices: number[]): number {
    let ans = 0;
    for (let i = 1; i < prices.length; i++) {
        ans += Math.max(0, prices[i] - prices[i - 1]);
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut res = 0;
        for i in 1..prices.len() {
            res += (0).max(prices[i] - prices[i - 1]);
        }
        res
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let ans = 0;
    for (let i = 1; i < prices.length; i++) {
        ans += Math.max(0, prices[i] - prices[i - 1]);
    }
    return ans;
};
```

#### C#

```cs
public class Solution {
    public int MaxProfit(int[] prices) {
        int ans = 0;
        for (int i = 1; i < prices.Length; ++i) {
            ans += Math.Max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i][j]$ as the maximum profit after trading on the $i$th day, where $j$ indicates whether we currently hold the stock. When holding the stock, $j=0$, and when not holding the stock, $j=1$. The initial state is $f[0][0]=-prices[0]$, and all other states are $0$.

If we currently hold the stock, it may be that we held the stock the day before and do nothing today, i.e., $f[i][0]=f[i-1][0]$. Or it may be that we did not hold the stock the day before and bought the stock today, i.e., $f[i][0]=f[i-1][1]-prices[i]$.

If we currently do not hold the stock, it may be that we did not hold the stock the day before and do nothing today, i.e., $f[i][1]=f[i-1][1]$. Or it may be that we held the stock the day before and sold the stock today, i.e., $f[i][1]=f[i-1][0]+prices[i]$.

Therefore, we can write the state transition equation as:

$$
\begin{cases}
f[i][0]=\max(f[i-1][0],f[i-1][1]-prices[i])\\
f[i][1]=\max(f[i-1][1],f[i-1][0]+prices[i])
\end{cases}
$$

The final answer is $f[n-1][1]$, where $n$ is the length of the `prices` array.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the `prices` array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][0] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] - prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 1][0] + prices[i])
        return f[n - 1][1]
```

#### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] f = new int[n][2];
        f[0][0] = -prices[0];
        for (int i = 1; i < n; ++i) {
            f[i][0] = Math.max(f[i - 1][0], f[i - 1][1] - prices[i]);
            f[i][1] = Math.max(f[i - 1][1], f[i - 1][0] + prices[i]);
        }
        return f[n - 1][1];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int f[n][2];
        f[0][0] = -prices[0];
        f[0][1] = 0;
        for (int i = 1; i < n; ++i) {
            f[i][0] = max(f[i - 1][0], f[i - 1][1] - prices[i]);
            f[i][1] = max(f[i - 1][1], f[i - 1][0] + prices[i]);
        }
        return f[n - 1][1];
    }
};
```

#### Go

```go
func maxProfit(prices []int) int {
	n := len(prices)
	f := make([][2]int, n)
	f[0][0] = -prices[0]
	for i := 1; i < n; i++ {
		f[i][0] = max(f[i-1][0], f[i-1][1]-prices[i])
		f[i][1] = max(f[i-1][1], f[i-1][0]+prices[i])
	}
	return f[n-1][1]
}
```

#### C#

```cs
public class Solution {
    public int MaxProfit(int[] prices) {
        int f1 = -prices[0], f2 = 0;
        for (int i = 1; i < prices.Length; ++i)
        {
            f1 = Math.Max(f1, f2 - prices[i]);
            f2 = Math.Max(f2, f1 + prices[i]);
        }
        return f2;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming (Space Optimization)

We can find that in Solution 2, the state of the $i$th day is only related to the state of the $i-1$th day. Therefore, we can use only two variables to maintain the state of the $i-1$th day, thereby optimizing the space complexity to $O(1)$.

The time complexity is $O(n)$, where $n$ is the length of the `prices` array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [-prices[0], 0]
        for i in range(1, n):
            g = [0] * 2
            g[0] = max(f[0], f[1] - prices[i])
            g[1] = max(f[1], f[0] + prices[i])
            f = g
        return f[1]
```

#### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] f = new int[] {-prices[0], 0};
        for (int i = 1; i < n; ++i) {
            int[] g = new int[2];
            g[0] = Math.max(f[0], f[1] - prices[i]);
            g[1] = Math.max(f[1], f[0] + prices[i]);
            f = g;
        }
        return f[1];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int f[2] = {-prices[0], 0};
        for (int i = 1; i < n; ++i) {
            int g[2];
            g[0] = max(f[0], f[1] - prices[i]);
            g[1] = max(f[1], f[0] + prices[i]);
            f[0] = g[0], f[1] = g[1];
        }
        return f[1];
    }
};
```

#### Go

```go
func maxProfit(prices []int) int {
	n := len(prices)
	f := [2]int{-prices[0], 0}
	for i := 1; i < n; i++ {
		g := [2]int{}
		g[0] = max(f[0], f[1]-prices[i])
		g[1] = max(f[1], f[0]+prices[i])
		f = g
	}
	return f[1]
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0123.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)

[中文文档](/solution/0100-0199/0123.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III/README.md)

## Description

<!-- description:start -->

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define the following variables:

-   `f1` represents the maximum profit after the first purchase of the stock;
-   `f2` represents the maximum profit after the first sale of the stock;
-   `f3` represents the maximum profit after the second purchase of the stock;
-   `f4` represents the maximum profit after the second sale of the stock.

During the traversal, we directly calculate `f1`, `f2`, `f3`, `f4`. We consider that buying and selling on the same day will result in a profit of $0$, which will not affect the answer.

Finally, return `f4`.

The time complexity is $O(n)$, where $n$ is the length of the `prices` array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 第一次买入，第一次卖出，第二次买入，第二次卖出
        f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, -price)
            f2 = max(f2, f1 + price)
            f3 = max(f3, f2 - price)
            f4 = max(f4, f3 + price)
        return f4
```

#### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        // 第一次买入，第一次卖出，第二次买入，第二次卖出
        int f1 = -prices[0], f2 = 0, f3 = -prices[0], f4 = 0;
        for (int i = 1; i < prices.length; ++i) {
            f1 = Math.max(f1, -prices[i]);
            f2 = Math.max(f2, f1 + prices[i]);
            f3 = Math.max(f3, f2 - prices[i]);
            f4 = Math.max(f4, f3 + prices[i]);
        }
        return f4;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int f1 = -prices[0], f2 = 0, f3 = -prices[0], f4 = 0;
        for (int i = 1; i < prices.size(); ++i) {
            f1 = max(f1, -prices[i]);
            f2 = max(f2, f1 + prices[i]);
            f3 = max(f3, f2 - prices[i]);
            f4 = max(f4, f3 + prices[i]);
        }
        return f4;
    }
};
```

#### Go

```go
func maxProfit(prices []int) int {
	f1, f2, f3, f4 := -prices[0], 0, -prices[0], 0
	for i := 1; i < len(prices); i++ {
		f1 = max(f1, -prices[i])
		f2 = max(f2, f1+prices[i])
		f3 = max(f3, f2-prices[i])
		f4 = max(f4, f3+prices[i])
	}
	return f4
}
```

#### TypeScript

```ts
function maxProfit(prices: number[]): number {
    let [f1, f2, f3, f4] = [-prices[0], 0, -prices[0], 0];
    for (let i = 1; i < prices.length; ++i) {
        f1 = Math.max(f1, -prices[i]);
        f2 = Math.max(f2, f1 + prices[i]);
        f3 = Math.max(f3, f2 - prices[i]);
        f4 = Math.max(f4, f3 + prices[i]);
    }
    return f4;
}
```

#### Rust

```rust
impl Solution {
    #[allow(dead_code)]
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut f1 = -prices[0];
        let mut f2 = 0;
        let mut f3 = -prices[0];
        let mut f4 = 0;
        let n = prices.len();

        for i in 1..n {
            f1 = std::cmp::max(f1, -prices[i]);
            f2 = std::cmp::max(f2, f1 + prices[i]);
            f3 = std::cmp::max(f3, f2 - prices[i]);
            f4 = std::cmp::max(f4, f3 + prices[i]);
        }

        f4
    }
}
```

#### C#

```cs
public class Solution {
    public int MaxProfit(int[] prices) {
        int f1 = -prices[0], f2 = 0, f3 = -prices[0], f4 = 0;
        for (int i = 1; i < prices.Length; ++i) {
            f1 = Math.Max(f1, -prices[i]);
            f2 = Math.Max(f2, f1 + prices[i]);
            f3 = Math.Max(f3, f2 - prices[i]);
            f4 = Math.Max(f4, f3 + prices[i]);
        }
        return f4;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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

### Without Using Global Variable(Important for META)
```python
class Solution:
   def sumNumbers(self, root: Optional[TreeNode]) -> int:
       
       def util(root, curr):
           if not root:
               return 0
           curr = curr * 10 + root.val
           if not (root.left or root.right):
               return curr
           return util(root.left, curr) + util(root.right, curr)
       return util(root, 0)
```

## Meta variant
```
What if you nodes could be larger than 9?
```
```python
class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = [0]
        
        def getMultiplier(n):
            if n < 10:
                return 10
            m = 1
            while n:
                m *= 10
                n = n//10
            return m

        def util(root, n, s):
            if not root:
                return
            curr = n * getMultiplier(root.val) + root.val
            if not (root.left or root.right):
                s[0] += curr
            util(root.left, curr, s)
            util(root.right, curr, s)

        util(root, 0, s)
        return s[0]

solution = Solution()
root = Solution.TreeNode(3)
root.left = Solution.TreeNode(79, right=Solution.TreeNode(111))
root.right = Solution.TreeNode(2)
assert solution.sumNumbers(root) == 379143

root = Solution.TreeNode(1)
root.left = Solution.TreeNode(2)
root.left.left = Solution.TreeNode(90)
root.right = Solution.TreeNode(42)
root.right.left = Solution.TreeNode(511)
assert solution.sumNumbers(root) == 1290 + 142511

root = Solution.TreeNode(1)
root.left = Solution.TreeNode(2)
root.left.left = Solution.TreeNode(912)
root.left.left.left = Solution.TreeNode(3)
root.left.left.right = Solution.TreeNode(4)
root.right = Solution.TreeNode(46)
root.right.left = Solution.TreeNode(5)
root.right.right = Solution.TreeNode(61)
assert solution.sumNumbers(root) == 129123 + 129124 + 1465 + 14661

root = Solution.TreeNode(1)
root.left = Solution.TreeNode(2)
root.right = Solution.TreeNode(3)
assert solution.sumNumbers(root) == 12 + 13

root = Solution.TreeNode(10)
root.left = Solution.TreeNode(200)
root.right = Solution.TreeNode(3000)
assert solution.sumNumbers(root) == 10200 + 103000

root = Solution.TreeNode(10)
root.left = Solution.TreeNode(0)
root.right = Solution.TreeNode(0)
assert solution.sumNumbers(root) == 200

root = None
assert solution.sumNumbers(root) == 0
```

## Meta variant
```
What if you had to ignore negative signs in your calculations until
you reached a leaf node, and instead, only consider signage if a root-to-leaf path is
a "negative path"?
```
```python
class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, curr_sum, num_negatives):
            if node is None:
                return 0

            curr_sum = (curr_sum * 10) + abs(node.val)
            if node.val < 0:
                num_negatives += 1

            if node.left is None and node.right is None:
                sign = -1 if num_negatives % 2 == 1 else 1
                return curr_sum * sign

            left_sum = helper(node.left, curr_sum, num_negatives)
            right_sum = helper(node.right, curr_sum, num_negatives)

            return left_sum + right_sum

        return helper(root, 0, 0)


solution = Solution()
root = Solution.TreeNode(1, 
    left=Solution.TreeNode(-2), 
    right=Solution.TreeNode(3))
assert solution.sumNumbers(root) == 1

root = Solution.TreeNode(-1, 
    left=Solution.TreeNode(-2, 
	left=Solution.TreeNode(-9)), 
    right=Solution.TreeNode(4, 
	left=Solution.TreeNode(-5)))
assert solution.sumNumbers(root) == -129 + 145

root = Solution.TreeNode(-1, 
    left=Solution.TreeNode(-2, 
	left=Solution.TreeNode(-9, 
	    left=Solution.TreeNode(3), 
		right=Solution.TreeNode(-3))),
    right=Solution.TreeNode(4, 
	left=Solution.TreeNode(-5), 
	    right=Solution.TreeNode(6)))
assert solution.sumNumbers(root) == -1293 + 1293 + 145 + -146

root = Solution.TreeNode(1, 
    left=Solution.TreeNode(2), 
    right=Solution.TreeNode(3))
assert solution.sumNumbers(root) == 12 + 13

root = Solution.TreeNode(-1, 
    left=Solution.TreeNode(-2), 
    right=Solution.TreeNode(-3))
assert solution.sumNumbers(root) == 12 + 13

root = Solution.TreeNode(-1, 
    left=Solution.TreeNode(-2, 
	left=Solution.TreeNode(-3)))
assert solution.sumNumbers(root) == -123

root = None
assert solution.sumNumbers(root) == 0
```

# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome)


## Description

<!-- description:start -->

<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers $i$ and $j$ to point to the two ends of the string $s$, and then loop through the following process until $i \geq j$:

1. If $s[i]$ is not a letter or a number, move the pointer $i$ one step to the right and continue to the next loop.
2. If $s[j]$ is not a letter or a number, move the pointer $j$ one step to the left and continue to the next loop.
3. If the lowercase form of $s[i]$ and $s[j]$ are not equal, return `false`.
4. Otherwise, move the pointer $i$ one step to the right and the pointer $j$ one step to the left, and continue to the next loop.

At the end of the loop, return `true`.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
# pay attention to isalnum(), it includes a-z, A-Z and 0-9
# if you want to compare only a-z and A-Z use isalpha() instead
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
```

## Meta variant
What if you could only consider a limited set of characters as a part of a potential palindrome?
```python
class Solution:
    def isPalindrome(self, s: str, include: list[str]) -> bool:
        include_set = set(include)
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in include_set and left < right:
                left += 1
            while s[right] not in include_set and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert not solution.isPalindrome("racecarX", ["r", "X"])
    assert solution.isPalindrome("Yo, banana boY!", ["Y", "o", "b", "a", "n"])
    assert solution.isPalindrome("yo banana boy!", ["y", "o", "b", "a", "n"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", " ", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "e"])
    assert not solution.isPalindrome("Wow", ["W", "o", "w"])
    assert solution.isPalindrome("WwoWWWWWWWWWWWWWow", ["o", "w"])
    assert solution.isPalindrome("__________________", ["1", "2"])
    assert not solution.isPalindrome("________133__________", ["1", "3"])
    assert not solution.isPalindrome("____1____133_______________", ["1", "3", "_"])
    assert solution.isPalindrome("", ["1", "3", "_"])
    assert solution.isPalindrome("", [])
    assert solution.isPalindrome("MadaM", [])
    assert solution.isPalindrome("MadaM", ["z", "M", "d"])
    assert not solution.isPalindrome("MadaMM", ["z", "M", "d"])
    assert not solution.isPalindrome("racecarX", ["r", "X"])
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
## Meta variant
What if you had to define the data structures yourself and clone the disconnected graph?
```
Use multiple roots and create a clone of each root same as the normal solution.
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


### With Extra space and One pass

```python
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        m = {}
        temp = head
        prev = None
        while temp:
            if temp not in m:
                m[temp] = Node(temp.val)
            if temp.random:
                if temp.random not in m:
                    m[temp.random] = Node(temp.random.val)
                m[temp].random = m[temp.random]
            if prev:
                m[prev].next = m[temp]
            prev = temp
            temp = temp.next
        return m[head]
```

### Using DFS
```python
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        visited = {}

        def dfs(head):
            if head is None:
                return None
            if head in visited:
                return visited[head]
            node = Node(head.val)
            visited[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)
            return node

        return dfs(head)
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

## Meta Variant
What if you had to deep copy a binary tree, not a linked list?

```python
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        visited = {}

        def dfs(root) -> "Optional[NodeCopy]":
            if root is None:
                return None
            if root in visited:
                return visited[root]
            copy = NodeCopy(root.val)
            visited[root] = copy
            copy.left = dfs(root.left)
            copy.right = dfs(root.right)
            copy.random = dfs(root.random)
            return copy

        return dfs(root)
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


---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0140.Word%20Break%20II/README_EN.md
tags:
    - Trie
    - Memoization
    - Array
    - Hash Table
    - String
    - Dynamic Programming
    - Backtracking
---

<!-- problem:start -->

# [140. Word Break II](https://leetcode.com/problems/word-break-ii)

[中文文档](/solution/0100-0199/0140.Word%20Break%20II/README.md)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, add spaces in <code>s</code> to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in <strong>any order</strong>.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsanddog&quot;, wordDict = [&quot;cat&quot;,&quot;cats&quot;,&quot;and&quot;,&quot;sand&quot;,&quot;dog&quot;]
<strong>Output:</strong> [&quot;cats and dog&quot;,&quot;cat sand dog&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pineapplepenapple&quot;, wordDict = [&quot;apple&quot;,&quot;pen&quot;,&quot;applepen&quot;,&quot;pine&quot;,&quot;pineapple&quot;]
<strong>Output:</strong> [&quot;pine apple pen apple&quot;,&quot;pineapple pen apple&quot;,&quot;pine applepen apple&quot;]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;,&quot;dog&quot;,&quot;sand&quot;,&quot;and&quot;,&quot;cat&quot;]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 10</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
	<li>Input is generated in a way that the length of the answer doesn&#39;t exceed&nbsp;10<sup>5</sup>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->


<!-- tabs:start -->

### Recursion with memoization

```python

class Solution(object):
    def wordBreak(self, s, wordDict):
        @cache
        def helper(s):
            if not s:
                return []

            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    resultOfTheRest = helper(s[len(word) :])
                    for item in resultOfTheRest:
                        item = word + " " + item
                        res.append(item)
            return res

        return helper(s)
```

### Using Trie
```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_end


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s):
            if not s:
                return [[]]
            res = []
            for i in range(1, len(s) + 1):
                if trie.search(s[:i]):
                    for v in dfs(s[i:]):
                        res.append([s[:i]] + v)
            return res

        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        ans = dfs(s)
        return [' '.join(v) for v in ans]
```

#### Java

```java
class Trie {
    Trie[] children = new Trie[26];
    boolean isEnd;

    void insert(String word) {
        Trie node = this;
        for (char c : word.toCharArray()) {
            c -= 'a';
            if (node.children[c] == null) {
                node.children[c] = new Trie();
            }
            node = node.children[c];
        }
        node.isEnd = true;
    }

    boolean search(String word) {
        Trie node = this;
        for (char c : word.toCharArray()) {
            c -= 'a';
            if (node.children[c] == null) {
                return false;
            }
            node = node.children[c];
        }
        return node.isEnd;
    }
}

class Solution {
    private Trie trie = new Trie();

    public List<String> wordBreak(String s, List<String> wordDict) {
        for (String w : wordDict) {
            trie.insert(w);
        }
        List<List<String>> res = dfs(s);
        return res.stream().map(e -> String.join(" ", e)).collect(Collectors.toList());
    }

    private List<List<String>> dfs(String s) {
        List<List<String>> res = new ArrayList<>();
        if ("".equals(s)) {
            res.add(new ArrayList<>());
            return res;
        }
        for (int i = 1; i <= s.length(); ++i) {
            if (trie.search(s.substring(0, i))) {
                for (List<String> v : dfs(s.substring(i))) {
                    v.add(0, s.substring(0, i));
                    res.add(v);
                }
            }
        }
        return res;
    }
}
```

#### Go

```go
type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func newTrie() *Trie {
	return &Trie{}
}
func (this *Trie) insert(word string) {
	node := this
	for _, c := range word {
		c -= 'a'
		if node.children[c] == nil {
			node.children[c] = newTrie()
		}
		node = node.children[c]
	}
	node.isEnd = true
}
func (this *Trie) search(word string) bool {
	node := this
	for _, c := range word {
		c -= 'a'
		if node.children[c] == nil {
			return false
		}
		node = node.children[c]
	}
	return node.isEnd
}

func wordBreak(s string, wordDict []string) []string {
	trie := newTrie()
	for _, w := range wordDict {
		trie.insert(w)
	}
	var dfs func(string) [][]string
	dfs = func(s string) [][]string {
		res := [][]string{}
		if len(s) == 0 {
			res = append(res, []string{})
			return res
		}
		for i := 1; i <= len(s); i++ {
			if trie.search(s[:i]) {
				for _, v := range dfs(s[i:]) {
					v = append([]string{s[:i]}, v...)
					res = append(res, v)
				}
			}
		}
		return res
	}
	res := dfs(s)
	ans := []string{}
	for _, v := range res {
		ans = append(ans, strings.Join(v, " "))
	}
	return ans
}
```

#### C#

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Node
{
    public int Index1 { get; set; }
    public int Index2 { get; set; }
}

public class Solution {
    public IList<string> WordBreak(string s, IList<string> wordDict) {
        var paths = new List<Tuple<int, string>>[s.Length + 1];
        paths[s.Length] = new List<Tuple<int, string>> { Tuple.Create(-1, (string)null) };
        var wordDictGroup = wordDict.GroupBy(word => word.Length);
        for (var i = s.Length - 1; i >= 0; --i)
        {
            paths[i] = new List<Tuple<int, string>>();
            foreach (var wordGroup in wordDictGroup)
            {
                var wordLength = wordGroup.Key;
                if (i + wordLength <= s.Length && paths[i + wordLength].Count > 0)
                {
                    foreach (var word in wordGroup)
                    {
                        if (s.Substring(i, wordLength) == word)
                        {
                            paths[i].Add(Tuple.Create(i + wordLength, word));
                        }
                    }
                }
            }
        }

        return GenerateResults(paths);
    }

    private IList<string> GenerateResults(List<Tuple<int, string>>[] paths)
    {
        var results = new List<string>();
        var sb = new StringBuilder();
        var stack = new Stack<Node>();
        stack.Push(new Node());
        while (stack.Count > 0)
        {
            var node = stack.Peek();
            if (node.Index1 == paths.Length - 1 || node.Index2 == paths[node.Index1].Count)
            {
                if (node.Index1 == paths.Length - 1)
                {
                    results.Add(sb.ToString());
                }
                stack.Pop();
                if (stack.Count > 0)
                {
                    var parent = stack.Peek();
                    var length = paths[parent.Index1][parent.Index2 - 1].Item2.Length;
                    if (length < sb.Length) ++length;
                    sb.Remove(sb.Length - length, length);
                }
            }
            else
            {
                var newNode = new Node { Index1 = paths[node.Index1][node.Index2].Item1, Index2 = 0 };
                if (sb.Length != 0)
                {
                    sb.Append(' ');
                }
                sb.Append(paths[node.Index1][node.Index2].Item2);
                stack.Push(newNode);
                ++node.Index2;
            }
        }
        return results;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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

# [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
Medium
```
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
 
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 
Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
```

```python
class Solution(object):
   def findPeakElement(self, nums):
       left = 0
       right = len(nums)-1
       while left < right:
           mid = (left+right)//2
           if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
               return mid
           if nums[mid] < nums[mid+1]:
               left = mid+1
           else:
               right = mid-1
       return left
```

## Meta variant
What if you had to find the valley element, no longer a peak element?

```python
def findValleyElement(nums):
    left = 0
    right = len(nums)-1
    while left < right:
       mid = (left+right)//2
       if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
           return mid
       if nums[mid] > nums[mid+1]:
           left = mid+1
       else:
           right = mid-1
    return left
    
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert findValleyElement(nums) == 0  # Left pos infinity yields valley

    nums = [1, 2, 3, 5, 3, 4, 3, 1, 6]
    assert findValleyElement(nums) == 4

    nums = [3, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 1

    nums = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 0

    nums = [1, 2, 3, 2, 1, 0]
    assert findValleyElement(nums) == 5  # Right pos infinity yields valley

    nums = [1, 2, 3, 2, 1, 6]
    assert findValleyElement(nums) == 4    
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0163.Missing%20Ranges/README_EN.md
tags:
    - Array
---

<!-- problem:start -->

# [163. Missing Ranges 🔒](https://leetcode.com/problems/missing-ranges)

[中文文档](/solution/0100-0199/0163.Missing%20Ranges/README.md)

## Description

<!-- description:start -->

<p>You are given an inclusive range <code>[lower, upper]</code> and a <strong>sorted unique</strong> integer array <code>nums</code>, where all elements are within the inclusive range.</p>

<p>A number <code>x</code> is considered <strong>missing</strong> if <code>x</code> is in the range <code>[lower, upper]</code> and <code>x</code> is not in <code>nums</code>.</p>

<p>Return <em>the <strong>shortest sorted</strong> list of ranges that <b>exactly covers all the missing numbers</b></em>. That is, no element of <code>nums</code> is included in any of the ranges, and each missing number is covered by one of the ranges.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,3,50,75], lower = 0, upper = 99
<strong>Output:</strong> [[2,2],[4,49],[51,74],[76,99]]
<strong>Explanation:</strong> The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1], lower = -1, upper = -1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no missing ranges since there are no missing numbers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>9</sup> &lt;= lower &lt;= upper &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>lower &lt;= nums[i] &lt;= upper</code></li>
	<li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can simulate the problem directly according to the requirements.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
from typing import List
class Solution:
   def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
       # Initialize the size of the nums array
       num_elements = len(nums)
    
       # If nums is empty, return the entire range from lower to upper
       if num_elements == 0:
           return [[lower, upper]]
    
       # List to store the missing ranges
       missing_ranges = []
    
       # Check if there is a missing range before the start of the array
       if nums[0] > lower:
           missing_ranges.append([lower, nums[0] - 1])
    
       # Use zip to create pairs of sequential elements (a, b) and loop through
       for a, b in zip(nums, nums[1:]):
           # If there is a gap greater than one between the two numbers, a missing range is found
           if b - a > 1:
               missing_ranges.append([a + 1, b - 1])
    
       # Check if there is a missing range after the end of the array
       if nums[-1] < upper:
           missing_ranges.append([nums[-1] + 1, upper])
    
       # Return the list of missing ranges
       return missing_ranges
```

## Meta Variant
What if you had to abide by 3 formatting requirements when capturing missing ranges?

```python
class Solution:
    def findMissingRangesVariant(self, nums, lower, upper):
        curr_lower = lower
        missing_ranges = []
        nums.append(upper + 1)
        
        for num in nums:
            if num - curr_lower > 2:
                missing_ranges.append(f"{curr_lower}-{num - 1}")
            elif num - curr_lower == 2:
                missing_ranges.append(str(curr_lower))
                missing_ranges.append(str(curr_lower + 1))
            elif num - curr_lower == 1:
                missing_ranges.append(str(curr_lower))
            
            curr_lower = num + 1
        
        return missing_ranges


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    solution = Solution()
    # Empty vector cases
    assert solution.findMissingRangesVariant([], 0, 0) == ["0"]
    assert solution.findMissingRangesVariant([], 5, 35) == ["5-35"]
    assert solution.findMissingRangesVariant([], 0, 35) == ["0-35"]

    # Valid cases
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    # Upper bound with dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 800) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-800",
    ]

    # Upper bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 21) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
    ]

    # Upper bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 22) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # Upper bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 20) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # No missing ranges with one element
    assert solution.findMissingRangesVariant([0], 0, 0) == []

    # No missing ranges with one element V2
    assert solution.findMissingRangesVariant([6], 6, 6) == []

    # Lower bound with dash
    assert solution.findMissingRangesVariant([0, 8, 9, 15, 16, 18, 20], 0, 20) == [
        "1-7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 20) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 3, 20) == [
        "3",
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 4, 20) == [
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Upper bound with no dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 22) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # One element with two ranges missing
    assert solution.findMissingRangesVariant([10], 5, 22) == ["5-9", "11-22"]
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
        self._pushToStack(root)

    def _pushToStack(self, node):
        while node:
            self.s.append(node)
            node = node.left

    def next(self) -> int:
        if not self.hasNext():
            return -1
        top = self.s.pop()
        self._pushToStack(top.right)
        return top.val

    def hasNext(self) -> bool:
        return self.s != []
```


The average time complexity of next() function is O(1) indeed in your case. As the next function can be called n times at most,   
and the number of right nodes in self.pushAll(tmpNode.right) function is maximal n in a tree which has n nodes, so the amortized   
time complexity is O(1).  
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
            ans.append(q[0].val)
            for _ in range(len(q)):
                top = q.popleft()
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
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

## Meta variant
What if you had to return both the left- and right side views of a binary tree?
```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftRightSideViewVariant(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        left_side = []
        right_side = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i == 0:
                    left_side.append(node.val)
                if size == i + 1:
                    right_side.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        result = []
        result.extend(reversed(left_side))
        result.extend(right_side[1:])
        return result


if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: Based on the example in the problem
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   5       4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root1) == [5, 2, 1, 3, 4]
    # Test Case 2: Based on the second example
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root2) == [4, 2, 1, 3, 5]

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(7)
    root1.right.left = TreeNode(6)
    root1.right.right.left = TreeNode(8)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root1) == [8, 4, 2, 1, 3, 7, 8]

    root2 = TreeNode(1)
    assert solution.leftRightSideViewVariant(root2) == [1]

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    assert solution.leftRightSideViewVariant(root3) == [3, 2, 1, 2, 3]

    root4 = None
    assert solution.leftRightSideViewVariant(root4) == []

    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.right.left = TreeNode(5)
    root5.right.left.right = TreeNode(6)
    root5.right.left.right.right = TreeNode(7)
    root5.left.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root5) == [7, 6, 4, 2, 1, 3, 5, 6, 7]
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
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0207.Course%20Schedule/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Topological Sort
---

<!-- problem:start -->

# [207. Course Schedule](https://leetcode.com/problems/course-schedule)

[中文文档](/solution/0200-0299/0207.Course%20Schedule/README.md)

## Description

<!-- description:start -->

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Topological Sorting

For this problem, we can consider the courses as nodes in a graph, and prerequisites as edges in the graph. Thus, we can transform this problem into determining whether there is a cycle in the directed graph.

Specifically, we can use the idea of topological sorting. For each node with an in-degree of $0$, we reduce the in-degree of its out-degree nodes by $1$, until all nodes have been traversed.

If all nodes have been traversed, it means there is no cycle in the graph, and we can complete all courses; otherwise, we cannot complete all courses.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ are the number of courses and prerequisites respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        d_count = defaultdict(int)
        dep = defaultdict(list)
        for p in pre:
            dep[p[1]].append(p[0])
            d_count[p[0]] += 1
        q = deque()
        for i in range(numCourses):
            if not d_count[i]:
                q.append(i)
        while q:
            top = q.popleft()
            for t in dep[top]:
                d_count[t] -= 1
                if not d_count[t]:
                    q.append(t)
        return max(d_count.values()) == 0
```

#### Java

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] g = new List[numCourses];
        Arrays.setAll(g, k -> new ArrayList<>());
        int[] indeg = new int[numCourses];
        for (var p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].add(a);
            ++indeg[a];
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.offer(i);
            }
        }
        while (!q.isEmpty()) {
            int i = q.poll();
            --numCourses;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.offer(j);
                }
            }
        }
        return numCourses == 0;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].push_back(a);
            ++indeg[a];
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            --numCourses;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.push(j);
                }
            }
        }
        return numCourses == 0;
    }
};
```

#### Go

```go
func canFinish(numCourses int, prerequisites [][]int) bool {
	g := make([][]int, numCourses)
	indeg := make([]int, numCourses)
	for _, p := range prerequisites {
		a, b := p[0], p[1]
		g[b] = append(g[b], a)
		indeg[a]++
	}
	q := []int{}
	for i, x := range indeg {
		if x == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		i := q[0]
		q = q[1:]
		numCourses--
		for _, j := range g[i] {
			indeg[j]--
			if indeg[j] == 0 {
				q = append(q, j)
			}
		}
	}
	return numCourses == 0
}
```

#### TypeScript

```ts
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const g: number[][] = Array.from({ length: numCourses }, () => []);
    const indeg: number[] = Array(numCourses).fill(0);
    for (const [a, b] of prerequisites) {
        g[b].push(a);
        indeg[a]++;
    }
    const q: number[] = [];
    for (let i = 0; i < numCourses; ++i) {
        if (indeg[i] === 0) {
            q.push(i);
        }
    }
    for (const i of q) {
        --numCourses;
        for (const j of g[i]) {
            if (--indeg[j] === 0) {
                q.push(j);
            }
        }
    }
    return numCourses === 0;
}
```

#### Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn can_finish(mut num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut g: Vec<Vec<i32>> = vec![vec![]; num_courses as usize];
        let mut indeg: Vec<i32> = vec![0; num_courses as usize];

        for p in prerequisites {
            let a = p[0] as usize;
            let b = p[1] as usize;
            g[b].push(a as i32);
            indeg[a] += 1;
        }

        let mut q: VecDeque<usize> = VecDeque::new();
        for i in 0..num_courses {
            if indeg[i as usize] == 0 {
                q.push_back(i as usize);
            }
        }

        while let Some(i) = q.pop_front() {
            num_courses -= 1;
            for &j in &g[i] {
                let j = j as usize;
                indeg[j] -= 1;
                if indeg[j] == 0 {
                    q.push_back(j);
                }
            }
        }

        num_courses == 0
    }
}
```

#### C#

```cs
public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var g = new List<int>[numCourses];
        for (int i = 0; i < numCourses; ++i) {
            g[i] = new List<int>();
        }
        var indeg = new int[numCourses];
        foreach (var p in prerequisites) {
            int a = p[0], b = p[1];
            g[b].Add(a);
            ++indeg[a];
        }
        var q = new Queue<int>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.Enqueue(i);
            }
        }
        while (q.Count > 0) {
            int i = q.Dequeue();
            --numCourses;
            foreach (int j in g[i]) {
                if (--indeg[j] == 0) {
                    q.Enqueue(j);
                }
            }
        }
        return numCourses == 0;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
Medium
<p>
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
</p>

### Using QuickSelect

<p>

1. First, we need to choose so-calledpivotand partition element of nums into 3 parts: elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: less and more or equal)
2. Next step is to see how many elements we have in each group: ifk <= L, whereLis size of left, than we can be sure that we need to look into the left part. Ifk > L + M, whereMis size ofmidgroup, than we can be sure, that we need to look into the right part. Finally, if none of these two condition holds, we need to look in themidpart, but because all elements there are equal, we can immedietly returnmid[0].

Complexity: time complexity isO(n)in average, because on each time we reduce searching range approximately2times. This is not strict proof, for more details you can do some googling. Space complexity isO(n)as well.

Proof of average time complexity:

The expression you provided is a geometric series:
n+n/2+n/4+n/8+⋯+1

This is an infinite geometric series where the first term a=na=n and the common ratio r=1/2​.

The sum of an infinite geometric series is given by the formula:
S=a/1−r, here a = n and r = 1/2
So, the sum of the infinite series is:
S=2n
</p>


### (Important solution)RunTime O(N)
```python
class Solution:
   def findKthLargest(self, nums: List[int], k: int) -> int:
       pivot = random.choice(nums)
       left = [x for x in nums if x > pivot]
       mid = [x for x in nums if x == pivot]
       right = [x for x in nums if x < pivot]
       L, M = len(left), len(mid)
       if L >= k:
           return self.findKthLargest(left, k)
       elif k > L + M:
           return self.findKthLargest(right, k-L-M)
       else:
           return mid[0]
```

### Using PriorityQueue
```python
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for n in nums:
            q.put(n)
            if q.qsize() > k:
                q.get()
        return q.get()
```


---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0219.Contains%20Duplicate%20II/README_EN.md
tags:
    - Array
    - Hash Table
    - Sliding Window
---

<!-- problem:start -->

# [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii)

[中文文档](/solution/0200-0299/0219.Contains%20Duplicate%20II/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We use a hash table $\textit{d}$ to store the recently traversed numbers and their corresponding indices.

Traverse the array $\textit{nums}$. For the current element $\textit{nums}[i]$, if it exists in the hash table and the difference between the indices is no more than $k$, return $\text{true}$. Otherwise, add the current element to the hash table.

After traversing, return $\text{false}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, x in enumerate(nums):
            if x in d and i - d[x] <= k:
                return True
            d[x] = i
        return False
```

#### Java

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            if (i - d.getOrDefault(nums[i], -1000000) <= k) {
                return true;
            }
            d.put(nums[i], i);
        }
        return false;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        for (int i = 0; i < nums.size(); ++i) {
            if (d.count(nums[i]) && i - d[nums[i]] <= k) {
                return true;
            }
            d[nums[i]] = i;
        }
        return false;
    }
};
```

#### Go

```go
func containsNearbyDuplicate(nums []int, k int) bool {
	d := map[int]int{}
	for i, x := range nums {
		if j, ok := d[x]; ok && i-j <= k {
			return true
		}
		d[x] = i
	}
	return false
}
```

#### TypeScript

```ts
function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const d: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; ++i) {
        if (d.has(nums[i]) && i - d.get(nums[i])! <= k) {
            return true;
        }
        d.set(nums[i], i);
    }
    return false;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
    const d = new Map();
    for (let i = 0; i < nums.length; ++i) {
        if (d.has(nums[i]) && i - d.get(nums[i]) <= k) {
            return true;
        }
        d.set(nums[i], i);
    }
    return false;
};
```

#### C#

```cs
public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var d = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; ++i) {
            if (d.ContainsKey(nums[i]) && i - d[nums[i]] <= k) {
                return true;
            }
            d[nums[i]] = i;
        }
        return false;
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function containsNearbyDuplicate($nums, $k) {
        $d = [];
        for ($i = 0; $i < count($nums); ++$i) {
            if (array_key_exists($nums[$i], $d) && $i - $d[$nums[$i]] <= $k) {
                return true;
            }
            $d[$nums[$i]] = $i;
        }
        return false;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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
    def calculate(self, s):
        def calc(it):
            def update(op, v):
                if op == "+":
                    stack.append(v)
                if op == "-":
                    stack.append(-v)
                if op == "*":
                    stack.append(stack.pop() * v)
                # pay attention to this. we are doing it this way because -3//2 will not truncate
                # towards 0. -3//2 is -2 not -1.
                if op == "/":
                    stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, it = calc(it + 1)
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
```
### 227. Basic Calculator II
Medium
```
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the 
range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().
 
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
```

### Solution that works for Basic Calculator II:

```python
class Solution:
    def calculate(self, s: str) -> int:
        st = []
        num = 0
        sign = "+"

        def update(num, sign):
            if sign == "+":
                st.append(num)
            elif sign == "-":
                st.append(-num)
            elif sign == "*":
                st.append(num * st.pop())
            else:
                # pay attention to this. we are doing it this way because -3//2 will not truncate
                # towards 0. -3//2 is -2 not -1.
                st.append(int(st.pop() / num))

        for c in s:
            if c in "+-/*":
                update(num, sign)
                sign = c
                num = 0
            elif c.isdigit():
                num = num * 10 + int(c)
        update(num, sign)
        return sum(st)

```



### Solution that work for all Basic Calculator problems.

It supports parenthesis too.

```python
class Solution:
    def calculate(self, s):
        def calc(it):
            def update(op, v):
                if op == "+":
                    stack.append(v)
                if op == "-":
                    stack.append(-v)
                if op == "*":
                    stack.append(stack.pop() * v)
                # pay attention to this. we are doing it this way because -3//2 will not truncate
                # towards 0. -3//2 is -2 not -1.
                if op == "/":
                    stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, it = calc(it + 1)
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
```

# 235. Lowest Common Ancestor of a Binary Search Tree
Medium
```
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
 
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according
to the LCA definition.
Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### Recursive
```python
class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       if p.val > root.val and q.val > root.val:
           return self.lowestCommonAncestor(root.right, p, q)
       if p.val < root.val and q.val < root.val:
           return self.lowestCommonAncestor(root.left, p, q)
       return root
```


### Iterative
```python
class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       pv = p.val
       qv = q.val
       while root:
           rv = root.val
           if rv > pv and rv > qv:
               root = root.left
               continue
           if rv < pv and rv < qv:
               root = root.right
               continue
           return root

```
# 236. Lowest Common Ancestor of a Binary Tree
Medium
```
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”
 
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself 
according to the LCA definition.
Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
```

```python
class Solution:
   def lowestCommonAncestor(
       self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
   ) -> "TreeNode":
       if not root:
           return None
       if root.val == p.val or root.val == q.val:
           return root
       left = self.lowestCommonAncestor(root.left, p, q)
       right = self.lowestCommonAncestor(root.right, p, q)
       if left and right:
           return root
       return left if left else right

```

## Meta variant
How to do this for n-ary tree?

```python
class TreeNode:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q


if __name__ == "__main__":
    # Tree structure:
    #       1
    #    /  |  \
    #   3   2   4
    #  / \
    # 5   6
    root1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root1.children = [node3, node2, node4]
    node3.children = [node5, node6]
    solution = Solution()
    assert solution.lowestCommonAncestor(root1, node5, node2) == root1
    assert solution.lowestCommonAncestor(root1, node5, node6) == node3

    # Test Case 2: More complex tree
    # Tree structure:
    #        10
    #     /  |  \  \
    #    5   1   7  8
    #   / \  |      |
    #  2  4  3      9
    #    /
    #   6
    root2 = TreeNode(10)
    node5_2 = TreeNode(5)
    node1 = TreeNode(1)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node2_2 = TreeNode(2)
    node4_2 = TreeNode(4)
    node3_2 = TreeNode(3)
    node9 = TreeNode(9)
    node6_2 = TreeNode(6)

    root2.children = [node5_2, node1, node7, node8]
    node5_2.children = [node2_2, node4_2]
    node1.children = [node3_2]
    node8.children = [node9]
    node4_2.children = [node6_2]
    assert solution.lowestCommonAncestor(root2, node6_2, node3_2) == root2
    assert solution.lowestCommonAncestor(root2, node6_2, node2_2) == node5_2

    # Tree structure:
    #       1
    #    /  |  \
    #   2   3   4
    #  / \     / | \
    # 5   6   7  8  9
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7, node8, node9]
    solution = Solution()
    # Root as the LCA
    assert solution.lowestCommonAncestor(root, node5, node7) == root
    assert solution.lowestCommonAncestor(root, node5, node8) == root
    assert solution.lowestCommonAncestor(root, node5, node9) == root
    assert solution.lowestCommonAncestor(root, node6, node7) == root
    assert solution.lowestCommonAncestor(root, node6, node8) == root
    assert solution.lowestCommonAncestor(root, node6, node9) == root

    assert solution.lowestCommonAncestor(root, node2, node9) == root

    assert solution.lowestCommonAncestor(root, node2, node4) == root
    assert solution.lowestCommonAncestor(root, node2, node3) == root

    # Node 4 as the LCA
    assert solution.lowestCommonAncestor(root, node7, node8) == node4
    assert solution.lowestCommonAncestor(root, node7, node9) == node4

    # Node 2 as the LCA
    assert solution.lowestCommonAncestor(root, node5, node6) == node2

    # Same tree structure for the second test case:
    #       1
    #    /  |  \
    #   2   3   4
    #  / \     / | \
    # 5   6   7  8  9
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7, node8, node9]

    solution = Solution()
    # Root as the LCA
    assert solution.lowestCommonAncestor(root, root, node2) == root
    assert solution.lowestCommonAncestor(root, root, node3) == root
    assert solution.lowestCommonAncestor(root, root, node4) == root
    assert solution.lowestCommonAncestor(root, root, node5) == root
    assert solution.lowestCommonAncestor(root, root, node6) == root
    assert solution.lowestCommonAncestor(root, root, node7) == root
    assert solution.lowestCommonAncestor(root, root, node8) == root
    assert solution.lowestCommonAncestor(root, root, node9) == root

    # Node 4 as the LCA
    assert solution.lowestCommonAncestor(root, node4, node8) == node4
    assert solution.lowestCommonAncestor(root, node4, node9) == node4

    # Node 2 as the LCA
    assert solution.lowestCommonAncestor(root, node2, node6) == node2
```
# 239. Sliding Window Maximum
Hard
```
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can only
see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
 
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:
Input: nums = [1], k = 1
Output: [1]
```

### Using Deque(Most Optimal)
Complexity:  
Time: O(NlogK), each operation of BST of size K costs O(logK)  
Space: O(K)
```python
class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, v in enumerate(nums):
            # Make sure the queue stores only index in the range up to
            # q[0] ----> q[0] + k and remove index if out of window left
            if q and i - k + 1 > q[0]:
               q.popleft()
            # Pop from right all indices with value less than current index   
            while q and nums[q[-1]] <= v:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
```

### Using Priority Queue
Complexity:  
Time: O(NlogN), each operation of maxHeap of size N costs O(logN)  
Space: O(N)
```python
from queue import PriorityQueue


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = PriorityQueue()
        res = []
        for i, n in enumerate(nums):
            while q.qsize():
                top, index = q.get()
                if -top > n:
                    q.put((top, index))
                    break
            while q.qsize():
                top, index = q.get()
                if index > i - k:
                    q.put((top, index))
                    break
            q.put((-n, i))
            if i >= k - 1:
                top, index = q.get()
                res.append(-top)
                q.put((top, index))
        return res
```
# [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii)

[中文文档](/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/README.md)

## Description

<!-- description:start -->

<p>Write an efficient algorithm that searches for a value <code>target</code> in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/images/searchgrid2.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/images/searchgrid.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                r +=1
            else:
                c -=1
        return False

```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0249.Group%20Shifted%20Strings/README_EN.md
tags:
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [249. Group Shifted Strings 🔒](https://leetcode.com/problems/group-shifted-strings)

[中文文档](/solution/0200-0299/0249.Group%20Shifted%20Strings/README.md)

## Description

<!-- description:start -->

<p>Perform the following shift operations on a string:</p>

<ul>
	<li><strong>Right shift</strong>: Replace every letter with the <strong>successive</strong> letter of the English alphabet, where &#39;z&#39; is replaced by &#39;a&#39;. For example, <code>&quot;abc&quot;</code> can be right-shifted to <code>&quot;bcd&quot; </code>or <code>&quot;xyz&quot;</code> can be right-shifted to <code>&quot;yza&quot;</code>.</li>
	<li><strong>Left shift</strong>: Replace every letter with the <strong>preceding</strong> letter of the English alphabet, where &#39;a&#39; is replaced by &#39;z&#39;. For example, <code>&quot;bcd&quot;</code> can be left-shifted to <code>&quot;abc&quot;<font face="Times New Roman"> or </font></code><code>&quot;yza&quot;</code> can be left-shifted to <code>&quot;xyz&quot;</code>.</li>
</ul>

<p>We can keep shifting the string in both directions to form an <strong>endless</strong> <strong>shifting sequence</strong>.</p>

<ul>
	<li>For example, shift <code>&quot;abc&quot;</code> to form the sequence: <code>... &lt;-&gt; &quot;abc&quot; &lt;-&gt; &quot;bcd&quot; &lt;-&gt; ... &lt;-&gt; &quot;xyz&quot; &lt;-&gt; &quot;yza&quot; &lt;-&gt; ...</code>.<code> &lt;-&gt; &quot;zab&quot; &lt;-&gt; &quot;abc&quot; &lt;-&gt; ...</code></li>
</ul>

<p>You are given an array of strings <code>strings</code>, group together all <code>strings[i]</code> that belong to the same shifting sequence. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strings = [&quot;abc&quot;,&quot;bcd&quot;,&quot;acef&quot;,&quot;xyz&quot;,&quot;az&quot;,&quot;ba&quot;,&quot;a&quot;,&quot;z&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;acef&quot;],[&quot;a&quot;,&quot;z&quot;],[&quot;abc&quot;,&quot;bcd&quot;,&quot;xyz&quot;],[&quot;az&quot;,&quot;ba&quot;]]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strings = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strings.length &lt;= 200</code></li>
	<li><code>1 &lt;= strings[i].length &lt;= 50</code></li>
	<li><code>strings[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

The relative distance between each letter of the string and the first character is equal.
For example, abc and efg are mutually offset. For abc, the distance between b and a is 1, and the distance between c and a is 2. For efg, the distance between f and e is 1, and the distance between g and e is 2.
Let’s look at another example. The distance between az and yx, z and a is 25, and the distance between x and y is also 25 (direct subtraction is -1, which is the reason for adding 26 and taking the remainder).
Then, in this case, all strings that are offset from each other have a unique distance difference. According to this, the mapping can be well grouped.

<!-- tabs:start -->

#### Python3

```python
import collections
# Total lowercase letter
ALPHA = 26
# Method to a difference string for a given string. If string
# is "adf" then difference string will be "cb" (first difference
# 3 then difference 2)
def getDiffString(str):
   shift=""
   for i in range(1, len(str)):
       dif = ((ord(str[i]) - ord(str[i - 1])) + ALPHA) % ALPHA
       shift += chr(dif + ord('a'))
   return shift
def groupShiftedString(str):
   n = len(str)
   groupMap = collections.defaultdict(list)
   for i in range(n):
       diffStr = getDiffString(str[i])
       groupMap[diffStr].append(str[i])
  
   return list(groupMap.values())
   
print(groupShiftedString(["abc","bcd","acef","xyz","az","ba","a","z"]))
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0253.Meeting%20Rooms%20II/README_EN.md
tags:
    - Greedy
    - Array
    - Two Pointers
    - Prefix Sum
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [253. Meeting Rooms II 🔒](https://leetcode.com/problems/meeting-rooms-ii)

[中文文档](/solution/0200-0299/0253.Meeting%20Rooms%20II/README.md)

## Description

<!-- description:start -->

<p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of conference rooms required</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution(object):
    def minMeetingRooms(self, intervals):
        meetings = []
        for i in intervals:
            meetings.append((i.start, 1))
            meetings.append((i.end, 0))
        meetings.sort()
        ans = 0
        count = 0
        for meeting in meetings:
            if meeting[1] == 1:
                count += 1
            else:
                count -= 1
            ans = max(ans, count)
        return ans
```
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0269.Alien%20Dictionary/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Topological Sort
    - Array
    - String
---

<!-- problem:start -->

# [269. Alien Dictionary 🔒](https://leetcode.com/problems/alien-dictionary)

[中文文档](/solution/0200-0299/0269.Alien%20Dictionary/README.md)

## Description

<!-- description:start -->

<p>There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.</p>

<p>You are given a list of strings <code>words</code> from the alien language&#39;s dictionary. Now it is claimed that the strings in <code>words</code> are <span data-keyword="lexicographically-smaller-string-alien"><strong>sorted lexicographically</strong></span> by the rules of this new language.</p>

<p>If this claim is incorrect, and the given arrangement of string in&nbsp;<code>words</code>&nbsp;cannot correspond to any order of letters,&nbsp;return&nbsp;<code>&quot;&quot;.</code></p>

<p>Otherwise, return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language&#39;s rules</em><em>. </em>If there are multiple solutions, return<em> <strong>any of them</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]
<strong>Output:</strong> &quot;wertf&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;]
<strong>Output:</strong> &quot;zx&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;,&quot;z&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> The order is invalid, so return <code>&quot;&quot;</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1
```

Algorithm
It is actually a problem of directed graph traversal.
The solution consists of two steps:
Create the graph and indegree map:
For each character in the words, initialize its indegree to 0.
For each adjacent pair of words, find the first character that is different.
If the second character is not already in the adjacency list of the first character, add it and increment its indegree by 1.
Stop processing the current pair of words and move on to the next pair.
If all characters of the first word match the second word and the first word is longer than the second,
it means that the order of characters is invalid, so return an empty string.
Topological sort
Add all characters with an indegree of 0 to the queue.
For each character in the queue, add it to the result and decrement the indegree of its neighbors.
If the indegree of a neighbor becomes 0, add it to the queue.
If the length of the result equals the length of the indegree map, return the result as a string. Otherwise, return an empty string.
```


#### Python3

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        inDegree = defaultdict(int)
        self._buildGraph(graph, words, inDegree)
        return self._topology(graph, inDegree)

    def _buildGraph(
        self, graph: Dict[str, Set[str]], words: List[str], inDegree: Dict[str, int]
    ) -> None:
        # Create a node for each character in each word
        for word in words:
            for c in word:
                inDegree[c] = 0  # necessary for final char counting
        for first, second in zip(words, words[1:]):
            length = min(len(first), len(second))
            for j in range(length):
                u = first[j]
                v = second[j]
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        inDegree[v] += 1
                    break  # Later characters' order is meaningless
                if j == length - 1 and len(first) > len(second):
                    # If 'ab' comes before 'a', it's an invalid order
                    graph.clear()
                    return

    def _topology(self, graph: Dict[str, Set[str]], inDegree: Dict[str, int]) -> str:
        result = ""
        q = deque([c for c in inDegree if inDegree[c] == 0])
        while q:
            u = q.popleft()
            result += u
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        # If there are remaining characters in inDegree, it means there's a cycle
        if any(inDegree.values()):
            return ""
        # Words = ['z', 'x', 'y', 'x']
        return result if len(result) == len(indegree) else ""
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0270.Closest%20Binary%20Search%20Tree%20Value/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Binary Search
    - Binary Tree
---

<!-- problem:start -->

# [270. Closest Binary Search Tree Value 🔒](https://leetcode.com/problems/closest-binary-search-tree-value)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree and a <code>target</code> value, return <em>the value in the BST that is closest to the</em> <code>target</code>. If there are multiple answers, print the smallest.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0270.Closest%20Binary%20Search%20Tree%20Value/images/closest1-1-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,2,5,1,3], target = 3.714286
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1], target = 4.428571
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

We define a recursive function `dfs(node)`, which starts from the current node `node` and finds the node closest to the target value `target`. We can update the answer by comparing the absolute difference between the current node's value and the target value. If the target value is less than the current node's value, we recursively search the left subtree; otherwise, we recursively search the right subtree.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary search tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def closest_value(self, root: TreeNode, target: float) -> int:
        # Initialize the closest_value with the root's value
        closest_value = root.val
      
        # Initialize the minimum difference found
        minimum_difference = float('inf')

        # Iterate over the nodes of the binary search tree
        while root:
            # Calculate the current difference between node's value and the target
            current_difference = abs(root.val - target)

            # If the current difference is smaller or equal but with a lesser value, update the closest_value
            if current_difference < minimum_difference or (current_difference == minimum_difference and root.val < closest_value):
                minimum_difference = current_difference
                closest_value = root.val
          
            # Move left if the target is smaller than the current node's value
            if root.val > target:
                root = root.left
            # Otherwise, move right
            else:
                root = root.right
      
        # Once we find the closest value, return it
        return closest_value
```
# 282. Expression Add Operators
Hard
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0283.Move%20Zeroes/README_EN.md
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes)

[中文文档](/solution/0200-0299/0283.Move%20Zeroes/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use a pointer $k$ to record the current position to insert, initially $k = 0$.

Then we iterate through the array $\textit{nums}$, and each time we encounter a non-zero number, we swap it with $\textit{nums}[k]$ and increment $k$ by 1.

This way, we can ensure that the first $k$ elements of $\textit{nums}$ are non-zero, and their relative order is the same as in the original array.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for i, n in enumerate(nums):
            if n == 0:
                continue
            nums[lastNonZero] = nums[i]
            lastNonZero += 1
        while lastNonZero < len(nums):
            nums[lastNonZero] = 0
            lastNonZero += 1
```

## Meta variant
What if you had to move zeroes to the front, not the back?

Start iterating the array from the end instead of from the front.

```python
def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums) -1
    lastNonZero = n
    for i in range(n, -1,-1):
        if nums[i] == 0:
            continue
        nums[lastNonZero] = nums[i]
        lastNonZero -= 1
    while lastNonZero >= 0:
        nums[lastNonZero] = 0
        lastNonZero -= 1
nums = [1, 3, 12, 0, 0, 0]
moveZeroes(nums)
print(nums)

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
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0301.Remove%20Invalid%20Parentheses/README_EN.md
tags:
    - Breadth-First Search
    - String
    - Backtracking
---

<!-- problem:start -->

# [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)

[中文文档](/solution/0300-0399/0301.Remove%20Invalid%20Parentheses/README.md)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.</p>

<p>Return <em>a list of <strong>unique strings</strong> that are valid with the minimum number of removals</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()())()&quot;
<strong>Output:</strong> [&quot;(())()&quot;,&quot;()()()&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a)())()&quot;
<strong>Output:</strong> [&quot;(a())()&quot;,&quot;(a)()()&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)(&quot;
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 25</code></li>
	<li><code>s</code> consists of lowercase English letters and parentheses <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li>There will be at most <code>20</code> parentheses in <code>s</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # define when a combination of parenthesis is still valid
        def valid(candidate):
            counter = 0
            for char in candidate:
                if char == "(": counter += 1
                elif char == ")": counter -= 1
                if counter < 0: return False
            # balanced?
            return counter == 0
        # the actual BFS, we return the minimum of removals, so we stop as soon as we have something
        result = set()
        q = deque([s])
        visited = set([s])
        while q:
            for _ in range(len(q)):
                top = q.popleft()
                if valid(top):
                    result.add(top)
                # If result is not empty, it means we found one valid palindrome with minimum
                # removals. So we should not add more to the queue but continue processing
                # existing elements to see if already more valid strings are present in the queue    
                if result:
                    continue
                    # generate more candidates based on this candidate
                for i, letter in enumerate(top):
                    # skip trash
                    if letter not in "()": 
                        continue
                    next = top[:i] + top[i+1:]
                    if next not in visited:
                        visited.add(next)
                        q.append(next)
                        
        return result
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
# [314. Binary Tree Vertical Order Traversal 🔒](https://leetcode.com/problems/binary-tree-vertical-order-traversal)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em><strong>the vertical order traversal</strong> of its nodes&#39; values</em>. (i.e., from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <strong>left to right</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image1.png" style="width: 400px; height: 273px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image3.png" style="width: 450px; height: 285px;" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7]
<strong>Output:</strong> [[4],[9],[3,0,1],[8],[7]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0314.Binary%20Tree%20Vertical%20Order%20Traversal/images/image2.png" style="width: 350px; height: 342px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
<strong>Output:</strong> [[4],[2,5],[1,10,9,6],[3],[11]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

```python
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        d = defaultdict(list)
        while q:
            for _ in range(len(q)):
                root, offset = q.popleft()
                d[offset].append(root.val)
                if root.left:
                    q.append((root.left, offset - 1))
                if root.right:
                    q.append((root.right, offset + 1))
        return [v for _, v in sorted(d.items())]
```

### Another Solution
<p>
This is the solution for problem 987, where The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. 
</p>

```python
class Solution(object):
    def verticalOrder(self, root):
        def dfs(p, i, j, res):  # i -> depth, j -> vertical-shift
            if p:
                res[j].append((p.val, i))
                self.leftMost = min(j, self.leftMost)
                dfs(p.left, i + 1, j - 1, res)
                dfs(p.right, i + 1, j + 1, res)

        self.leftMost = float("inf")
        ans = []
        res = defaultdict(list)
        dfs(root, 0, 0, res)
        i = self.leftMost
        while True:
            if not res[i]:
                break
            ans.append([item[0] for item in sorted(res[i], key=lambda a: a[1])])
            i += 1
        return ans
```
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0317.Shortest%20Distance%20from%20All%20Buildings/README_EN.md
tags:
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->

# [317. Shortest Distance from All Buildings 🔒](https://leetcode.com/problems/shortest-distance-from-all-buildings)

[中文文档](/solution/0300-0399/0317.Shortest%20Distance%20from%20All%20Buildings/README.md)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> grid <code>grid</code> of values <code>0</code>, <code>1</code>, or <code>2</code>, where:</p>

<ul>
	<li>each <code>0</code> marks <strong>an empty land</strong> that you can pass by freely,</li>
	<li>each <code>1</code> marks <strong>a building</strong> that you cannot pass through, and</li>
	<li>each <code>2</code> marks <strong>an obstacle</strong> that you cannot pass through.</li>
</ul>

<p>You want to build a house on an empty land that reaches all buildings in the <strong>shortest total travel</strong> distance. You can only move up, down, left, and right.</p>

<p>Return <em>the <strong>shortest travel distance</strong> for such a house</em>. If it is not possible to build such a house according to the above rules, return <code>-1</code>.</p>

<p>The <strong>total travel distance</strong> is the sum of the distances between the houses of the friends and the meeting point.</p>

<p>The distance is calculated using <a href="http://en.wikipedia.org/wiki/Taxicab_geometry" target="_blank">Manhattan Distance</a>, where <code>distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0317.Shortest%20Distance%20from%20All%20Buildings/images/buildings-grid.jpg" style="width: 413px; height: 253px;" />
<pre>
<strong>Input:</strong> grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
	<li>There will be <strong>at least one</strong> building in the <code>grid</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
from collections import deque

class Solution:
   def shortestDistance(self, grid):
       # Initialize rows `m` and columns `n` based on the grid dimensions
       m, n = len(grid), len(grid[0])
     
       # A queue for breadth-first search
       queue = deque()
     
       # Total number of buildings
       total_buildings = 0
     
       # Data structures to keep count of how many buildings each empty land can reach
       reach_count = [[0] * n for _ in range(m)]
     
       # Data structures to keep track of total distances from each empty land to all buildings
       distance_sum = [[0] * n for _ in range(m)]
     
       # Loop through each cell in the grid
       for i in range(m):
           for j in range(n):
               # If the cell is a building, perform a BFS from this building
               if grid[i][j] == 1:
                   total_buildings += 1
                   queue.append((i, j))
                   level_distance = 0
                   visited = set()
                   while queue:
                       # Increase the distance level by 1 for each level of BFS
                       level_distance += 1
                     
                       # Loop through each cell in the current BFS level
                       for _ in range(len(queue)):
                           r, c = queue.popleft()
                           # Explore the four directions around the current cell
                           for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                               x, y = r + dr, c + dc
                               # If the next cell is valid, not visited, and is an empty land
                               if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not visited:
                                   # Increment the building reach count and add the distance
                                   reach_count[x][y] += 1
                                   distance_sum[x][y] += level_distance
                                 
                                   # Add the cell to the queue and mark it as visited
                                   queue.append((x, y))
                                   visited.add((x, y))
     
       # Set an initial answer as infinity to find the minimum
       answer = float('inf')
     
       # Loop to find the minimum distance of an empty land cell that can reach all buildings
       for i in range(m):
           for j in range(n):
               if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                   answer = min(answer, distance_sum[i][j])
     
       # If no cell can reach all buildings, return -1; otherwise, return the minimum distance
       return -1 if answer == float('inf') else answer
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0339.Nested%20List%20Weight%20Sum/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
---

<!-- problem:start -->

# [339. Nested List Weight Sum 🔒](https://leetcode.com/problems/nested-list-weight-sum)


## Description

<!-- description:start -->

<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>The <strong>depth</strong> of an integer is the number of lists that it is inside of. For example, the nested list <code>[1,[2,2],[[3],2],1]</code> has each integer&#39;s value set to its <strong>depth</strong>.</p>

<p>Return <em>the sum of each integer in </em><code>nestedList</code><em> multiplied by its <strong>depth</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0339.Nested%20List%20Weight%20Sum/images/nestedlistweightsumex1.png" style="width: 405px; height: 99px;" />
<pre>
<strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Four 1&#39;s at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0339.Nested%20List%20Weight%20Sum/images/nestedlistweightsumex2.png" style="width: 315px; height: 106px;" />
<pre>
<strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> 27
<strong>Explanation:</strong> One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nestedList = [0]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 50</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-100, 100]</code>.</li>
	<li>The maximum <strong>depth</strong> of any integer is less than or equal to <code>50</code>.</li>
</ul>


```python
class Solution(object):
    def depthSum(self, nestedList):
        def helper(root, depth):
            res = 0
            for nested in root:
                if nested.isInteger():
                    res += depth * nested.getInteger()
                else:
                    res += helper(nested.getList(), depth + 1)
            return res

        return helper(nestedList, 1)
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
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#    
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

### Alternate and simple solution
```python
from queue import Queue

class MovingAverage_346:
    def __init__(self, size: int):
        self.size = size
        self.queue = Queue()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window_sum += val
        self.queue.put(val)

        if self.queue.qsize() > self.size:
            self.window_sum -= self.queue.get()

        return self.window_sum / self.queue.qsize()
```


## Meta variant
What if you had to return a resulting array of the averages of each subarray of size, "size"?

```python
from typing import List
def compute_running_sum_variant_346(nums: List[int], size: int) -> List[int]:
    result = []
    window_sum = 0
    for right in range(len(nums)):
        window_sum += nums[right]

        left = right - size
        if left >= 0:
            window_sum -= nums[left]

        if right >= size - 1:
            result.append(window_sum // size)

    return result

if __name__ == '__main__':
    nums = [5, 2, 8, 14, 3]
    size = 3
    assert compute_running_sum_variant_346(nums, size) == [5, 8, 8]

    nums = [6]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [6]

    nums = [1, 2, 3]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [1, 2, 3]

    nums = [2, 4, 6, 8, 10, 12]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [3, 5, 7, 9, 11]

    nums = [2, 4, 6, 8, 10, 12]
    size = 6
    assert compute_running_sum_variant_346(nums, size) == [(2+4+6+8+10+12)/size]

    nums = [1, 2, 3, 4, 5]
    size = 4
    assert compute_running_sum_variant_346(nums, size) == [2, 3]

    nums = [1, 2, 1, 2]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [1, 1, 1]
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0347.Top%20K%20Frequent%20Elements/README_EN.md
tags:
    - Array
    - Hash Table
    - Divide and Conquer
    - Bucket Sort
    - Counting
    - Quickselect
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

[中文文档](/solution/0300-0399/0347.Top%20K%20Frequent%20Elements/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>

<!-- description:end -->
### Time Complexity O(nlogn)
```python
from queue import PriorityQueue
class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       s = defaultdict(int)
       for n in nums:
           s[n] += 1
       q = PriorityQueue()
       for i, v in s.items():
           q.put((-v, i))
       res = []
       for _ in range(k):
           res.append(q.get()[1])
       return res
```




### Time Complexity O(n)
```
Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a 
number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or 
by recursively applying the bucket sorting algorithm.
In this process we gonna follow 3 major steps :-
Step - 1 :
 Create Frequency map:
 1.1 Iterate thru the given nums[] array
 1.2. With each iteration - check if map already contains current key
 If current key is already in the map just increase the value for this key
 Else add key value pair.
 Where key is current int and value is 1 (1 -> we encounter given key for the first time)

Step - 2 :
 Create Bucket List[]:
 index of bucket[] arr will represent the value from our map
 Why not use int[] arr? Multiple values can have the same frequency that's why we use List[] array of lists instead of regular array
 Iterate thrue the map and for each value add key at the index of that value

Step - 3 :
 If we look at bucket arr we can see that most frequent elements are located at the end of arr
 and leat frequent elemnts at the begining
 Last step is to iterate from the end to the begining of the arr and add elements to result List
```
```python
class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       s = defaultdict(int)
       for n in nums:
          s[n] += 1
       d = defaultdict(list)
       for element, freq in s.items():
           d[freq].append(element)
       res = []
       for freq in range(len(nums) , 0, -1):
           if d[freq]:
               res.extend(d[freq])
               if len(res) >= k:
                   return res[:k]
       return res
```


---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0348.Design%20Tic-Tac-Toe/README_EN.md
tags:
    - Design
    - Array
    - Hash Table
    - Matrix
    - Simulation
---

<!-- problem:start -->

# [348. Design Tic-Tac-Toe 🔒](https://leetcode.com/problems/design-tic-tac-toe)

[中文文档](/solution/0300-0399/0348.Design%20Tic-Tac-Toe/README.md)

## Description

<!-- description:start -->

<p>Assume the following rules are for the tic-tac-toe game on an <code>n x n</code> board between two players:</p>

<ol>
	<li>A move is guaranteed to be valid and is placed on an empty block.</li>
	<li>Once a winning condition is reached, no more moves are allowed.</li>
	<li>A player who succeeds in placing <code>n</code> of their marks in a horizontal, vertical, or diagonal row wins the game.</li>
</ol>

<p>Implement the <code>TicTacToe</code> class:</p>

<ul>
	<li><code>TicTacToe(int n)</code> Initializes the object the size of the board <code>n</code>.</li>
	<li><code>int move(int row, int col, int player)</code> Indicates that the player with id <code>player</code> plays at the cell <code>(row, col)</code> of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
	<ul>
		<li><code>0</code> if there is <strong>no winner</strong> after the move,</li>
		<li><code>1</code> if <strong>player 1</strong> is the winner after the move, or</li>
		<li><code>2</code> if <strong>player 2</strong> is the winner after the move.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;TicTacToe&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
<strong>Output</strong>
[null, 0, 0, 0, 0, 0, 0, 1]

<strong>Explanation</strong>
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is &quot;X&quot; and player 2 is &quot;O&quot; in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1&nbsp;(player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li>player is <code>1</code> or <code>2</code>.</li>
	<li><code>0 &lt;= row, col &lt; n</code></li>
	<li><code>(row, col)</code> are <strong>unique</strong> for each different call to <code>move</code>.</li>
	<li>At most <code>n<sup>2</sup></code> calls will be made to <code>move</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Could you do better than <code>O(n<sup>2</sup>)</code> per <code>move()</code> operation?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We can use an array of length $n \times 2 + 2$ to record the number of pieces each player has in each row, each column, and the two diagonals. We need two such arrays to record the number of pieces for the two players respectively.

When a player has $n$ pieces in a certain row, column, or diagonal, that player wins.

In terms of time complexity, the time complexity of each move is $O(1)$. The space complexity is $O(n)$, where $n$ is the length of the side of the chessboard.

<!-- tabs:start -->

#### Python3

```python
class TicTacToe:
   def __init__(self, n: int):
       """
       Initialize the TicTacToe game board with a given size.
       """
       self.board_size = n
       # self.counters store the counts for (rows, columns, diagonal, anti-diagonal)
       # self.counters[player][i]:
       # i from 0 to n-1 (row counts), i from n to 2*n-1 (column counts),
       # i equals 2*n (main diagonal count), i equals 2*n + 1 (anti-diagonal count)
       # Index 0: player 1, Index 1: player 2
       self.counters = [[0] * (2 * n + 2) for _ in range(2)]
   def move(self, row: int, col: int, player: int) -> int:
       """
       Player makes a move at a specified row and column.
       :param row: The row index of the board, 0-indexed.
       :param col: The column index of the board, 0-indexed.
       :param player: The identifier of the player (either 1 or 2).
       :return: The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
       """
       player_index = player - 1  # Convert to 0-indexing for players 1 and 2
       diagonal_index = 2 * self.board_size
       anti_diagonal_index = 2 * self.board_size + 1
       # Update the row, column, and possibly the diagonal counts for the move
       self.counters[player_index][row] += 1  # Row count
       self.counters[player_index][col + self.board_size] += 1  # Column count
       if row == col:
           self.counters[player_index][diagonal_index] += 1  # Diagonal count
       if row + col == self.board_size - 1:
           self.counters[player_index][anti_diagonal_index] += 1  # Anti-diagonal count
       # Check if any count has reached the board size, which means a win.
       if (
           self.counters[player_index][row] == self.board_size
           or self.counters[player_index][col + self.board_size] == self.board_size
           or self.counters[player_index][diagonal_index] == self.board_size
           or self.counters[player_index][anti_diagonal_index] == self.board_size
       ):
           return player  # The current player wins
       # If no win, return 0 indicating no winner yet
       return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
```

#### Java

```java
class TicTacToe {
    private int n;
    private int[][] cnt;

    public TicTacToe(int n) {
        this.n = n;
        cnt = new int[2][(n << 1) + 2];
    }

    public int move(int row, int col, int player) {
        int[] cur = cnt[player - 1];
        ++cur[row];
        ++cur[n + col];
        if (row == col) {
            ++cur[n << 1];
        }
        if (row + col == n - 1) {
            ++cur[n << 1 | 1];
        }
        if (cur[row] == n || cur[n + col] == n || cur[n << 1] == n || cur[n << 1 | 1] == n) {
            return player;
        }
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
```

#### C++

```cpp
class TicTacToe {
private:
    int n;
    vector<vector<int>> cnt;

public:
    TicTacToe(int n)
        : n(n)
        , cnt(2, vector<int>((n << 1) + 2, 0)) {
    }

    int move(int row, int col, int player) {
        vector<int>& cur = cnt[player - 1];
        ++cur[row];
        ++cur[n + col];
        if (row == col) {
            ++cur[n << 1];
        }
        if (row + col == n - 1) {
            ++cur[n << 1 | 1];
        }
        if (cur[row] == n || cur[n + col] == n || cur[n << 1] == n || cur[n << 1 | 1] == n) {
            return player;
        }
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
```

#### Go

```go
type TicTacToe struct {
	n   int
	cnt [][]int
}

func Constructor(n int) TicTacToe {
	cnt := make([][]int, 2)
	for i := range cnt {
		cnt[i] = make([]int, (n<<1)+2)
	}
	return TicTacToe{n, cnt}
}

func (this *TicTacToe) Move(row int, col int, player int) int {
	cur := this.cnt[player-1]
	cur[row]++
	cur[this.n+col]++
	if row == col {
		cur[this.n<<1]++
	}
	if row+col == this.n-1 {
		cur[this.n<<1|1]++
	}
	if cur[row] == this.n || cur[this.n+col] == this.n || cur[this.n<<1] == this.n || cur[this.n<<1|1] == this.n {
		return player
	}
	return 0
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Move(row,col,player);
 */
```

#### TypeScript

```ts
class TicTacToe {
    private n: number;
    private cnt: number[][];

    constructor(n: number) {
        this.n = n;
        this.cnt = [Array((n << 1) + 2).fill(0), Array((n << 1) + 2).fill(0)];
    }

    move(row: number, col: number, player: number): number {
        const cur = this.cnt[player - 1];
        cur[row]++;
        cur[this.n + col]++;
        if (row === col) {
            cur[this.n << 1]++;
        }
        if (row + col === this.n - 1) {
            cur[(this.n << 1) | 1]++;
        }
        if (
            cur[row] === this.n ||
            cur[this.n + col] === this.n ||
            cur[this.n << 1] === this.n ||
            cur[(this.n << 1) | 1] === this.n
        ) {
            return player;
        }
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0378.Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix/README_EN.md
tags:
    - Array
    - Binary Search
    - Matrix
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)

[中文文档](/solution/0300-0399/0378.Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix/README.md)

## Description

<!-- description:start -->

<p>Given an <code>n x n</code> <code>matrix</code> where each of the rows and columns is sorted in ascending order, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest element in the matrix</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> smallest element <strong>in the sorted order</strong>, not the <code>k<sup>th</sup></code> <strong>distinct</strong> element.</p>

<p>You must find a solution with a memory complexity better than <code>O(n<sup>2</sup>)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
<strong>Output:</strong> 13
<strong>Explanation:</strong> The elements in the matrix are [1,5,9,10,11,12,13,<u><strong>13</strong></u>,15], and the 8<sup>th</sup> smallest number is 13
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[-5]], k = 1
<strong>Output:</strong> -5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the rows and columns of <code>matrix</code> are <strong>guaranteed</strong> to be sorted in <strong>non-decreasing order</strong>.</li>
	<li><code>1 &lt;= k &lt;= n<sup>2</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Could you solve the problem with a constant memory (i.e., <code>O(1)</code> memory complexity)?</li>
	<li>Could you solve the problem in <code>O(n)</code> time complexity? The solution may be too advanced for an interview but you may find reading <a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a> fun.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->


<!-- tabs:start -->

#### Python3

#### Using PriorityQueue(Inefficient)
Time: O(M * N * logK), where M <= 300 is the number of rows, N <= 300 is the number of columns.
Space: O(K), space for heap which stores up to k elements.
```python
from queue import PriorityQueue


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = PriorityQueue()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                q.put(-matrix[i][j])
                if q.qsize() > k:
                    q.get()
        return -q.get()

```
#### Using more efficient PriorityQueue
Since each of the rows in matrix are already sorted, we can understand the problem as finding the kth smallest element from amongst M sorted rows.
We start the pointers to point to the beginning of each rows, then we iterate k times, for each time ith, the top of the minHeap is the ith smallest element in the matrix. We pop the top from the minHeap then add the next element which has the same row with that top to the minHeap.


Time: O(K * logK)
Space: O(K)
```python
from queue import PriorityQueue


class Solution:  # 204 ms, faster than 54.32%
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = PriorityQueue()
        for r in range(min(k, m)):
            q.put((matrix[r][0], r, 0))
        ans = -1  # any dummy value
        for i in range(k):
            ans, r, c = q.get()
            if c + 1 < n:
                q.put((matrix[r][c + 1], r, c + 1))
        return ans
```

#### Using Binary Search
Algorithm

Start with left = minOfMatrix = matrix[0][0] and right = maxOfMatrix = matrix[n-1][n-1].  
Find the mid of the left and the right. This middle number is NOT necessarily an element in the matrix.  
If countLessOrEqual(mid) >= k, we keep current ans = mid and try to find smaller value by searching in the left side. Otherwise, we search in the right side.  
Since ans is the smallest value which countLessOrEqual(ans) >= k, so it's the k th smallest element in the matrix.  

How to count number of elements less or equal to x efficiently?

Since our matrix is sorted in ascending order by rows and columns.  
We use two pointers, one points to the rightmost column c = n-1, and one points to the lowest row r = 0.  
If matrix[r][c] <= x then the number of elements in row r less or equal to x is (c+1) (Because row[r] is sorted in ascending order, so if matrix[r][c] <= x then matrix[r][c-1] is also <= x). Then we go to next row to continue counting.  
Else if matrix[r][c] > x, we decrease column c until matrix[r][c] <= x (Because column is sorted in ascending order, so if matrix[r][c] > x then matrix[r+1][c] is also > x).  
Time complexity for counting: O(M+N).
```python
class Solution:  # 160 ms, faster than 93.06%
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(
            matrix[0]
        )  # For general, the matrix need not be a square

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1  # decrease column until matrix[r][c] <= x
                cnt += c + 1
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans
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


---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0392.Is%20Subsequence/README_EN.md
tags:
    - Two Pointers
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence)

[中文文档](/solution/0300-0399/0392.Is%20Subsequence/README.md)

## Description

<!-- description:start -->

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>subsequence</strong> of </em><code>t</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Suppose there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We define two pointers $i$ and $j$ to point to the initial position of the string $s$ and $t$ respectively. Each time we compare the two characters pointed to by the two pointers, if they are the same, both pointers move right at the same time; if they are not the same, only $j$ moves right. When the pointer $i$ moves to the end of the string $s$, it means that $s$ is the subsequence of $t$.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the strings $s$ and $t$ respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0398.Random%20Pick%20Index/README_EN.md
tags:
    - Reservoir Sampling
    - Hash Table
    - Math
    - Randomized
---

<!-- problem:start -->

# [398. Random Pick Index](https://leetcode.com/problems/random-pick-index)

[中文文档](/solution/0300-0399/0398.Random%20Pick%20Index/README.md)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> with possible <strong>duplicates</strong>, randomly output the index of a given <code>target</code> number. You can assume that the given target number must exist in the array.</p>

<p>Implement the <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int[] nums)</code> Initializes the object with the array <code>nums</code>.</li>
	<li><code>int pick(int target)</code> Picks a random index <code>i</code> from <code>nums</code> where <code>nums[i] == target</code>. If there are multiple valid i&#39;s, then each index should have an equal probability of returning.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Solution&quot;, &quot;pick&quot;, &quot;pick&quot;, &quot;pick&quot;]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
<strong>Output</strong>
[null, 4, 0, 2]

<strong>Explanation</strong>
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>target</code> is an integer from <code>nums</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>pick</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = ans = 0
        for i, v in enumerate(self.nums):
            if v == target:
                n += 1
                x = random.randint(1, n)
                if x == n:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

## Meta variant
What if you had to use reservoir sampling to pick an index of the maximum value in the array?
```
#pragma once

#include <vector>

// VARIANT: What if you had to use reservoir sampling to pick an index of the maximum value in the array?
int randomPickIndex_second_variant_398(std::vector<int>& nums)
{
    int max_number = INT_MIN;
    int picked_index = -1;
    int n = 0;
    for (int i = 0; i < nums.size(); i++) {
        int curr_num = nums[i];
        if (curr_num < max_number)
            continue;

        if (curr_num > max_number) {
            max_number = curr_num;
            picked_index = i;
            n = 1;
        }
        else if (curr_num == max_number) {
            n++;
            int r = rand() % n;
            if (r == 0)
                picked_index = i;
        }
    }
    return picked_index;
}
```

# [408. Valid Word Abbreviation 🔒](https://leetcode.com/problems/valid-word-abbreviation)


## Description

<!-- description:start -->

<p>A string can be <strong>abbreviated</strong> by replacing any number of <strong>non-adjacent</strong>, <strong>non-empty</strong> substrings with their lengths. The lengths <strong>should not</strong> have leading zeros.</p>

<p>For example, a string such as <code>&quot;substitution&quot;</code> could be abbreviated as (but not limited to):</p>

<ul>
	<li><code>&quot;s10n&quot;</code> (<code>&quot;s <u>ubstitutio</u> n&quot;</code>)</li>
	<li><code>&quot;sub4u4&quot;</code> (<code>&quot;sub <u>stit</u> u <u>tion</u>&quot;</code>)</li>
	<li><code>&quot;12&quot;</code> (<code>&quot;<u>substitution</u>&quot;</code>)</li>
	<li><code>&quot;su3i1u2on&quot;</code> (<code>&quot;su <u>bst</u> i <u>t</u> u <u>ti</u> on&quot;</code>)</li>
	<li><code>&quot;substitution&quot;</code> (no substrings replaced)</li>
</ul>

<p>The following are <strong>not valid</strong> abbreviations:</p>

<ul>
	<li><code>&quot;s55n&quot;</code> (<code>&quot;s <u>ubsti</u> <u>tutio</u> n&quot;</code>, the replaced substrings are adjacent)</li>
	<li><code>&quot;s010n&quot;</code> (has leading zeros)</li>
	<li><code>&quot;s0ubstitution&quot;</code> (replaces an empty substring)</li>
</ul>

<p>Given a string <code>word</code> and an abbreviation <code>abbr</code>, return <em>whether the string <strong>matches</strong> the given abbreviation</em>.</p>

<p>A <strong>substring</strong> is a contiguous <strong>non-empty</strong> sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;internationalization&quot;, abbr = &quot;i12iz4n&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The word &quot;internationalization&quot; can be abbreviated as &quot;i12iz4n&quot; (&quot;i <u>nternational</u> iz <u>atio</u> n&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;apple&quot;, abbr = &quot;a2e&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The word &quot;apple&quot; cannot be abbreviated as &quot;a2e&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 20</code></li>
	<li><code>word</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= abbr.length &lt;= 10</code></li>
	<li><code>abbr</code> consists of lowercase English letters and digits.</li>
	<li>All the integers in <code>abbr</code> will fit in a 32-bit integer.</li>
</ul>

### Solution 1: Simulation

We can directly simulate character matching and replacement.

Assume the lengths of the string $word$ and the string $abbr$ are $m$ and $n$ respectively. We use two pointers $i$ and $j$ to point to the initial positions of the string $word$ and the string $abbr$ respectively, and use an integer variable $x$ to record the current matched number in $abbr$.

Loop to match each character of the string $word$ and the string $abbr$:

If the character $abbr[j]$ pointed by the pointer $j$ is a number, if $abbr[j]$ is `'0'` and $x$ is $0$, it means that the number in $abbr$ has leading zeros, so it is not a valid abbreviation, return `false`; otherwise, update $x$ to $x \times 10 + abbr[j] - '0'$.

If the character $abbr[j]$ pointed by the pointer $j$ is not a number, then we move the pointer $i$ forward by $x$ positions at this time, and then reset $x$ to $0$. If $i \geq m$ or $word[i] \neq abbr[j]$ at this time, it means that the two strings cannot match, return `false`; otherwise, move the pointer $i$ forward by $1$ position.

Then we move the pointer $j$ forward by $1$ position, repeat the above process, until $i$ exceeds the length of the string $word$ or $j$ exceeds the length of the string $abbr$.

Finally, if $i + x$ equals $m$ and $j$ equals $n$, it means that the string $word$ can be abbreviated as the string $abbr$, return `true`; otherwise return `false`.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the string $word$ and the string $abbr$ respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = x = 0
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == "0" and x == 0:
                    return False
                x = x * 10 + int(abbr[j])
            else:
                i += x
                x = 0
                if i >= m or word[i] != abbr[j]:
                    return False
                i += 1
            j += 1
        return i + x == m and j == n
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0415.Add%20Strings/README_EN.md
tags:
    - Math
    - String
    - Simulation
---

<!-- problem:start -->

# [415. Add Strings](https://leetcode.com/problems/add-strings)

[中文文档](/solution/0400-0499/0415.Add%20Strings/README.md)

## Description

<!-- description:start -->

<p>Given two non-negative integers, <code>num1</code> and <code>num2</code> represented as string, return <em>the sum of</em> <code>num1</code> <em>and</em> <code>num2</code> <em>as a string</em>.</p>

<p>You must solve the problem without using any built-in library for handling large integers (such as <code>BigInteger</code>). You must also not convert the inputs to integers directly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;11&quot;, num2 = &quot;123&quot;
<strong>Output:</strong> &quot;134&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;456&quot;, num2 = &quot;77&quot;
<strong>Output:</strong> &quot;533&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;0&quot;, num2 = &quot;0&quot;
<strong>Output:</strong> &quot;0&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1.length, num2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>num1</code> and <code>num2</code> consist of only digits.</li>
	<li><code>num1</code> and <code>num2</code> don&#39;t have any leading zeros except for the zero itself.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers $i$ and $j$ to point to the end of the two strings respectively, and start adding bit by bit from the end. Each time we take out the corresponding digits $a$ and $b$, calculate their sum $a + b + c$, where $c$ represents the carry from the last addition. Finally, we append the units digit of $a + b + c$ to the end of the answer string, and then take the tens digit of $a + b + c$ as the value of the carry $c$, and loop this process until the pointers of both strings have pointed to the beginning of the string and the value of the carry $c$ is $0$.

Finally, reverse the answer string and return it.

The time complexity is $O(\max(m, n))$, where $m$ and $n$ are the lengths of the two strings respectively. Ignoring the space consumption of the answer string, the space complexity is $O(1)$.

The following code also implements string subtraction, refer to the `subStrings(num1, num2)` function.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0 or j >= 0 or c:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            c, v = divmod(a + b + c, 10)
            ans.append(str(v))
            i, j = i - 1, j - 1
        return "".join(ans[::-1])

    def subStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        neg = m < n or (m == n and num1 < num2)
        if neg:
            num1, num2 = num2, num1
        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0:
            c = int(num1[i]) - c - (0 if j < 0 else int(num2[j]))
            ans.append(str((c + 10) % 10))
            c = 1 if c < 0 else 0
            i, j = i - 1, j - 1
        while len(ans) > 1 and ans[-1] == '0':
            ans.pop()
        if neg:
            ans.append('-')
        return ''.join(ans[::-1])
```

## Meta variant
What if you had to add two strings of numbers that could contain decimals?
Both, one or neither could have decimals. Very, very tricky...
```python
class Solution:
    def add_string_decimals_415(self, num1: str, num2: str) -> str:
        nums1 = num1.split('.')
        nums2 = num2.split('.')
        decimals1 = nums1[1] if len(nums1) > 1 else ''
        decimals2 = nums2[1] if len(nums2) > 1 else ''

        max_len = max(len(decimals1), len(decimals2))
        decimals1 = decimals1.ljust(max_len, '0')
        decimals2 = decimals2.ljust(max_len, '0')

        carry = [0]
        result = []
        
        def add_strings_415(num1: str, num2: str, carry: list) -> str:
            n1 = len(num1) - 1
            n2 = len(num2) - 1
            result = []
            while n1 >= 0 or n2 >= 0:
                sum = 0
                if n1 >= 0:
                    sum += int(num1[n1])
                    n1 -= 1
                if n2 >= 0:
                    sum += int(num2[n2])
                    n2 -= 1
                sum += carry[0]

                result.append(str(sum % 10))
                carry[0] = sum // 10
            
            return ''.join(result)

        result.append(add_strings_415(decimals1, decimals2, carry))

        if decimals1 or decimals2:
            result.append('.')
        
        result.append(add_strings_415(nums1[0], nums2[0], carry))
        if carry[0]:
            print(carry)
            result.append(str(carry[0]))
        return "".join(result)[::-1]


if __name__ == "__main__":
    solution = Solution()
    # Only Whole Numbers
    assert solution.add_string_decimals_415("11", "123") == "134"
    assert solution.add_string_decimals_415("456", "77") == "533"
    assert solution.add_string_decimals_415("0", "0") == "0"
    assert solution.add_string_decimals_415("0", "2983435243982343") == "2983435243982343"
    assert solution.add_string_decimals_415("99999999", "2983435243982343") == "2983435343982342"
    assert solution.add_string_decimals_415("99999999", "99999999999") == "100099999998"

    # Both Decimals With And Without Carry
    assert solution.add_string_decimals_415("123.53", "11.2") == "134.73"
    assert solution.add_string_decimals_415("687345.3434321", "389457248.24374657243") == "390144593.58717867243"
    assert solution.add_string_decimals_415(".56", ".12") == ".68"
    assert solution.add_string_decimals_415(".5995495049556", ".12") == ".7195495049556"
    assert solution.add_string_decimals_415(".9479823748932", ".716400040030") == "1.6643824149232"
    assert solution.add_string_decimals_415(".00009479823748932", ".000000716400040030") == ".000095514637529350"
    assert solution.add_string_decimals_415(".00009479823748932", ".00000071640004003000000") == ".00009551463752935000000"
    assert solution.add_string_decimals_415("110.12", "9.") == "119.12"
    assert solution.add_string_decimals_415("111111110.0013430430433434454001", "9.") == "111111119.0013430430433434454001"
    assert solution.add_string_decimals_415("111111110.0013430430433434454001", "993483400013438854.") == "993483400124549964.0013430430433434454001"
    assert solution.add_string_decimals_415("910.99999", "999.9999") == "1910.99989"
    assert solution.add_string_decimals_415("999999.99999", "999999.9999") == "1999999.99989"
    assert solution.add_string_decimals_415("123.525", "11.2") == "134.725"
    assert solution.add_string_decimals_415("1234540458475845.", "8348736.") == "1234540466824581"

    # # One Decimal, One Whole Number
    assert solution.add_string_decimals_415("110.75", "9") == "119.75"
    assert solution.add_string_decimals_415("110.75", "9999999") == "10000109.75"
    assert solution.add_string_decimals_415("150423434.00000000000", "9999999.") == "160423433.00000000000"
    assert solution.add_string_decimals_415("150423434.0000009184837483", "9999999.") == "160423433.0000009184837483"
    assert solution.add_string_decimals_415("110.9010479382798527", "9999999.") == "10000109.9010479382798527"
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/README_EN.md
tags:
    - Stack
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Linked List
    - Binary Tree
    - Doubly-Linked List
---

<!-- problem:start -->

# [426. Convert Binary Search Tree to Sorted Doubly Linked List 🔒](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list)

[中文文档](/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/README.md)

## Description

<!-- description:start -->

<p>Convert a <strong>Binary Search Tree</strong> to a sorted <strong>Circular Doubly-Linked List</strong> in place.</p>

<p>You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.</p>

<p>We want to do the transformation <strong>in place</strong>. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/images/bstdlloriginalbst.png" style="width: 100%; max-width: 300px;" /></p>

<pre>
<strong>Input:</strong> root = [4,2,5,1,3]

<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/images/bstdllreturndll.png" style="width: 100%; max-width: 450px;" />
<strong>Output:</strong> [1,2,3,4,5]

<strong>Explanation:</strong> The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/images/bstdllreturnbst.png" style="width: 100%; max-width: 450px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>All the values of the tree are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if root is None:
                return
            nonlocal prev, head
            dfs(root.left)
            if prev:
                prev.right = root
                root.left = prev
            else:
                head = root
            prev = root
            dfs(root.right)

        if root is None:
            return None
        head = prev = None
        dfs(root)
        prev.right = head
        head.left = prev
        return head
```

#### Without Using Global Variables(using stack) Important for META
```python
class Solution:
   def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
   if not root:
       return root
   st = []
   temp = prev = result = None
   while root:
       st.append(root)
       root = root.left
  
   while st:
       curr = st.pop()
       if prev:
           prev.right = curr
           curr.left = prev
       else:
           result = curr
       prev = curr
       temp = curr.right
       while temp:
           st.append(temp)
           temp = temp.left
      
   result.left = prev
   prev.right = result
   return result
```
#### Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class Solution {
    private Node prev;
    private Node head;

    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return null;
        }
        prev = null;
        head = null;
        dfs(root);
        prev.right = head;
        head.left = prev;
        return head;
    }

    private void dfs(Node root) {
        if (root == null) {
            return;
        }
        dfs(root.left);
        if (prev != null) {
            prev.right = root;
            root.left = prev;
        } else {
            head = root;
        }
        prev = root;
        dfs(root.right);
    }
}
```

#### C++

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class Solution {
public:
    Node* prev;
    Node* head;

    Node* treeToDoublyList(Node* root) {
        if (!root) return nullptr;
        prev = nullptr;
        head = nullptr;
        dfs(root);
        prev->right = head;
        head->left = prev;
        return head;
    }

    void dfs(Node* root) {
        if (!root) return;
        dfs(root->left);
        if (prev) {
            prev->right = root;
            root->left = prev;
        } else
            head = root;
        prev = root;
        dfs(root->right);
    }
};
```

#### Go

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 * }
 */

func treeToDoublyList(root *Node) *Node {
	if root == nil {
		return root
	}
	var prev, head *Node

	var dfs func(root *Node)
	dfs = func(root *Node) {
		if root == nil {
			return
		}
		dfs(root.Left)
		if prev != nil {
			prev.Right = root
			root.Left = prev
		} else {
			head = root
		}
		prev = root
		dfs(root.Right)
	}
	dfs(root)
	prev.Right = head
	head.Left = prev
	return head
}
```

#### JavaScript

```js
/**
 * // Definition for a Node.
 * function Node(val, left, right) {
 *      this.val = val;
 *      this.left = left;
 *      this.right = right;
 *  };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var treeToDoublyList = function (root) {
    if (!root) return root;
    let prev = null;
    let head = null;

    function dfs(root) {
        if (!root) return;
        dfs(root.left);
        if (prev) {
            prev.right = root;
            root.left = prev;
        } else {
            head = root;
        }
        prev = root;
        dfs(root.right);
    }
    dfs(root);
    prev.right = head;
    head.left = prev;
    return head;
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0435.Non-overlapping%20Intervals/README_EN.md
tags:
    - Greedy
    - Array
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)

[中文文档](/solution/0400-0499/0435.Non-overlapping%20Intervals/README.md)

## Description

<!-- description:start -->

<p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p><strong>Note</strong> that intervals which only touch at a point are <strong>non-overlapping</strong>. For example, <code>[1, 2]</code> and <code>[2, 3]</code> are non-overlapping.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1
Actually, the problem is the same as "Given a collection of intervals, find the maximum number of intervals that are non-overlapping." (the classic Greedy problem: Interval Scheduling). With the solution to that problem, guess how do we get the minimum number of intervals to remove? : )
Sorting Interval.end in ascending order is O(nlogn), then traverse intervals array to get the maximum number of non-overlapping intervals is O(n). Total is O(nlogn).

<!-- tabs:start -->

#### Python3

```python
class Solution:
   def eraseOverlapIntervals(self, it: List[List[int]]) -> int:
       it.sort(key = lambda x: x[1])
       count = 1
       end = it[0][1]
       for i in range(1, len(it)):
           if it[i][0] >= end:
               end = it[i][1]
               count += 1
       return len(it) - count
```

#### Java

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int t = intervals[0][1], ans = 0;
        for (int i = 1; i < intervals.length; ++i) {
            if (intervals[i][0] >= t) {
                t = intervals[i][1];
            } else {
                ++ans;
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) { return a[1] < b[1]; });
        int ans = 0, t = intervals[0][1];
        for (int i = 1; i < intervals.size(); ++i) {
            if (t <= intervals[i][0])
                t = intervals[i][1];
            else
                ++ans;
        }
        return ans;
    }
};
```

#### Go

```go
func eraseOverlapIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})
	t, ans := intervals[0][1], 0
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] >= t {
			t = intervals[i][1]
		} else {
			ans++
		}
	}
	return ans
}
```

#### TypeScript

```ts
function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);
    let end = intervals[0][1],
        ans = 0;
    for (let i = 1; i < intervals.length; ++i) {
        let cur = intervals[i];
        if (end > cur[0]) {
            ans++;
        } else {
            end = cur[1];
        }
    }
    return ans;
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        d = [intervals[0][1]]
        for s, e in intervals[1:]:
            if s >= d[-1]:
                d.append(e)
            else:
                idx = bisect_left(d, s)
                d[idx] = min(d[idx], e)
        return len(intervals) - len(d)
```

#### Java

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        int n = intervals.length;
        int[] d = new int[n + 1];
        d[1] = intervals[0][1];
        int size = 1;
        for (int i = 1; i < n; ++i) {
            int s = intervals[i][0], e = intervals[i][1];
            if (s >= d[size]) {
                d[++size] = e;
            } else {
                int left = 1, right = size;
                while (left < right) {
                    int mid = (left + right) >> 1;
                    if (d[mid] >= s) {
                        right = mid;
                    } else {
                        left = mid + 1;
                    }
                }
                d[left] = Math.min(d[left], e);
            }
        }
        return n - size;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0480.Sliding%20Window%20Median/README_EN.md
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median)

[中文文档](/solution/0400-0499/0480.Sliding%20Window%20Median/README.md)

## Description

<!-- description:start -->

<p>The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.</p>

<ul>
	<li>For examples, if <code>arr = [2,<u>3</u>,4]</code>, the median is <code>3</code>.</li>
	<li>For examples, if <code>arr = [1,<u>2,3</u>,4]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. There is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the median array for each window in the original array</em>. Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
<strong>Explanation:</strong> 
Window position                Median
---------------                -----
[<strong>1  3  -1</strong>] -3  5  3  6  7        1
 1 [<strong>3  -1  -3</strong>] 5  3  6  7       -1
 1  3 [<strong>-1  -3  5</strong>] 3  6  7       -1
 1  3  -1 [<strong>-3  5  3</strong>] 6  7        3
 1  3  -1  -3 [<strong>5  3  6</strong>] 7        5
 1  3  -1  -3  5 [<strong>3  6  7</strong>]       6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,2,3,1,4,2], k = 3
<strong>Output:</strong> [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dual Priority Queues (Min-Heap and Max-Heap) + Lazy Deletion

We can use two priority queues (min-heap and max-heap) to maintain the elements in the current window. One priority queue stores the smaller half of the elements, and the other priority queue stores the larger half of the elements. This way, the median of the current window is either the average of the top elements of the two heaps or one of the top elements.

We design a class $\textit{MedianFinder}$ to maintain the elements in the current window. This class includes the following methods:

-   `add_num(num)`: Adds $\textit{num}$ to the current window.
-   `find_median()`: Returns the median of the elements in the current window.
-   `remove_num(num)`: Removes $\textit{num}$ from the current window.
-   `prune(pq)`: If the top element of the heap is in the lazy deletion dictionary $\textit{delayed}$, it pops the top element from the heap and decrements its lazy deletion count. If the lazy deletion count of the element becomes zero, it removes the element from the lazy deletion dictionary.
-   `rebalance()`: If the number of elements in the smaller half exceeds the number of elements in the larger half by $2$, it moves the top element of the larger half to the smaller half. If the number of elements in the smaller half is less than the number of elements in the larger half, it moves the top element of the larger half to the smaller half.

In the `add_num(num)` method, we first consider adding $\textit{num}$ to the smaller half. If $\textit{num}$ is greater than the top element of the larger half, we add $\textit{num}$ to the larger half. Then we call the `rebalance()` method to ensure that the size difference between the two priority queues does not exceed $1$.

In the `remove_num(num)` method, we increment the lazy deletion count of $\textit{num}$. Then we compare $\textit{num}$ with the top element of the smaller half. If $\textit{num}$ is less than or equal to the top element of the smaller half, we update the size of the smaller half and call the `prune()` method to ensure that the top element of the smaller half is not in the lazy deletion dictionary. Otherwise, we update the size of the larger half and call the `prune()` method to ensure that the top element of the larger half is not in the lazy deletion dictionary.

In the `find_median()` method, if the current window size is odd, we return the top element of the smaller half; otherwise, we return the average of the top elements of the smaller half and the larger half.

In the `prune(pq)` method, if the top element of the heap is in the lazy deletion dictionary, it pops the top element from the heap and decrements its lazy deletion count. If the lazy deletion count of the element becomes zero, it removes the element from the lazy deletion dictionary.

In the `rebalance()` method, if the number of elements in the smaller half exceeds the number of elements in the larger half by $2$, it moves the top element of the larger half to the smaller half. If the number of elements in the smaller half is less than the number of elements in the larger half, it moves the top element of the larger half to the smaller half.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class MedianFinder:
    def __init__(self, k: int):
        self.k = k
        self.small = []
        self.large = []
        self.delayed = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def add_num(self, num: int):
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
            self.small_size += 1
        else:
            heappush(self.large, num)
            self.large_size += 1
        self.rebalance()

    def find_median(self) -> float:
        return -self.small[0] if self.k & 1 else (-self.small[0] + self.large[0]) / 2

    def remove_num(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.rebalance()

    def prune(self, pq: List[int]):
        sign = -1 if pq is self.small else 1
        while pq and sign * pq[0] in self.delayed:
            self.delayed[sign * pq[0]] -= 1
            if self.delayed[sign * pq[0]] == 0:
                self.delayed.pop(sign * pq[0])
            heappop(pq)

    def rebalance(self):
        if self.small_size > self.large_size + 1:
            heappush(self.large, -heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heappush(self.small, -heappop(self.large))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder(k)
        for x in nums[:k]:
            finder.add_num(x)
        ans = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.remove_num(nums[i - k])
            ans.append(finder.find_median())
        return ans
```

#### Java

```java
class MedianFinder {
    private PriorityQueue<Integer> small = new PriorityQueue<>(Comparator.reverseOrder());
    private PriorityQueue<Integer> large = new PriorityQueue<>();
    private Map<Integer, Integer> delayed = new HashMap<>();
    private int smallSize;
    private int largeSize;
    private int k;

    public MedianFinder(int k) {
        this.k = k;
    }

    public void addNum(int num) {
        if (small.isEmpty() || num <= small.peek()) {
            small.offer(num);
            ++smallSize;
        } else {
            large.offer(num);
            ++largeSize;
        }
        rebalance();
    }

    public double findMedian() {
        return (k & 1) == 1 ? small.peek() : ((double) small.peek() + large.peek()) / 2;
    }

    public void removeNum(int num) {
        delayed.merge(num, 1, Integer::sum);
        if (num <= small.peek()) {
            --smallSize;
            if (num == small.peek()) {
                prune(small);
            }
        } else {
            --largeSize;
            if (num == large.peek()) {
                prune(large);
            }
        }
        rebalance();
    }

    private void prune(PriorityQueue<Integer> pq) {
        while (!pq.isEmpty() && delayed.containsKey(pq.peek())) {
            if (delayed.merge(pq.peek(), -1, Integer::sum) == 0) {
                delayed.remove(pq.peek());
            }
            pq.poll();
        }
    }

    private void rebalance() {
        if (smallSize > largeSize + 1) {
            large.offer(small.poll());
            --smallSize;
            ++largeSize;
            prune(small);
        } else if (smallSize < largeSize) {
            small.offer(large.poll());
            --largeSize;
            ++smallSize;
            prune(large);
        }
    }
}

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        MedianFinder finder = new MedianFinder(k);
        for (int i = 0; i < k; ++i) {
            finder.addNum(nums[i]);
        }
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        ans[0] = finder.findMedian();
        for (int i = k; i < n; ++i) {
            finder.addNum(nums[i]);
            finder.removeNum(nums[i - k]);
            ans[i - k + 1] = finder.findMedian();
        }
        return ans;
    }
}
```

#### C++

```cpp
class MedianFinder {
public:
    MedianFinder(int k) {
        this->k = k;
    }

    void addNum(int num) {
        if (small.empty() || num <= small.top()) {
            small.push(num);
            ++smallSize;
        } else {
            large.push(num);
            ++largeSize;
        }
        reblance();
    }

    void removeNum(int num) {
        ++delayed[num];
        if (num <= small.top()) {
            --smallSize;
            if (num == small.top()) {
                prune(small);
            }
        } else {
            --largeSize;
            if (num == large.top()) {
                prune(large);
            }
        }
        reblance();
    }

    double findMedian() {
        return k & 1 ? small.top() : ((double) small.top() + large.top()) / 2.0;
    }

private:
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> large;
    unordered_map<int, int> delayed;
    int smallSize = 0;
    int largeSize = 0;
    int k;

    template <typename T>
    void prune(T& pq) {
        while (!pq.empty() && delayed[pq.top()]) {
            if (--delayed[pq.top()] == 0) {
                delayed.erase(pq.top());
            }
            pq.pop();
        }
    }

    void reblance() {
        if (smallSize > largeSize + 1) {
            large.push(small.top());
            small.pop();
            --smallSize;
            ++largeSize;
            prune(small);
        } else if (smallSize < largeSize) {
            small.push(large.top());
            large.pop();
            ++smallSize;
            --largeSize;
            prune(large);
        }
    }
};

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        MedianFinder finder(k);
        for (int i = 0; i < k; ++i) {
            finder.addNum(nums[i]);
        }
        vector<double> ans = {finder.findMedian()};
        for (int i = k; i < nums.size(); ++i) {
            finder.addNum(nums[i]);
            finder.removeNum(nums[i - k]);
            ans.push_back(finder.findMedian());
        }
        return ans;
    }
};
```

#### Go

```go
type MedianFinder struct {
	small                hp
	large                hp
	delayed              map[int]int
	smallSize, largeSize int
	k                    int
}

func Constructor(k int) MedianFinder {
	return MedianFinder{hp{}, hp{}, map[int]int{}, 0, 0, k}
}

func (this *MedianFinder) AddNum(num int) {
	if this.small.Len() == 0 || num <= -this.small.IntSlice[0] {
		heap.Push(&this.small, -num)
		this.smallSize++
	} else {
		heap.Push(&this.large, num)
		this.largeSize++
	}
	this.rebalance()
}

func (this *MedianFinder) FindMedian() float64 {
	if this.k&1 == 1 {
		return float64(-this.small.IntSlice[0])
	}
	return float64(-this.small.IntSlice[0]+this.large.IntSlice[0]) / 2
}

func (this *MedianFinder) removeNum(num int) {
	this.delayed[num]++
	if num <= -this.small.IntSlice[0] {
		this.smallSize--
		if num == -this.small.IntSlice[0] {
			this.prune(&this.small)
		}
	} else {
		this.largeSize--
		if num == this.large.IntSlice[0] {
			this.prune(&this.large)
		}
	}
	this.rebalance()
}

func (this *MedianFinder) prune(pq *hp) {
	sign := 1
	if pq == &this.small {
		sign = -1
	}
	for pq.Len() > 0 && this.delayed[sign*pq.IntSlice[0]] > 0 {
		this.delayed[sign*pq.IntSlice[0]]--
		if this.delayed[sign*pq.IntSlice[0]] == 0 {
			delete(this.delayed, sign*pq.IntSlice[0])
		}
		heap.Pop(pq)
	}
}

func (this *MedianFinder) rebalance() {
	if this.smallSize > this.largeSize+1 {
		heap.Push(&this.large, -heap.Pop(&this.small).(int))
		this.smallSize--
		this.largeSize++
		this.prune(&this.small)
	} else if this.smallSize < this.largeSize {
		heap.Push(&this.small, -heap.Pop(&this.large).(int))
		this.smallSize++
		this.largeSize--
		this.prune(&this.large)
	}
}

func medianSlidingWindow(nums []int, k int) []float64 {
	finder := Constructor(k)
	for _, num := range nums[:k] {
		finder.AddNum(num)
	}
	ans := []float64{finder.FindMedian()}
	for i := k; i < len(nums); i++ {
		finder.AddNum(nums[i])
		finder.removeNum(nums[i-k])
		ans = append(ans, finder.FindMedian())
	}
	return ans
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool { return h.IntSlice[i] < h.IntSlice[j] }
func (h *hp) Push(v any)        { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Ordered Set

We can use two ordered sets to maintain the elements in the current window. The ordered set $l$ stores the smaller half of the elements in the current window, and the ordered set $r$ stores the larger half of the elements.

We traverse the array $\textit{nums}$. For each element $x$, we add it to the ordered set $r$, then move the smallest element in the ordered set $r$ to the ordered set $l$. If the size of the ordered set $l$ is greater than the size of the ordered set $r$ by more than $1$, we move the largest element in the ordered set $l$ to the ordered set $r$.

If the total number of elements in the current window is $k$ and the size is odd, the maximum value in the ordered set $l$ is the median. If the size of the current window is even, the average of the maximum value in the ordered set $l$ and the minimum value in the ordered set $r$ is the median. Then, we remove the leftmost element of the window and continue traversing the array.

The time complexity is $O(n \log k)$, and the space complexity is $O(k)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = SortedList()
        r = SortedList()
        ans = []
        for i, x in enumerate(nums):
            r.add(x)
            l.add(r.pop(0))
            while len(l) - len(r) > 1:
                r.add(l.pop())
            j = i - k + 1
            if j >= 0:
                ans.append(l[-1] if k & 1 else (l[-1] + r[0]) / 2)
                if nums[j] in l:
                    l.remove(nums[j])
                else:
                    r.remove(nums[j])
        return ans
```

#### Java

```java
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        TreeMap<Integer, Integer> l = new TreeMap<>();
        TreeMap<Integer, Integer> r = new TreeMap<>();
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        int lSize = 0, rSize = 0;
        for (int i = 0; i < n; ++i) {
            r.merge(nums[i], 1, Integer::sum);
            int x = r.firstKey();
            if (r.merge(x, -1, Integer::sum) == 0) {
                r.remove(x);
            }
            l.merge(x, 1, Integer::sum);
            ++lSize;
            while (lSize - rSize > 1) {
                x = l.lastKey();
                if (l.merge(x, -1, Integer::sum) == 0) {
                    l.remove(x);
                }
                r.merge(x, 1, Integer::sum);
                --lSize;
                ++rSize;
            }
            int j = i - k + 1;
            if (j >= 0) {
                ans[j] = k % 2 == 1 ? l.lastKey() : ((double) l.lastKey() + r.firstKey()) / 2;
                if (l.containsKey(nums[j])) {
                    if (l.merge(nums[j], -1, Integer::sum) == 0) {
                        l.remove(nums[j]);
                    }
                    --lSize;
                } else {
                    if (r.merge(nums[j], -1, Integer::sum) == 0) {
                        r.remove(nums[j]);
                    }
                    --rSize;
                }
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> l, r;
        int n = nums.size();
        vector<double> ans;
        for (int i = 0; i < n; ++i) {
            r.insert(nums[i]);
            l.insert(*r.begin());
            r.erase(r.begin());
            while (l.size() - r.size() > 1) {
                r.insert(*l.rbegin());
                l.erase(prev(l.end()));
            }
            int j = i - k + 1;
            if (j >= 0) {
                ans.push_back(k % 2 ? *l.rbegin() : ((double) *l.rbegin() + *r.begin()) / 2);
                auto it = l.find(nums[j]);
                if (it != l.end()) {
                    l.erase(it);
                } else {
                    r.erase(r.find(nums[j]));
                }
            }
        }
        return ans;
    }
};
```

#### Go

```go
func medianSlidingWindow(nums []int, k int) (ans []float64) {
	l := redblacktree.New[int, int]()
	r := redblacktree.New[int, int]()
	merge := func(st *redblacktree.Tree[int, int], x, v int) {
		c, _ := st.Get(x)
		if c+v == 0 {
			st.Remove(x)
		} else {
			st.Put(x, c+v)
		}
	}
	lSize, rSize := 0, 0
	for i, x := range nums {
		merge(r, x, 1)
		x = r.Left().Key
		merge(r, x, -1)
		merge(l, x, 1)
		lSize++
		for lSize-rSize > 1 {
			x = l.Right().Key
			merge(l, x, -1)
			merge(r, x, 1)
			lSize--
			rSize++
		}
		if j := i - k + 1; j >= 0 {
			if k%2 == 1 {
				ans = append(ans, float64(l.Right().Key))
			} else {
				ans = append(ans, float64(l.Right().Key+r.Left().Key)/2)
			}
			if x = nums[j]; x <= l.Right().Key {
				merge(l, x, -1)
				lSize--
			} else {
				merge(r, x, -1)
				rSize--
			}
		}
	}
	return
}
```

#### TypeScript

```ts
function medianSlidingWindow(nums: number[], k: number): number[] {
    const l = new TreapMultiSet<number>((a, b) => a - b);
    const r = new TreapMultiSet<number>((a, b) => a - b);
    const n = nums.length;
    const ans: number[] = [];
    for (let i = 0; i < n; ++i) {
        r.add(nums[i]);
        l.add(r.shift()!);
        while (l.size - r.size > 1) {
            r.add(l.pop()!);
        }
        const j = i - k + 1;
        if (j >= 0) {
            ans[j] = k % 2 ? l.last()! : (l.last()! + r.first()!) / 2;
            if (nums[j] <= l.last()!) {
                l.delete(nums[j]);
            } else {
                r.delete(nums[j]);
            }
        }
    }
    return ans;
}

type CompareFunction<T, R extends 'number' | 'boolean'> = (
    a: T,
    b: T,
) => R extends 'number' ? number : boolean;

interface ITreapMultiSet<T> extends Iterable<T> {
    add: (...value: T[]) => this;
    has: (value: T) => boolean;
    delete: (value: T) => void;

    bisectLeft: (value: T) => number;
    bisectRight: (value: T) => number;

    indexOf: (value: T) => number;
    lastIndexOf: (value: T) => number;

    at: (index: number) => T | undefined;
    first: () => T | undefined;
    last: () => T | undefined;

    lower: (value: T) => T | undefined;
    higher: (value: T) => T | undefined;
    floor: (value: T) => T | undefined;
    ceil: (value: T) => T | undefined;

    shift: () => T | undefined;
    pop: (index?: number) => T | undefined;

    count: (value: T) => number;

    keys: () => IterableIterator<T>;
    values: () => IterableIterator<T>;
    rvalues: () => IterableIterator<T>;
    entries: () => IterableIterator<[number, T]>;

    readonly size: number;
}

class TreapNode<T = number> {
    value: T;
    count: number;
    size: number;
    priority: number;
    left: TreapNode<T> | null;
    right: TreapNode<T> | null;

    constructor(value: T) {
        this.value = value;
        this.count = 1;
        this.size = 1;
        this.priority = Math.random();
        this.left = null;
        this.right = null;
    }

    static getSize(node: TreapNode<any> | null): number {
        return node?.size ?? 0;
    }

    static getFac(node: TreapNode<any> | null): number {
        return node?.priority ?? 0;
    }

    pushUp(): void {
        let tmp = this.count;
        tmp += TreapNode.getSize(this.left);
        tmp += TreapNode.getSize(this.right);
        this.size = tmp;
    }

    rotateRight(): TreapNode<T> {
        // eslint-disable-next-line @typescript-eslint/no-this-alias
        let node: TreapNode<T> = this;
        const left = node.left;
        node.left = left?.right ?? null;
        left && (left.right = node);
        left && (node = left);
        node.right?.pushUp();
        node.pushUp();
        return node;
    }

    rotateLeft(): TreapNode<T> {
        // eslint-disable-next-line @typescript-eslint/no-this-alias
        let node: TreapNode<T> = this;
        const right = node.right;
        node.right = right?.left ?? null;
        right && (right.left = node);
        right && (node = right);
        node.left?.pushUp();
        node.pushUp();
        return node;
    }
}

class TreapMultiSet<T = number> implements ITreapMultiSet<T> {
    private readonly root: TreapNode<T>;
    private readonly compareFn: CompareFunction<T, 'number'>;
    private readonly leftBound: T;
    private readonly rightBound: T;

    constructor(compareFn?: CompareFunction<T, 'number'>);
    constructor(compareFn: CompareFunction<T, 'number'>, leftBound: T, rightBound: T);
    constructor(
        compareFn: CompareFunction<T, any> = (a: any, b: any) => a - b,
        leftBound: any = -Infinity,
        rightBound: any = Infinity,
    ) {
        this.root = new TreapNode<T>(rightBound);
        this.root.priority = Infinity;
        this.root.left = new TreapNode<T>(leftBound);
        this.root.left.priority = -Infinity;
        this.root.pushUp();

        this.leftBound = leftBound;
        this.rightBound = rightBound;
        this.compareFn = compareFn;
    }

    get size(): number {
        return this.root.size - 2;
    }

    get height(): number {
        const getHeight = (node: TreapNode<T> | null): number => {
            if (node == null) return 0;
            return 1 + Math.max(getHeight(node.left), getHeight(node.right));
        };

        return getHeight(this.root);
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns true if value is a member.
     */
    has(value: T): boolean {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): boolean => {
            if (node == null) return false;
            if (compare(node.value, value) === 0) return true;
            if (compare(node.value, value) < 0) return dfs(node.right, value);
            return dfs(node.left, value);
        };

        return dfs(this.root, value);
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Add value to sorted set.
     */
    add(...values: T[]): this {
        const compare = this.compareFn;
        const dfs = (
            node: TreapNode<T> | null,
            value: T,
            parent: TreapNode<T>,
            direction: 'left' | 'right',
        ): void => {
            if (node == null) return;
            if (compare(node.value, value) === 0) {
                node.count++;
                node.pushUp();
            } else if (compare(node.value, value) > 0) {
                if (node.left) {
                    dfs(node.left, value, node, 'left');
                } else {
                    node.left = new TreapNode(value);
                    node.pushUp();
                }

                if (TreapNode.getFac(node.left) > node.priority) {
                    parent[direction] = node.rotateRight();
                }
            } else if (compare(node.value, value) < 0) {
                if (node.right) {
                    dfs(node.right, value, node, 'right');
                } else {
                    node.right = new TreapNode(value);
                    node.pushUp();
                }

                if (TreapNode.getFac(node.right) > node.priority) {
                    parent[direction] = node.rotateLeft();
                }
            }
            parent.pushUp();
        };

        values.forEach(value => dfs(this.root.left, value, this.root, 'left'));
        return this;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Remove value from sorted set if it is a member.
     * If value is not a member, do nothing.
     */
    delete(value: T): void {
        const compare = this.compareFn;
        const dfs = (
            node: TreapNode<T> | null,
            value: T,
            parent: TreapNode<T>,
            direction: 'left' | 'right',
        ): void => {
            if (node == null) return;

            if (compare(node.value, value) === 0) {
                if (node.count > 1) {
                    node.count--;
                    node?.pushUp();
                } else if (node.left == null && node.right == null) {
                    parent[direction] = null;
                } else {
                    // 旋到根节点
                    if (
                        node.right == null ||
                        TreapNode.getFac(node.left) > TreapNode.getFac(node.right)
                    ) {
                        parent[direction] = node.rotateRight();
                        dfs(parent[direction]?.right ?? null, value, parent[direction]!, 'right');
                    } else {
                        parent[direction] = node.rotateLeft();
                        dfs(parent[direction]?.left ?? null, value, parent[direction]!, 'left');
                    }
                }
            } else if (compare(node.value, value) > 0) {
                dfs(node.left, value, node, 'left');
            } else if (compare(node.value, value) < 0) {
                dfs(node.right, value, node, 'right');
            }

            parent?.pushUp();
        };

        dfs(this.root.left, value, this.root, 'left');
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns an index to insert value in the sorted set.
     * If the value is already present, the insertion point will be before (to the left of) any existing values.
     */
    bisectLeft(value: T): number {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): number => {
            if (node == null) return 0;

            if (compare(node.value, value) === 0) {
                return TreapNode.getSize(node.left);
            } else if (compare(node.value, value) > 0) {
                return dfs(node.left, value);
            } else if (compare(node.value, value) < 0) {
                return dfs(node.right, value) + TreapNode.getSize(node.left) + node.count;
            }

            return 0;
        };

        return dfs(this.root, value) - 1;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns an index to insert value in the sorted set.
     * If the value is already present, the insertion point will be before (to the right of) any existing values.
     */
    bisectRight(value: T): number {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): number => {
            if (node == null) return 0;

            if (compare(node.value, value) === 0) {
                return TreapNode.getSize(node.left) + node.count;
            } else if (compare(node.value, value) > 0) {
                return dfs(node.left, value);
            } else if (compare(node.value, value) < 0) {
                return dfs(node.right, value) + TreapNode.getSize(node.left) + node.count;
            }

            return 0;
        };
        return dfs(this.root, value) - 1;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns the index of the first occurrence of a value in the set, or -1 if it is not present.
     */
    indexOf(value: T): number {
        const compare = this.compareFn;
        let isExist = false;

        const dfs = (node: TreapNode<T> | null, value: T): number => {
            if (node == null) return 0;

            if (compare(node.value, value) === 0) {
                isExist = true;
                return TreapNode.getSize(node.left);
            } else if (compare(node.value, value) > 0) {
                return dfs(node.left, value);
            } else if (compare(node.value, value) < 0) {
                return dfs(node.right, value) + TreapNode.getSize(node.left) + node.count;
            }

            return 0;
        };
        const res = dfs(this.root, value) - 1;
        return isExist ? res : -1;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns the index of the last occurrence of a value in the set, or -1 if it is not present.
     */
    lastIndexOf(value: T): number {
        const compare = this.compareFn;
        let isExist = false;

        const dfs = (node: TreapNode<T> | null, value: T): number => {
            if (node == null) return 0;

            if (compare(node.value, value) === 0) {
                isExist = true;
                return TreapNode.getSize(node.left) + node.count - 1;
            } else if (compare(node.value, value) > 0) {
                return dfs(node.left, value);
            } else if (compare(node.value, value) < 0) {
                return dfs(node.right, value) + TreapNode.getSize(node.left) + node.count;
            }

            return 0;
        };

        const res = dfs(this.root, value) - 1;
        return isExist ? res : -1;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Returns the item located at the specified index.
     * @param index The zero-based index of the desired code unit. A negative index will count back from the last item.
     */
    at(index: number): T | undefined {
        if (index < 0) index += this.size;
        if (index < 0 || index >= this.size) return undefined;

        const dfs = (node: TreapNode<T> | null, rank: number): T | undefined => {
            if (node == null) return undefined;

            if (TreapNode.getSize(node.left) >= rank) {
                return dfs(node.left, rank);
            } else if (TreapNode.getSize(node.left) + node.count >= rank) {
                return node.value;
            } else {
                return dfs(node.right, rank - TreapNode.getSize(node.left) - node.count);
            }
        };

        const res = dfs(this.root, index + 2);
        return ([this.leftBound, this.rightBound] as any[]).includes(res) ? undefined : res;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Find and return the element less than `val`, return `undefined` if no such element found.
     */
    lower(value: T): T | undefined {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): T | undefined => {
            if (node == null) return undefined;
            if (compare(node.value, value) >= 0) return dfs(node.left, value);

            const tmp = dfs(node.right, value);
            if (tmp == null || compare(node.value, tmp) > 0) {
                return node.value;
            } else {
                return tmp;
            }
        };

        const res = dfs(this.root, value) as any;
        return res === this.leftBound ? undefined : res;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Find and return the element greater than `val`, return `undefined` if no such element found.
     */
    higher(value: T): T | undefined {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): T | undefined => {
            if (node == null) return undefined;
            if (compare(node.value, value) <= 0) return dfs(node.right, value);

            const tmp = dfs(node.left, value);

            if (tmp == null || compare(node.value, tmp) < 0) {
                return node.value;
            } else {
                return tmp;
            }
        };

        const res = dfs(this.root, value) as any;
        return res === this.rightBound ? undefined : res;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Find and return the element less than or equal to `val`, return `undefined` if no such element found.
     */
    floor(value: T): T | undefined {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): T | undefined => {
            if (node == null) return undefined;
            if (compare(node.value, value) === 0) return node.value;
            if (compare(node.value, value) >= 0) return dfs(node.left, value);

            const tmp = dfs(node.right, value);
            if (tmp == null || compare(node.value, tmp) > 0) {
                return node.value;
            } else {
                return tmp;
            }
        };

        const res = dfs(this.root, value) as any;
        return res === this.leftBound ? undefined : res;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description Find and return the element greater than or equal to `val`, return `undefined` if no such element found.
     */
    ceil(value: T): T | undefined {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): T | undefined => {
            if (node == null) return undefined;
            if (compare(node.value, value) === 0) return node.value;
            if (compare(node.value, value) <= 0) return dfs(node.right, value);

            const tmp = dfs(node.left, value);

            if (tmp == null || compare(node.value, tmp) < 0) {
                return node.value;
            } else {
                return tmp;
            }
        };

        const res = dfs(this.root, value) as any;
        return res === this.rightBound ? undefined : res;
    }

    /**
     * @complexity `O(logn)`
     * @description
     * Returns the last element from set.
     * If the set is empty, undefined is returned.
     */
    first(): T | undefined {
        const iter = this.inOrder();
        iter.next();
        const res = iter.next().value;
        return res === this.rightBound ? undefined : res;
    }

    /**
     * @complexity `O(logn)`
     * @description
     * Returns the last element from set.
     * If the set is empty, undefined is returned .
     */
    last(): T | undefined {
        const iter = this.reverseInOrder();
        iter.next();
        const res = iter.next().value;
        return res === this.leftBound ? undefined : res;
    }

    /**
     * @complexity `O(logn)`
     * @description
     * Removes the first element from an set and returns it.
     * If the set is empty, undefined is returned and the set is not modified.
     */
    shift(): T | undefined {
        const first = this.first();
        if (first === undefined) return undefined;
        this.delete(first);
        return first;
    }

    /**
     * @complexity `O(logn)`
     * @description
     * Removes the last element from an set and returns it.
     * If the set is empty, undefined is returned and the set is not modified.
     */
    pop(index?: number): T | undefined {
        if (index == null) {
            const last = this.last();
            if (last === undefined) return undefined;
            this.delete(last);
            return last;
        }

        const toDelete = this.at(index);
        if (toDelete == null) return;
        this.delete(toDelete);
        return toDelete;
    }

    /**
     *
     * @complexity `O(logn)`
     * @description
     * Returns number of occurrences of value in the sorted set.
     */
    count(value: T): number {
        const compare = this.compareFn;
        const dfs = (node: TreapNode<T> | null, value: T): number => {
            if (node == null) return 0;
            if (compare(node.value, value) === 0) return node.count;
            if (compare(node.value, value) < 0) return dfs(node.right, value);
            return dfs(node.left, value);
        };

        return dfs(this.root, value);
    }

    *[Symbol.iterator](): Generator<T, any, any> {
        yield* this.values();
    }

    /**
     * @description
     * Returns an iterable of keys in the set.
     */
    *keys(): Generator<T, any, any> {
        yield* this.values();
    }

    /**
     * @description
     * Returns an iterable of values in the set.
     */
    *values(): Generator<T, any, any> {
        const iter = this.inOrder();
        iter.next();
        const steps = this.size;
        for (let _ = 0; _ < steps; _++) {
            yield iter.next().value;
        }
    }

    /**
     * @description
     * Returns a generator for reversed order traversing the set.
     */
    *rvalues(): Generator<T, any, any> {
        const iter = this.reverseInOrder();
        iter.next();
        const steps = this.size;
        for (let _ = 0; _ < steps; _++) {
            yield iter.next().value;
        }
    }

    /**
     * @description
     * Returns an iterable of key, value pairs for every entry in the set.
     */
    *entries(): IterableIterator<[number, T]> {
        const iter = this.inOrder();
        iter.next();
        const steps = this.size;
        for (let i = 0; i < steps; i++) {
            yield [i, iter.next().value];
        }
    }

    private *inOrder(root: TreapNode<T> | null = this.root): Generator<T, any, any> {
        if (root == null) return;
        yield* this.inOrder(root.left);
        const count = root.count;
        for (let _ = 0; _ < count; _++) {
            yield root.value;
        }
        yield* this.inOrder(root.right);
    }

    private *reverseInOrder(root: TreapNode<T> | null = this.root): Generator<T, any, any> {
        if (root == null) return;
        yield* this.reverseInOrder(root.right);
        const count = root.count;
        for (let _ = 0; _ < count; _++) {
            yield root.value;
        }
        yield* this.reverseInOrder(root.left);
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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
        Cleans the entire room using a depth-first search algorithm.

        :type robot: Robot
        :rtype: None
        """

        def go_back():
            """
            Makes the robot go back to the previous cell and restore the original direction.
            """
            robot.turnLeft()
            robot.turnLeft()  # Rotate 180 degrees to face the opposite direction
            robot.move()
            robot.turnLeft()
            robot.turnLeft()  # Rotate another 180 degrees to restore initial direction

        def dfs(x, y, direction):
            """
            Cleans the room recursively using depth-first search.

            :param x: Current x-coordinate of the robot
            :param y: Current y-coordinate of the robot
            :param direction: Current direction the robot is facing
            """
            visited.add((x, y))
            robot.clean()
          
            # Loop through all directions: 0 - up, 1 - right, 2 - down, 3 - left
            for k in range(4):
                new_direction = (direction + k) % 4
                new_x = x + directions[new_direction]
                new_y = y + directions[new_direction + 1]
              
                if (new_x, new_y) not in visited and robot.move():
                    dfs(new_x, new_y, new_direction)
                    go_back()  # Go back to the previous cell after cleaning
              
                # Turn the robot clockwise to explore next direction
                robot.turnRight()
      
        # Define directions corresponding to up, right, down, left movements
        # in order: up(-1, 0), right(0, 1), down(1, 0), left(0, -1)
        directions = (-1, 0, 1, 0, -1)
      
        # Use a set to keep track of visited cells (coordinates)
        visited = set()
      
        # Start the DFS from the starting point (0,0) facing up (direction 0)
        dfs(0, 0, 0)
```

### Time and Space Complexity
The time complexity of the above code is O(4^(N-M)), where N is the total number of cells in the room and M is the number of obstacles. This is because the algorithm has to visit each non-obstacle cell once and at each cell, it makes up to 4 decisions – move in 4 possible directions. The recursion may go up to 4 branches at each level but would not revisit cells that are already visited, summarized by visited set vis.  
The space complexity of the DFS is O(N) for the recursive call stack as well as the space to hold the set of visited cells (in the worst case where there are no obstacles and we can move to every cell). However, in a densely packed room with obstructions, the number of visited states will be less than N.
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0498.Diagonal%20Traverse/README_EN.md
tags:
    - Array
    - Matrix
    - Simulation
---

<!-- problem:start -->

# [498. Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse)

[中文文档](/solution/0400-0499/0498.Diagonal%20Traverse/README.md)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> matrix <code>mat</code>, return <em>an array of all the elements of the array in a diagonal order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0498.Diagonal%20Traverse/images/diag1-grid.jpg" style="width: 334px; height: 334px;" />
<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,4,7,5,3,6,8,9]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i + j].append(mat[i][j])
        res = []
        direction = False
        for k in range(len(mat) + len(mat[0]) - 1):
            if direction:
                res.extend(d[k])
            else:
                res.extend(d[k][::-1])
            direction = not direction
        return res
```

#### Java

```java
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] ans = new int[m * n];
        int idx = 0;
        List<Integer> t = new ArrayList<>();
        for (int k = 0; k < m + n - 1; ++k) {
            int i = k < n ? 0 : k - n + 1;
            int j = k < n ? k : n - 1;
            while (i < m && j >= 0) {
                t.add(mat[i][j]);
                ++i;
                --j;
            }
            if (k % 2 == 0) {
                Collections.reverse(t);
            }
            for (int v : t) {
                ans[idx++] = v;
            }
            t.clear();
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> ans;
        vector<int> t;
        for (int k = 0; k < m + n - 1; ++k) {
            int i = k < n ? 0 : k - n + 1;
            int j = k < n ? k : n - 1;
            while (i < m && j >= 0) t.push_back(mat[i++][j--]);
            if (k % 2 == 0) reverse(t.begin(), t.end());
            for (int& v : t) ans.push_back(v);
            t.clear();
        }
        return ans;
    }
};
```

#### Go

```go
func findDiagonalOrder(mat [][]int) []int {
	m, n := len(mat), len(mat[0])
	var ans []int
	for k := 0; k < m+n-1; k++ {
		var t []int
		i, j := k-n+1, n-1
		if k < n {
			i, j = 0, k
		}
		for i < m && j >= 0 {
			t = append(t, mat[i][j])
			i++
			j--
		}
		if k%2 == 0 {
			p, q := 0, len(t)-1
			for p < q {
				t[p], t[q] = t[q], t[p]
				p++
				q--
			}
		}
		for _, v := range t {
			ans = append(ans, v)
		}
	}
	return ans
}
```

#### TypeScript

```ts
function findDiagonalOrder(mat: number[][]): number[] {
    const res = [];
    const m = mat.length;
    const n = mat[0].length;
    let i = 0;
    let j = 0;
    let mark = true;
    while (res.length !== n * m) {
        if (mark) {
            while (i >= 0 && j < n) {
                res.push(mat[i][j]);
                i--;
                j++;
            }
            if (j === n) {
                j--;
                i++;
            }
            i++;
        } else {
            while (i < m && j >= 0) {
                res.push(mat[i][j]);
                i++;
                j--;
            }
            if (i === m) {
                i--;
                j++;
            }
            j++;
        }
        mark = !mark;
    }
    return res;
}
```

#### Rust

```rust
impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let (m, n) = (mat.len(), mat[0].len());
        let (mut i, mut j) = (0, 0);
        (0..m * n)
            .map(|_| {
                let res = mat[i][j];
                if (i + j) % 2 == 0 {
                    if j == n - 1 {
                        i += 1;
                    } else if i == 0 {
                        j += 1;
                    } else {
                        i -= 1;
                        j += 1;
                    }
                } else {
                    if i == m - 1 {
                        j += 1;
                    } else if j == 0 {
                        i += 1;
                    } else {
                        i += 1;
                        j -= 1;
                    }
                }
                res
            })
            .collect()
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0503.Next%20Greater%20Element%20II/README_EN.md
tags:
    - Stack
    - Array
    - Monotonic Stack
---

<!-- problem:start -->

# [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii)

[中文文档](/solution/0500-0599/0503.Next%20Greater%20Element%20II/README.md)

## Description

<!-- description:start -->

<p>Given a circular integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em>the <strong>next greater number</strong> for every element in</em> <code>nums</code>.</p>

<p>The <strong>next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn&#39;t exist, return <code>-1</code> for this number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
Explanation: The first 1&#39;s next greater number is 2; 
The number 2 can&#39;t find next greater number. 
The second 1&#39;s next greater number needs to search circularly, which is also 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:</strong> [2,3,4,-1,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

The problem requires us to find the next greater element for each element. Therefore, we can traverse the array from back to front, which effectively turns the problem into finding the previous greater element. Additionally, since the array is circular, we can traverse the array twice.

Specifically, we start traversing the array from index $n \times 2 - 1$, where $n$ is the length of the array. Then, we let $j = i \bmod n$, where $\bmod$ represents the modulo operation. If the stack is not empty and the top element of the stack is less than or equal to $nums[j]$, then we continuously pop the top element of the stack until the stack is empty or the top element of the stack is greater than $nums[j]$. At this point, the top element of the stack is the previous greater element for $nums[j]$, and we assign it to $ans[j]$. Finally, we push $nums[j]$ onto the stack. We continue to the next element.

After the traversal is complete, we can obtain the array $ans$, which represents the next greater element for each element in the array $nums$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stk = []
        for i in range(n * 2 - 1, -1, -1):
            i %= n
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(nums[i])
        return ans
```

#### Java

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Deque<Integer> stk = new ArrayDeque<>();
        for (int i = n * 2 - 1; i >= 0; --i) {
            int j = i % n;
            while (!stk.isEmpty() && stk.peek() <= nums[j]) {
                stk.pop();
            }
            if (!stk.isEmpty()) {
                ans[j] = stk.peek();
            }
            stk.push(nums[j]);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        stack<int> stk;
        for (int i = n * 2 - 1; ~i; --i) {
            int j = i % n;
            while (stk.size() && stk.top() <= nums[j]) {
                stk.pop();
            }
            if (stk.size()) {
                ans[j] = stk.top();
            }
            stk.push(nums[j]);
        }
        return ans;
    }
};
```

#### Go

```go
func nextGreaterElements(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	stk := []int{}
	for i := n*2 - 1; i >= 0; i-- {
		j := i % n
		for len(stk) > 0 && stk[len(stk)-1] <= nums[j] {
			stk = stk[:len(stk)-1]
		}
		if len(stk) > 0 {
			ans[j] = stk[len(stk)-1]
		}
		stk = append(stk, nums[j])
	}
	return ans
}
```

#### TypeScript

```ts
function nextGreaterElements(nums: number[]): number[] {
    const n = nums.length;
    const stk: number[] = [];
    const ans: number[] = Array(n).fill(-1);
    for (let i = n * 2 - 1; ~i; --i) {
        const j = i % n;
        while (stk.length && stk.at(-1)! <= nums[j]) {
            stk.pop();
        }
        if (stk.length) {
            ans[j] = stk.at(-1)!;
        }
        stk.push(nums[j]);
    }
    return ans;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
    const n = nums.length;
    const stk = [];
    const ans = Array(n).fill(-1);
    for (let i = n * 2 - 1; ~i; --i) {
        const j = i % n;
        while (stk.length && stk.at(-1) <= nums[j]) {
            stk.pop();
        }
        if (stk.length) {
            ans[j] = stk.at(-1);
        }
        stk.push(nums[j]);
    }
    return ans;
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0525.Contiguous%20Array/README_EN.md
tags:
    - Array
    - Hash Table
    - Prefix Sum
---

<!-- problem:start -->

# [525. Contiguous Array](https://leetcode.com/problems/contiguous-array)

[中文文档](/solution/0500-0599/0525.Contiguous%20Array/README.md)

## Description

<!-- description:start -->

<p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of </em><code>0</code><em> and </em><code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,1,1,1,0,0,0]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Hash Table

According to the problem description, we can treat $0$s in the array as $-1$. In this way, when encountering a $0$, the prefix sum $s$ will decrease by one, and when encountering a $1$, the prefix sum $s$ will increase by one. Therefore, suppose the prefix sum $s$ is equal at indices $j$ and $i$, where $j < i$, then the subarray from index $j + 1$ to $i$ has an equal number of $0$s and $1$s.

We use a hash table to store all prefix sums and their first occurrence indices. Initially, we map the prefix sum of $0$ to $-1$.

As we iterate through the array, we calculate the prefix sum $s$. If $s$ is already in the hash table, then we have found a subarray with a sum of $0$, and its length is $i - d[s]$, where $d[s]$ is the index where $s$ first appeared in the hash table. If $s$ is not in the hash table, we store $s$ and its index $i$ in the hash table.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        ans = s = 0
        for i, x in enumerate(nums):
            s += 1 if x else -1
            if s in d:
                ans = max(ans, i - d[s])
            else:
                d[s] = i
        return ans
```

#### Java

```java
class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> d = new HashMap<>();
        d.put(0, -1);
        int ans = 0, s = 0;
        for (int i = 0; i < nums.length; ++i) {
            s += nums[i] == 1 ? 1 : -1;
            if (d.containsKey(s)) {
                ans = Math.max(ans, i - d.get(s));
            } else {
                d.put(s, i);
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> d{{0, -1}};
        int ans = 0, s = 0;
        for (int i = 0; i < nums.size(); ++i) {
            s += nums[i] ? 1 : -1;
            if (d.contains(s)) {
                ans = max(ans, i - d[s]);
            } else {
                d[s] = i;
            }
        }
        return ans;
    }
};
```

#### Go

```go
func findMaxLength(nums []int) int {
	d := map[int]int{0: -1}
	ans, s := 0, 0
	for i, x := range nums {
		if x == 0 {
			x = -1
		}
		s += x
		if j, ok := d[s]; ok {
			ans = max(ans, i-j)
		} else {
			d[s] = i
		}
	}
	return ans
}
```

#### TypeScript

```ts
function findMaxLength(nums: number[]): number {
    const d: Record<number, number> = { 0: -1 };
    let ans = 0;
    let s = 0;
    for (let i = 0; i < nums.length; ++i) {
        s += nums[i] ? 1 : -1;
        if (d.hasOwnProperty(s)) {
            ans = Math.max(ans, i - d[s]);
        } else {
            d[s] = i;
        }
    }
    return ans;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
    const d = { 0: -1 };
    let ans = 0;
    let s = 0;
    for (let i = 0; i < nums.length; ++i) {
        s += nums[i] ? 1 : -1;
        if (d.hasOwnProperty(s)) {
            ans = Math.max(ans, i - d[s]);
        } else {
            d[s] = i;
        }
    }
    return ans;
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
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
        self.w = list(w)
        self.res = list(w)
        for i in range(1, len(w)):
            self.res[i] += self.res[i - 1]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.res[-1])
        low = 0
        high = len(self.res)
        while low < high:
            mid = (low + high) // 2
            if self.res[mid] == rand:
                return mid
            if self.res[mid] < rand:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0529.Minesweeper/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->

# [529. Minesweeper](https://leetcode.com/problems/minesweeper)

[中文文档](/solution/0500-0599/0529.Minesweeper/README.md)

## Description

<!-- description:start -->

<p>Let&#39;s play the minesweeper game (<a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)" target="_blank">Wikipedia</a>, <a href="http://minesweeperonline.com" target="_blank">online game</a>)!</p>

<p>You are given an <code>m x n</code> char matrix <code>board</code> representing the game board where:</p>

<ul>
	<li><code>&#39;M&#39;</code> represents an unrevealed mine,</li>
	<li><code>&#39;E&#39;</code> represents an unrevealed empty square,</li>
	<li><code>&#39;B&#39;</code> represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),</li>
	<li>digit (<code>&#39;1&#39;</code> to <code>&#39;8&#39;</code>) represents how many mines are adjacent to this revealed square, and</li>
	<li><code>&#39;X&#39;</code> represents a revealed mine.</li>
</ul>

<p>You are also given an integer array <code>click</code> where <code>click = [click<sub>r</sub>, click<sub>c</sub>]</code> represents the next click position among all the unrevealed squares (<code>&#39;M&#39;</code> or <code>&#39;E&#39;</code>).</p>

<p>Return <em>the board after revealing this position according to the following rules</em>:</p>

<ol>
	<li>If a mine <code>&#39;M&#39;</code> is revealed, then the game is over. You should change it to <code>&#39;X&#39;</code>.</li>
	<li>If an empty square <code>&#39;E&#39;</code> with no adjacent mines is revealed, then change it to a revealed blank <code>&#39;B&#39;</code> and all of its adjacent unrevealed squares should be revealed recursively.</li>
	<li>If an empty square <code>&#39;E&#39;</code> with at least one adjacent mine is revealed, then change it to a digit (<code>&#39;1&#39;</code> to <code>&#39;8&#39;</code>) representing the number of adjacent mines.</li>
	<li>Return the board when no more squares will be revealed.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0529.Minesweeper/images/untitled.jpeg" style="width: 500px; max-width: 400px; height: 269px;" />
<pre>
<strong>Input:</strong> board = [[&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;],[&quot;E&quot;,&quot;E&quot;,&quot;M&quot;,&quot;E&quot;,&quot;E&quot;],[&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;],[&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;,&quot;E&quot;]], click = [3,0]
<strong>Output:</strong> [[&quot;B&quot;,&quot;1&quot;,&quot;E&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;M&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0529.Minesweeper/images/untitled-2.jpeg" style="width: 489px; max-width: 400px; height: 269px;" />
<pre>
<strong>Input:</strong> board = [[&quot;B&quot;,&quot;1&quot;,&quot;E&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;M&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;]], click = [1,2]
<strong>Output:</strong> [[&quot;B&quot;,&quot;1&quot;,&quot;E&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;X&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;B&quot;],[&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>board[i][j]</code> is either <code>&#39;M&#39;</code>, <code>&#39;E&#39;</code>, <code>&#39;B&#39;</code>, or a digit from <code>&#39;1&#39;</code> to <code>&#39;8&#39;</code>.</li>
	<li><code>click.length == 2</code></li>
	<li><code>0 &lt;= click<sub>r</sub> &lt; m</code></li>
	<li><code>0 &lt;= click<sub>c</sub> &lt; n</code></li>
	<li><code>board[click<sub>r</sub>][click<sub>c</sub>]</code> is either <code>&#39;M&#39;</code> or <code>&#39;E&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        surround = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
            (1, -1),
            (1, 1),
            (-1, 1),
            (-1, -1),
        ]

        def available(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def reveal(board, x, y):
            # reveal blank cell with dfs
            if not available(x, y) or board[x][y] != "E":
                return
            # count adjacent mines
            mine_count = 0
            for dx, dy in surround:
                if available(dx + x, dy + y) and board[dx + x][dy + y] == "M":
                    mine_count += 1
            if mine_count:
                # have mines in adjacent cells
                board[x][y] = str(mine_count)
            else:
                # not adjacent mines
                board[x][y] = "B"
                for dx, dy in surround:
                    reveal(board, dx + x, dy + y)

        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            reveal(board, x, y)
        return board
```

#### Java

```java
class Solution {
    private char[][] board;
    private int m;
    private int n;

    public char[][] updateBoard(char[][] board, int[] click) {
        m = board.length;
        n = board[0].length;
        this.board = board;
        int i = click[0], j = click[1];
        if (board[i][j] == 'M') {
            board[i][j] = 'X';
        } else {
            dfs(i, j);
        }
        return board;
    }

    private void dfs(int i, int j) {
        int cnt = 0;
        for (int x = i - 1; x <= i + 1; ++x) {
            for (int y = j - 1; y <= j + 1; ++y) {
                if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'M') {
                    ++cnt;
                }
            }
        }
        if (cnt > 0) {
            board[i][j] = (char) (cnt + '0');
        } else {
            board[i][j] = 'B';
            for (int x = i - 1; x <= i + 1; ++x) {
                for (int y = j - 1; y <= j + 1; ++y) {
                    if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'E') {
                        dfs(x, y);
                    }
                }
            }
        }
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int m = board.size(), n = board[0].size();
        int i = click[0], j = click[1];

        function<void(int, int)> dfs = [&](int i, int j) {
            int cnt = 0;
            for (int x = i - 1; x <= i + 1; ++x) {
                for (int y = j - 1; y <= j + 1; ++y) {
                    if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'M') {
                        ++cnt;
                    }
                }
            }
            if (cnt) {
                board[i][j] = cnt + '0';
            } else {
                board[i][j] = 'B';
                for (int x = i - 1; x <= i + 1; ++x) {
                    for (int y = j - 1; y <= j + 1; ++y) {
                        if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'E') {
                            dfs(x, y);
                        }
                    }
                }
            }
        };

        if (board[i][j] == 'M') {
            board[i][j] = 'X';
        } else {
            dfs(i, j);
        }
        return board;
    }
};
```

#### Go

```go
func updateBoard(board [][]byte, click []int) [][]byte {
	m, n := len(board), len(board[0])
	i, j := click[0], click[1]

	var dfs func(i, j int)
	dfs = func(i, j int) {
		cnt := 0
		for x := i - 1; x <= i+1; x++ {
			for y := j - 1; y <= j+1; y++ {
				if x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'M' {
					cnt++
				}
			}
		}
		if cnt > 0 {
			board[i][j] = byte(cnt + '0')
			return
		}
		board[i][j] = 'B'
		for x := i - 1; x <= i+1; x++ {
			for y := j - 1; y <= j+1; y++ {
				if x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'E' {
					dfs(x, y)
				}
			}
		}
	}

	if board[i][j] == 'M' {
		board[i][j] = 'X'
	} else {
		dfs(i, j)
	}
	return board
}
```

#### TypeScript

```ts
function updateBoard(board: string[][], click: number[]): string[][] {
    const m = board.length;
    const n = board[0].length;
    const [i, j] = click;

    const dfs = (i: number, j: number) => {
        let cnt = 0;
        for (let x = i - 1; x <= i + 1; ++x) {
            for (let y = j - 1; y <= j + 1; ++y) {
                if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] === 'M') {
                    ++cnt;
                }
            }
        }
        if (cnt > 0) {
            board[i][j] = cnt.toString();
            return;
        }
        board[i][j] = 'B';
        for (let x = i - 1; x <= i + 1; ++x) {
            for (let y = j - 1; y <= j + 1; ++y) {
                if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] === 'E') {
                    dfs(x, y);
                }
            }
        }
    };

    if (board[i][j] === 'M') {
        board[i][j] = 'X';
    } else {
        dfs(i, j);
    }
    return board;
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0536.Construct%20Binary%20Tree%20from%20String/README_EN.md
tags:
    - Stack
    - Tree
    - Depth-First Search
    - String
    - Binary Tree
---

<!-- problem:start -->

# [536. Construct Binary Tree from String 🔒](https://leetcode.com/problems/construct-binary-tree-from-string)

[中文文档](/solution/0500-0599/0536.Construct%20Binary%20Tree%20from%20String/README.md)

## Description

<!-- description:start -->

<p>You need to construct a binary tree from a string consisting of parenthesis and integers.</p>

<p>The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root&#39;s value and a pair of parenthesis contains a child binary tree with the same structure.</p>

<p>You always start to construct the <b>left</b> child node of the parent first if it exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0536.Construct%20Binary%20Tree%20from%20String/images/butree.jpg" style="width: 382px; height: 322px;" />
<pre>
<strong>Input:</strong> s = &quot;4(2(3)(1))(6(5))&quot;
<strong>Output:</strong> [4,2,6,3,1,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;4(2(3)(1))(6(5)(7))&quot;
<strong>Output:</strong> [4,2,6,3,1,5,7]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;-4(2(3)(1))(6(5)(7))&quot;
<strong>Output:</strong> [-4,2,6,3,1,5,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of digits, <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, and <code>&#39;-&#39;</code> only.</li>
	<li>All numbers in the tree have value <strong>at most</strong> than <code>2<sup>30</sup></code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(s):
            if not s:
                return None
            p = s.find('(')
            if p == -1:
                return TreeNode(int(s))
            root = TreeNode(int(s[:p]))
            start = p
            cnt = 0
            for i in range(p, len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                if cnt == 0:
                    if start == p:
                        root.left = dfs(s[start + 1 : i])
                        start = i + 1
                    else:
                        root.right = dfs(s[start + 1 : i])
            return root

        return dfs(s)
```
# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)

[中文文档](/solution/0500-0599/0543.Diameter%20of%20Binary%20Tree/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0543.Diameter%20of%20Binary%20Tree/images/diamtree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

### Not optimal(Works and Accepted):
```python
class Solution:
   def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       def height(root):
           if not root:
               return 0
           lh = height(root.left)
           rh = height(root.right)
           return max(lh, rh) + 1
       def util(root, d):
           if not root:
               return 0
           util(root.left, d)
           util(root.right, d)
           lh = height(root.left)
           rh = height(root.right)
           d[0] = max(d[0], lh + rh)
           return max(lh, rh) + 1
       d = [0]
       util(root, d)
       return d[0]
```


### Optimal Solution(works and accepted)
```python
class Solution:
   def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       def util(root, d, h):
           if not root:
               return 0
           lh = [0]
           rh = [0]
           util(root.left, d, lh)
           util(root.right, d, rh)
           h[0] = max(lh[0], rh[0]) + 1
           d[0] = max(d[0], lh[0] + rh[0])
       d = [0]
       h = [0]
       util(root, d, h)
       return d[0]
```

### Without using Global variable(May be asked in Meta)
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(root):
            if not root:
                return (0, 0)
            lh, ld = helper(root.left)
            rh, rd = helper(root.right)

            return (max(lh, rh) + 1, max(ld, rd, lh + rh))

        return helper(root)[1]
```

## Meta variant
Diameter of a n-ary tree

```python
from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node: 'Node'):
            if node is None:
                return 0

            max_height = 0
            second_max_height = 0
            for child in node.children:
                height = longest_path(child)
                if height > max_height:
                    second_max_height = max_height
                    max_height = height
                elif height > second_max_height:
                    second_max_height = height
            nonlocal diameter
            diameter = max(diameter, max_height + second_max_height)
            return max_height + 1

        longest_path(root)

        return diameter
```




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
            count += m[running_sum - k]
            # make sure to add 1 to existing instead of assigning
            # 1. There may be multiple subarrays with same sum
            m[running_sum] += 1
        return count
```

## meta variant
 What if you had to return true or false if there exists at least one  subarray that equals K?
```python
class Solution:
    def subarraySumExists(self, nums: list[int], k: int) -> bool:
        count, cumulative = 0, 0
        prefix_sums = set([0])
        for num in nums:
            cumulative += num
            if (cumulative - k) in prefix_sums:
                return True
            prefix_sums.add(cumulative)
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExists([1, 1, 1], 2)
    assert not solution.subarraySumExists([1, 4, 7], 3)

    # SubarraySum_FirstVariant True
    assert solution.subarraySumExists([1, 1, 1], 2) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], 7) == True
    assert solution.subarraySumExists([1, 2, 3, -3, 1, 1], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -3, 3, -3], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], 8) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], -1) == True
    assert solution.subarraySumExists([5], 5) == True
    assert solution.subarraySumExists([5], 10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -5) == True
    assert solution.subarraySumExists([-1, -2, -3, -4], -10) == True
    assert solution.subarraySumExists([0, 0, 0, 0, 0], 0) == True
    assert solution.subarraySumExists([8, 3, 6, 1, -5, 10], 10) == True

    # SubarraySum_FirstVariant False
    assert solution.subarraySumExists([1, 1, 1], 4) == False
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], -10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -15) == False
```
## meta variant
What if you had to optimize the space complexity in the case you're only given positive integers in the array?
```python
class Solution:
    def subarraySumExistsPositiveNums(self, nums: list[int], k: int) -> bool:
        left, right = 0, 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum > k:
                window_sum -= nums[left]
                left += 1

            if window_sum == k:
                return True
            
        return False

if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2)
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3)

    # SubarraySum_SecondVariant True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([5], 5) == True
    assert solution.subarraySumExistsPositiveNums([5], 10) == False
    assert solution.subarraySumExistsPositiveNums([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 8) == True
    assert solution.subarraySumExistsPositiveNums([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.subarraySumExistsPositiveNums([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 4) == False
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.subarraySumExistsPositiveNums([100, 101, 102, 103], 2) == False
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 7) == False
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0606.Construct%20String%20from%20Binary%20Tree/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - String
    - Binary Tree
---

<!-- problem:start -->

# [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree)

## Description

<!-- description:start -->

<p>Given the <code>root</code> node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:</p>

<ul>
	<li>
	<p><strong>Node Representation</strong>: Each node in the tree should be represented by its integer value.</p>
	</li>
	<li>
	<p><strong>Parentheses for Children</strong>: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:</p>
	</li>
	<ul>
    	<li>If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node&#39;s value.</li>
    	<li>If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.</li>
    </ul>
	<li>
    <p><strong>Omitting Empty Parentheses</strong>: Any empty parentheses pairs (i.e., <code>()</code>) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.</p></li>
</ul>

<p>In summary, empty parentheses pairs should be omitted when a node has only a left child or no children. However, when a node has a right child but no left child, an empty pair of parentheses must precede the representation of the right child to reflect the tree&#39;s structure accurately.</p>


<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0606.Construct%20String%20from%20Binary%20Tree/images/cons1-tree.jpg" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4]
<strong>Output:</strong> &quot;1(2(4))(3)&quot;
<strong>Explanation:</strong> Originally, it needs to be &quot;1(2(4)())(3()())&quot;, but you need to omit all the empty parenthesis pairs. And it will be &quot;1(2(4))(3)&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0606.Construct%20String%20from%20Binary%20Tree/images/cons2-tree.jpg" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> &quot;1(2()(4))(3)&quot;
<strong>Explanation:</strong> Almost the same as the first example, except the <code>()</code> after <code>2</code> is necessary to indicate the absence of a left child for <code>2</code> and the presence of a right child.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def format(val):
            return f"({val})"

        def helper(root):
            if not root:
                return None

            left = helper(root.left)
            right = helper(root.right)

            if not left and not right:
                return str(root.val)

            result = "()" if not left else format(left)
            if right:
                result += format(right)
            return str(root.val) + result

        return helper(root)
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

# [670. Maximum Swap](https://leetcode.com/problems/maximum-swap)


## Description

<!-- description:start -->

<p>You are given an integer <code>num</code>. You can swap two digits at most once to get the maximum valued number.</p>

<p>Return <em>the maximum valued number you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 2736
<strong>Output:</strong> 7236
<strong>Explanation:</strong> Swap the number 2 and the number 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 9973
<strong>Output:</strong> 9973
<strong>Explanation:</strong> No swap.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy Algorithm

First, we convert the number into a string $s$. Then, we traverse the string $s$ from right to left, using an array or hash table $d$ to record the position of the maximum number to the right of each number (it can be the position of the number itself).

Next, we traverse $d$ from left to right. If $s[i] < s[d[i]]$, we swap them and exit the traversal process.

Finally, we convert the string $s$ back into a number, which is the answer.

The time complexity is $O(\log M)$, and the space complexity is $O(\log M)$. Here, $M$ is the range of the number $num$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        d = list(range(n))
        for i in range(n - 2, -1, -1):
            if s[i] <= s[d[i + 1]]:
                d[i] = d[i + 1]
        for i, j in enumerate(d):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
                break
        return int(''.join(s))
```

## Meta variant

What if you had to build the second largest number?
```python
class Solution:
    def buildSecondLargestNumber(self, num: list[int]) -> list[int]:
        if not num or len(num) == 1:
            return []
        
        freqs = [0 for _ in range(10)]
        for digit in num:
            freqs[digit] += 1

        largest_num = []
        for i in range(9, -1, -1):
            for _ in range(freqs[i]):
                largest_num.append(i)

        for i in range(len(largest_num) - 1, 0, -1):
            if largest_num[i - 1] != largest_num[i]:
                largest_num[i - 1], largest_num[i] = largest_num[i], largest_num[i - 1]
                return largest_num

        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]

    # MaximumSwap_Variant_BuildSecondLargest True
    assert solution.buildSecondLargestNumber([]) == []
    assert solution.buildSecondLargestNumber([1]) == []
    assert solution.buildSecondLargestNumber([2]) == []
    assert solution.buildSecondLargestNumber([3]) == []
    assert solution.buildSecondLargestNumber([4]) == []
    assert solution.buildSecondLargestNumber([5]) == []
    assert solution.buildSecondLargestNumber([6]) == []
    assert solution.buildSecondLargestNumber([7]) == []
    assert solution.buildSecondLargestNumber([8]) == []
    assert solution.buildSecondLargestNumber([9]) == []
    assert solution.buildSecondLargestNumber([0]) == []

    # Distinct Digits And One Swap
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([2, 3, 4, 1, 8]) == [8, 4, 3, 1, 2]

    # All Duplicate Digits Cannot Build Second Largest
    assert solution.buildSecondLargestNumber([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == []
    assert solution.buildSecondLargestNumber([2, 2]) == []
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 0]) == []

    # Duplicate Digits And Looped Swap
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6]) == [9, 9, 7, 6, 6, 6, 6, 3, 5]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6, 3, 3]) == [9, 9, 7, 6, 6, 6, 6, 3, 5, 3, 3]
    assert solution.buildSecondLargestNumber([4, 4, 4, 4, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 4, 9, 4, 4, 4]

    # Zeroes
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 6, 0]) == [0, 6, 0, 0, 0, 0, 0]
    assert solution.buildSecondLargestNumber([0, 0, 1, 2, 3, 3]) == [3, 3, 2, 0, 1, 0]
    assert solution.buildSecondLargestNumber([0, 0, 8, 4, 9, 9, 6, 7]) == [9, 9, 8, 7, 6, 0, 4, 0]
```
# [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii)


## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <code>true</code> <em>if the </em><code>s</code><em> can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abca&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You could delete the character &#39;c&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers to point to the left and right ends of the string, respectively. Each time, we check whether the characters pointed to by the two pointers are the same. If they are not the same, we check whether the string is a palindrome after deleting the character corresponding to the left pointer, or we check whether the string is a palindrome after deleting the character corresponding to the right pointer. If the characters pointed to by the two pointers are the same, we move both pointers towards the middle by one position, until the two pointers meet.

If we have not encountered a situation where the characters pointed to by the pointers are different by the end of the traversal, then the string itself is a palindrome, and we return `true`.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check(i, j - 1) or check(i + 1, j)
            i, j = i + 1, j - 1
        return True
```
# [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island)


## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>&#39;s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <strong>area</strong> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0695.Max%20Area%20of%20Island/images/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (0, -1), (-1,0), (1,0)]
        def dfs(i, j, count):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != 1
            ):
                return
            count[0] += 1
            grid[i][j] = 0
            for d in dirs:
                dfs(i + d[0], j + d[1], count)
        if not grid:
            return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = [0]
                if grid[i][j] == 1:
                    dfs(i, j, count)
                max_area = max(max_area, count[0])
        return max_area
```


---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0708.Insert%20into%20a%20Sorted%20Circular%20Linked%20List/README_EN.md
tags:
    - Linked List
---

<!-- problem:start -->

# [708. Insert into a Sorted Circular Linked List 🔒](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list)

[中文文档](/solution/0700-0799/0708.Insert%20into%20a%20Sorted%20Circular%20Linked%20List/README.md)

## Description

<!-- description:start -->

<p>Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value <code>insertVal</code> into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.</p>

<p>If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.</p>

<p>If the list is empty (i.e., the given node is <code>null</code>), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0708.Insert%20into%20a%20Sorted%20Circular%20Linked%20List/images/example_1_before_65p.jpg" style="width: 250px; height: 149px;" /><br />
&nbsp;
<pre>
<strong>Input:</strong> head = [3,4,1], insertVal = 2
<strong>Output:</strong> [3,4,1,2]
<strong>Explanation:</strong> In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0708.Insert%20into%20a%20Sorted%20Circular%20Linked%20List/images/example_1_after_65p.jpg" style="width: 250px; height: 149px;" />

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [], insertVal = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The list is empty (given head is&nbsp;<code>null</code>). We create a new single circular list and return the reference to that single node.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1], insertVal = 0
<strong>Output:</strong> [1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>6</sup> &lt;= Node.val, insertVal &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        prev, curr = head, head.next
        while curr != head:
            # Either we find nodes where insertval is > than prev and less than next
            if prev.val <= insertVal <= curr.val 
            or 
            # 
            (
                # we reached the point where loop happens
                prev.val > curr.val 
                # insertval is less than next or greater than current
                and (insertVal >= prev.val or insertVal <= curr.val)
            ):
                break
            prev, curr = curr, curr.next
        prev.next = node
        node.next = curr
        return head
```

#### Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        Node node = new Node(insertVal);
        if (head == null) {
            node.next = node;
            return node;
        }
        Node prev = head, curr = head.next;
        while (curr != head) {
            if ((prev.val <= insertVal && insertVal <= curr.val)
                || (prev.val > curr.val && (insertVal >= prev.val || insertVal <= curr.val))) {
                break;
            }
            prev = curr;
            curr = curr.next;
        }
        prev.next = node;
        node.next = curr;
        return head;
    }
}
```

#### C++

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        Node* node = new Node(insertVal);
        if (!head) {
            node->next = node;
            return node;
        }
        Node *prev = head, *curr = head->next;
        while (curr != head) {
            if ((prev->val <= insertVal && insertVal <= curr->val) || (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val))) break;
            prev = curr;
            curr = curr->next;
        }
        prev->next = node;
        node->next = curr;
        return head;
    }
};
```

#### Go

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 * }
 */

func insert(head *Node, x int) *Node {
	node := &Node{Val: x}
	if head == nil {
		node.Next = node
		return node
	}
	prev, curr := head, head.Next
	for curr != head {
		if (prev.Val <= x && x <= curr.Val) || (prev.Val > curr.Val && (x >= prev.Val || x <= curr.Val)) {
			break
		}
		prev, curr = curr, curr.Next
	}
	prev.Next = node
	node.Next = curr
	return head
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0721.Accounts%20Merge/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [721. Accounts Merge](https://leetcode.com/problems/accounts-merge)

[中文文档](/solution/0700-0799/0721.Accounts%20Merge/README.md)

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
## Meta variant
What if you were given the input as a map from an ID to a list of corresponding emails?
Furthermore, you have to return a 2D list of all of the same IDs.

```python
class Solution:
    def accountsMerge(self, m):
        d = defaultdict(set)
        for k, v in m.items():
            for e in v:
                d[e].add(k)
        visited = set()
        ans = []
        def dfs(e, ids):
            if e in visited:
                return
            visited.add(e)
            for k in d[e]:
                res.add(k)
                for oe in m[k]:
                    dfs(oe, res)
        for e in d:
            if e not in visited:
                res = set()
                dfs(e, res)
                ans.append(sorted(list(res)))
        return ans
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0733.Flood%20Fill/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->

# [733. Flood Fill](https://leetcode.com/problems/flood-fill)

[中文文档](/solution/0700-0799/0733.Flood%20Fill/README.md)

## Description

<!-- description:start -->

<p>You are given an image represented by an <code>m x n</code> grid of integers <code>image</code>, where <code>image[i][j]</code> represents the pixel value of the image. You are also given three integers <code>sr</code>, <code>sc</code>, and <code>color</code>. Your task is to perform a <strong>flood fill</strong> on the image starting from the pixel <code>image[sr][sc]</code>.</p>

<p>To perform a <strong>flood fill</strong>:</p>

<ol>
	<li>Begin with the starting pixel and change its color to <code>color</code>.</li>
	<li>Perform the same process for each pixel that is <strong>directly adjacent</strong> (pixels that share a side with the original pixel, either horizontally or vertically) and shares the <strong>same color</strong> as the starting pixel.</li>
	<li>Keep <strong>repeating</strong> this process by checking neighboring pixels of the <em>updated</em> pixels&nbsp;and modifying their color if it matches the original color of the starting pixel.</li>
	<li>The process <strong>stops</strong> when there are <strong>no more</strong> adjacent pixels of the original color to update.</li>
</ol>

<p>Return the <strong>modified</strong> image after performing the flood fill.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[[2,2,2],[2,2,0],[2,0,1]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0733.Flood%20Fill/images/flood1-grid.jpg" style="width: 613px; height: 253px;" /></p>

<p>From the center of the image with position <code>(sr, sc) = (1, 1)</code> (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.</p>

<p>Note the bottom corner is <strong>not</strong> colored 2, because it is not horizontally or vertically connected to the starting pixel.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">[[0,0,0],[0,0,0]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= image[i][j], color &lt; 2<sup>16</sup></code></li>
	<li><code>0 &lt;= sr &lt; m</code></li>
	<li><code>0 &lt;= sc &lt; n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We denote the initial pixel's color as $\textit{oc}$. If $\textit{oc}$ is not equal to the target color $\textit{color}$, we start a depth-first search from $(\textit{sr}, \textit{sc})$ to change the color of all eligible pixels to the target color.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the 2D array $\textit{image}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def dfs(i: int, j: int):
            image[i][j] = color
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oc:
                    dfs(x, y)

        oc = image[sr][sc]
        if oc != color:
            dirs = (-1, 0, 1, 0, -1)
            dfs(sr, sc)
        return image
```

#### Java

```java
class Solution {
    private int[][] image;
    private int oc;
    private int color;
    private final int[] dirs = {-1, 0, 1, 0, -1};

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        oc = image[sr][sc];
        if (oc == color) {
            return image;
        }
        this.image = image;
        this.color = color;
        dfs(sr, sc);
        return image;
    }

    private void dfs(int i, int j) {
        image[i][j] = color;
        for (int k = 0; k < 4; ++k) {
            int x = i + dirs[k], y = j + dirs[k + 1];
            if (x >= 0 && x < image.length && y >= 0 && y < image[0].length && image[x][y] == oc) {
                dfs(x, y);
            }
        }
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m = image.size(), n = image[0].size();
        int oc = image[sr][sc];
        if (oc == color) {
            return image;
        }
        const int dirs[5] = {-1, 0, 1, 0, -1};
        auto dfs = [&](this auto&& dfs, int i, int j) -> void {
            image[i][j] = color;
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && image[x][y] == oc) {
                    dfs(x, y);
                }
            }
        };
        dfs(sr, sc);
        return image;
    }
};
```

#### Go

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	m, n := len(image), len(image[0])
	oc := image[sr][sc]
	if oc == color {
		return image
	}

	dirs := []int{-1, 0, 1, 0, -1}

	var dfs func(i, j int)
	dfs = func(i, j int) {
		image[i][j] = color
		for k := 0; k < 4; k++ {
			x, y := i+dirs[k], j+dirs[k+1]
			if x >= 0 && x < m && y >= 0 && y < n && image[x][y] == oc {
				dfs(x, y)
			}
		}
	}

	dfs(sr, sc)
	return image
}
```

#### TypeScript

```ts
function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const [m, n] = [image.length, image[0].length];
    const oc = image[sr][sc];
    if (oc === color) {
        return image;
    }

    const dirs = [-1, 0, 1, 0, -1];

    const dfs = (i: number, j: number): void => {
        image[i][j] = color;
        for (let k = 0; k < 4; k++) {
            const [x, y] = [i + dirs[k], j + dirs[k + 1]];
            if (x >= 0 && x < m && y >= 0 && y < n && image[x][y] === oc) {
                dfs(x, y);
            }
        }
    };

    dfs(sr, sc);
    return image;
}
```

#### Rust

```rust
impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let m = image.len();
        let n = image[0].len();
        let sr = sr as usize;
        let sc = sc as usize;

        let oc = image[sr][sc];
        if oc == color {
            return image;
        }
        let dirs = [-1, 0, 1, 0, -1];
        fn dfs(
            image: &mut Vec<Vec<i32>>,
            i: usize,
            j: usize,
            oc: i32,
            color: i32,
            m: usize,
            n: usize,
            dirs: &[i32; 5],
        ) {
            image[i][j] = color;
            for k in 0..4 {
                let x = i as isize + dirs[k] as isize;
                let y = j as isize + dirs[k + 1] as isize;
                if x >= 0 && x < m as isize && y >= 0 && y < n as isize {
                    let x = x as usize;
                    let y = y as usize;
                    if image[x][y] == oc {
                        dfs(image, x, y, oc, color, m, n, dirs);
                    }
                }
            }
        }

        dfs(&mut image, sr, sc, oc, color, m, n, &dirs);
        image
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: BFS

We first check if the initial pixel's color is equal to the target color. If it is, we return the original image directly. Otherwise, we can use the breadth-first search method, starting from $(\textit{sr}, \textit{sc})$, to change the color of all eligible pixels to the target color.

Specifically, we define a queue $\textit{q}$ and add the initial pixel $(\textit{sr}, \textit{sc})$ to the queue. Then, we continuously take pixels $(i, j)$ from the queue, change their color to the target color, and add the pixels in the four directions (up, down, left, right) that have the same original color as the initial pixel to the queue. When the queue is empty, we have completed the flood fill.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the 2D array $\textit{image}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        q = deque([(sr, sc)])
        oc = image[sr][sc]
        image[sr][sc] = color
        dirs = (-1, 0, 1, 0, -1)
        while q:
            i, j = q.popleft()
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oc:
                    q.append((x, y))
                    image[x][y] = color
        return image
```

#### Java

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {sr, sc});
        int oc = image[sr][sc];
        image[sr][sc] = color;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!q.isEmpty()) {
            int[] p = q.poll();
            int i = p[0], j = p[1];
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < image.length && y >= 0 && y < image[0].length
                    && image[x][y] == oc) {
                    q.offer(new int[] {x, y});
                    image[x][y] = color;
                }
            }
        }
        return image;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        int oc = image[sr][sc];
        image[sr][sc] = color;
        queue<pair<int, int>> q;
        q.push({sr, sc});
        int dirs[5] = {-1, 0, 1, 0, -1};
        while (!q.empty()) {
            auto [a, b] = q.front();
            q.pop();
            for (int k = 0; k < 4; ++k) {
                int x = a + dirs[k];
                int y = b + dirs[k + 1];
                if (x >= 0 && x < image.size() && y >= 0 && y < image[0].size() && image[x][y] == oc) {
                    q.push({x, y});
                    image[x][y] = color;
                }
            }
        }
        return image;
    }
};
```

#### Go

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	if image[sr][sc] == color {
		return image
	}
	oc := image[sr][sc]
	q := [][]int{[]int{sr, sc}}
	image[sr][sc] = color
	dirs := []int{-1, 0, 1, 0, -1}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		for k := 0; k < 4; k++ {
			x, y := p[0]+dirs[k], p[1]+dirs[k+1]
			if x >= 0 && x < len(image) && y >= 0 && y < len(image[0]) && image[x][y] == oc {
				q = append(q, []int{x, y})
				image[x][y] = color
			}
		}
	}
	return image
}
```

#### TypeScript

```ts
function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    if (image[sr][sc] === color) {
        return image;
    }

    const oc = image[sr][sc];
    image[sr][sc] = color;

    const q: [number, number][] = [];
    q.push([sr, sc]);

    const dirs = [-1, 0, 1, 0, -1];
    const [m, n] = [image.length, image[0].length];

    while (q.length > 0) {
        const [a, b] = q.shift()!;
        for (let k = 0; k < 4; ++k) {
            const x = a + dirs[k];
            const y = b + dirs[k + 1];
            if (x >= 0 && x < m && y >= 0 && y < n && image[x][y] === oc) {
                q.push([x, y]);
                image[x][y] = color;
            }
        }
    }

    return image;
}
```

#### Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let m = image.len();
        let n = image[0].len();
        let (sr, sc) = (sr as usize, sc as usize);

        if image[sr][sc] == color {
            return image;
        }

        let oc = image[sr][sc];
        image[sr][sc] = color;

        let mut q = VecDeque::new();
        q.push_back((sr, sc));

        let dirs = [-1, 0, 1, 0, -1];

        while let Some((i, j)) = q.pop_front() {
            for k in 0..4 {
                let x = i as isize + dirs[k] as isize;
                let y = j as isize + dirs[k + 1] as isize;

                if x >= 0 && x < m as isize && y >= 0 && y < n as isize {
                    let (x, y) = (x as usize, y as usize);
                    if image[x][y] == oc {
                        q.push_back((x, y));
                        image[x][y] = color;
                    }
                }
            }
        }

        image
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0766.Toeplitz%20Matrix/README_EN.md
tags:
    - Array
    - Matrix
---

<!-- problem:start -->

# [766. Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix)

[中文文档](/solution/0700-0799/0766.Toeplitz%20Matrix/README.md)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> <code>matrix</code>, return&nbsp;<em><code>true</code>&nbsp;if the matrix is Toeplitz. Otherwise, return <code>false</code>.</em></p>

<p>A matrix is <strong>Toeplitz</strong> if every diagonal from top-left to bottom-right has the same elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0766.Toeplitz%20Matrix/images/ex1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong>
In the above grid, the&nbsp;diagonals are:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;.
In each diagonal all elements are the same, so the answer is True.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0766.Toeplitz%20Matrix/images/ex2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2],[2,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong>
The diagonal &quot;[1, 2]&quot; has different elements.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>0 &lt;= matrix[i][j] &lt;= 99</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>What if the <code>matrix</code> is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?</li>
	<li>What if the <code>matrix</code> is so large that you can only load up a partial row into the memory at once?</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        return all(
            matrix[i][j] == matrix[i - 1][j - 1]
            for i in range(1, m)
            for j in range(1, n)
        )
```

#### Java

```java
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] != matrix[i - 1][j - 1]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] != matrix[i - 1][j - 1]) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

#### Go

```go
func isToeplitzMatrix(matrix [][]int) bool {
	m, n := len(matrix), len(matrix[0])
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] != matrix[i-1][j-1] {
				return false
			}
		}
	}
	return true
}
```

#### JavaScript

```js
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function (matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    for (let i = 1; i < m; ++i) {
        for (let j = 1; j < n; ++j) {
            if (matrix[i][j] != matrix[i - 1][j - 1]) {
                return false;
            }
        }
    }
    return true;
};
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
# [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string)

## Description

<!-- description:start -->

<p>You are given two strings <code>order</code> and <code>s</code>. All the characters of <code>order</code> are <strong>unique</strong> and were sorted in some custom order previously.</p>

<p>Permute the characters of <code>s</code> so that they match the order that <code>order</code> was sorted. More specifically, if a character <code>x</code> occurs before a character <code>y</code> in <code>order</code>, then <code>x</code> should occur before <code>y</code> in the permuted string.</p>

<p>Return <em>any permutation of </em><code>s</code><em> that satisfies this property</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = &quot;cba&quot;, s = &quot;abcd&quot; </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;cbad&quot; </span></p>

<p><strong>Explanation: </strong> <code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code> appear in order, so the order of <code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code> should be <code>&quot;c&quot;</code>, <code>&quot;b&quot;</code>, and <code>&quot;a&quot;</code>.</p>

<p>Since <code>&quot;d&quot;</code> does not appear in <code>order</code>, it can be at any position in the returned string. <code>&quot;dcba&quot;</code>, <code>&quot;cdba&quot;</code>, <code>&quot;cbda&quot;</code> are also valid outputs.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = &quot;bcafg&quot;, s = &quot;abcd&quot; </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;bcad&quot; </span></p>

<p><strong>Explanation: </strong> The characters <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, and <code>&quot;a&quot;</code> from <code>order</code> dictate the order for the characters in <code>s</code>. The character <code>&quot;d&quot;</code> in <code>s</code> does not appear in <code>order</code>, so its position is flexible.</p>

<p>Following the order of appearance in <code>order</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, and <code>&quot;a&quot;</code> from <code>s</code> should be arranged as <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, <code>&quot;a&quot;</code>. <code>&quot;d&quot;</code> can be placed at any position since it&#39;s not in order. The output <code>&quot;bcad&quot;</code> correctly follows this rule. Other arrangements like <code>&quot;dbca&quot;</code> or <code>&quot;bcda&quot;</code> would also be valid, as long as <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, <code>&quot;a&quot;</code> maintain their order.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= order.length &lt;= 26</code></li>
	<li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>order</code> and <code>s</code> consist of lowercase English letters.</li>
	<li>All the characters of <code>order</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->
### Solution 1 Using frequency
```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Get frequency of each character in the string
        counter = Counter(s)
        result = ''
        # iterate over order and create sorted string
        for c in order:
            if c in counter:
                result += c * counter[c]
                counter[c] = 0
        # process left over characters not present in order
        for c, v in counter.items():
            if v:
                result += c * v
        return result
```

## Meta variant

What if you are not allowed to use map/dict?

Solution - Use array instead since the alphabets are fixed
```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Get frequency of each character in the string
        counter = [0] * 26
        result = ""
        for c in s:
            counter[ord(c) - ord("a")] += 1
        # iterate over order and create sorted string
        for c in order:
            if counter[ord(c) - ord('a')]:
                result += c * counter[ord(c) - ord('a')]
                counter[ord(c) - ord('a')] = 0
        # process left over characters not present in order
        for i, v in enumerate(counter):
            if v:
                result += chr(i + ord('a')) * v
        return result
```



        
### Solution 2 with sorting the string based on order(Time complexity is more, avoid using in interview)

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: d.get(x, 0)))
```


---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0824.Goat%20Latin/README_EN.md
tags:
    - String
---

<!-- problem:start -->

# [824. Goat Latin](https://leetcode.com/problems/goat-latin)

[中文文档](/solution/0800-0899/0824.Goat%20Latin/README.md)

## Description

<!-- description:start -->

<p>You are given a string <code>sentence</code> that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.</p>

<p>We would like to convert the sentence to &quot;Goat Latin&quot; (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:</p>

<ul>
	<li>If a word begins with a vowel (<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, or <code>&#39;u&#39;</code>), append <code>&quot;ma&quot;</code> to the end of the word.

    <ul>
    	<li>For example, the word <code>&quot;apple&quot;</code> becomes <code>&quot;applema&quot;</code>.</li>
    </ul>
    </li>
    <li>If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add <code>&quot;ma&quot;</code>.
    <ul>
    	<li>For example, the word <code>&quot;goat&quot;</code> becomes <code>&quot;oatgma&quot;</code>.</li>
    </ul>
    </li>
    <li>Add one letter <code>&#39;a&#39;</code> to the end of each word per its word index in the sentence, starting with <code>1</code>.
    <ul>
    	<li>For example, the first word gets <code>&quot;a&quot;</code> added to the end, the second word gets <code>&quot;aa&quot;</code> added to the end, and so on.</li>
    </ul>
    </li>

</ul>

<p>Return<em> the final sentence representing the conversion from sentence to Goat Latin</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sentence = "I speak Goat Latin"
<strong>Output:</strong> "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sentence = "The quick brown fox jumped over the lazy dog"
<strong>Output:</strong> "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 150</code></li>
	<li><code>sentence</code> consists of English letters and spaces.</li>
	<li><code>sentence</code> has no leading or trailing spaces.</li>
	<li>All the words in <code>sentence</code> are separated by a single space.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        for i, word in enumerate(sentence.split()):
            if word.lower()[0] not in ['a', 'e', 'i', 'o', 'u']:
                word = word[1:] + word[0]
            word += 'ma'
            word += 'a' * (i + 1)
            ans.append(word)
        return ' '.join(ans)
```

#### Java

```java
class Solution {
    public String toGoatLatin(String sentence) {
        List<String> ans = new ArrayList<>();
        Set<Character> vowels
            = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        int i = 1;
        for (String word : sentence.split(" ")) {
            StringBuilder t = new StringBuilder();
            if (!vowels.contains(word.charAt(0))) {
                t.append(word.substring(1));
                t.append(word.charAt(0));
            } else {
                t.append(word);
            }
            t.append("ma");
            for (int j = 0; j < i; ++j) {
                t.append("a");
            }
            ++i;
            ans.add(t.toString());
        }
        return String.join(" ", ans);
    }
}
```

#### TypeScript

```ts
function toGoatLatin(sentence: string): string {
    return sentence
        .split(' ')
        .map((s, i) => {
            let startStr: string;
            if (/[aeiou]/i.test(s[0])) {
                startStr = s;
            } else {
                startStr = s.slice(1) + s[0];
            }
            return `${startStr}ma${'a'.repeat(i + 1)}`;
        })
        .join(' ');
}
```

#### Rust

```rust
use std::collections::HashSet;
impl Solution {
    pub fn to_goat_latin(sentence: String) -> String {
        let set: HashSet<&char> = ['a', 'e', 'i', 'o', 'u'].into_iter().collect();
        sentence
            .split_whitespace()
            .enumerate()
            .map(|(i, s)| {
                let first = char::from(s.as_bytes()[0]);
                let mut res = if set.contains(&first.to_ascii_lowercase()) {
                    s.to_string()
                } else {
                    s[1..].to_string() + &first.to_string()
                };
                res.push_str("ma");
                res.push_str(&"a".repeat(i + 1));
                res
            })
            .into_iter()
            .collect::<Vec<String>>()
            .join(" ")
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
# [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island)

[中文文档](/solution/0800-0899/0827.Making%20A%20Large%20Island/README.md)

## Description

<!-- description:start -->

<p>You are given an <code>n x n</code> binary matrix <code>grid</code>. You are allowed to change <strong>at most one</strong> <code>0</code> to be <code>1</code>.</p>

<p>Return <em>the size of the largest <strong>island</strong> in</em> <code>grid</code> <em>after applying this operation</em>.</p>

<p>An <strong>island</strong> is a 4-directionally connected group of <code>1</code>s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1],[1,0]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Change the 0 to 1 and make the island bigger, only one island with area = 4.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1],[1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Can&#39;t change any 0 to 1, only one island with area = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


### Solution 1: DFS - Paint different connected components by different colors
```
The idea is that we dfs to paint different connected components by different colors,
we gonna paint in-place on the grid matrix, so we start color from 2, because 0 and 1 is already existed in the grid.
We need a counter, let componentSize[color] be the size of connected component corresponding to color.
Iterate over rows and columns in the matrix again, this time we calculate the new
size that can be formed if we turn matrix[r][c] from 0 into 1, that is:
If matrix[r][c] == 0 then:
Get color ids of landing neighboring cells to calculate component size.
(We get unique color ids to avoid calculating the size of 2 connected component two times)
Calculate total size can be formed.
Update the largest size can be formed so far to our answer.
```

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n, nextColor = len(grid), len(grid[0]), 2
        componentSize = defaultdict(int)

        def paint(r, c, color):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1: return
            grid[r][c] = color
            componentSize[color] += 1
            for i in range(4):
                paint(r + DIR[i], c + DIR[i + 1], color)

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1: continue  # Only paint when it's an island cell
                paint(r, c, nextColor)
                nextColor += 1

        ans = max(componentSize.values() or [0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0: continue
                neiColors = set()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    neiColors.add(grid[nr][nc])
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for color in neiColors:
                    sizeFormed += componentSize[color]
                ans = max(ans, sizeFormed)

        return ans
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0863.All%20Nodes%20Distance%20K%20in%20Binary%20Tree/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Hash Table
    - Binary Tree
---

<!-- problem:start -->

# [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, the value of a target node <code>target</code>, and an integer <code>k</code>, return <em>an array of the values of all nodes that have a distance </em><code>k</code><em> from the target node.</em></p>

<p>You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0863.All%20Nodes%20Distance%20K%20in%20Binary%20Tree/images/sketch0.png" style="width: 500px; height: 429px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
<strong>Output:</strong> [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1], target = 1, k = 3
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>target</code> is the value of one of the nodes in the tree.</li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Hash Table

We first use DFS to traverse the entire tree and save each node's parent node in the hash table $\textit{g}$.

Next, we use DFS again, starting from $\textit{target}$, to search for nodes at a distance of $k$ both upwards and downwards, and add them to the result array.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)

        def createLinkage(parent, child):
            if child:
                d[parent].append(child)
                d[child].append(parent)
                createLinkage(child, child.left)
                createLinkage(child, child.right)

        createLinkage(None, root)
        start = [node for node in d if node == target]
        q = deque(start)
        visited = set(start)
        while q and k:
            for _ in range(len(q)):
                top = q.popleft()
                for n in d[top]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
            k -= 1
        return [a.val for a in list(q) if a]
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0865.Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Hash Table
    - Binary Tree
---

<!-- problem:start -->

# [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes)

[中文文档](/solution/0800-0899/0865.Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, the depth of each node is <strong>the shortest distance to the root</strong>.</p>

<p>Return <em>the smallest subtree</em> such that it contains <strong>all the deepest nodes</strong> in the original tree.</p>

<p>A node is called <strong>the deepest</strong> if it has the largest depth possible among any node in the entire tree.</p>

<p>The <strong>subtree</strong> of a node is a tree consisting of that node, plus the set of all descendants of that node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0865.Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes/images/sketch1.png" style="width: 600px; height: 510px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4]
<strong>Output:</strong> [2,7,4]
<strong>Explanation:</strong> We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The root is the deepest node in the tree.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [0,1,3,null,2]
<strong>Output:</strong> [2]
<strong>Explanation:</strong> The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>The values of the nodes in the tree are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1123: <a href="https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/" target="_blank">https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/</a></p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

We design a function $\textit{dfs}(\textit{root})$ that returns the smallest subtree containing all the deepest nodes in the subtree rooted at $\textit{root}$, as well as the depth of the subtree rooted at $\textit{root}$.

The execution process of the function $\textit{dfs}(\textit{root})$ is as follows:

-   If $\textit{root}$ is null, return $\text{null}$ and $0$.
-   Otherwise, recursively calculate the smallest subtree and depth of the left and right subtrees of $\textit{root}$, denoted as $l$ and $l_d$, and $r$ and $r_d$, respectively. If $l_d > r_d$, then the smallest subtree containing all the deepest nodes in the subtree rooted at the left child of $\textit{root}$ is $l$, with a depth of $l_d + 1$. If $l_d < r_d$, then the smallest subtree containing all the deepest nodes in the subtree rooted at the right child of $\textit{root}$ is $r$, with a depth of $r_d + 1$. If $l_d = r_d$, then $\textit{root}$ is the smallest subtree containing all the deepest nodes, with a depth of $l_d + 1$.

Finally, return the first element of the result of $\textit{dfs}(\textit{root})$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def deepestDepth(node, depth):

            if not node:
                return node, depth

            left, leftDepth = deepestDepth(node.left, depth + 1)
            right, rightDepth = deepestDepth(node.right, depth + 1)

            # If the deepest node on the left subtree is deeper than the deepest node
            # on the right subtree return the left subtree and the left deepest depth
            if leftDepth > rightDepth:
                return left, leftDepth

            # If the deepest node on the right subtree is deeper than the deepest node
            # on the left subtree return the right subtree and the right deepest depth
            if rightDepth > leftDepth:
                return right, rightDepth

            # If the above two conditions isn't met, then leftDepth == rightDepth
            #
            # leftDepth equal rightDepth means that the deepest node
            # in the left subtree has the same depth as the deepest node
            # in the right subtree, as such, we should return the current node
            # as it is the root of the current subtree that contains the deepest
            # nodes on the left and right subtree.
            #
            # return statment can also be `return node, rightDepth`
            return node, leftDepth

        return deepestDepth(root, 0)[0]
```
# [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)
Medium
```
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

### Without Stack Solution Time O(N) Space O(1)
What if you had to return the parentheses string itself after the minimum adds?
```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closeNeeded = 0
        openNeeded = 0
        for c in s:
            if c == "(":
                closeNeeded += 1
            else:
                if closeNeeded > 0:
                    closeNeeded -= 1
                else:
                    openNeeded += 1
        return closeNeeded + openNeeded
```

### With Stack Time O(N) and space O(N)

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if c == "(":
                st.append(c)
            else:
                if st and st[-1] == "(":
                    st.pop()
                else:
                    st.append(c)
        return len(st)
```

## META variant

```python
class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        result = []
        extra_opens = 0
        for c in s:
            if c == '(':
                extra_opens += 1
            elif c == ')':
                if extra_opens == 0:
                    result.append("(")
                else:
                    extra_opens -= 1
            result.append(c)

        
        result += [')'] * extra_opens
        return "".join(result)
```
# [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst)

[中文文档](/solution/0900-0999/0938.Range%20Sum%20of%20BST/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> node of a binary search tree and two integers <code>low</code> and <code>high</code>, return <em>the sum of values of all nodes with a value in the <strong>inclusive</strong> range </em><code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0938.Range%20Sum%20of%20BST/images/bst1.jpg" style="width: 400px; height: 222px;" />
<pre>
<strong>Input:</strong> root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>Output:</strong> 32
<strong>Explanation:</strong> Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0938.Range%20Sum%20of%20BST/images/bst2.jpg" style="width: 400px; height: 335px;" />
<pre>
<strong>Input:</strong> root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>Output:</strong> 23
<strong>Explanation:</strong> Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We design a function $dfs(root)$, which represents the sum of the values of all nodes in the subtree with $root$ as the root, and the values are within the range $[low, high]$. The answer is $dfs(root)$.

The execution logic of the function $dfs(root)$ is as follows:

-   If $root$ is null, return $0$.
-   If the value $x$ of $root$ is within the range $[low, high]$, then the initial answer of the function $dfs(root)$ is $x$, otherwise it is $0$.
-   If $x > low$, it means that there may be nodes in the left subtree of $root$ with values within the range $[low, high]$, so we need to recursively call $dfs(root.left)$ and add the result to the answer.
-   If $x < high$, it means that there may be nodes in the right subtree of $root$ with values within the range $[low, high]$, so we need to recursively call $dfs(root.right)$ and add the result to the answer.
-   Finally, return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary search tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
```

## Meta variant 1
Find the average of all numbers in the range low to high

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, low, high):
            if not root:
                return (0, 0)
            if root.val < low:
                return helper(root.right, low, high)
            if root.val > high:
                return helper(root.left, low, high)

            ls, lc = helper(root.left, low, high)
            rs, rc = helper(root.right, low, high)
            return (ls + rs + root.val, lc + rc + 1)

        sum, count = helper(root, low, high)
        print(sum / count)
        return sum
```

## Meta variant 2
What if you had to optimize your solution for 10^4 function invocations? How would your algorithm change?

```python
from typing import Optional
from itertools import accumulate
from bisect import bisect_left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.vals = []
        self.prefix_sums = []
        self.inorder(root)
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.vals.append(root.val)
        if not self.prefix_sums:
            self.prefix_sums.append(root.val)
        else:
            self.prefix_sums.append(self.prefix_sums[-1] + root.val)
        self.inorder(root.right)
    
    def find_right_boundary(self, left, right, upper):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] <= upper:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def find_left_boundary(self, left, right, lower):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] >= lower:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def calculate(self, lower, upper):
        right_boundary = self.find_right_boundary(0, len(self.vals) - 1, upper)
        left_boundary = self.find_left_boundary(0, len(self.vals) - 1, lower)
        
        if left_boundary == 0:
            return self.prefix_sums[right_boundary]
        
        return self.prefix_sums[right_boundary] - self.prefix_sums[left_boundary - 1]
```
# [953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)
Easy
```
In an alien language, surprisingly, they also use English lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as
the blank character which is less than any other character (More info).
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
```

```python
class Solution:
    def isAlienSorted(self, words, order):
        d = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[: len(b)] == b:
                return False
            for i, j in zip(a, b):
                if d[i] < d[j]:
                    break
                if d[i] > d[j]:
                    return False
        return True
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0958.Check%20Completeness%20of%20a%20Binary%20Tree/README_EN.md
tags:
    - Tree
    - Breadth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [958. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree)


## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, determine if it is a <em>complete binary tree</em>.</p>

<p>In a <strong><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">complete binary tree</a></strong>, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0958.Check%20Completeness%20of%20a%20Binary%20Tree/images/complete-binary-tree-1.png" style="width: 180px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0958.Check%20Completeness%20of%20a%20Binary%20Tree/images/complete-binary-tree-2.png" style="width: 200px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,null,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> The node with value 7 isn&#39;t as far left as possible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        while q:
            top = q.popleft()
            if not top:
                return not any(q)
            q.append(top.left)
            q.append(top.right)
        return True
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
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0986.Interval%20List%20Intersections/README_EN.md
tags:
    - Array
    - Two Pointers
    - Line Sweep
---

<!-- problem:start -->

# [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections)

[中文文档](/solution/0900-0999/0986.Interval%20List%20Intersections/README.md)

## Description

<!-- description:start -->

<p>You are given two lists of closed intervals, <code>firstList</code> and <code>secondList</code>, where <code>firstList[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> and <code>secondList[j] = [start<sub>j</sub>, end<sub>j</sub>]</code>. Each list of intervals is pairwise <strong>disjoint</strong> and in <strong>sorted order</strong>.</p>

<p>Return <em>the intersection of these two interval lists</em>.</p>

<p>A <strong>closed interval</strong> <code>[a, b]</code> (with <code>a &lt;= b</code>) denotes the set of real numbers <code>x</code> with <code>a &lt;= x &lt;= b</code>.</p>

<p>The <strong>intersection</strong> of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of <code>[1, 3]</code> and <code>[2, 4]</code> is <code>[2, 3]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0986.Interval%20List%20Intersections/images/interval1.png" style="width: 700px; height: 194px;" />
<pre>
<strong>Input:</strong> firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
<strong>Output:</strong> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> firstList = [[1,3],[5,9]], secondList = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= firstList.length, secondList.length &lt;= 1000</code></li>
	<li><code>firstList.length + secondList.length &gt;= 1</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>end<sub>i</sub> &lt; start<sub>i+1</sub></code></li>
	<li><code>0 &lt;= start<sub>j</sub> &lt; end<sub>j</sub> &lt;= 10<sup>9</sup> </code></li>
	<li><code>end<sub>j</sub> &lt; start<sub>j+1</sub></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        res = []
        while i < m and j < n:
            if (
                firstList[i][0] <= secondList[j][1]
                and secondList[j][0] <= firstList[i][1]
            ):
                res.append(
                    [
                        max(firstList[i][0], secondList[j][0]),
                        min(firstList[i][1], secondList[j][1]),
                    ]
                )
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
```
# [987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree)

[中文文档](/solution/0900-0999/0987.Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, calculate the <strong>vertical order traversal</strong> of the binary tree.</p>

<p>For each node at position <code>(row, col)</code>, its left and right children will be at positions <code>(row + 1, col - 1)</code> and <code>(row + 1, col + 1)</code> respectively. The root of the tree is at <code>(0, 0)</code>.</p>

<p>The <strong>vertical order traversal</strong> of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.</p>

<p>Return <em>the <strong>vertical order traversal</strong> of the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0987.Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/images/vtree1.jpg" style="width: 431px; height: 304px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
<strong>Explanation:</strong>
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0987.Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/images/vtree2.jpg" style="width: 512px; height: 304px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7]
<strong>Output:</strong> [[4],[2],[1,5,6],[3],[7]]
<strong>Explanation:</strong>
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0987.Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/images/vtree3.jpg" style="width: 512px; height: 304px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,6,5,7]
<strong>Output:</strong> [[4],[2],[1,5,6],[3],[7]]
<strong>Explanation:</strong>
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

```python
class Solution:
   def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
       d = defaultdict(list)
       def util(root, offset, m, depth):
           if not root:
               return
           d[offset].append((root.val, depth))
           if offset < m[0]:
               m[0] = offset
           util(root.left, offset -1, m, depth+1)
           util(root.right, offset + 1, m, depth+1)
       m = [0]
       util(root, 0, m, 0)
       i = m[0]
       ans = []
       while True:
           if not d[i]:
               break
           ans.append(x[0] for x in sorted(d[i], key = lambda a:(a[1], a[0])))
           i += 1
       return ans
```
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
# [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)


## Description

<!-- description:start -->

<p>A conveyor belt has packages that must be shipped from one port to another within <code>days</code> days.</p>

<p>The <code>i<sup>th</sup></code> package on the conveyor belt has a weight of <code>weights[i]</code>. Each day, we load the ship with packages on the conveyor belt (in the order given by <code>weights</code>). We may not load more weight than the maximum weight capacity of the ship.</p>

<p>Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within <code>days</code> days.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> weights = [1,2,3,4,5,6,7,8,9,10], days = 5
<strong>Output:</strong> 15
<strong>Explanation:</strong> A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> weights = [3,2,2,4,1,4], days = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> weights = [1,2,3,1,1], days = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong>
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= weights.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= weights[i] &lt;= 500</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mx):
            ws, cnt = 0, 1
            for w in weights:
                ws += w
                if ws > mx:
                    cnt += 1
                    ws = w
            return cnt <= days

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if not check(mid):
                low = mid + 1
            else:
                high = mid
        return low
```
# [1028. Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal)

## Description

<!-- description:start -->

<p>We run a&nbsp;preorder&nbsp;depth-first search (DFS) on the <code>root</code> of a binary tree.</p>

<p>At each node in this traversal, we output <code>D</code> dashes (where <code>D</code> is the depth of this node), then we output the value of this node.&nbsp; If the depth of a node is <code>D</code>, the depth of its immediate child is <code>D + 1</code>.&nbsp; The depth of the <code>root</code> node is <code>0</code>.</p>

<p>If a node has only one child, that child is guaranteed to be <strong>the left child</strong>.</p>

<p>Given the output <code>traversal</code> of this traversal, recover the tree and return <em>its</em> <code>root</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex1.png" style="width: 423px; height: 200px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3--4-5--6--7&quot;
<strong>Output:</strong> [1,2,5,3,4,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex2.png" style="width: 432px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3---4-5--6---7&quot;
<strong>Output:</strong> [1,2,5,3,null,6,null,4,null,7]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex3.png" style="width: 305px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-401--349---90--88&quot;
<strong>Output:</strong> [1,401,null,349,88,90]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the original tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->
#### Python
```python
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        st = []
        i = 0
        while i < len(traversal):
            num = 0
            depth = 0
            while i < len(traversal) and traversal[i] == "-":
                depth += 1
                i += 1
            while i < len(traversal) and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            node = TreeNode(num)
            while len(st) > depth:
                st.pop()
            if not st:
                st.append(node)
                continue
            if st[-1].left:
                st[-1].right = node
            else:
                st[-1].left = node
            st.append(node)
        if not st:
            return None
        return st[0]
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1047.Remove%20All%20Adjacent%20Duplicates%20In%20String/README_EN.md
rating: 1286
source: Weekly Contest 137 Q2
tags:
    - Stack
    - String
---

<!-- problem:start -->

# [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string)

[中文文档](/solution/1000-1099/1047.Remove%20All%20Adjacent%20Duplicates%20In%20String/README.md)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaca&quot;
<strong>Output:</strong> &quot;ca&quot;
<strong>Explanation:</strong> 
For example, in &quot;abbaca&quot; we could remove &quot;bb&quot; since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is &quot;aaca&quot;, of which only &quot;aa&quot; is possible, so the final string is &quot;ca&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;azxxzy&quot;
<strong>Output:</strong> &quot;ay&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->
### O(N) time and O(1) space complexity
```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        index = 0
        result = [""] * len(s)
        for right in range(0, len(s)):
            result[index] = s[right]
            if index > 0 and result[index] == result[index - 1]:
                index = index - 2
            index += 1
        return "".join(result[:index])
```

### Using Stack(Extra memory)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)
```
## Meta variant
What if you had to remove all adjacent duplicates as you iterate left-to-right?

```python
def remove_all_adjacent_duplicates_variant_1047_python(s):
    letters = []
    for ch in s:
        if not letters:
            letters.append({'val': ch, 'freq': 1})
            continue
        if letters[-1]['val'] == ch:
            letters[-1]['freq'] += 1
            continue

        if letters[-1]['freq'] > 1:
            letters.pop()

        if not letters or letters[-1]['val'] != ch:
            letters.append({'val': ch, 'freq': 1})
        elif letters[-1]['val'] == ch:
            letters[-1]['freq'] += 1

    if letters and letters[-1]['freq'] > 1:
        letters.pop()

    result = ''.join([letter['val'] for letter in letters])
    return result

if __name__ == '__main__':
    s = "azxxxzy"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

    s = "abbaxx"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabbccdd"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aaabbaad"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

    s = "abcdefg"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

    s = "abbcddeff"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

    s = "abcdeffedcba"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabccddeeffbbbbbbbbbf"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

    s = "abbbacca"; # Cannot pick and choose duplicates in the middle to delete first
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "a"
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1079.Letter%20Tile%20Possibilities/README_EN.md
rating: 1740
source: Weekly Contest 140 Q2
tags:
    - Hash Table
    - String
    - Backtracking
    - Counting
---

<!-- problem:start -->

# [1079. Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities)

[中文文档](/solution/1000-1099/1079.Letter%20Tile%20Possibilities/README.md)

## Description

<!-- description:start -->

<p>You have <code>n</code>&nbsp;&nbsp;<code>tiles</code>, where each tile has one letter <code>tiles[i]</code> printed on it.</p>

<p>Return <em>the number of possible non-empty sequences of letters</em> you can make using the letters printed on those <code>tiles</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;AAB&quot;
<strong>Output:</strong> 8
<strong>Explanation: </strong>The possible sequences are &quot;A&quot;, &quot;B&quot;, &quot;AA&quot;, &quot;AB&quot;, &quot;BA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;BAA&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;AAABBC&quot;
<strong>Output:</strong> 188
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;V&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tiles.length &lt;= 7</code></li>
	<li><code>tiles</code> consists of uppercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def helper(path, current):
            if path:
                res.add(path)
            for i in range(len(current)):
                helper(path + current[i], current[:i] + current[i + 1 :])

        helper("", tiles)
        return len(res)
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix/README_EN.md
rating: 1658
source: Weekly Contest 141 Q3
tags:
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->

# [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix)

[中文文档](/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix/README.md)

## Description

<!-- description:start -->

<p>Given an <code>n x n</code> binary matrix <code>grid</code>, return <em>the length of the shortest <strong>clear path</strong> in the matrix</em>. If there is no clear path, return <code>-1</code>.</p>

<p>A <strong>clear path</strong> in a binary matrix is a path from the <strong>top-left</strong> cell (i.e., <code>(0, 0)</code>) to the <strong>bottom-right</strong> cell (i.e., <code>(n - 1, n - 1)</code>) such that:</p>

<ul>
	<li>All the visited cells of the path are <code>0</code>.</li>
	<li>All the adjacent cells of the path are <strong>8-directionally</strong> connected (i.e., they are different and they share an edge or a corner).</li>
</ul>

<p>The <strong>length of a clear path</strong> is the number of visited cells of this path.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix/images/example1_1.png" style="width: 500px; height: 234px;" />
<pre>
<strong>Input:</strong> grid = [[0,1],[1,0]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix/images/example2_1.png" style="height: 216px; width: 500px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,0],[1,1,0],[1,1,0]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,0,0],[1,1,0],[1,1,0]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>grid[i][j] is 0 or 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        neibs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        n = len(grid)
        grid[0][0] = 1
        q = deque([(0, 0)])
        ans = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == c == n - 1:
                    return ans
                for i, j in neibs:
                    x, y = r + i, c + j
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))
            ans += 1
        return -1
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1209.Remove%20All%20Adjacent%20Duplicates%20in%20String%20II/README_EN.md
rating: 1541
source: Weekly Contest 156 Q3
tags:
    - Stack
    - String
---

<!-- problem:start -->

# [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii)

[中文文档](/solution/1200-1299/1209.Remove%20All%20Adjacent%20Duplicates%20in%20String%20II/README.md)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and an integer <code>k</code>, a <code>k</code> <strong>duplicate removal</strong> consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them, causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It is guaranteed that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, k = 2
<strong>Output:</strong> &quot;abcd&quot;
<strong>Explanation: </strong>There&#39;s nothing to delete.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;deeedbbcccbdaa&quot;, k = 3
<strong>Output:</strong> &quot;aa&quot;
<strong>Explanation: 
</strong>First delete &quot;eee&quot; and &quot;ccc&quot;, get &quot;ddbbbdaa&quot;
Then delete &quot;bbb&quot;, get &quot;dddaa&quot;
Finally delete &quot;ddd&quot;, get &quot;aa&quot;</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pbbcggttciiippooaais&quot;, k = 2
<strong>Output:</strong> &quot;ps&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> only contains lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We can traverse the string $s$, maintaining a stack that stores the characters and their occurrence counts. When traversing to character $c$, if the character at the top of the stack is the same as $c$, we increment the count of the top element by one; otherwise, we push the character $c$ and count $1$ into the stack. When the count of the top element equals $k$, we pop the top element from the stack.

After traversing the string $s$, the elements remaining in the stack form the final result. We can pop the elements from the stack one by one, concatenate them into a string, and that's our answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if st and st[-1][0] == c:
                if st[-1][1] + 1 == k:
                    st.pop()
                else:
                    st[-1][1] += 1
            else:
                st.append([c, 1])
        return "".join([c * v for c, v in st])
```

#### Java

```java
class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<int[]> stk = new ArrayDeque<>();
        for (int i = 0; i < s.length(); ++i) {
            int j = s.charAt(i) - 'a';
            if (!stk.isEmpty() && stk.peek()[0] == j) {
                stk.peek()[1] = (stk.peek()[1] + 1) % k;
                if (stk.peek()[1] == 0) {
                    stk.pop();
                }
            } else {
                stk.push(new int[] {j, 1});
            }
        }
        StringBuilder ans = new StringBuilder();
        for (var e : stk) {
            char c = (char) (e[0] + 'a');
            for (int i = 0; i < e[1]; ++i) {
                ans.append(c);
            }
        }
        ans.reverse();
        return ans.toString();
    }
}
```

#### C++

```cpp
class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> stk;
        for (char& c : s) {
            if (stk.size() && stk.back().first == c) {
                stk.back().second = (stk.back().second + 1) % k;
                if (stk.back().second == 0) {
                    stk.pop_back();
                }
            } else {
                stk.push_back({c, 1});
            }
        }
        string ans;
        for (auto [c, v] : stk) {
            ans += string(v, c);
        }
        return ans;
    }
};
```

#### Go

```go
func removeDuplicates(s string, k int) string {
	stk := []pair{}
	for _, c := range s {
		if len(stk) > 0 && stk[len(stk)-1].c == c {
			stk[len(stk)-1].v = (stk[len(stk)-1].v + 1) % k
			if stk[len(stk)-1].v == 0 {
				stk = stk[:len(stk)-1]
			}
		} else {
			stk = append(stk, pair{c, 1})
		}
	}
	ans := []rune{}
	for _, e := range stk {
		for i := 0; i < e.v; i++ {
			ans = append(ans, e.c)
		}
	}
	return string(ans)
}

type pair struct {
	c rune
	v int
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1216.Valid%20Palindrome%20III/README_EN.md
rating: 1753
source: Biweekly Contest 10 Q4
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [1216. Valid Palindrome III 🔒](https://leetcode.com/problems/valid-palindrome-iii)

[中文文档](/solution/1200-1299/1216.Valid%20Palindrome%20III/README.md)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and an integer <code>k</code>, return <code>true</code> if <code>s</code> is a <code>k</code><strong>-palindrome</strong>.</p>

<p>A string is <code>k</code><strong>-palindrome</strong> if it can be transformed into a palindrome by removing at most <code>k</code> characters from it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcdeca&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Remove &#39;b&#39; and &#39;e&#39; characters.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbababa&quot;, k = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>

<!-- description:end -->

## Solutions

### recursion with caching

```python
class Solution:    
    def isValidPalindrome(self,s,k):
        @cache
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
               if s[l].lower() != s[r].lower():
                   return False
               l +=1; r -= 1
            return True

        @cache
        def solve(s, k):
            if k <0:
                return False
            if isPalindrome(s):
                return True
            for i in range(len(s)):
                if solve(s[:i] + s[i+1:], k-1):
                    return True
            return False
        return solve(s,k)
```
<!-- solution:start -->

### Solution 1: Dynamic Programming

The problem requires us to remove at most $k$ characters to make the remaining string a palindrome. This can be transformed into finding the longest palindromic subsequence.

We define $f[i][j]$ as the length of the longest palindromic subsequence in the substring $s[i..j]$. Initially, we have $f[i][i] = 1$ for all $i$, since each single character is a palindrome.

If $s[i] = s[j]$, then we have $f[i][j] = f[i+1][j-1] + 2$, since we can add both $s[i]$ and $s[j]$ to the longest palindromic subsequence of $s[i+1..j-1]$.

If $s[i] \neq s[j]$, then we have $f[i][j] = \max(f[i+1][j], f[i][j-1])$, since we need to remove either $s[i]$ or $s[j]$ to make the remaining substring a palindrome.

Finally, we check whether there exists $f[i][j] + k \geq n$, where $n$ is the length of the string $s$. If so, it means that we can remove at most $k$ characters to make the remaining string a palindrome.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if f[i][j] + k >= n:
                    return True
        return False
```
# [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

## Description

<!-- description:start -->

<p>Given a string <font face="monospace">s</font> of <code>&#39;(&#39;</code> , <code>&#39;)&#39;</code> and lowercase English characters.</p>

<p>Your task is to remove the minimum number of parentheses ( <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>, in any positions ) so that the resulting <em>parentheses string</em> is valid and return <strong>any</strong> valid string.</p>

<p>Formally, a <em>parentheses string</em> is valid if and only if:</p>

<ul>
	<li>It is the empty string, contains only lowercase characters, or</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lee(t(c)o)de)&quot;
<strong>Output:</strong> &quot;lee(t(c)o)de&quot;
<strong>Explanation:</strong> &quot;lee(t(co)de)&quot; , &quot;lee(t(c)ode)&quot; would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a)b(c)d&quot;
<strong>Output:</strong> &quot;ab(c)d&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;))((&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> An empty string is also valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either&nbsp;<code>&#39;(&#39;</code> , <code>&#39;)&#39;</code>, or lowercase English letter.</li>
</ul>

### Solution 1: Two Passes

First, we scan from left to right and remove the extra right parentheses. Then, we scan from right to left and remove the extra left parentheses.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the string $s$.

Similar problems:

-   [678. Valid Parenthesis String](https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0678.Valid%20Parenthesis%20String/README_EN.md)
-   [2116. Check if a Parentheses String Can Be Valid](https://github.com/doocs/leetcode/blob/main/solution/2100-2199/2116.Check%20if%20a%20Parentheses%20String%20Can%20Be%20Valid/README_EN.md)

### Solution 

#### TC O(n) SC O(n)
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        for i, c in enumerate(s):
            if c == "(":
                st.append(i)
            elif c == ")":
                if st and s[st[-1]] == "(":
                    st.pop()
                else:
                    st.append(i)
        res = ""
        ind = 0
        for j in range(len(s)):
            if ind < len(st) and j == st[ind]:
                ind += 1
                continue
            res += s[j]
        return res
```

#### TC O(n) SC O(1)
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        count = 0
        for i in range(len(res)):
            if res[i] == "(":
                count += 1
            elif res[i] == ")":
                if count > 0:
                    count -= 1
                else:
                    res[i] = ""
        count = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] == ")":
                count += 1
            elif res[i] == "(":
                if count > 0:
                    count -= 1
                else:
                    res[i] = ""
        return "".join(res)
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1382.Balance%20a%20Binary%20Search%20Tree/README_EN.md
rating: 1540
source: Weekly Contest 180 Q3
tags:
    - Greedy
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Divide and Conquer
    - Binary Tree
---

<!-- problem:start -->

# [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree)

[中文文档](/solution/1300-1399/1382.Balance%20a%20Binary%20Search%20Tree/README.md)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree, return <em>a <strong>balanced</strong> binary search tree with the same node values</em>. If there is more than one answer, return <strong>any of them</strong>.</p>

<p>A binary search tree is <strong>balanced</strong> if the depth of the two subtrees of every node never differs by more than <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1382.Balance%20a%20Binary%20Search%20Tree/images/balance1-tree.jpg" style="width: 500px; height: 319px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,null,3,null,4,null,null]
<strong>Output:</strong> [2,1,3,null,null,null,4]
<b>Explanation:</b> This is not the only correct answer, [3,1,4,null,2] is also correct.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1382.Balance%20a%20Binary%20Search%20Tree/images/balanced2-tree.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: In-order Traversal + Construct Balanced Binary Search Tree

Since the original tree is a binary search tree, we can save the result of the in-order traversal in an array $nums$. Then we design a function $build(i, j)$, which is used to construct a balanced binary search tree within the index range $[i, j]$ in $nums$. The answer is $build(0, |nums| - 1)$.

The execution logic of the function $build(i, j)$ is as follows:

-   If $i > j$, then the balanced binary search tree is empty, return an empty node;
-   Otherwise, we take $mid = (i + j) / 2$ as the root node, then recursively build the left and right subtrees, and return the root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary search tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        def build(i: int, j: int) -> TreeNode:
            if i > j:
                return None
            mid = (i + j) // 2
            left = build(i, mid - 1)
            right = build(mid + 1, j)
            return TreeNode(nums[mid], left, right)

        nums = []
        inorder(root)
        return build(0, len(nums) - 1)

```
# [1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii)


## Description

<!-- description:start -->

<p>Given a 2D integer array <code>nums</code>, return <em>all elements of </em><code>nums</code><em> in diagonal order as shown in the below images</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1424.Diagonal%20Traverse%20II/images/sample_1_1784.png" style="width: 158px; height: 143px;" />
<pre>
<strong>Input:</strong> nums = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,4,2,7,5,3,8,6,9]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1424.Diagonal%20Traverse%20II/images/sample_2_1784.png" style="width: 230px; height: 177px;" />
<pre>
<strong>Input:</strong> nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
<strong>Output:</strong> [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sum(nums[i].length) &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

We observe that:

-   The value of $i + j$ is the same for each diagonal;
-   The value of $i + j$ for the next diagonal is greater than that of the previous diagonal;
-   Within the same diagonal, the value of $i + j$ is the same, and the value of $j$ increases from small to large.

Therefore, we store all numbers in the form of $(i, j, \textit{nums}[i][j])$ into $\textit{arr}$, and then sort according to the first two items. Finally, return the array composed of the values at index 2 of all elements in $\textit{arr}$.

The time complexity is $O(n \times \log n)$, where $n$ is the number of elements in the array $\textit{nums}$. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python without sorting
```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        D = collections.defaultdict(list)
        R = len(nums)

        for r in range(R):
            for c in range(len(nums[r])):
                D[r+c].append(nums[r][c])

        res = []
        i = 0
        while True:
            if i not in D:
                break
            res.extend(D[i][::-1])
            i += 1
        return res
```
        
#### Python3(With Sorting)
Increases time complexity as you have to sort the result array

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                arr.append((i + j, j, v))
        arr.sort()
        return [v[2] for v in arr]
```
# [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number)

## Description

<!-- description:start -->

<p>Given an array <code>arr</code> of positive integers sorted in a <strong>strictly increasing order</strong>, and an integer <code>k</code>.</p>

<p>Return <em>the</em> <code>k<sup>th</sup></code> <em><strong>positive</strong> integer that is <strong>missing</strong> from this array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,3,4,7,11], k = 5
<strong>Output:</strong> 9
<strong>Explanation: </strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup>&nbsp;missing positive integer is 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4], k = 2
<strong>Output:</strong> 6
<strong>Explanation: </strong>The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>arr[i] &lt; arr[j]</code> for <code>1 &lt;= i &lt; j &lt;= arr.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<p>Could you solve this problem in less than O(n) complexity?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### O(n+k) time complexity

```python
class Solution:
    def findKthPositive(self, arr, k):
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i
```

#### Binary Search O(logN)
```
Now, we have two good indicators, that we need to use binary search: sorted data and O(log n) complexity.
Let us look for the following example for more understanding:
2, 3, 4, 7, 11, 12 and k = 5.
We need to find place, of k-th missing positive number, so, let us create virtual list
(virtual, because we will not compute it full, but only elements we need):
B = [2 - 1, 3 - 2, 4 - 3, 7 - 4, 11 - 5, 12 - 6] = [1, 1, 1, 3, 6, 6].
What this list represents is how many missing numbers we have for each inex: for first number we have missing number [1],
for next two iterations also, when we add 7, we have 3 missing numbers: [1, 5, 6], when we add 11,
we have 6 missing numbers: [1, 5, 6, 8, 9, 10]. How we evalaute values of list B? Very easy, it is just A[i] - i - 1.
What we need to find now in array B: first element, which is greater or equal than k.
In our example, we have [1, 1, 1, 3, 6, 6]. We will find it with binary search:
this element have index end = 4. Finally, we need to go back to original data, we have
arr = [2, 3, 4, 7, 11, 12]
 B = [1, 1, 1, 3, 6, 6]
So, what we now know that our answer is between numbers 7 and 11 and it is equal to arr[end] - (B[end] - k + 1),
where the second part is how many steps we need to make backward. Using B[end] = arr[end] - end - 1,
we have end + k, we need to return.
Complexity: time complexity is O(log n), space is O(1).
```

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] - mid - 1 >= k:
                right = mid
            else:
                left = mid + 1
        # At index i, arr[i] - i - 1 elements are missing. subtract this from
        # k, we get the remaining elements we have to add.
        # we add this remaining number to arr[left-1] to get the answer
        return k - (arr[left - 1] - (left - 1) -1) + arr[left - 1]
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1570.Dot%20Product%20of%20Two%20Sparse%20Vectors/README_EN.md
tags:
    - Design
    - Array
    - Hash Table
    - Two Pointers
---

<!-- problem:start -->

# [1570. Dot Product of Two Sparse Vectors 🔒](https://leetcode.com/problems/dot-product-of-two-sparse-vectors)

[中文文档](/solution/1500-1599/1570.Dot%20Product%20of%20Two%20Sparse%20Vectors/README.md)

## Description

<!-- description:start -->

<p>Given two sparse vectors, compute their dot product.</p>

<p>Implement class <code>SparseVector</code>:</p>

<ul data-indent="0" data-stringify-type="unordered-list">
	<li><code>SparseVector(nums)</code>&nbsp;Initializes the object with the vector <code>nums</code></li>
	<li><code>dotProduct(vec)</code>&nbsp;Compute the dot product between the instance of <em>SparseVector</em> and <code>vec</code></li>
</ul>

<p>A <strong>sparse vector</strong> is a vector that has mostly zero values, you should store the sparse vector&nbsp;<strong>efficiently </strong>and compute the dot product between two <em>SparseVector</em>.</p>

<p><strong>Follow up:&nbsp;</strong>What if only one of the vectors is sparse?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
<strong>Output:</strong> 8
<strong>Explanation:</strong> v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i]&nbsp;&lt;= 100</code></li>
</ul>


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
## Meta variant
What if you had to optimize your algorithm using binary search?
```python
from collections import namedtuple
from bisect import bisect_left


class SparseVectorVariant:
    def __init__(self, nums: list[int]):
        Pair = namedtuple("Pair", "index value")
        self.pairs = [
            Pair(index, value) for index, value in enumerate(nums) if value != 0
        ]

    def dotProduct(self, vec: "SparseVectorVariant") -> int:
        result = 0
        shorter, longer = (
            (self.pairs, vec.pairs)
            if len(self.pairs) < len(vec.pairs)
            else (vec.pairs, self.pairs)
        )
        for pair in shorter:
            matched_idx = bisect_left(longer, (pair.index,))
            if matched_idx >= len(longer) or longer[matched_idx].index != pair.index:
                continue
            result += pair.value * longer[matched_idx].value

        return result
nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]

s1 = SparseVectorVariant(nums1)
s2 = SparseVectorVariant(nums2)

print(s1.dotProduct(s2))
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

## Meta variant
What if you were given all the nodes as a part of a vector, and no longer the root node?
```
iterate over the vector and create child_to_parent map using left and right of each node and then do the same.
```

```python
def findancestor(nodes, p_start, q_start):
    for node in nodes:
        if node.left:
            child_to_parent_map[node.left] = node
        if node.right:
            child_to_parent_map[node.right] = node
            
        p = p_start
        q = q_start
        while p != q:
            p = child_to_parent_map[p] if p in child_to_parent_map else q_start
            q = child_to_parent_map[q] if q in child_to_parent_map else p_start
        return p
```

---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1762.Buildings%20With%20an%20Ocean%20View/README_EN.md
tags:
    - Stack
    - Array
    - Monotonic Stack
---

<!-- problem:start -->

# [1762. Buildings With an Ocean View 🔒](https://leetcode.com/problems/buildings-with-an-ocean-view)

[中文文档](/solution/1700-1799/1762.Buildings%20With%20an%20Ocean%20View/README.md)

## Description

<!-- description:start -->

<p>There are <code>n</code> buildings in a line. You are given an integer array <code>heights</code> of size <code>n</code> that represents the heights of the buildings in the line.</p>

<p>The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a <strong>smaller</strong> height.</p>

<p>Return a list of indices <strong>(0-indexed)</strong> of buildings that have an ocean view, sorted in increasing order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> heights = [4,2,3,1]
<strong>Output:</strong> [0,2,3]
<strong>Explanation:</strong> Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [4,3,2,1]
<strong>Output:</strong> [0,1,2,3]
<strong>Explanation:</strong> All the buildings have an ocean view.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> heights = [1,3,2,4]
<strong>Output:</strong> [3]
<strong>Explanation:</strong> Only building 3 has an ocean view.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>9</sup></code></li>
</ul>

```python
class Solution:
   def findBuildings(self, heights: List[int]) -> List[int]:
       ans = []
       mx = 0
       for i in range(len(heights) - 1, -1, -1):
           if heights[i] > mx:
               ans.append(i)
               mx = heights[i]
       return ans[::-1]
```

## Meta variant
 What if you had to return all of the buildings that either have an ocean view to its left and/or its right? This becomes very similar to Leetcode 42 Trapping Rain Water
```
std::vector<int> findBuildingViewCount_second_variant_1762(std::vector<int>& heights) {
    int n = heights.size();
    if (n == 1)
        return {0};

    int left = 0, right = n - 1;
    std::vector<int> left_view{left};
    std::vector<int> right_view{right};
    int left_max = heights[left];
    int right_max = heights[right];
    while (left < right) {
        if (left_max < right_max) {
            left++;
            if (heights[left] > left_max && left < right) {
                left_view.push_back(left);
                left_max = heights[left];
            }
        }
        else {
            right--;
            if (heights[right] > right_max && left < right) {
                right_view.push_back(right);
                right_max = heights[right];
            }
        }
    }
    left_view.insert(left_view.end(), right_view.rbegin(), right_view.rend());
    return left_view;
}
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1768.Merge%20Strings%20Alternately/README_EN.md
rating: 1166
source: Weekly Contest 229 Q1
tags:
    - Two Pointers
    - String
---

<!-- problem:start -->

# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately)

[中文文档](/solution/1700-1799/1768.Merge%20Strings%20Alternately/README.md)

## Description

<!-- description:start -->

<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>Return <em>the merged string.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;
<strong>Output:</strong> &quot;apbqcr&quot;
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;
<strong>Output:</strong> &quot;apbqrs&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;
<strong>Output:</strong> &quot;apbqcd&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Simulation

We traverse the two strings `word1` and `word2`, take out the characters one by one, and append them to the result string. The Python code can be simplified into one line.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the two strings respectively. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = j = 0
        m, n = len(word1), len(word2)
        while i < m or j < n:
            res += word1[i] if i < m else ""
            res += word2[j] if j < n else ""
            i += 1
            j += 1
        return res
```

#### Alternate Python
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = j = 0
        count = 0
        for a, b in zip(word1, word2):
            res += a + b
        if len(word1) < len(word2):
            res += word2[len(word1) :]
        else:
            res += word1[len(word2) :]
        return res
```
# [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)


## Description

<!-- description:start -->

<p>You are given two strings <code>s1</code> and <code>s2</code> of equal length. A <strong>string swap</strong> is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.</p>

<p>Return <code>true</code> <em>if it is possible to make both strings equal by performing <strong>at most one string swap </strong>on <strong>exactly one</strong> of the strings. </em>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;bank&quot;, s2 = &quot;kanb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> For example, swap the first character with the last character of s2 to make &quot;bank&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;attack&quot;, s2 = &quot;defend&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make them equal with one string swap.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;kelb&quot;, s2 = &quot;kelb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The two strings are already equal, so no string swap operation is required.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1</code> and <code>s2</code> consist of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We use a variable $cnt$ to record the number of characters at the same position in the two strings that are different. If the two strings meet the requirements of the problem, then $cnt$ must be $0$ or $2$. We also use two character variables $c1$ and $c2$ to record the characters that are different at the same position in the two strings.

While traversing the two strings simultaneously, for two characters $a$ and $b$ at the same position, if $a \ne b$, then $cnt$ is incremented by $1$. If at this time $cnt$ is greater than $2$, or $cnt$ is $2$ and $a \ne c2$ or $b \ne c1$, then we directly return `false`. Note to record $c1$ and $c2$.

At the end of the traversal, if $cnt \neq 1$, return `true`.

The time complexity is $O(n)$, where $n$ is the length of the string. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff1 = diff2 = -1
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2:
                    return False
                if diff1 == -1:
                    diff1 = i
                else:
                    diff2 = i
        return count == 0 or (
            count == 2 and s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]
        )
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1891.Cutting%20Ribbons/README_EN.md
tags:
    - Array
    - Binary Search
---

<!-- problem:start -->

# [1891. Cutting Ribbons 🔒](https://leetcode.com/problems/cutting-ribbons)

[中文文档](/solution/1800-1899/1891.Cutting%20Ribbons/README.md)

## Description

<!-- description:start -->

<p>You are given an integer array <code>ribbons</code>, where <code>ribbons[i]</code> represents the length of the <code>i<sup>th</sup></code> ribbon, and an integer <code>k</code>. You may cut any of the ribbons into any number of segments of <strong>positive integer</strong> lengths, or perform no cuts at all.</p>

<p>For example, if you have a ribbon of length <code>4</code>, you can:</p>
<ul>
    	<li>Keep the ribbon of length <code>4</code>,</li>
    	<li>Cut it into one ribbon of length <code>3</code> and one ribbon of length <code>1</code>,</li>
    	<li>Cut it into two ribbons of length <code>2</code>,</li>
    	<li>Cut it into one ribbon of length <code>2</code> and two ribbons of length <code>1</code>, or</li>
    	<li>Cut it into four ribbons of length <code>1</code>.</li>

</ul>

<p>Your task is to determine the <strong>maximum</strong> length of ribbon, <code>x</code>, that allows you to cut <em>at least</em> <code>k</code> ribbons, each of length <code>x</code>. You can discard any leftover ribbon from the cuts. If it is <strong>impossible</strong> to cut <code>k</code> ribbons of the same length, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ribbons = [9,7,5], k = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong>
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ribbons = [7,5,9], k = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> ribbons = [5,7,9], k = 22
<strong>Output:</strong> 0
<strong>Explanation:</strong> You cannot obtain k ribbons of the same positive integer length.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ribbons.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= ribbons[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

We observe that if we can obtain $k$ ropes of length $x$, then we can also obtain $k$ ropes of length $x-1$. This implies that there is a monotonicity property, and we can use binary search to find the maximum length $x$ such that we can obtain $k$ ropes of length $x$.

We define the left boundary of the binary search as $left=0$, the right boundary as $right=\max(ribbons)$, and the middle value as $mid=(left+right+1)/2$. We then calculate the number of ropes we can obtain with length $mid$, denoted as $cnt$. If $cnt \geq k$, it means we can obtain $k$ ropes of length $mid$, so we update $left$ to $mid$. Otherwise, we update $right$ to $mid-1$.

Finally, we return $left$ as the maximum length of the ropes we can obtain.

The time complexity is $O(n \times \log M)$, where $n$ and $M$ are the number of ropes and the maximum length of the ropes, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
def maxLength(ribbons, k: int) -> int:
    left, right = 0, max(ribbons)
    while left < right:
        mid = (left + right)//2
        if mid == 0:
            return mid
        cnt = sum(x // mid for x in ribbons)
        if cnt > k:
            left = mid + 1
        else:
            right = mid
    return left
```
---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2965.Find%20Missing%20and%20Repeated%20Values/README_EN.md
rating: 1244
source: Weekly Contest 376 Q1
tags:
    - Array
    - Hash Table
    - Math
    - Matrix
---

<!-- problem:start -->

# [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values)

[中文文档](/solution/2900-2999/2965.Find%20Missing%20and%20Repeated%20Values/README.md)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> 2D integer matrix <code><font face="monospace">grid</font></code> of size <code>n * n</code> with values in the range <code>[1, n<sup>2</sup>]</code>. Each integer appears <strong>exactly once</strong> except <code>a</code> which appears <strong>twice</strong> and <code>b</code> which is <strong>missing</strong>. The task is to find the repeating and missing numbers <code>a</code> and <code>b</code>.</p>

<p>Return <em>a <strong>0-indexed </strong>integer array </em><code>ans</code><em> of size </em><code>2</code><em> where </em><code>ans[0]</code><em> equals to </em><code>a</code><em> and </em><code>ans[1]</code><em> equals to </em><code>b</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,3],[2,2]]
<strong>Output:</strong> [2,4]
<strong>Explanation:</strong> Number 2 is repeated and number 4 is missing so the answer is [2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[9,1,7],[8,9,2],[3,4,6]]
<strong>Output:</strong> [9,5]
<strong>Explanation:</strong> Number 9 is repeated and number 5 is missing so the answer is [9,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == grid.length == grid[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= n * n</code></li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> there is exactly one <code>x</code> that is not equal to any of the grid members.</li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> there is exactly one <code>x</code> that is equal to exactly two of the grid members.</li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> except two of them there is exatly one pair of <code>i, j</code> that <code>0 &lt;= i, j &lt;= n - 1</code> and <code>grid[i][j] == x</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We create an array $cnt$ of length $n^2 + 1$ to count the frequency of each number in the matrix.

Next, we traverse $i \in [1, n^2]$. If $cnt[i] = 2$, then $i$ is the duplicated number, and we set the first element of the answer to $i$. If $cnt[i] = 0$, then $i$ is the missing number, and we set the second element of the answer to $i$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Here, $n$ is the side length of the matrix.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for row in grid:
            for v in row:
                cnt[v] += 1
        ans = [0] * 2
        for i in range(1, n * n + 1):
            if cnt[i] == 2:
                ans[0] = i
            if cnt[i] == 0:
                ans[1] = i
        return ans
```

### Using math
```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n_squared = n * n
        
        expected_sum = n_squared * (n_squared + 1) // 2
        expected_sum_squares = n_squared * (n_squared + 1) * (2 * n_squared + 1) // 6
        
        actual_sum = 0
        actual_sum_squares = 0
        
        for i in range(n):
            for j in range(n):
                actual_sum += grid[i][j]
                actual_sum_squares += grid[i][j] * grid[i][j]

        # a - b
        diff_sum = actual_sum - expected_sum

        # a² - b²
        diff_sum_squares = actual_sum_squares - expected_sum_squares
        
        # a + b = (a² - b²) / (a - b)
        sum_a_b = diff_sum_squares // diff_sum
        
        # Now we can find a and b
        a = (sum_a_b + diff_sum) // 2
        b = (sum_a_b - diff_sum) // 2
        
        return [a, b]
```
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3371.Identify%20the%20Largest%20Outlier%20in%20an%20Array/README_EN.md
rating: 1643
source: Weekly Contest 426 Q2
tags:
    - Array
    - Hash Table
    - Counting
    - Enumeration
---

<!-- problem:start -->

# [3371. Identify the Largest Outlier in an Array](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array)


## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. This array contains <code>n</code> elements, where <strong>exactly</strong> <code>n - 2</code> elements are <strong>special</strong><strong> numbers</strong>. One of the remaining <strong>two</strong> elements is the <em>sum</em> of these <strong>special numbers</strong>, and the other is an <strong>outlier</strong>.</p>

<p>An <strong>outlier</strong> is defined as a number that is <em>neither</em> one of the original special numbers <em>nor</em> the element representing the sum of those numbers.</p>

<p><strong>Note</strong> that special numbers, the sum element, and the outlier must have <strong>distinct</strong> indices, but <em>may </em>share the <strong>same</strong> value.</p>

<p>Return the <strong>largest</strong><strong> </strong>potential<strong> outlier</strong> in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-2,-1,-3,-6,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1,5,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li>The input is generated such that at least <strong>one</strong> potential outlier exists in <code>nums</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

We use a hash table $\textit{cnt}$ to record the frequency of each element in the array $\textit{nums}$.

Next, we enumerate each element $x$ in the array $\textit{nums}$ as a possible outlier. For each $x$, we calculate the sum $t$ of all elements in the array $\textit{nums}$ except $x$. If $t$ is not even, or half of $t$ is not in $\textit{cnt}$, then $x$ does not meet the condition, and we skip this $x$. Otherwise, if $x$ is not equal to half of $t$, or $x$ appears more than once in $\textit{cnt}$, then $x$ is a possible outlier, and we update the answer.

After enumerating all elements, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        cnt = Counter(nums)
        ans = -inf
        for x, v in cnt.items():
            t = s - x
            if t % 2 or cnt[t // 2] == 0:
                continue
            if x != t // 2 or v > 1:
                ans = max(ans, x)
        return ans
```
