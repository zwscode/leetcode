"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:
1 <= n <= 9

https://leetcode.com/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        nQueens = [['.' for _ in range(n)] for _ in range(n)]
        self.solve_helper(res, nQueens, 0, n)
        return res

    def solve_helper(self, res, nQueens, row, n):
        if row == n:
            res.append([''.join(row) for row in nQueens])
            return
        for col in range(n):
            if self.is_valid(nQueens, row, col, n):
                nQueens[row][col] = 'Q'
                self.solve_helper(res, nQueens, row + 1, n)
                nQueens[row][col] = '.'

    def is_valid(self, nQueens, row, col, n):
        for i in range(row):
            if nQueens[i][col] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if nQueens[i][j] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if nQueens[i][j] == 'Q':
                return False
        return True
