"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

https://leetcode.com/problems/container-with-most-water/
"""


"""
idea:
1. The widest container (using first and last line) is a good candidate, because of its width. 
	Its water level is the height of the smaller one of first and last line.
2. All other containers are less wide and thus would need a higher water level in order to hold more water.
3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
"""

class Solution:
	def maxArea(self, height):
		i, j = 0, len(height) - 1
		water = 0
		while i < j:
			water = max(water, (j - i) * min(height[i], height[j]))
			if height[i] < height[j]:
				i += 1
			else:
				j -= 1
		return water
