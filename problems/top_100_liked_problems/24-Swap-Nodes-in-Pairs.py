"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

https://leetcode.com/problems/swap-nodes-in-pairs/
"""

"""
summary:
evaluate the ablitiy to manipulate linked list
recursion

though it's Medium, but it's pretty hard to get right.
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        newHead = head.next
        while cur and cur.next:
            first = cur
            # set cur to 2nd node
            cur = cur.next
            # set 1st.next to 3rd node
            first.next = cur.next
            # set 2nd.next to 1st node
            cur.next = first

            # set cur to point to 3rd node, so while loop may continue
            cur = first.next

            # set 1st.next to 4th node, so first.next may point to the right node: 4th node.
            if cur and cur.next:
                first.next = cur.next
        return newHead
