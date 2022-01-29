"""
https://leetcode-cn.com/problems/3u1WK4/
思路:
    双指针
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headB or not headA:
            return
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa