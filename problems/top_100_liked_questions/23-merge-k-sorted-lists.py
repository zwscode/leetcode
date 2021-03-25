"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

https://leetcode.com/problems/merge-k-sorted-lists/
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    # repeatedly pick the smallest node
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        oBefore = ListNode()
        oCur = oBefore
        
        while(lists):
            lDelIdx = []
            iMinIdx = -1
            iMin = float("inf")
            oMin = None
            for iIdx, oListNode in enumerate(lists):
                if not oListNode:
                    lDelIdx.append(iIdx)
                    continue
                if oListNode.val < iMin:
                    iMin = oListNode.val
                    oMin = oListNode
                    iMinIdx = iIdx
            if oMin:
                oCur.next = oMin
                lists[iMinIdx] = oMin.next
            if lDelIdx:
                for iIdx in reversed(lDelIdx):
                    del lists[iIdx]
        return oBefore.next
    
    # put all node in a list, sort the list, put nodes in a List
    def mergeKLists2(self, lists):
        if not lists:
            return None
        lNode = []
        for oNode in lists:
            oCur = oNode
            while(oCur):
                lNode.append(oCur)
                oCur = oCur.next
        lNode.sort(key=lambda x:x.val)
        oBefore = ListNode()
        oCur = oBefore
        for oNode in lNode:
            oCur.next = oNode
            oCur = oNode
        return oBefore.next