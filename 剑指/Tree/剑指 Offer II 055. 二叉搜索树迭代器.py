"""
https://leetcode-cn.com/problems/kTOapQ/


"""

class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(root):
            if root:
                dfs(root.left)
                self.li.append(root.val)
                dfs(root.right)

        self.cur = 0
        self.li = []
        dfs(root)

    def next(self) -> int:
        ret = self.li[self.cur]
        self.cur += 1
        return ret

    def hasNext(self) -> bool:
        return self.cur < len(self.li)





