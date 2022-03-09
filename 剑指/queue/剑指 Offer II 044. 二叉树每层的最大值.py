"""
https://leetcode-cn.com/problems/hPov7L/
思路:
    BFS
"""
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        que = deque([root])
        si = len(que)
        while si != 0:
            mx = -float('inf')
            for i in range(si):
                node = que.popleft()
                mx = max(mx, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            si = len(que)
            ret.append(mx)

        return ret
