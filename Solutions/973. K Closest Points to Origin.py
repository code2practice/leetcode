'''
973. K Closest Points to Origin
Medium
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
 
Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
'''

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

'''
Randomized QuickSelect
This solution is a modifed version of Quick-sort meant to be used when we need to find k(or kth) smallest(or largest) elements (based on some comparator) but not in any particular order. Most of the partition logic used in this algorithm remains the same as in quicksort but we just modify the recursive part of quicksort to suit our use case.

Each time, we choose a pivot and partition the array around that pivot using a comparator. In this case, we will choose a randomized pivot (the choice of pivot majorly affects the performace of algorithm and we need to try to choose a pivot that partitions the range roughly equally for best result. Without any knowledge of the way that elements occur in array, it's best to choose randomized pivot each time to avoid worst case) and for comparator, we will use the squared euclidean distance.

Initially we start with whole range of array [L, R] = [0, size(P)-1]. After each partition, the partition function will return the pivot index (denoted as p below) which is basically the element which separates all the elements <= than it to left side and all elements > than it to the right side (not in particular order). We have:

If p < k, then we now have p elements which are closest to origin (although they aren't sorted in any particular order) but we still need some more elements to get k points in total. Thus, we iterate again and partition the array from indices [p+1, R] till we find k elements (by getting pivot at kth index)
If p > k, then we now have more than k elements with us that are closest to origin. But we are sure that any element to the right of p wont be ever in our answer. So we iterate again and partition just the range [L, p-1] till we find k elements
If p == k, we now have exactly k elements with us which are closest to origin. Thus, we return the 1st k elements of array

Time Complexity : O(N), at each partition, we are eliminating one end and re-partitioning the other end till we get pivot at kth index. On average, the partitions roughly eliminate half of remaining elements each time thus leading to N + N/2 + N/4 + ... + 1 = O(2N) iterations. However, in the worst case, there's still a chance (although very low) that we choose the worst pivot at each partition and this leads to N + N-1 + N-2 + ... + 1 = N2 total iterations leading to time complexity of O(N2)
Space Complexity : O(1), only constant extra space is being used
'''
# Using quick select
class Solution:
   def kClosest(self, P, k):
       euclidean = lambda p: p[0] ** 2 + p[1] ** 2
       def partition(L, R):
           random = randint(L, R)  # choosing random pivot
           P[R], P[random] = P[random], P[R]  # and swapping it to the end
           i, pivotDist = L, euclidean(P[R])
           for j in range(L, R + 1):
               if euclidean(P[j]) <= pivotDist:
                   P[i], P[j] = P[j], P[i]
                   i += 1
           return i - 1
       L, R, p = 0, len(P) - 1, len(P)
       while p != k:
           p = partition(L, R)
           if p < k:
               L = p + 1
           else:
               R = p - 1
       return P[:k]
