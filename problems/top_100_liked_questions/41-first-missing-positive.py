"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 
Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

https://leetcode.com/problems/first-missing-positive/
"""

from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)
		for i in range(n):
			while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
				temp = nums[i]
				nums[i] = nums[temp - 1]
				nums[temp - 1] = temp
				print("i:%s swap (%s, %s), nums:%s" % (i, nums[i], nums[temp - 1], nums))
		for i in range(n):
			if nums[i] != i + 1:
				return i+1
		return nums[-1] + 1

if __name__ == "__main__":
	nums = [1]
	oSolution = Solution()
	print (oSolution.firstMissingPositive(nums))