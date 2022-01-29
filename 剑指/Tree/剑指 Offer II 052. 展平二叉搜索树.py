"""
https://leetcode-cn.com/problems/NYBBNL
思路:
    DFS
"""


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = None
        def dfs(node):
            if not node:
                return None
            nonlocal pre

            dfs(node.right)
            node.right, pre = pre, node
            dfs(node.left)
            node.left = None
        return dfs(root) or pre


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        new_root = TreeNode(res[0])
        cur = new_root
        for val in res[1:]:
            cur.right = TreeNode(val)
            cur = cur.right
        return new_root
