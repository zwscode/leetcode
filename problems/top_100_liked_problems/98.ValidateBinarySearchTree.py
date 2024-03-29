# https://leetcode.com/problems/validate-binary-search-tree/description/
# medium

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: This problem is hard because we need to make sure all left nodes are smaller than the root node and all right nodes are larger than the root node. Not just the immediate left and right nodes. 
# We need to use a helper function to pass the min and max.

# The intuition of that helper function is that we need to pass the min and max value to the left and right nodes.

class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.helper(root, float('-inf'), float('inf'))
		
	def helper(self, root, min, max):
		if not root:
			return True
		if root.val <= min or root.val >= max:
			return False
		return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)