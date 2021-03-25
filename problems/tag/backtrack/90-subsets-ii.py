"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

https://leetcode.com/problems/subsets-ii/
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lResult = []
        lPrev = []
        nums.sort()
        self.backtrack(lResult, lPrev, nums, 0)
        return lResult
    
    def backtrack(self, lResult, lPrev, lNums, iStart):
        lResult.append(lPrev[:])
        for i in range(iStart, len(lNums)):
            if lNums[i] == lNums[i-1] and i > iStart:
                continue
            lPrev.append(lNums[i])
            self.backtrack(lResult, lPrev, lNums, i + 1)
            lPrev.pop()
