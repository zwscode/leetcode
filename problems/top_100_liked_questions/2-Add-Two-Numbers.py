"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		head = ListNode(0)
		ptr = head
		cur = 0
		carry = 0
		while l1 or l2 or carry:
			ptr.next = ListNode()
			ptr = ptr.next

			first = l1.val if l1 else 0
			second = l2.val if l2 else 0
			sum = first + second + carry
			cur = sum % 10
			carry = 1 if sum >= 10 else 0
			ptr.val = cur
			
			
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
		return head.next or head
