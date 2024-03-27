# https://leetcode.com/problems/word-search/description/
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

# This problem is a typical search problem.
class Solution:
    def __init__(self):
        self.found = False
    
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, word, 0)
                if self.found:
                    return True
        return False
    
    def dfs(self, board, i, j, word, p):
        if p == len(word):
            self.found = True
            return
        if self.found:
            return
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if board[i][j] != word[p]:
            return
        
		# similar to the idea of backtracking, we change the value of board[i][j] to '0' to avoid visiting it again
        temp = board[i][j]
        board[i][j] = '0'
        
        self.dfs(board, i+1, j, word, p+1)
        self.dfs(board, i, j+1, word, p+1)
        self.dfs(board, i-1, j, word, p+1)
        self.dfs(board, i, j-1, word, p+1)
        # similar to backtracking, we need to restore the value of board[i][j] after recursion
        board[i][j] = temp