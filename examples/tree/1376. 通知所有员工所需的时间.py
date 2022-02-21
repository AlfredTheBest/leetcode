"""
https://leetcode-cn.com/problems/time-needed-to-inform-all-employees/
思路:
    dfs
"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        self.son = defaultdict(list)
        for i in range(n):
            if i != headID:
                self.son[manager[i]].append(i)

        return self.dfs(headID, informTime)

    def dfs(self, u, informTime):
        res = 0
        for s in self.son[u]:
            res = max(res, informTime[u] + self.dfs(s, informTime))
        return res
