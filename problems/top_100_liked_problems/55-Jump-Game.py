"""
You are given an integer array nums.
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

https://leetcode.com/problems/jump-game/
"""

class Solution:
		def canJump(self, nums: List[int]) -> bool:
				n = len(nums)
				farthest = 0
				for i in range(n - 1):
						farthest = max(farthest, i + nums[i])
						if farthest <= i:
								return False
				return farthest >= n - 1

class Solution:
		def canJump(self, nums: List[int]) -> bool:
			last_position = len(nums)-1   
			for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
				if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
					last_position = i # Since we just need to reach to this new index
			return last_position == 0



