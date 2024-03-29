# https://leetcode.com/problems/sort-list/description/
# medium

"""
Given the head of a linked list, return the list after sorting it in ascending order.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Idea: The easy solution is to read all elements into a list, sort the list, then put them back into a list. But this solution is not O(1) memory. 
# Usually when we are asked to do something in O(1) memory, we need to do recursion.

# The trick to write recursion function is to assume it works, call the function itself, then check the base case.
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        temp = None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeList(l1, l2)
    
    def mergeList(self, l1,  l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next


