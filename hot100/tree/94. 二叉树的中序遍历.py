"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
思路：
    dfs
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res
