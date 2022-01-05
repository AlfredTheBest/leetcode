"""
https://leetcode-cn.com/problems/WNC0Lk/
思路:
    BFS
"""

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        que = deque([root])
        si = len(que)
        while si != 0:
            for i in range(si):

                node = que.popleft()

                if i == si-1:
                    ret.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            si = len(que)

        return ret