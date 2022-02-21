"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
思路:
    双指针
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dum = ListNode()
        dum.next = head

        fast = slow = dum
        while n != 0:
            fast = fast.next
            n -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.nex

        return dum.next













