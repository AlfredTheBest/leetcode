"""
https://leetcode-cn.com/problems/Qv1Da2/
思路:
    堆栈
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return head

        dummy = Node(-1, None, None, None)

        pre = dummy
        stk = [head]
        while stk:
            x = stk.pop()

            pre.next = x
            x.prev = pre

            if x.next:
                stk.append(x.next)
            if x.child:
                stk.append(x.child)
                x.child = None

            pre = x

        dummy.next.prev = None
        return dummy.next


