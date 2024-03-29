# https://leetcode.com/problems/pascals-triangle/
# easy

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
"""

class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		if numRows == 1:
			return [[1]]
		res = []
		for i in range(numRows):
			level = []
			for j in range(i + 1):
				if j == 0 or j == i:
					level.append(1)
				else:
					val = res[-1][j - 1] + res[-1][j]
					level.append(val)
			res.append(level)
		return res