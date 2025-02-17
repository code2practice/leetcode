'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
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

'''
Time Complexity
The given code has two main operations:
Sorting the intervals list.
Iterating through the sorted list and merging overlapping intervals.
For a list of n intervals:
The sort operation typically has a complexity of O(n log n), since Python uses TimSort (a hybrid sorting algorithm derived from merge sort and 
insertion sort) for sorting lists.
The iteration over the list has a complexity of O(n), because we go through the intervals only once.
Hence, the total time complexity is the sum of these two operations, which is O(n log n) + O(n). Since O(n log n) is the higher order term, 
it dominates the total time complexity, which simplifies to O(n log n).
'''
