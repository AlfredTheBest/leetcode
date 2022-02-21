"""
https://leetcode-cn.com/problems/7WHec2/submissions/
思路:
   转list 排序 转listNode

"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        arr.sort()

        p = head
        for num in arr:
            p.val = num
            p = p.next

        return head










