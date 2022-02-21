"""
https://leetcode-cn.com/problems/aMhZSa/
思路:
    反转链表比较
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        if fast:
            slow = slow.next
        while slow:
            if slow.val != pre.val:
                return False
            slow, pre = slow.next, pre.next
        return True









