class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True
