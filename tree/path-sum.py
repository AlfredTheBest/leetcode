# iteration

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True
            if root.left:
                targetsum -= root.left.val
                if isornot(root.left, targetsum): return True
                targetsum += root.left.val
            
            if root.right:
                targetsum -= root.right.val
                if isornot(root.right, targetsum): return True
                targetsum += root.right.val

            if root == None:
                return False
            else:
                return isornot(root, targetsum - root.val)


# sequence traversal
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        stack = []
        stack.append((root, root.val))

        while stack:
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetSum:
                return True
            
            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))

            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False  























