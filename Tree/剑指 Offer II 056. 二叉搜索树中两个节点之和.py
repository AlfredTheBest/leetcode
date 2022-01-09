"""
https://leetcode-cn.com/problems/opLdQZ/
思路:
    DFS

"""


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        res = False

        def dfs(r):
            nonlocal res
            if not r or res:
                return
            dfs(r.left)
            if r.val not in d:
                d.add(k-r.val)
            else:
                res = True
                return
            dfs(r.right)
        dfs(root)
        return res



class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ret = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)

        dfs(root)
        left, right = 0, len(ret) - 1
        while left < right:
            if ret[left] + ret[right] > k: right -= 1
            elif ret[left] + ret[right] < k: left += 1
            else: return True
        return False



