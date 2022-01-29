"""
https://leetcode-cn.com/problems/UHnkqh/
https://leetcode-cn.com/problems/UHnkqh/solution/shua-chuan-jian-zhi-offer-day12-lian-bia-190d/

思路:
    拿到pre和next就可以循环反转
"""

class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre

