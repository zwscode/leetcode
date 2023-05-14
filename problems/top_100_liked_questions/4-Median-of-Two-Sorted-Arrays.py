"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


"""
idea: 
cut both array to left and right parts,
left of nums1 and left of nums2 forms left group.
right of nums1 and right of nums2 forms right group.

Invariant:
len(left group) == len(right group) or len(right group) + 1
max(left group) < min(right group).

in this case, the median is max(left group) or the average of max(left group) and min(right group)


key point: how to find such cuts?

initially set `left, right = 0, m`
cut p = (left + right) // 2
cut q = (m + n + 1) // 2 - p
if p, q is not the final cut we want, we set `left = p + 1` or `right = p - 1`,
and repeat to find a better cut, until we find the cut we want.

youtube video:
https://www.youtube.com/watch?v=q6IEA26hvXc
"""
class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		# Ensure that nums1 is the shorter array
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1
		
		# Perform a binary search on nums1
		m, n = len(nums1), len(nums2)
		left, right = 0, m
		while left <= right:
			# Partition the two arrays
			p = (left + right) // 2
			q = (m + n + 1) // 2 - p
			
			# Check if the partition is correct
			max_left1 = float('-inf') if p == 0 else nums1[p-1]
			max_left2 = float('-inf') if q == 0 else nums2[q-1]
			min_right1 = float('inf') if p == m else nums1[p]
			min_right2 = float('inf') if q == n else nums2[q]
			
			if max_left1 <= min_right2 and max_left2 <= min_right1:
				# Calculate the median
				if (m + n) % 2 == 0:
					return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
				else:
					return max(max_left1, max_left2)
			elif max_left1 > min_right2:
				right = p - 1
			else:
				left = p + 1