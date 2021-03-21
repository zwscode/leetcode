"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        lResult = []
        lPrev = []
        self.backtrack(lResult, lPrev, nums, 0)
        return lResult
    
    def backtrack(self, lResult, lPrev, lNums, iStart):
        if lPrev and len(lPrev) == len(lNums):
            lResult.append(lPrev[:])
            return
        for i in range(0, len(lNums)):
            if lNums[i] not in lPrev:
                lPrev.append(lNums[i])
                self.backtrack(lResult, lPrev, lNums, i + 1)
                lPrev.pop()
