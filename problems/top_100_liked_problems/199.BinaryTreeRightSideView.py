# https://leetcode.com/problems/binary-tree-right-side-view/description/
# medium

"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]
"""

# Wrong idea: visit the right child, if right child is None, visit the left child. Repeat.

class WrongSolution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		self.res = []
		self.traverse(root)
		return self.res
	
	def traverse(self, node):
		if node:
			self.res.append(node.val)
		if node.right:
			self.traverse(node.right)
		elif node.left:
			self.traverse(node.left)

# For [1,2,3,4] the output should be [1,3,4], but the output is [1,3]. 4 is the left child of 2, 2 is the left child of 1. Because 3 doesn't have a child, when we look from the right side, we can see 4.
			
# Right idea: Do a level order traversal, and only add the last element of each level to the result. Check "102.BinaryTreeLevelOrderTraversal.py".

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		q = deque()
		q.append(root)
		result = []
		while q:
			qLen = len(q)
			for i in range(qLen):
				node = q.popleft()
				if node:
					if node.left:
						q.append(node.left)
					if node.right:
						q.append(node.right)
				if i == qLen - 1:
					result.append(node.val)
		return result