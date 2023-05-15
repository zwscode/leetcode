"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

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
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

https://leetcode.com/problems/combination-sum-ii/
"""
from typing import List
class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		result = []
		prev = []
		candidates.sort()
		used = [False for i in range(len(candidates))]
		self.backtrack(result, prev, candidates, used, 0, target)
		return result
	
	def backtrack(self, result, prev, candidates, used, start, target):
		if target == 0:
			result.append(prev[:])
			return
		for i in range(start, len(candidates)):
			num = candidates[i]
			if num > target:
				break
			if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
				continue
			used[i] = True
			prev.append(num)
			self.backtrack(result, prev, candidates, used, i + 1, target - num)
			prev.pop()
			used[i] = False