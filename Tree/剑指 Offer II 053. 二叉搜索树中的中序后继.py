"""
https://leetcode-cn.com/problems/P5rCT8
思路:
    DFS
"""

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None

        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right

        return res

