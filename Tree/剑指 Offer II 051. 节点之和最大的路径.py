"""
https://leetcode-cn.com/problems/jC7MId/
思路:
    DFS
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.res = max(self.res, root.val + left + right)

            return root.val + max(left, right)
        self.res = root.val
        dfs(root)
        return self.res




























