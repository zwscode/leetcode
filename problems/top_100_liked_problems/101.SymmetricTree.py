# https://leetcode.com/problems/symmetric-tree/description/
# easy
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: Tree problem usually involves recursion. This problem is about symmetry, we need to make sure left and right are symmetric. We need to use some helper function like this: self.helper(left.left, right.right) and self.helper(left.right, right.left) are the same.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isEqual(root.left, root.right)

    def isEqual(self, left, right):
        if not left and right:
            return False
        if not right and left:
            return False
        if not left and not right:
            return True
        return left.val == right.val and self.isEqual(left.left, right.right) and \
            self.isEqual(left.right, right.left)