"""
https://leetcode-cn.com/problems/c32eOV/
https://leetcode-cn.com/problems/c32eOV/solution/shua-chuan-jian-zhi-offer-day12-lian-bia-lv78/
思路:
    快慢指针
"""

class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


