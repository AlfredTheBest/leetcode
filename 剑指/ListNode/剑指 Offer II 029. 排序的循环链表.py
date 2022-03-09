"""
https://leetcode-cn.com/problems/4ueAj6/
思路:
    在递增区间插入或者 递减且 比最小值小或比最小值大
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        cur=head
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break
            if cur.val > cur.next.val and (cur.val < insertVal or insertVal < cur.next.val):
                break
            cur = cur.next
        node.next = cur.next
        cur.next = node
        return head
