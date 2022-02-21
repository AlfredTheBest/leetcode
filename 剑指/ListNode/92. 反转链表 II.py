"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/

反转listnode
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dum_node = ListNode(-1)
        dum_node.next = head
        pre = dum_node

        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next

        return dum_node.next












