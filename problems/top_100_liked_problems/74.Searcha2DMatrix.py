# https://leetcode.com/problems/search-a-2d-matrix/description/

"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

# idea: convert this matrix search problem to a 1D array search problem, then apply binary search

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while(left <= right):
            mid = left + (right - left) // 2
            if(self.get(matrix, mid) == target):
                return True
            elif self.get(matrix, mid) < target:
                left = mid + 1
            elif self.get(matrix, mid) > target:
                right = mid - 1
        return False

    def get(self, matrix, index):
        m, n = len(matrix), len(matrix[0])
        i, j = index // n, index % n
        return matrix[i][j]
