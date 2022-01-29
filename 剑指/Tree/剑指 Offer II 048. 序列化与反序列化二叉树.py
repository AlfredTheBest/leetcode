"""
https://leetcode-cn.com/problems/h54YBf/
思路:
    DFS
"""

class Codec:
    def serialize(self, root):
        if not root:
            return 'None'
        root.left = self.serialize(root.left)
        root.right = self.serialize(root.right)
        return f"{root.val},{root.left},{root.right}"

    def deserialize(self, data):
        dq = deque(data.split(','))

        def dfs(li):
            val = li.popleft()
            if val == "None":
                return None
            root = TreeNode(int(val))
            root.left = dfs(li)
            root.right = dfs(li)
            return root
        return dfs(dq)












