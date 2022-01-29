"""
https://leetcode-cn.com/problems/3Etpl5/
思路:
    DFS
"""

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node, val):
            if not node:
                return 0
            val = val * 10 + node.val

            if not(node.left or node.right):
                return val

            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)














