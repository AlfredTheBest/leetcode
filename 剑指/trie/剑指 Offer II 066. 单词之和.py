"""
https://leetcode-cn.com/problems/z1R5dt
思路:
    Trie
"""




class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            node = node.setdefault(c, {})
        node['#'] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return 0
        self.res = 0
        def dfs(node):
            for key, val in node.items():

                if key =='#':
                    self.res+=val
                else:
                    dfs(val)
        dfs(node)
        return self.res
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)









