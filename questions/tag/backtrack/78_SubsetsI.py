class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        previous = []
        self.backtrack(result, previous, nums, 0)
        return result
        
    def backtrack(self, result, previous, nums, iIdx):
        result.append(previous[:])

        for i in range(iIdx, len(nums)):
            previous.append(nums[i])
            self.backtrack(result, previous, nums, i + 1)
            previous.pop()