"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 

Follow up: Can you achieve this in O(log n) time complexity?

https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

# idea:
# 1. Find the smallest number in the list. This can be achieved through binary search.
# 2. Binaray search in left or right side of the smallest number

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        numsLen = len(nums)
        low, high = 0, numsLen - 1
        # 1. find smallest
        while(low < high):
            mid = int(low + (high - low) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        smallest = low
        if nums[smallest] <= target <= nums[numsLen - 1]:
            low, high = smallest, numsLen -1
        else:
            low ,high = 0, smallest - 1
        # 2. binary search
        while(low < high):
            mid = int(low + (high - low) / 2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] == target:
            return low
        return - 1

if __name__ == "__main__":
    nums = [1,3]
    target = 1
    oSolution = Solution()
    print (oSolution.search(nums, target))