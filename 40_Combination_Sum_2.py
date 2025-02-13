'''
40. Combination Sum II
Medium
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate 
numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
 
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''
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
