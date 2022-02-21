"""
https://leetcode-cn.com/problems/SLwz0R/
https://leetcode-cn.com/problems/SLwz0R/solution/shua-chuan-jian-zhi-offer-day11-lian-bia-tuyw/

思路:
    双指针
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(-1)
        dum.next = head
        fast = slow = dum

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next


        return dum.next