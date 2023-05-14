"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

https://leetcode.com/problems/permutations-ii/
"""
from typing import List
class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		lUsed = [False for i in range(len(nums))]
		lResult = []
		lPrev = []
		self.backtrack(lResult, lPrev, nums, lUsed)
		return lResult

	def backtrack(self, lResult, lPrev, lNums, lUsed):
		if len(lPrev) == len(lNums):
			lResult.append(lPrev[:])
			return
		
		for i in range(len(lNums)):
			if lUsed[i] or (i > 0 and lNums[i] == lNums[i-1] and not lUsed[i - 1]):
				continue
			lUsed[i] = True
			lPrev.append(lNums[i])
			self.backtrack(lResult, lPrev, lNums, lUsed)
			lUsed[i] = False
			lPrev.pop()

