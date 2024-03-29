# https://leetcode.com/problems/maximum-product-subarray/description/
# medium

"""
Given an integer array nums, find a 
subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution1(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1:
			return nums[0]
		dp = [0] * len(nums)
		dp[0] = nums[0]
		maxVal = float('-inf')
		for i in range(1, len(nums)):
			dp[i] = max(dp[i - 1] * nums[i], nums[i])
			maxVal = max(maxVal, dp[i])
		return maxVal

# Solution1 is wrong. [-2,3,-4] should return 24, but it returns 3. The reason for this is that 'dp[i] != dp[i - 1] * nums[i]'. Solution1 would be correct if all elements in nums are positive.

# Here is the correct solution:
class Solution:
	def maxProduct(self, nums):
		n = len(nums)

		# definition: the subarray ending with nums[i], the min product is dp1[i]
		dp1 = [0] * n
		# definition: the subarray ending with nums[i], the max product is dp2[i]
		dp2 = [0] * n

		# base case
		dp1[0] = nums[0]
		dp2[0] = nums[0]

		# state transition
		for i in range(1, n):
			dp1[i] = min(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])
			dp2[i] = max(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])

		# find max value in dp2
		res = float('-inf')
		for i in range(n):
			res = max(res, dp2[i])

		return res