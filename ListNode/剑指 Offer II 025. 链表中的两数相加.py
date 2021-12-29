"""
https://leetcode-cn.com/problems/lMSNwu/
https://leetcode-cn.com/problems/lMSNwu/solution/shua-chuan-jian-zhi-offer-day13-lian-bia-cl27/

思路:
    反转链表后相加
"""


class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre

    def addTwoNumbers(self, l1, l2):
        rev_l1 = self.reverseList(l1)
        rev_l2 = self.reverseList(l2)
        count = 0
        ret = ListNode()
        tmp = ret
        while rev_l1 or rev_l2 or count:
            num = 0
            if rev_l1:
                num += rev_l1.val
                rev_l1 = rev_l1.next
            if rev_l2:
                num += rev_l2.val
                rev_l2 = rev_l2.next
            count, num = divmod(num + count, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return self.reverseList(ret.next)
