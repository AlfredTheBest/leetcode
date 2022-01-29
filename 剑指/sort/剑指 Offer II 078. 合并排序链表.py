"""
https://leetcode-cn.com/problems/vvXgSW/
思路:
    heapq
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p = g = ListNode(0)
        h = []
        for a, i in enumerate(lists):
            if i:
                heappush(h, (i.val, a, i))

        while h:
            a, b, c = heappop(h)
            p.next = p = c
            c = c.next
            if c:
                heappush(h, (c.val, b, c))

        return g.next







