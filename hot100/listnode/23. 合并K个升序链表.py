"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/
思路:
    heapq
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next

        d = c = ListNode(-1)
        while heap:
            c.next = ListNode(heapq.heappop(heap))
            c = c.next

        return d.next







