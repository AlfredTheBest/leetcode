"""
https://leetcode-cn.com/problems/NaqhDT/
https://leetcode-cn.com/problems/NaqhDT/solution/jian-zhi-offer043-wang-wan-quan-er-cha-s-risj/
思路:
    queue
"""
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = []
        self.queue.append(root)
        while self.queue[0].left != None and self.queue[0].right != None:

            node = self.queue.pop(0)
            self.queue.append(node.left)
            self.queue.append(node.right)

    def insert(self, v: int) -> int:
        parent = self.queue[0]
        node = TreeNode(v)
        if parent.left == None:
            parent.left = node
        else:
            parent.right = node
            self.queue.pop(0)
            self.queue.append(parent.left)
            self.queue.append(parent.right)
        return parent.val


    def get_root(self) -> TreeNode:
        return self.root
