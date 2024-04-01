# https://leetcode.com/problems/majority-element/description/
# ez

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
"""

# Idea: The easiest way to solve this is to use a hashmap to count all appearances of each element, iterate through the hashmap to get the majority element. But this is boring.

# The smart way is to classify all the elements into 2 categories: majority element and non-majority element. Use a counter to count the elements, if it meets the same element, increase the counter, otherwise decrease the counter. If the counter is 0, change the current element to be counted.


class Solution:
	def majorityElement(self, nums):
		# the counted element
		target = 0
		# the counter
		count = 0
		for i in range(len(nums)):
			if count == 0:
				# change the current element to be counted
				target = nums[i]
				count = 1
			elif nums[i] == target:
				# meets the same element, increase the counter
				count += 1
			else:
				# otherwise, decrease the counter
				count -= 1
		# in the end, the target is the majority element
		return target