#https://leetcode-cn.com/problems/house-robber-iii/
#https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.md

class Solution:
    def rob(self, root):
        result = self.rob_tree(root)
        return max(result[0], result[1])

    def rob_tree(self, node):
        if node is None:
            return (0, 0)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1]
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        return (val1, val2)





















