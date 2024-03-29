# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# medium

"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: the easy solution would be to do a pre-order traversal and then flatten the tree. 
# The optimal approach would be solving it in O(1) space. Usaully we use recursion to achieve this.
class Solution:
	def flatten(self, root):
		"""
		Do not return anything, modify root in-place instead.
		"""
		# base case
		if not root:
			return
		
		# recursively flatten left and right subtrees
		self.flatten(root.left)
		self.flatten(root.right)
		
		left = root.left
		right = root.right
		
		# move left subtree to right
		root.left = None
		root.right = left
		
		# attach right subtree to the end of the previous left subtree
		p = root
		while p.right:
			p = p.right
		p.right = right
