'''
347. Top K Frequent Elements
Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''


# Time Complexity O(nlogn)
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

'''
Time Complexity O(n)
Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.
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
'''

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
