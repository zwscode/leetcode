# https://leetcode.com/problems/sort-colors/description/
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

class Solution(object):
	
	# Solution1: Counting Sort
	# Idea: Count the number of each color, then overwrite the original array.
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		c = [0] * 3
		for x in nums:
			c[x] += 1
		
		i = 0
		for color, count in enumerate(c):
			while count > 0:
				nums[i] = color
				i += 1
				count -= 1

	# Solution2: Double Pointers
	# Idea: Use two pointers to partition the array into three parts: 0, 1, 2.
	def sortColors2(self, nums):
		n = len(nums)
		l = 0
		r = n - 1

		i = 0
		while i <= r:
			if nums[i] == 0:
				nums[i], nums[l] = nums[l], nums[i]
				l += 1
				i += 1
			elif nums[i] == 2:
				nums[i], nums[r] = nums[r], nums[i]
				r -= 1
			else:
				i += 1