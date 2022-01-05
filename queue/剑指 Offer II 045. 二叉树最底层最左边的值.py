"""
https://leetcode-cn.com/problems/LwUNpT/
思路:
    BFS
"""


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None

        ret = None
        que = deque([root])
        si = len(que)
        while si != 0:
            for i in range(si):
                node = que.popleft()

                if i == 0:
                    ret = node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            si = len(que)
        return ret