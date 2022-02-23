"""
    查找
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root):
            # 如果是 None
            if not root:
                return 0
            left = max(dfs(root.left), 0) 左边处理逻辑
            right = max(dfs(root.right), 0) 左边处理逻辑

            # 业务逻辑
            self.res = max(self.res, root.val + left + right)

            # 返回逻辑
            return root.val + max(left, right)

        self.res = root.val
        dfs(root)
        return self.res

    节点关系
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = None
        def dfs(node):
            # 如果是 None
            if not node:
                return None
            nonlocal pre

            dfs(node.right) 左边处理逻辑
            node.right, pre = pre, node 业务逻辑
            dfs(node.left) 右边处理逻辑
            node.left = None
        # 返回逻辑
        return dfs(root) or pre



"""