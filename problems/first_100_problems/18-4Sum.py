"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

https://leetcode.com/problems/4sum/
"""

"""
summary:
turn Nsum to (N-1)sum, repeat, solve 2Sum.
evaluate the ability to turn a big problem into smaller problem
"""

def fourSum(self, nums, target):
	def findNsum(nums, target, N, result, results):
		if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
			return
		if N == 2: # two pointers solve sorted 2-sum problem
			l,r = 0,len(nums)-1
			while l < r:
				s = nums[l] + nums[r]
				if s == target:
					results.append(result + [nums[l], nums[r]])
					l += 1
					while l < r and nums[l] == nums[l-1]:
						l += 1
				elif s < target:
					l += 1
				else:
					r -= 1
		else: # recursively reduce N
			for i in range(len(nums)-N+1):
				if i == 0 or (i > 0 and nums[i-1] != nums[i]):
					findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

	results = []
	findNsum(sorted(nums), target, 4, [], results)
	return results
