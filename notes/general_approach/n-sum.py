# Here is the code to solve N-Sum problem

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, 3, 0, 0)

    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        if n == 2:
            # two pointers solve sorted 2-sum problem
            lo, hi = start, sz - 1
            while lo < hi:
                s = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if s < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif s > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            # n > 2, do (n-1)Sum
            for i in range(start, sz):
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < sz - 1 and nums[i] == nums[i + 1]:
                    i += 1
        return res
