# https://leetcode.com/problems/unique-paths/description/

"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
Constraints:
1 <= m, n <= 100
"""


class Solution:
    memo = []

    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[0] * n for _ in range(m)]
        return self.dp(m - 1, n - 1)

    # definition of dp: the number of unique paths to reach (x, y)
    def dp(self, x: int, y: int) -> int:
        # base case
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0
        # memoization
        if self.memo[x][y] > 0:
            return self.memo[x][y]
        # state transfer equation
        self.memo[x][y] = self.dp(x - 1, y) + self.dp(x, y - 1)
        return self.memo[x][y]

