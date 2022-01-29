"""
https://leetcode-cn.com/problems/w6cpku/
思路:
    dfs
"""

class Solution:
    add = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            root.val += self.add
            self.add = root.val
            self.convertBST(root.left)
        return root











