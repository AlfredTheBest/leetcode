"""
https://leetcode-cn.com/problems/add-two-numbers/
思路:
    链表
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = r = ListNode(0)
        t = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            summ = a + b + t
            t = summ // 10
            r.next = ListNode(summ % 10)
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


        if t > 0:
            r.next = ListNode(1)
        return result.next









