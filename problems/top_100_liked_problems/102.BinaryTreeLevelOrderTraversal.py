# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# medium
"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: level order traversal is a typical BFS problem. One thing to note is that we need to keep track of the length of the current level and the length of the next level.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        # do not forget to check if root is None
        if not root:
            return []
        q = deque()
        q.append(root)
        level_len = 1
        next_lv_len = 0
        res = []
        while q:
            level = []
            next_lv_len = 0
            for i in range(level_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                        next_lv_len += 1
                    if node.right:
                        q.append(node.right)
                        next_lv_len +=1
            res.append(level)
            level_len = next_lv_len
        return res