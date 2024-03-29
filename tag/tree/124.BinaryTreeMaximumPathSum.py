# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# hard

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: It is easy to think of something like "max_val = node.leftMax + node.rightMax + node.val". But the question says, the path does not need to pass through the root. So we need "leftMax = max(0, leftMaxVal), rightMax = max(0, rightMaxVal)" to make sure the path does not need to pass through the root.

class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.m_maxVal = float('-inf')
		self.findMax(root)
		return self.m_maxVal

	def findMax(self, node):
		if not node:
			return 0
		leftMax = max(0, self.findMax(node.left))
		rightMax = max(0, self.findMax(node.right))
		self.m_maxVal = max(self.m_maxVal, leftMax + rightMax + node.val)
		return max(leftMax, rightMax) + node.val
		