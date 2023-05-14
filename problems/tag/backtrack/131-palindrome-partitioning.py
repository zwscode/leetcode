"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

https://leetcode.com/problems/palindrome-partitioning/
"""
from typing import List
class Solution:
	def partition(self, s: str) -> List[List[str]]:
		result = []
		splitpos = []
		self.backtrack(result, splitpos, s, 0)
	
	def backtrack(self, result, splitpos, str, idx):
		if self.isLeftValidSplit(splitpos, len(str) - 1, str):
			result.append(splitpos[:])

		for i in range(idx, len(str) - 1):
			if self.isLeftValidSplit(splitpos, i, str):
				splitpos.append(i)
				self.backtrack(result, splitpos, str, i + 1)
				splitpos.remove()

	def isLeftValidSplit(self, splitpos, right, str):
		if not splitpos:
			return True
		if right == 0:
			return True
		left = splitpos[-1] if splitpos else 0
		mid = left + (right - left) / 2
		for i in range(mid - left + 1):
			if str[left + i + 1] != str[right - i]:
				return False
		return True